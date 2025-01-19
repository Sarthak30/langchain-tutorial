from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
)

messages = [
    SystemMessage(content="Translate the user sentence to French."),
    HumanMessage(content="I love programming."),
]

result = chat_model.invoke(messages)
print("Answer: ", result.content)

messages = [
    SystemMessage(content="Translate the user sentence to French."),
    HumanMessage(content="I love programming."),
    AIMessage(content="J'adore programmer."),
    HumanMessage(content="I love cricket."),
]

result = chat_model.invoke(messages)
print("Answer: ", result.content)
