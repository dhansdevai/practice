# Python and Generative AI Exercises

A hands-on collection of Python lessons and small AI projects. The exercises
start with Python fundamentals, then build toward LLM-powered chatbots,
structured outputs, APIs, and a complete review-analysis application.

## Exercise roadmap

| Folder | Topics |
| --- | --- |
| `python-ai-exercise/1_datatypes_functions` | Data types, lists, loops, dictionaries, tuples, and conditionals |
| `python-ai-exercise/2_functions` | Functions, type hints, `*args` / `**kwargs`, and a chai bill calculator |
| `python-ai-exercise/3_classes_overview` | Classes, objects, methods, and Pydantic models |
| `python-ai-exercise/4_call_llm` | Calling a large language model and generating a recipe |
| `python-ai-exercise/5_error_handling` | Tracebacks, common errors, and `try` / `except` |
| `python-ai-exercise/6_chatbot_memory` | Conversation history and a Streamlit movie-recommendation buddy |
| `python-ai-exercise/7_structured_output` | Getting validated, structured data from an LLM |
| `python-ai-exercise/8_files` | Reading and writing files, and analyzing document content |
| `python-ai-exercise/9_calling_apis` | Calling web APIs and using live data |
| `python-ai-exercise/10_fastapi` | Building an API with FastAPI and structured LLM output |
| `python-ai-exercise/11_databases` | Saving and retrieving data with SQLite |
| `python-ai-exercise/12_project_feedback_analyzer` | A feedback-analysis service, Streamlit dashboard, and SQLite history |

Most lessons are Jupyter notebooks. The `app.py` files are runnable applications
that let you try the ideas interactively.

## Getting started

1. Open a lesson notebook (`.ipynb`) in VS Code with the Jupyter extension, or
   use JupyterLab.
2. Select a Python environment with the packages needed by that lesson.
3. For projects with a `pyproject.toml`, install their dependencies from the
   project folder with [uv](https://docs.astral.sh/uv/):

   ```powershell
   cd python-ai-exercise\10_fastapi
   uv sync
   ```

   The feedback-analyzer project also has its own `pyproject.toml`:

   ```powershell
   cd python-ai-exercise\12_project_feedback_analyzer
   uv sync
   ```

4. Configure the API key required by the exercise. Depending on the code, this
   may be `OPENAI_API_KEY` or `GOOGLE_API_KEY`. Put secrets in a local `.env`
   file or environment variable; never commit real API keys.

The project manifests list dependencies for their respective projects. Other
lessons may need packages installed in the selected notebook environment.

## Run the Streamlit apps

From the repository root, start the recipe generator:

```powershell
python -m streamlit run python-ai-exercise\4_call_llm\app.py
```

Start the movie-recommendation buddy with:

```powershell
python -m streamlit run python-ai-exercise\6_chatbot_memory\app.py
```

These apps use LangChain's OpenAI integration and need an `OPENAI_API_KEY`.
The movie buddy also looks for a `.env` file in `python-ai-exercise\4_call_llm`.

## Run the feedback analyzer

The feedback analyzer has a FastAPI backend and a Streamlit frontend. Open two
terminals in `python-ai-exercise\12_project_feedback_analyzer`.

In the first terminal, start the API:

```powershell
uv run fastapi dev api.py
```

In the second terminal, start the dashboard:

```powershell
uv run streamlit run app.py
```

The dashboard opens in your browser and sends reviews to the local API. The API
documentation and interactive endpoint tester are available at
`http://127.0.0.1:8000/docs`. This project uses an OpenAI API key.

## Learning by experimenting

Run notebook cells in order, change the examples, and try the exercises in each
lesson. LLM-powered examples may send prompts to an external provider and can
incur usage charges, so keep your API key private and check your provider's
pricing and usage limits.
