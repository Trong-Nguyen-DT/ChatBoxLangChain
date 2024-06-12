import json
import requests

from langchain_chroma import Chroma
from langchain_core.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.tools.retriever import create_retriever_tool
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import WEATHER_HOST, WEATHER_KEY


@tool
def get_current_weather(location, unit="celsius"):
    """Get the current weather for a given location."""
    base_url = WEATHER_HOST
    api_key = WEATHER_KEY
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        temperature = data['main']['temp']
        temperature_str = str(temperature)
        return json.dumps({"location": location.title(), "temperature": temperature_str, "unit": unit})
    else:
        return json.dumps({"error": "Unable to retrieve weather information for the location."})
    
def retrieval_data():
    loader = TextLoader("/home/trongnguyendt/PartTimeDAC/Project/app/data/data.txt")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512, chunk_overlap=50
    )
    documents = text_splitter.split_documents(docs)
    db = Chroma.from_documents(documents, OpenAIEmbeddings())
    retriever = db.as_retriever()
    retriever_tool = create_retriever_tool(
        retriever,
        "my_information_search",
        "Search for information about me. For any questions about me, you must use this tool!",
    )
    return retriever_tool