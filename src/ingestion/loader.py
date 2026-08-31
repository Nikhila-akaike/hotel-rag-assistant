# one module responsible for loading the source document --> loader.py

from pypdf import PdfReader
from src.ingestion.document import Document


def load_pdf(file_path: str):
    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            document = Document(
                text=text.strip(),
                source=file_path,
                page=page_number
            )

            documents.append(document)

    return documents


if __name__ == "__main__":
    documents = load_pdf("data/hotel_restaurant_knowledge_base.pdf")

    print(f"Total documents: {len(documents)}")

    first_document = documents[0]

    print("\nFirst document:")
    print(first_document)

    print("\nText:")
    print(first_document.text[:500])

    print("\nMetadata:")
    print(f"Source: {first_document.source}")
    print(f"Page: {first_document.page}")