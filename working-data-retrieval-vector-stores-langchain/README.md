# Working with Data Retrieval and Vector Stores in LangChain

A collection of Python demos covering the data ingestion and retrieval stages
of a LangChain application. The course progresses from loading and splitting
documents through embeddings, vector stores, retrievers, RAG, and hybrid
structured/unstructured querying.

## Course roadmap

### Module 1 — Document loaders and data ingestion

Practice loading documents from files and external sources, exploring document
content and metadata, and handling large directories of files.

| Exercise | What it covers |
| --- | --- |
| [clip3_1_textloader.py](01/demos/Module1/module1/clip3_1_textloader.py) | Load a UTF-8 text file with `TextLoader` and inspect its content and metadata. |
| [clip3_2_csvloader.py](01/demos/Module1/module1/clip3_2_csvloader.py) | Load CSV rows as LangChain documents. |
| [clip3_3_pdfloader.py](01/demos/Module1/module1/clip3_3_pdfloader.py) | Load a PDF and inspect the resulting document content. |
| [clip4_1_webloader.py](01/demos/Module1/module1/clip4_1_webloader.py) | Fetch multiple web pages and examine the documents created from them. |
| [clip4_2_wikpedia.py](01/demos/Module1/module1/clip4_2_wikpedia.py) | Retrieve Wikipedia article content as documents. |
| [clip4_3_arxiv.py](01/demos/Module1/module1/clip4_3_arxiv.py) | Search arXiv and load paper content and metadata. |
| [clip5_1_text_directory.py](01/demos/Module1/module1/clip5_1_text_directory.py) | Load multiple text files from a directory. |
| [clip5_2_pdf_directory.py](01/demos/Module1/module1/clip5_2_pdf_directory.py) | Load PDFs from a directory as documents. |
| [clip5_3_text_pdf.py](01/demos/Module1/module1/clip5_3_text_pdf.py) | Load text and PDF files together from a directory. |
| [clip5_4_error_progress.py](01/demos/Module1/module1/clip5_4_error_progress.py) | Process a directory of PDFs while tracking progress and skipping problematic files. |
| [clip6_1_lazyload.py](01/demos/Module1/module1/clip6_1_lazyload.py) | Use lazy loading to iterate through PDFs without loading the entire collection at once. |

