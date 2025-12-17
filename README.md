# git_stats

Analyse/Visualise git logs with Streamlit.

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Input file format (gitlog.txt)

Generate a compatible file from any git repo:

```bash
git log --numstat --format="%H %ct %an" > gitlog.txt
```

Then upload `gitlog.txt` in the app UI.

## Deploy to Streamlit Community Cloud

- Push this repository to GitHub.
- In Streamlit Cloud, create a new app from the repo.
- Set **Main file path** to `streamlit_app.py`.
- Streamlit Cloud will install dependencies from `requirements.txt` and use `runtime.txt` for the Python version.
