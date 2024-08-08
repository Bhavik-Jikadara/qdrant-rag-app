from langchain_qdrant import QdrantVectorStore
from src.models import embeddings
from qdrant_client import QdrantClient
import sys

try:
    # Initialize the Qdrant client
    client = QdrantClient(url="http://localhost:6333", prefer_grpc=False)
    print(client, " | Initialize the Qdrant client")

    # Initialize the Qdrant vector store with embeddings
    db = QdrantVectorStore(client=client, embedding=embeddings, collection_name="small_finance_bank")

    print(db, " | Initialize the Qdrant vector store with embeddings")
    print("-"*100)

except Exception as e:
    print(f"Error during initialization: {e}")
    sys.exit(1)  # Exit if the initialization fails

while True:
    try:
        query = input("Enter your query (or 'exit' to quit): ")

        if query.lower() == "exit":
            break

        # Perform similarity search with score
        docs = db.similarity_search_with_score(query=query, k=1)

        if not docs:
            print("No documents found for the query.")
            continue

        for i in docs:
            doc, score = i
            print(f"Question: {query}")
            print(f"Answer: \n{doc.page_content}")
            print("-" * 100)

    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error during query processing: {e}")

print("Goodbye!")
