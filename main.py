from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from prompt import CHEF_PROMPT , SYSTEM_CHEF_PROMPT
from image_decoder import choose_image_file, build_image_message
from tools import web_search
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

load_dotenv()

models = init_chat_model(
    model=os.getenv("MODELS"),
    model_provider="openai",
    base_url="https://kenari.id/v1",
    api_key=os.getenv("KENARI_API_KEY")
)

logging.info("creating our chef agent...")
agent = create_agent(
    model=models,
    system_prompt=SystemMessage(content=SYSTEM_CHEF_PROMPT),
    tools=[web_search]
)

logging.info("agent created successfully. Now, let's choose an image file to analyze.")
path = choose_image_file()
message = build_image_message(path, CHEF_PROMPT)

response = agent.invoke(
    {"messages": [message]}
    )
print(response["messages"][-1].content)