import streamlit as st
from llama_index import VectorStoreIndex
from llama_index.vector_stores import ChromaVectorStore
import chromadb

st.title('Precident')

# load and prime the index
db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
)
query_engine = index.as_query_engine()

# add search bar
search = st.text_input('Search', 'Enter query here')
response = query_engine.query(search)
st.write(response)
