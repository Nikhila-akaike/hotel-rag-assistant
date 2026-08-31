import chromadb


class ChromaStore:

    def __init__(
        self,
        persist_directory: str = "vector_db",
        collection_name: str = "hotel_knowledge"
    ):

        self.client = chromadb.PersistentClient(
            path=persist_directory
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        ids: list[str],
        documents: list[str],
        embeddings,
        metadatas: list[dict]
    ):

        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def count(self):
        return self.collection.count()