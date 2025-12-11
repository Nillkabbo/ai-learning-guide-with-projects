"""
Document Q&A System - Starter Code
Chapter 27 Project

This starter code provides a basic structure for building a RAG system
with document indexing, vector search, and context augmentation.
"""

import os
from typing import List, Dict

# TODO: Import required libraries
# from dotenv import load_dotenv
# import openai
# import chromadb
# from chromadb.config import Settings


class RAGSystem:
    """RAG-powered document Q&A system."""
    
    def __init__(self):
        """Initialize RAG system."""
        # TODO: Initialize vector database
        # TODO: Initialize OpenAI client
        # TODO: Initialize embedding model
        pass
    
    def index_document(self, document_path: str):
        """
        Index a document into vector database.
        
        Args:
            document_path: Path to document
        """
        # TODO: Load document
        # TODO: Chunk document
        # TODO: Generate embeddings
        # TODO: Store in vector DB
        pass
    
    def retrieve_context(self, query: str, top_k: int = 3) -> List[str]:
        """
        Retrieve relevant context for query.
        
        Args:
            query: User query
            top_k: Number of results
            
        Returns:
            List of relevant chunks
        """
        # TODO: Embed query
        # TODO: Search vector DB
        # TODO: Return top-k chunks
        return []
    
    def answer_question(self, query: str) -> str:
        """
        Answer question using RAG.
        
        Args:
            query: User question
            
        Returns:
            Answer with context
        """
        # TODO: Retrieve context
        # TODO: Augment prompt
        # TODO: Generate answer
        # TODO: Return answer with citations
        return "TODO: Answer"


def main():
    """Main function."""
    print("📚 Document Q&A System")
    print("Type 'quit' to exit\n")
    
    # TODO: Initialize RAG system
    # rag = RAGSystem()
    
    # TODO: Index documents
    # TODO: Implement Q&A loop


if __name__ == "__main__":
    main()
