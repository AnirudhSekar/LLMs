from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate



def handle_conversation(user_input):
    template = """
    Answer the question below:

    Here is the conversation history: {context}

    Question: {question}

    Answer: 
    """

    model = OllamaLLM(model="llama3")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    context = open('context.txt').readlines()
    if user_input.lower() == "exit":
        return "Thanks for chatting! I had a great time!"
    if user_input.lower() == "clear":
        with open('context.txt', 'w') as f:
              f.write("")
        return "Conversation history cleared"
    result = chain.invoke({'context':context, "question":user_input})
    context += f"\nUser: {user_input}\nBot: {result}"
    with open("context.txt", 'a') as f:
            f.write(f"\nUser: {user_input}\nBot: {result}")
    return f"{result}"

    