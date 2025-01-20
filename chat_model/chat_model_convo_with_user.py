from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
)

chat_history = []

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    result = chat_model.invoke(chat_history)
    content = result.content
    chat_history.append(AIMessage(content=content))
    print("AI: ", content)


print("================")
print("Chat history: ", chat_history)
