from langchain_pipeline import chain, textsearch

with open("test_queries.txt") as f:
    queries = f.read().split("\n")

with open("test_answers.txt", "w") as f:
    for query in queries:
        docs = textsearch.similarity_search(query)
        res = chain.run(input_documents=docs, question=query)
        f.write(f"Q: {query}\n")
        f.write(f"A:{res}\n\n")
