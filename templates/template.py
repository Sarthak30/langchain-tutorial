import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

dotenv.load_dotenv()

gemini_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
)

# template with single variable
template = "Tell me a scientific fact about {topic}"

prompt_template = ChatPromptTemplate.from_template(template)

print("-" * 10)
prompt = prompt_template.format(topic="Delhi")
print(prompt)
result = gemini_model.invoke(prompt)
print(result.content)
print("-" * 10)

# template with multiple variables
template_multiple = """
You are a helpful assistant.
Human: Tell me a {subject} fact about {topic}
Assistant: 
"""

prompt_template_multiple = ChatPromptTemplate.from_template(template_multiple)

print("-" * 10)
prompt = prompt_template_multiple.invoke({"subject": "historical", "topic": "Delhi"})
print(prompt)
result = gemini_model.invoke(prompt)
print(result.content)
print("-" * 10)

# template with multiple variables and multiple messages using tuples
messages = [
    ("system", "You are a helpful assistant who tells {subject} facts about {topic}"),
    ("human", "Tell me two facts."),
]

prompt_template_multiple_messages = ChatPromptTemplate.from_messages(messages)

print("-" * 10)
prompt = prompt_template_multiple_messages.invoke({"subject": "historical", "topic": "Delhi"})
result = gemini_model.invoke(prompt)
print(result.content)
print("-" * 10)
