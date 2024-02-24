import os
from typing import List, Optional
import autogen
from .datamodel import AgentConfig, AgentFlowSpec, AgentWorkFlowConfig, Message
from .utils import get_skills_from_prompt, clear_folder, sanitize_model
from datetime import datetime


class AutoGenWorkFlowManager:
    """
    AutoGenWorkFlowManager class to load agents from a provided configuration and run a chat between them
    """

    def __init__(
        self,
        config: AgentWorkFlowConfig,
        history: Optional[List[Message]] = None,
        work_dir: str = None,
        clear_work_dir: bool = True,
    ) -> None:
        """
        Initializes the AutoGenFlow with agents specified in the config and optional
        message history.

        Args:
            config: The configuration settings for the sender and receiver agents.
            history: An optional list of previous messages to populate the agents' history.

        """
        self.work_dir = work_dir or "work_dir"
        if clear_work_dir:
            clear_folder(self.work_dir)

        # given the config, return an AutoGen agent object
        self.sender = self.load(config.sender)
        # given the config, return an AutoGen agent object
        self.receiver = self.load(config.receiver)

        if config.receiver.type == "groupchat":
            # append self.sender to the list of agents
            self.receiver._groupchat.agents.append(self.sender)
            print(self.receiver)
        self.agent_history = []

        if history:
            self.populate_history(history)

    def process_reply(self, recipient, messages, sender, config):
        if "callback" in config and config["callback"] is not None:
            callback = config["callback"]
            callback(sender, recipient, messages[-1])
        last_message = messages[-1]

        sender = sender.name
        recipient = recipient.name
        if "name" in last_message:
            sender = last_message["name"]

        iteration = {
            "recipient": recipient,
            "sender": sender,
            "message": last_message,
            "timestamp": datetime.now().isoformat(),
        }
        self.agent_history.append(iteration)
        return False, None

    def _sanitize_history_message(self, message: str) -> str:
        """
        Sanitizes the message e.g. remove references to execution completed

        Args:
            message: The message to be sanitized.

        Returns:
            The sanitized message.
        """
        to_replace = ["execution succeeded", "exitcode"]
        for replace in to_replace:
            message = message.replace(replace, "")
        return message

    def populate_history(self, history: List[Message]) -> None:
        """
        Populates the agent message history from the provided list of messages.

        Args:
            history: A list of messages to populate the agents' history.
        """
        for msg in history:
            if isinstance(msg, dict):
                msg = Message(**msg)
            if msg.role == "user":
                self.sender.send(
                    msg.content,
                    self.receiver,
                    request_reply=False,
                )
            elif msg.role == "assistant":
                self.receiver.send(
                    msg.content,
                    self.sender,
                    request_reply=False,
                )

    def sanitize_agent_spec(self, agent_spec: AgentFlowSpec) -> AgentFlowSpec:
        """
        Sanitizes the agent spec by setting loading defaults

        Args:
            config: The agent configuration to be sanitized.
            agent_type: The type of the agent.

        Returns:
            The sanitized agent configuration.
        """

        agent_spec.config.is_termination_msg = agent_spec.config.is_termination_msg or (
            lambda x: "TERMINATE" in x.get("content", "").rstrip()[-20:]
        )

        def get_default_system_message(agent_type: str) -> str:
            if agent_type == "assistant":
                return autogen.AssistantAgent.DEFAULT_SYSTEM_MESSAGE
            else:
                return "You are a helpful AI Assistant."

        # sanitize llm_config if present
        if agent_spec.config.llm_config is not False:
            config_list = []
            for llm in agent_spec.config.llm_config.config_list:
                # check if api_key is present either in llm or env variable
                if "api_key" not in llm and "OPENAI_API_KEY" not in os.environ:
                    error_message = f"api_key is not present in llm_config or OPENAI_API_KEY env variable for agent ** {agent_spec.config.name}**. Update your workflow to provide an api_key to use the LLM."
                    raise ValueError(error_message)

                # only add key if value is not None
                sanitized_llm = sanitize_model(llm)
                config_list.append(sanitized_llm)
            agent_spec.config.llm_config.config_list = config_list
        if agent_spec.config.code_execution_config is not False:
            code_execution_config = agent_spec.config.code_execution_config or {}
            code_execution_config["work_dir"] = self.work_dir
            # tbd check if docker is installed
            code_execution_config["use_docker"] = False
            agent_spec.config.code_execution_config = code_execution_config
        if agent_spec.skills:
            # get skill prompt, also write skills to a file named skills.py
            skills_prompt = ""
            skills_prompt = get_skills_from_prompt(agent_spec.skills, self.work_dir)
            if agent_spec.config.system_message:
                agent_spec.config.system_message = agent_spec.config.system_message + "\n\n" + skills_prompt
            else:
                agent_spec.config.system_message = get_default_system_message(agent_spec.type) + "\n\n" + skills_prompt

        return agent_spec

    def load(self, agent_spec: AgentFlowSpec) -> autogen.Agent:
        """
        Loads an agent based on the provided agent specification.

        Args:
            agent_spec: The specification of the agent to be loaded.

        Returns:
            An instance of the loaded agent.
        """
        agent_spec = self.sanitize_agent_spec(agent_spec)
        if agent_spec.type == "groupchat":
            agents = [
                self.load(self.sanitize_agent_spec(agent_config)) for agent_config in agent_spec.groupchat_config.agents
            ]
            group_chat_config = agent_spec.groupchat_config.dict()
            group_chat_config["agents"] = agents
            groupchat = autogen.GroupChat(**group_chat_config)
            agent = autogen.GroupChatManager(groupchat=groupchat, **agent_spec.config.dict())
            agent.register_reply([autogen.Agent, None], reply_func=self.process_reply, config={"callback": None})
            return agent

        else:
            agent = self.load_agent_config(agent_spec.config, agent_spec.type)
            return agent

    def load_agent_config(self, agent_config: AgentConfig, agent_type: str) -> autogen.Agent:
        """
        Loads an agent based on the provided agent configuration.

        Args:
            agent_config: The configuration of the agent to be loaded.
            agent_type: The type of the agent to be loaded.

        Returns:
            An instance of the loaded agent.
        """
        if agent_type == "assistant":
            agent = autogen.AssistantAgent(**agent_config.dict())
        elif agent_type == "userproxy":
            agent = autogen.UserProxyAgent(**agent_config.dict())
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
        agent.register_reply([autogen.Agent, None], reply_func=self.process_reply, config={"callback": None})
        return agent

    def run(self, message: str, clear_history: bool = False) -> None:
        """
        Initiates a chat between the sender and receiver agents with an initial message
        and an option to clear the history.

        Args:
            message: The initial message to start the chat.
            clear_history: If set to True, clears the chat history before initiating.
        """
        self.sender.initiate_chat(
            self.receiver,
            message=message,
            clear_history=clear_history,
        )
        # pass
