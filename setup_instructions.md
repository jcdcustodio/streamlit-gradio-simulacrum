### How to set-up repo

**Preliminary**
1. Download the `uv` package manager. [Link](https://docs.astral.sh/uv/#highlights)
2. Download this repository and install it locally on your machine.

**Instruction Proper**
1. Ensure the current folder is `dssoc-streamlit-gradio-talk`
2. Double-check if the `pyproject.toml` is visible in your folder.
3. **Instantiate the virtual environment**: Run `uv venv` from your folder.
4. **Switch onto the virtual environment**: Type `source .venv/bin/activate`
5. Type `uv sync` to sync the dependencies of the environment according to your `pyproject.toml`

**Switching versions (Between Gradio and Streamlit)**
1. From `pyproject.toml`, take note of the "optional-dependencies" that are visible at the bottom of the configurations
```python
streamlit_build = [
  "streamlit"
]
gradio_build = [
  "gradio"
]
```

The optional-dependencies are grouped and labeled accordingly.

2. To switch to the Streamlit build, type `uv sync --extra streamlit_build`
3. To switch to the Gradio build, type `uv sync --extra gradio_build`

### Launching the application
1. Streamlit

- `streamlit run [application_file_name.py]`

2. Gradio

- `python3 [application_file_name.py]`