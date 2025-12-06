# ReviewRag
# 🍕 PizzaBot Review Assistant

A Retrieval-Augmented Generation (RAG) system built with LangChain and Ollama to answer customer questions about a pizza restaurant based on a large dataset of reviews.

This project utilizes a **Chroma vector store** to manage and retrieve relevant customer reviews, which are then provided as context to a **Large Language Model (LLM)** (specifically `phi3` via Ollama) to generate informed and context-aware answers.

## ✨ Features

* **RAG Architecture:** Efficiently retrieves contextually relevant information from a large corpus of reviews.
* **Local LLM:** Uses the `phi3` model running locally via **Ollama** for question answering.
* **Vector Store:** Employs **Chroma** for vector storage and similarity search.
* **Review Indexing:** Indexes review title and content, including metadata like rating and date.

## 🛠️ Prerequisites

Before running the project, you need to have the following installed:

1.  **Ollama:** Must be running on your system.
    * Install it from [ollama.com](https://ollama.com/).
2.  **Ollama Models:** You need to pull the models used in the project:
    ```bash
    ollama pull phi3
    ollama pull mxbai-embed-large
    ```
3.  **Python 3.x**

## 💻 Installation and Setup

1.  **Clone the repository (or set up the files):**
    ```bash
    # Assuming your files are in a directory named 'PizzaBot'
    mkdir PizzaBot
    cd PizzaBot
    # Place main.py and vector.py here
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas langchain-ollama langchain-chroma langchain-core
    ```

3.  **Dataset:** You must have a CSV file named `realistic_restaurant_reviews.csv` in the expected location (`/home/salma/Documents/ThinkBox/realistic_restaurant_reviews.csv` based on `vector.py`) or update the path in `vector.py`. The CSV must contain at least the columns `Title`, `Review`, `Rating`, and `Date`.

## 🚀 How to Run

1.  Ensure **Ollama** is running and the necessary models (`phi3`, `mxbai-embed-large`) are pulled.
2.  Run the main application:
    ```bash
    python main.py
    ```

3.  The first run will **create and persist** the Chroma database in the `chrome_langchain_db` directory. Subsequent runs will load the existing database.

4.  The script will prompt you to ask a question. Enter your query (e.g., "How is the crust on the Margherita pizza?"). Type `q` to quit.

## ⚙️ Project Structure

* `main.py`: Contains the main application logic, the RAG chain setup, prompt templating, and the user interaction loop.
* `vector.py`: Handles the initialization of the Ollama embeddings, loading the CSV data, creating/loading the Chroma vector store, and exposing the `retriever` object.
* `chrome_langchain_db/`: Directory where the Chroma vector store is persisted after the initial run.
* `realistic_restaurant_reviews.csv`: The required input data file (path specified in `vector.py`).
