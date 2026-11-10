# DocGenius — Revolutionizing PDFs with AI

## Introduction

DocGenius is an AI-powered PDF question-answering application that allows users to upload any PDF document and interact with it using natural language. Instead of manually reading through large documents, users can simply ask questions and receive precise, context-aware answers in seconds. The application combines the power of large language models with semantic search to understand and retrieve relevant information from PDF files.

---

## Objectives

- Enable users to **upload any PDF** and extract meaningful information through conversation
- Provide **accurate, context-grounded answers** strictly based on the document content
- Build a **simple, accessible web interface** that requires no technical knowledge to use
- Leverage **free and open LLMs** to keep the application cost-effective

---

## Tools & Technologies Used

| Category | Tool / Library | Purpose |
|---|---|---|
| **Frontend** | Streamlit | Web UI for uploading PDFs and displaying answers |
| **PDF Parsing** | PyPDF2 | Extracting raw text from PDF files |
| **Text Splitting** | LangChain `CharacterTextSplitter` | Breaking large text into manageable chunks |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` | Converting text chunks into vector representations |
| **Vector Store** | FAISS | Storing and searching embeddings efficiently |
| **LLM** | Groq — `llama-3.3-70b-versatile` | Generating natural language answers |
| **LLM Integration** | LangChain | Chaining the retrieval and generation steps |
| **Environment** | python-dotenv | Managing API keys securely via `.env` |
| **Language** | Python 3.9+ | Core programming language |

---

## How the Project Works

The application follows a **Retrieval-Augmented Generation (RAG)** pipeline:

```
PDF Upload → Text Extraction → Chunking → Embedding → Vector Store
                                                            ↓
                                User Question → Similarity Search → LLM → Answer
```

### Step-by-step breakdown:

1. **PDF Upload**  
   The user uploads a PDF file through the Streamlit interface.

2. **Text Extraction**  
   PyPDF2 reads the PDF and extracts all the raw text from every page.

3. **Text Chunking**  
   The extracted text is split into smaller overlapping chunks (1000 characters each, 200 overlap) using LangChain's `CharacterTextSplitter`.  This overlap ensures context is not lost between chunks.

4. **Embedding Generation**  
   Each chunk is converted into a numerical vector (embedding) using the HuggingFace `all-MiniLM-L6-v2` model. These embeddings capture the semantic meaning of the text.

5. **Vector Store (FAISS)**  
   All embeddings are stored in a FAISS vector database, which enables fast similarity search.

6. **User Question**  
   The user types a question in the text box.

7. **Semantic Search**  
   The question is also embedded and compared against all stored chunk embeddings. The most semantically similar chunks are retrieved.

8. **Answer Generation**  
   The retrieved chunks along with the user question are passed to the **Llama 3.3 70B** model via Groq. The LLM reads the context and generates a precise answer.

9. **Display**  
   The answer is displayed on the Streamlit page.

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/KalyanMurapaka45/DocGenius-Revolutionizing-PDFs-with-AI.git
   cd DocGenius-Revolutionizing-PDFs-with-AI
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv myenv
   source myenv/bin/activate   # On Windows: myenv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up your API key**  
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   Get a free Groq API key at [console.groq.com](https://console.groq.com)

4. **Run the application**
   ```bash
   streamlit run DocGenius/PDFChat.py
   ```
   Open your browser at `http://localhost:8501`

---

## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
