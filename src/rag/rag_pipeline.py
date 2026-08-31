from src.retrieval.retriever import Retriever
from src.generation.llm import LLM


class RAGPipeline:

    def __init__(self, top_k: int = 3):

        self.retriever = Retriever(top_k=top_k)
        self.llm = LLM()

    def build_prompt(self, question: str, context: str) -> str:

        prompt = f"""
You are the AI receptionist for Azure Haven Hotel & Bistro.

Answer the guest's question using ONLY the information
provided in the context below.

Rules:
1. Do not invent information.
2. If the answer is not available in the context,
   say that the information is not available.
3. Keep the answer clear, concise, and helpful.
4. Answer as a hotel receptionist.

Context:
-------------------------
{context}
-------------------------

Guest Question:
{question}

Answer:
"""

        return prompt

    def ask(self, question: str):

        # 1. Retrieve relevant chunks
        results = self.retriever.retrieve(question)

        documents = results["documents"][0]

        # 2. Combine retrieved chunks
        context = "\n\n".join(documents)

        # 3. Build prompt
        prompt = self.build_prompt(
            question,
            context
        )

        # 4. Generate answer
        answer = self.llm.generate(prompt)

        return answer


if __name__ == "__main__":

    rag = RAGPipeline(top_k=3)

    question = "Does the hotel have a swimming pool?"

    answer = rag.ask(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)