import os
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = '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'


llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
