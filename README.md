# RAG App using Qdrant VectorDB

This project is a Retrieval-Augmented Generation (RAG) application using the Qdrant vector database. Below is an overview of the project structure and steps to set up and run the application.

## Steps to Run the Application

* **Clone the Repository**: If you haven't already, clone the repository to your local machine:

    ```bash
    git clone https://github.com/Bhavik-Jikadara/qdrant-rag-app.git
    cd qdrant-rag-app
    ```

* **Set Up Virtual Environment**: Create a virtual environment to manage the project's dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

* **Install Python Dependencies**: Install the required Python packages specified in requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

* **Install Docker and Run Qdrant VectorDB Using Docker**: Install Docker if you haven't already. Then, pull and run the Qdrant Docker container:

    ```bash
    docker pull qdrant/qdrant
    docker run -p 6333:6333 -v $(pwd):/qdrant qdrant/qdrant
    ```

This will start Qdrant and make it accessible on `http://localhost:6333`.

* **Configure Environment Variables**: Update the .env file with necessary environment variables such as Qdrant API keys or database URLs.

* **Ingest Data into Qdrant**: Use the ingest.py script to load data into the Qdrant vector database:

    ```bash
    python src/ingest.py
    ```

* **Run the Application**: Finally, run the main application using:

    ```bash
    python app.py
    ```
