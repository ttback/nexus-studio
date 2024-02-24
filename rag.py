import os 
from autogenstudio.env import set_env_variables
set_env_variables()
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
embedder = NVIDIAEmbeddings(model="nvolveqa_40k")

from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_nvidia_ai_endpoints import ChatNVIDIA


def format_dicts_to_strings(data):
  """
  Takes a list of dictionaries and returns a list of strings with formatted key-value pairs.

  Args:
      data: A list of dictionaries.

  Returns:
      A list of strings with formatted key-value pairs.
  """
  formatted_strings = []
  for item in data:
    # Use f-strings for cleaner string formatting
    formatted_string = f"{', '.join(f'{key}: {value}' for key, value in item.items())}"
    formatted_strings.append(formatted_string)
  return formatted_strings

data = [
  {
    "title": "GTC 2024 Keynote [S62542]",
    "speaker": "Jensen Huang, Founder and Chief Executive Officer, NVIDIA",
    "description": "Don't miss this keynote from NVIDIA founder and CEO Jensen Huang. He'll share how NVIDIA's accelerated computing platform is driving the next wave in AI, digital twins, cloud technologies, and sustainable computing.",
    "start_time": "Monday, Mar 18 1:00 PM PDT",
    "end_time": "Monday, Mar 18 3:00 PM PDT"
  },
  {
    "title": "A Culture of Open and Reproducible Research, in the Era of Large Al [S62219]",
    "speaker": "Joelle Pineau, Vice President, All Research, Meta",
    "description": "We've seen incredible progress in the last year in large AI models, with increasing abilities to generate high-quality images, videos, text, sound, and more. The best of these models display signs of creativity, reasoning, generalization, and adaptation. However, these models are often complex and opaque, making it difficult to understand how they work and ensure their reliability. In this talk, I will discuss the importance of open and reproducible research in the era of large language models. I will also present some of our recent work on developing methods for making large language models more interpretable and trustworthy.",
    "start_time": "Tuesday, Mar 19 3:00 PM PDT",
    "end_time": "Tuesday, Mar 19 3:50 PM PDT"
  },
  {
    "title": "Fireside Chat with Fei-Fei Li and Bill Dally: The High-Speed Revolution in Al ☆ [S61069]",
    "speaker": "Fei-Fei Li, Sequoia Professor of Computer Science, Stanford University, Denning Family Co-Director, Stanford Institute for Human-Centered AI (HAI), Stanford University & Bill Dally, Chief Scientist and Senior Vice President of Research, NVIDIA",
    "description": "Fei-Fei will share insights from her recently published book, her experiences at the intersection of academia and enterprise, and large language models. How are image models emerging from this revolution in technology and what are some of the potential benefits and risks? Bill Dally will discuss the role of high-speed computing in enabling the next generation of AI, and the opportunities and challenges that lie ahead.",
    "start_time": "Tuesday, Mar 19 9:00 AM PDT",
    "end_time": "Tuesday, Mar 19 9:50 AM PDT"
  },
  {
    "title": "Transforming Al [S63046]",
    "speaker": "Jensen Huang, Founder and Chief Executive Officer, NVIDIA; Ashish Vaswani, Co-founder and CEO, Essential AI; Noam Shazeer, Chief Executive Officer and Co-Founder Character AI; Niki Parmar, Co-Founder Essential AI; Jakob Uszkoreit, Chief Executive Officer Inceptive; Llion Jones, Co-founder and Chief Technology Officer, Sakana AI; Aidan Gomez, Co-founder and Chief Executive Officer, Cohere; Lukasz Kaiser, Member of Technical Staff OpenAI; Illia Polosukhin, Co-Founder NEAR Protocol",
    "description": "The Transforming Al Panel features the authors of \"Attention is All You Need,\" the groundbreaking paper that introduced the transformer neural network architecture. Transformers have since dominated all areas of AI and revolutionized the industry. Panelists will discuss the impact of transformers on research and development, the challenges and opportunities of large language models, and the future of AI.",
    "start_time": "Wednesday, Mar 20 11:00 AM PDT",
    "end_time": "Wednesday, Mar 20 11:50 AM PDT"
  }
]
formatted_data = format_dicts_to_strings(data)
vectorstore = FAISS.from_texts(
    formatted_data,
    embedding=NVIDIAEmbeddings(model="nvolveqa_40k"),
)
retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer solely based on the following context:\n<Documents>\n{context}\n</Documents>",
        ),
        ("user", "{question}"),
    ]
)

model = ChatNVIDIA(model="mixtral_8x7b")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke("when is the keynote with Jensen?"))
