from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
)   

result = chat_model.invoke("What is the capital of France?")
print("Full response: ", result)
print("Content: ", result.content)  
