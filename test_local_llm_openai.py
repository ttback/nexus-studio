
from openai import OpenAI
# Define your OpenAI API key (replace "private" with your actual key)
api_key = "NONE"
# Instantiate the client with local open_ai proxy server URL and API key
client = OpenAI(base_url="http://127.0.0.1:8081", api_key=api_key)

# Define a function to interact with the ChatGPT model
def test_local_llm_tensort(prompt: str) -> str:
    """
    This function sends a prompt to the ChatGPT model and returns the response.

    Args:
        prompt (str): The prompt to send to the model.

    Returns:
        str: The response from the Local LLM model.
    """

    # Create a chat completion request with the given prompt and user role
    response = client.chat.completions.create(
        model="llama-2",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract the generated response content
    response_message = response.choices[0].message.content.strip()

    return response_message

# Example usage: the response to the prompt "Tell me about Nvidia"
#chat_gpt("Tell me about Nvidia")