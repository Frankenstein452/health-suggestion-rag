from typing import List, Dict

class RAGEngine:
    def __init__(self, embedding_model, document_store, llm_model):
        self.embedding_model = embedding_model
        self.document_store = document_store
        self.llm_model = llm_model

    def retrieve_relevant_documents(self, query: str, k: int = 5) -> List[Dict]:
        query_embedding = self.embedding_model.encode(query)
        return self.document_store.search(query_embedding, k=k)

    def generate_response(self, query: str, context_docs: List[Dict]) -> str:
        context = self._prepare_context(context_docs)
        prompt = self._create_prompt(query, context)
        return self.llm_model.generate(prompt)

    def _prepare_context(self, documents: List[Dict]) -> str:
        return "\n".join(doc['content'] for doc in documents)