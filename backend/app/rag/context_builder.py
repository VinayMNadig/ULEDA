from app.rag.retriever import retrieve


def build_context(question):

    return retrieve(question)