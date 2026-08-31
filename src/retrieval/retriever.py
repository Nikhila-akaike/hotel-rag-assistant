from src.embeddings.embedder import Embedder
from src.vectorstore.chroma_store import ChromaStore


class Retriever:

    def __init__(self, top_k: int = 3):

        self.top_k = top_k

        self.embedder = Embedder()

        self.vector_store = ChromaStore()


    def retrieve(self, query: str):

        # Convert the user question into a vector
        query_embedding = self.embedder.embed_text(query)


        # Search ChromaDB
        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=self.top_k
        )


        return results


if __name__ == "__main__":

    retriever = Retriever(top_k=3)

    query = "Can I order food to my room?"

    results = retriever.retrieve(query)

    print("\nQuery:")
    print(query)

    print("\nRetrieved documents:")

    for i, document in enumerate(
        results["documents"][0]
    ):

        print("\n----------------------------")
        print(f"Result {i + 1}")
        print("----------------------------")

        print(document)

        print(
            "\nMetadata:",
            results["metadatas"][0][i]
        )

        print(
            "\nDistance:",
            results["distances"][0][i]
        )