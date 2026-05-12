import typer
from rich.console import Console

from enterprise_rag.answering import AnswerEngine
from enterprise_rag.chunking import chunk_document
from enterprise_rag.sample_data import sample_documents

app = typer.Typer(help='Enterprise RAG CLI')
console = Console()


def build_engine() -> AnswerEngine:
    chunks = []
    for document in sample_documents():
        chunks.extend(chunk_document(document, chunk_size=80))
    return AnswerEngine(chunks)


@app.command()
def ask(query: str = 'What security controls are required?') -> None:
    engine = build_engine()
    response = engine.answer(query)
    console.print_json(data=response.model_dump())


@app.command()
def demo() -> None:
    engine = build_engine()
    response = engine.answer('How should ML services be operated?')
    console.print_json(data=response.model_dump())
