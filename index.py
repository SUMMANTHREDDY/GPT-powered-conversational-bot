from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, TextLoader
loader=DirectoryLoader(
  "hfcrawl/output/",
  glob="**/*.txt",
  loader_cls=TextLoader
 )
documents=loader.load()
text_splitter=CharacterTextSplitter(
    chunk_size=1024,chunk_overlap=128
)
persist_directory="db"
texts=text_splitter.split_documents(documents)
embeddings=OpenAIEmbeddings(openai_api_key="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")
vectordb=Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory=persist_directory,
)
vectordb.persist()