# Nexus Studio (AutoGen + TensorRT-LLM)

### Dependencies
- Set up TensorRT-LLM OpenAI project(https://github.com/NVIDIA/trt-llm-as-openai-windows) in another location, launch at port:8081
- Most of front-end from autogen-studio is built and included with the repo
- Python deps need to be installed

The env variables are setup at autogenstudio/env.py. The API keys are NOT required to run the application, but may be required for certain API-related skills

```bash
pip install -r requirements.txt
```
If any Skills script throw a dependency error, other requirements such as requirements_a2f.txt.

### Running the Application

Once installed, run the web UI by entering the following in your terminal:

```bash
autogenstudio ui --port 8088
```

This will start the application on the specified port. Open your web browser and go to `http://localhost:8081/` to begin using Nexus Studio.

## Capabilities

Nexus Studio proposes some high-level concepts.

**Agent Workflow**: An agent workflow is a specification of a set of agents that can work together to accomplish a task. The simplest version of this is a setup with two agents – a user proxy agent (that represents a user i.e. it compiles code and prints result) and an assistant that can address task requests (e.g., generating plans, writing code, evaluating responses, proposing error recovery steps, etc.). A more complex flow could be a group chat where even more agents work towards a solution.

**Session**: A session refers to a period of continuous interaction or engagement with an agent workflow, typically characterized by a sequence of activities or operations aimed at achieving specific objectives. It includes the agent workflow configuration, the interactions between the user and the agents. A session can be “published” to a “gallery”.

**Skills**: Skills are functions (e.g., Python functions) that describe how to solve a task. In general, a good skill has a descriptive name (e.g. `generate_images`), extensive docstrings and good defaults (e.g., writing out files to disk for persistence and reuse). You can add new skills Nexus Studio app via the provided UI. At inference time, these skills are made available to the assistant agent as they address your tasks.



## Acknowledgements

Nexus Studio is Based on the [AutoGen](https://microsoft.github.io/autogen) and its autogen-studio project. AutoGen was adapted from a research prototype built in October 2023 (original credits: Gagan Bansal, Adam Fourney, Victor Dibia, Piali Choudhury, Saleema Amershi, Ahmed Awadallah, Chi Wang).