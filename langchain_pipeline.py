import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

os.environ['OPENAI_API_KEY'] = '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'

with open("notion_data.txt") as f:
    notion_data = f.read()
with open("slack_final_data.txt") as f:
    slack_data = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(slack_data) + text_splitter.split_text(notion_data)
embeddings = OpenAIEmbeddings()
textsearch = FAISS.from_texts(texts, embeddings)

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff")


