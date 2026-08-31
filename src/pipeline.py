from src.ingestion.loader import load_pdf
from src.ingestion.chunker import chunk_document
from src.embeddings.embedder import Embedder
from src.vectorstore.chroma_store import ChromaStore


def build_documents(file_path: str):

    # --------------------------------
    # 1. Load PDF
    # --------------------------------

    documents = load_pdf(file_path)

    print(f"Loaded pages: {len(documents)}")


    # --------------------------------
    # 2. Chunk documents
    # --------------------------------

    all_chunks = []

    for document in documents:

        chunks = chunk_document(document)

        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")


    return all_chunks


def build_vector_store(file_path: str):

    # --------------------------------
    # 1. Build chunks
    # --------------------------------

    chunks = build_documents(file_path)


    # --------------------------------
    # 2. Create embeddings
    # --------------------------------

    embedder = Embedder()

    texts = [
        chunk.text
        for chunk in chunks
    ]

    embeddings = embedder.embed_documents(texts)


    # --------------------------------
    # 3. Prepare IDs
    # --------------------------------

    ids = [
        chunk.chunk_id
        for chunk in chunks
    ]


    # --------------------------------
    # 4. Prepare metadata
    # --------------------------------

    metadatas = [
        {
            "page": chunk.page,
            "source": chunk.source,
            "section": chunk.section or ""
        }
        for chunk in chunks
    ]


    # --------------------------------
    # 5. Store in Chroma
    # --------------------------------

    vector_store = ChromaStore()

    vector_store.add_documents(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )


    print(
        f"Documents in Chroma: "
        f"{vector_store.count()}"
    )


if __name__ == "__main__":

    build_vector_store(
        "data/hotel_restaurant_knowledge_base.pdf"
    )