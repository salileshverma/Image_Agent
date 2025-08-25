from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

print("Groq API Key:", groq_api_key)

# Create Groq model instance
groq_model = Groq(
    id="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=groq_api_key,
)

agent = Agent(
    model=groq_model,
    tools=[DuckDuckGo()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=["https://upload.wikimedia.org/wikipedia/commons/b/bf/Krakow_-_Kosciol_Mariacki.jpg"],
    stream=True,
)

try:
    agent.print_response(
        "Tell me about Kraków St. Mary's Basilica and give me the latest news about it.",
        stream=False  # 👈 non-streaming works better with tools
    )
except Exception as e:
    print("⚠️ Error:", e)