from langchain_qdrant.vectorstores import Qdrant
from models import embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path=r"D:\Project\qdrant-rag-app\src\data\small-finance-bank.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

texts = text_splitter.split_documents(documents)

url = "http://localhost:6333"
qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    url=url,
    prefer_grpc=False,
    collection_name="small_finance_bank"
)

print("Vector DB Successfully Created!")