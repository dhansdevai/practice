# LangChain Introduction Exercises

A hands-on introduction to building applications with LangChain and LangChain
Expression Language (LCEL). The exercises progress from a minimal model call
to reusable components, structured output, routing, parallel execution, and
callback-based debugging.

## Learning chapters

| Chapter | Notebook | Exercise |
| --- | --- | --- |
| 01 - LangChain fundamentals | `01/demos/01-minimal-langchain-setup.ipynb` | Install LangChain, load an OpenAI API key from `.env`, configure `ChatOpenAI`, and run a minimal prompt to verify the setup end to end. |
| 01 - LangChain fundamentals | `01/demos/02-building-blocks-imperative.ipynb` | Break an application into prompt, model, parser, and callback components. Build an imperative support-ticket workflow and convert model output into a Python dictionary. |
| 02 - Prompt engineering | `02/demos/03-Building Prompts with PromptTemplate.ipynb` | Compare direct string formatting with `PromptTemplate` and `ChatPromptTemplate`. Reuse variables and chat templates in LCEL prompts. |
| 02 - Prompt engineering | `02/demos/04-Building Example-driven Prompting.ipynb` | Improve support-ticket responses by adding examples and explicit decision patterns to prompts. Compare prompts with few or no examples and reuse one template with new tickets. |
| 02 - Prompt engineering | `02/demos/05-Integrating Templates in Langchain.ipynb` | Compose prompts from reusable system, task, format, and user-input blocks. Use `partial()` to prefill or dynamically provide template values and swap format blocks for modularity. |
| 03 - Chains and workflows | `03/demos/06-Building a Reusable Chain Component.ipynb` | Create a small prompt-to-model-to-string chain with a single responsibility. Reuse the same component for several different ticket inputs. |
| 03 - Chains and workflows | `03/demos/07-Executing a Multi-Step Workflow.ipynb` | Build a workflow that summarizes a ticket, assigns a priority, and recommends an action. Examine each intermediate result before the final result. |
| 03 - Chains and workflows | `03/demos/08-Routing Requests to Different Chains.ipynb` | Route tickets to specialized billing or technical-support chains according to their content. Compare the behavior of two different routes. |
| 03 - Chains and workflows | `03/demos/09-Debugging Workflow Transformations.ipynb` | Trace a summarization-priority-action workflow, identify an underspecified priority transformation, enforce a strict label, and rerun the corrected workflow. |
| 04 - Structured output | `04/demos/10-Applying Built-In Output Parsers.ipynb` | Compare `CommaSeparatedListOutputParser`, `JsonOutputParser`, and `PydanticOutputParser` on the same model response. Observe increasing levels of structure and validation. |
| 04 - Structured output | `04/demos/11-Building a Self-documenting Chain.ipynb` | Define a Pydantic output schema, embed its contract in the prompt, and run a typed chain. Use the resulting typed fields in downstream Python logic. |
| 04 - Structured output | `04/demos/12-Validating Structured Output.ipynb` | Generate deliberately invalid enum output, parse it with a strict Pydantic schema, handle validation failure, and retry with schema instructions. |
| 05 - Execution control | `05/demos/13-Controlling Execution Flow.ipynb` | Run issue extraction and priority classification in parallel with LCEL, then combine the outputs for technical and billing tickets. |
| 05 - Execution control | `05/demos/14-Context and Metadata in Chain.ipynb` | Pass an evolving context dictionary through several workflow steps. Add extracted issues and annotations before generating a final recommendation. |
| 05 - Execution control | `05/demos/15-Debugging Chain Execution.ipynb` | Add a callback handler to trace issue extraction, priority classification, and final action selection. Compare traced execution with a baseline run and inspect intermediate outputs. |

The PDF lecture slides for each chapter are stored beside the demo folders:

- `01/understanding-langchain-fundamentals-and-architecture-slides.pdf`
- `02/designing-and-engineering-prompttemplate-objects-slides.pdf`
- `03/understanding-and-engineering-chains-and-sequential-workflows-slides.pdf`
- `04/understanding-and-applying-output-parsers-for-structured-responses-slides.pdf`
- `05/understanding-data-flow-and-execution-control-in-langchain-slides.pdf`

## Getting started

### 1. Open the project

Open this repository in VS Code or JupyterLab. A Python environment with
Jupyter support is required.

### 2. Install the notebook dependencies

Most notebooks use these packages:

```powershell
python -m pip install -U langchain langchain-openai langchain-core python-dotenv jupyter
```

The notebook named `01-minimal-langchain-setup.ipynb` also performs this
installation interactively with a notebook `pip` command.

### 3. Configure an API key

The exercises call OpenAI through `ChatOpenAI` and require an API key.

Create a `.env` file in the directory used by the notebook:

```text
OPENAI_API_KEY=your_actual_api_key_here
```

The notebooks load the key with `python-dotenv` and do not embed the key in
source code. Never commit `.env` or real credentials. LLM calls may incur
provider usage charges.

### 4. Run the notebooks

Open each notebook in VS Code and select a Python kernel with LangChain
installed. Run the cells from top to bottom because later cells reuse imports,
the model instance, prompts, schemas, and variables created earlier.

## Example concepts demonstrated

- `ChatOpenAI` for chat-model inference
- `ChatPromptTemplate` and `PromptTemplate` for reusable prompts
- Few-shot examples and prompt composition
- `Runnable` pipelines and LCEL using the `|` operator
- Reusable chain components and multi-step workflows
- Routing and parallel execution
- `StrOutputParser`, `JsonOutputParser`, `CommaSeparatedListOutputParser`, and
  Pydantic-based parsing
- Strict output schemas and validation retries
- Context propagation and request metadata
- Callback handlers for execution tracing and debugging
- `partial()` for prefilled or dynamically supplied prompt variables

## Recommended learning order

1. Start with chapter 01 to configure LangChain and understand prompts, models,
   parsers, callbacks, and imperative chain construction.
2. Continue through chapter 02 and compare manual formatting, templates,
   examples, modular prompts, and partial values.
3. In chapter 03, create reusable chains and learn to sequence, route, and debug
   their transformations.
4. In chapter 04, move from unstructured text to lists, JSON, typed Pydantic
   data, enum validation, and retry behavior.
5. Finish chapter 05 by composing parallel branches and tracing context,
   metadata, intermediate values, and callback events.
