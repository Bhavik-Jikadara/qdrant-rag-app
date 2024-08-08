from langchain_community.embeddings import HuggingFaceBgeEmbeddings

# Load the embedding model 
embeddings = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-large-en",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': False}
)