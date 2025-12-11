"""
Document Q&A System - Complete Solution
Chapter 27 Project

Demonstrates RAG: document indexing, vector search, context augmentation, answer generation.
"""

import os
from typing import List, Dict
from dotenv import load_dotenv

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import chromadb
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False

load_dotenv()


class RAGSystem:
    """RAG-powered document Q&A system."""
    
    def __init__(self):
        """Initialize RAG system."""
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or not OPENAI_AVAILABLE:
            raise ValueError("OpenAI API key required")
        
        self.client = openai.OpenAI(api_key=api_key)
        
        # Initialize vector database
        if CHROMADB_AVAILABLE:
            self.chroma_client = chromadb.Client()
            self.collection = self.chroma_client.create_collection(name="documents")
        else:
            self.chroma_client = None
            self.collection = None
            # Fallback: in-memory storage
            self.documents = []
    
    def index_document(self, text: str, doc_id: str = None):
        """Index a document into vector database."""
        # Chunk document (simple chunking)
        chunk_size = 500
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        
        # Generate embeddings
        try:
            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=chunks
            )
            embeddings = [item.embedding for item in response.data]
            
            # Store in vector DB
            if self.collection:
                self.collection.add(
                    embeddings=embeddings,
                    documents=chunks,
                    ids=[f"{doc_id}_{i}" for i in range(len(chunks))]
                )
            else:
                # Fallback storage
                for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
                    self.documents.append({
                        "id": f"{doc_id}_{i}",
                        "text": chunk,
                        "embedding": emb
                    })
        except Exception as e:
            print(f"Error indexing document: {e}")
    
    def retrieve_context(self, query: str, top_k: int = 3) -> List[str]:
        """Retrieve relevant context for query."""
        try:
            # Embed query
            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=[query]
            )
            query_embedding = response.data[0].embedding
            
            # Search vector DB
            if self.collection:
                results = self.collection.query(
                    query_embeddings=[query_embedding],
                    n_results=top_k
                )
                return results['documents'][0] if results['documents'] else []
            else:
                # Simple similarity search (fallback)
                import numpy as np
                similarities = []
                for doc in self.documents:
                    sim = np.dot(query_embedding, doc["embedding"])
                    similarities.append((sim, doc["text"]))
                similarities.sort(reverse=True)
                return [text for _, text in similarities[:top_k]]
        except Exception as e:
            print(f"Error retrieving context: {e}")
            return []
    
    def answer_question(self, query: str) -> str:
        """Answer question using RAG."""
        # Retrieve context
        context_chunks = self.retrieve_context(query, top_k=3)
        context = "\n\n".join(context_chunks) if context_chunks else "No relevant context found."
        
        # Augment prompt with context
        prompt = f"""Answer the question using the following context. If the context doesn't contain the answer, say so.

Context:
{context}

Question: {query}

Answer:"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
            return answer
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function."""
    print("📚 Document Q&A System")
    print("Type 'quit' to exit\n")
    
    try:
        rag = RAGSystem()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Index sample document
    sample_doc = """
    IoT devices are connected devices that can collect and exchange data.
    Common IoT protocols include MQTT, CoAP, and HTTP.
    Temperature sensors typically measure between -40°C and 125°C.
    Humidity sensors measure relative humidity from 0% to 100%.
    """
    print("Indexing sample document...")
    rag.index_document(sample_doc, doc_id="iot_guide")
    print("Document indexed!\n")
    
    while True:
        try:
            query = input("Question (or 'quit'): ").strip()
            if query.lower() == 'quit':
                break
            
            if not query:
                continue
            
            answer = rag.answer_question(query)
            print(f"\nAnswer: {answer}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()
