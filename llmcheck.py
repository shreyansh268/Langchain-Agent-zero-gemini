from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # or "gemini-1.5-pro"
    temperature=0
)

print(llm.invoke("Hello Gemini!"))