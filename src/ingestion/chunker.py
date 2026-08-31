import re

from src.ingestion.document import Document


def is_section_heading(text: str) -> bool:
    """
    Check whether a line looks like a section heading.

    Example:
    '1. Property Overview'
    '2. Location & Directions'
    """

    pattern = r"^\d+\.\s+.+"

    return bool(re.match(pattern, text.strip()))


def chunk_document(
    document: Document,
    chunk_size: int = 600
):
    """
    Split a document into paragraph-aware chunks
    while preserving the current section.
    """

    paragraphs = [
        paragraph.strip()
        for paragraph in document.text.split("\n")
        if paragraph.strip()
    ]

    chunks = []

    current_chunk = ""
    current_section = None
    chunk_number = 1

    for paragraph in paragraphs:

        # Check if this paragraph is a section heading
        if is_section_heading(paragraph):
            current_section = paragraph

        # If paragraph fits into current chunk
        if len(current_chunk) + len(paragraph) + 1 <= chunk_size:

            if current_chunk:
                current_chunk += "\n"

            current_chunk += paragraph

        else:
            # Save previous chunk
            if current_chunk:

                chunks.append(
                    Document(
                        text=current_chunk,
                        source=document.source,
                        page=document.page,
                        chunk_id=f"page_{document.page}_chunk_{chunk_number}",
                        section=current_section
                    )
                )

                chunk_number += 1

            # Start a new chunk
            current_chunk = paragraph

    # Save final chunk
    if current_chunk:

        chunks.append(
            Document(
                text=current_chunk,
                source=document.source,
                page=document.page,
                chunk_id=f"page_{document.page}_chunk_{chunk_number}",
                section=current_section
            )
        )

    return chunks


if __name__ == "__main__":

    from src.ingestion.loader import load_pdf

    documents = load_pdf(
        "data/hotel_restaurant_knowledge_base.pdf"
    )

    # Test Page 2
    first_document = documents[1]

    chunks = chunk_document(first_document)

    print(f"Original document length: {len(first_document.text)}")
    print(f"Number of chunks: {len(chunks)}")

    for chunk in chunks:

        print("\n------------------------------")
        print(f"Chunk ID : {chunk.chunk_id}")
        print(f"Page     : {chunk.page}")
        print(f"Section  : {chunk.section}")
        print("------------------------------")

        print(chunk.text)