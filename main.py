from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  # your Chroma retriever from vector.py

# Initialize your model
model = OllamaLLM(model="phi3")

# Define prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# ... (rest of main.py content) ...

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    if question.lower() == "q":
        break
    docs = retriever.invoke(question) 
    reviews = "\n".join([doc.page_content for doc in docs])
    print("REVIEWS FOUND:", reviews)  # debug

    if not reviews:
        reviews = "No relevant reviews found."

    # Format the prompt and invoke the model
    formatted_prompt = prompt.format(reviews=reviews, question=question)
    result = model.invoke(formatted_prompt)
    print("\nAnswer:\n", result)  