Sample text, CSV, PDF, and other files are in [Module 1's data folder](01/demos/Module1/data).

### Module 2 — Text splitting strategies

Explore how chunk size, overlap, document structure, and programming language
affect the chunks produced for downstream retrieval.

| Exercise | What it covers |
| --- | --- |
| [clip3_1_char_split.py](02/demos/Module2/module2/clip3_1_char_split.py) | Split text into chunks with `CharacterTextSplitter`. |
| [clip3_2_doc_split.py](02/demos/Module2/module2/clip3_2_doc_split.py) | Split loaded documents and inspect chunk content and preserved metadata. |
| [clip4_1_rec_split.py](02/demos/Module2/module2/clip4_1_rec_split.py) | Use `RecursiveCharacterTextSplitter` to make size-controlled chunks. |
| [clip5_1_rec_overlap.py](02/demos/Module2/module2/clip5_1_rec_overlap.py) | Add overlap between chunks to preserve context at boundaries. |
| [clip6_1_md_split.py](02/demos/Module2/module2/clip6_1_md_split.py) | Split Markdown according to header hierarchy. |
| [clip6_2_md_rec_split.py](02/demos/Module2/module2/clip6_2_md_rec_split.py) | Combine Markdown-aware splitting with recursive size-based splitting. |
| [clip6_3_html_script.py](02/demos/Module2/module2/clip6_3_html_script.py) | Split HTML into sections using header tags. |
| [clip6_4_code_split.py](02/demos/Module2/module2/clip6_4_code_split.py) | Split Python and C code using language-aware separators. |

### Module 3 — Embeddings and vector representations

Generate vector representations for queries and documents, rank documents by
similarity, and evaluate retrieval quality with common top-k metrics.

| Exercise | What it covers |
| --- | --- |
| [clip2_1_openai_embed.py](03/demos/Module3/clip2_1_openai_embed.py) | Create query and document embeddings with OpenAI. |
| [clip2_2_gemini_embed.py](03/demos/Module3/clip2_2_gemini_embed.py) | Create query and document embeddings with Google Gemini. |
| [clip4_1_similarity_rank.py](03/demos/Module3/clip4_1_similarity_rank.py) | Compute cosine similarity and rank documents against a query. |
| [clip6_1_eval_metrics.py](03/demos/Module3/clip6_1_eval_metrics.py) | Evaluate ranked results using recall@k and precision@k against known relevant documents. |

### Module 4 — Vector stores and similarity search

Store embeddings, search for similar documents, persist indexes, filter on
metadata, and compare similarity search with maximal marginal relevance (MMR).

| Exercise | What it covers |
| --- | --- |
| [clip3_1_FAISS.py](04/demos/Module4/clip3_1_FAISS.py) | Create a local FAISS store, add/search/delete/update documents, and save the index. |
| [clip3_2_load_FAISS.py](04/demos/Module4/clip3_2_load_FAISS.py) | Load a saved FAISS store and search it. |
| [clip4_1_Pinecone.py](04/demos/Module4/clip4_1_Pinecone.py) | Create a Pinecone index and add, search, delete, and update documents. |
| [clip4_2_load_texfile.py](04/demos/Module4/clip4_2_load_texfile.py) | Load and split a text file, index it in Pinecone, and search it. |
| [clip5_1_FAISS_search.py](04/demos/Module4/clip5_1_FAISS_search.py) | Search a saved FAISS store and inspect similarity scores. |
| [clip5_2_Pinecone_search.py](04/demos/Module4/clip5_2_Pinecone_search.py) | Search a Pinecone vector store and inspect similarity results and scores. |
| [clip6_1_metadata.py](04/demos/Module4/clip6_1_metadata.py) | Compare regular similarity search with metadata-filtered search. |
| [clip7_1_mmr.py](04/demos/Module4/clip7_1_mmr.py) | Compare similarity search with MMR for more varied results. |

### Module 5 — Retrievers and advanced retrieval strategies

Compare keyword and vector retrieval, build RAG pipelines, and improve
retrieval with query expansion and contextual compression.

| Exercise | What it covers |
| --- | --- |
| [clip2_1_BM25.py](05/demos/Module5/clip2_1_BM25.py) | Retrieve documents using the BM25 keyword-ranking algorithm. |
| [clip2_2_wikipedia.py](05/demos/Module5/clip2_2_wikipedia.py) | Retrieve relevant Wikipedia results for a query. |
| [clip2_3_RAG.py](05/demos/Module5/clip2_3_RAG.py) | Retrieve Wikipedia context and ask an LLM to answer from that context. |
| [clip2_4_customRetriever.py](05/demos/Module5/clip2_4_customRetriever.py) | Implement a simple custom retriever using keyword matching. |
| [clip2_5_vectorstoreRetriever.py](05/demos/Module5/clip2_5_vectorstoreRetriever.py) | Explore vector-store retriever options, including top-k, filters, MMR, and score thresholds. |
| [clip2_6_RAG.py](05/demos/Module5/clip2_6_RAG.py) | Build an end-to-end RAG pipeline over a local story using chunking, FAISS, and an LLM. |
| [clip3_1_multiQuery.py](05/demos/Module5/clip3_1_multiQuery.py) | Use `MultiQueryRetriever` to generate alternate search queries and broaden retrieval. |
| [clip3_2_multiQueryLCEL.py](05/demos/Module5/clip3_2_multiQueryLCEL.py) | Build a multi-query retriever in LCEL and merge unique retrieved documents. |
| [clip4_1_compress.py](05/demos/Module5/clip4_1_compress.py) | Apply contextual compression to filter and shorten retrieved content. |
| [clip4_2_compressLCEL.py](05/demos/Module5/clip4_2_compressLCEL.py) | Implement a custom compression retriever with LCEL and compare it with the base retriever. |

### Module 6 — Structured and hybrid querying

Use natural-language questions with a SQL database, add query safety and
verification steps, and combine structured database queries with document
retrieval.

| Exercise | What it covers |
| --- | --- |
| [Clip1_1_create_db.py](06/demos/Module6/Clip1_1_create_db.py) | Create and populate a SQLite database with sample sales data. |
| [Clip2_1_LCEL.py](06/demos/Module6/Clip2_1_LCEL.py) | Build an LCEL pipeline that generates SQL, executes it, and synthesizes an answer. |
| [Clip2_2_create_agent.py](06/demos/Module6/Clip2_2_create_agent.py) | Use a tool-enabled agent to query the SQL database and answer questions. |
| [Clip3_1_validateLCEL.py](06/demos/Module6/Clip3_1_validateLCEL.py) | Add a validation layer to an LCEL SQL pipeline before executing a query. |
| [Clip3_2_agent_safetool.py](06/demos/Module6/Clip3_2_agent_safetool.py) | Wrap the agent's SQL execution tool with validation checks. |
| [Clip4_1_LLMchecker.py](06/demos/Module6/Clip4_1_LLMchecker.py) | Use an LLM-based SQL checker to review and correct generated queries. |
| [Clip4_2_resultverify.py](06/demos/Module6/Clip4_2_resultverify.py) | Validate query results as part of the SQL question-answering pipeline. |
| [Clip5_1.create_FAISS.py](06/demos/Module6/Clip5_1.create_FAISS.py) | Create and persist a local FAISS vector store from sample documents. |
| [Clip5_2_hybrid_LCEL.py](06/demos/Module6/Clip5_2_hybrid_LCEL.py) | Route questions through an LCEL pipeline to SQL or unstructured document retrieval. |
| [Clip5_3_hybrid_Agent.py](06/demos/Module6/Clip5_3_hybrid_Agent.py) | Build an agent that combines safe SQL querying with document retrieval. |

## Getting started

### Requirements

- Python 3.10 or later.
- The Python dependencies for each module are listed separately in that
  module's `requirements.txt`.
- Some exercises call hosted embedding or chat-model services and require
  credentials. The examples use OpenAI (`OPENAI_API_KEY`); the Gemini embedding
  example uses Google GenAI credentials; Pinecone examples also need
  `PINECONE_API_KEY`.

### Install a module's dependencies

Run these commands from the module folder you want to explore. For example,
from the repository root, set up Module 1 with PowerShell:

```powershell
Set-Location .\01\demos\Module1
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Repeat with the corresponding folder under `02\demos\Module2` through
`06\demos\Module6` to install that module's `requirements.txt`. In VS Code,
select the module's `.venv` Python interpreter (and notebook kernel, if using a
notebook) so execution uses the environment where the dependencies were
installed.

### Configure credentials

Set the key(s) needed by the exercise as environment variables, or create a
local `.env` file in the module's demo folder. Never commit real API keys.
Some modules already contain local `.env` files; keep credentials private and
do not overwrite or share them.

### Run the demos

Run the Python scripts from their demo directories. A few loader and splitter
scripts refer to sample files using paths relative to their own subfolder:

- Module 1 scripts are under `01\demos\Module1\module1`; run them with that
  directory as the working directory.
- Module 2 scripts are under `02\demos\Module2\module2`; run them with that
  directory as the working directory.
- Modules 3–6 scripts are directly in their respective `demos\ModuleX`
  folders; run them from there.

For example:

```powershell
Set-Location .\01\demos\Module1\module1
..\.venv\Scripts\python.exe .\clip3_1_textloader.py
```

Many demos call external APIs, so they need network access and can incur usage
charges. FAISS exercises create or load local index files; the Module 6
hybrid-query examples also use the included SQLite database and FAISS index.

## Slides

Each module includes a PDF companion deck:

1. [Document loaders and data ingestion](01/document-loaders-and-data-ingestion-in-langchain-slides.pdf)
2. [Text splitting strategies](02/text-splitting-strategies-slides.pdf)
3. [Embeddings and vector representations](03/understanding-embeddings-and-vector-representations-slides.pdf)
4. [Vector stores and scalable similarity search](04/vector-stores-and-scalable-similarity-search-slides.pdf)
5. [Retrievers and advanced retrieval strategies](05/retrievers-and-advanced-retrieval-strategies-in-langchain-slides.pdf)
6. [Structured and hybrid querying](06/structured-and-hybrid-querying-with-langchain-slides.pdf)