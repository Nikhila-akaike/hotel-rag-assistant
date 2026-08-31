from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed_text(self, text: str):
        return self.model.encode(text)

    def embed_documents(self, texts: list[str]):
        return self.model.encode(texts)


if __name__ == "__main__":

    embedder = Embedder()

    texts = [
        "What time is breakfast?",
        "When can I have the morning meal?",
        "Where can I park my car?"
    ]

    vectors = embedder.embed_documents(texts)

    print("Number of vectors:", len(vectors))
    print("Vector dimension:", len(vectors[0]))

    print("\n--- Similarity Experiment ---")

    similarity_ab = embedder.model.similarity(
        vectors[0],
        vectors[1]
    )

    similarity_ac = embedder.model.similarity(
        vectors[0],
        vectors[2]
    )

    print(
        "\nSimilarity between Question A and B:",
        similarity_ab.item()
    )

    print(
        "Similarity between Question A and C:",
        similarity_ac.item()
    )