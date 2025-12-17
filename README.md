# git_stats

Kleine Streamlit-App, die eine `git log --numstat`-Ausgabe analysiert und als Dashboard visualisiert.

## Live-App

https://gitlogs.streamlit.app/

## Nutzung

1. In einem Git-Repository eine kompatible Datei erzeugen:

```bash
git log --numstat --format="%H %ct %an" > gitlog.txt
```

2. In der App `gitlog.txt` hochladen.

## Eingabeformat (gitlog.txt)

Die Datei besteht aus wiederholten Blöcken:

- Kopfzeile pro Commit: `<40-hex-hash> <unix-timestamp> <author name>`
- Danach beliebig viele `--numstat`-Zeilen: `<added> <deleted> <path>`

Beispiel:

```
<hash> <timestamp> <author>
12 3 src/foo.py
0 1 README.md
```

## Lokal starten

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deployment (Streamlit Community Cloud)

- **Main file path**: `streamlit_app.py`
- Python-Version: `runtime.txt`
- Dependencies: `requirements.txt`

## English

# git_stats

Small Streamlit app that analyzes `git log --numstat` output and visualizes it as a dashboard.

## Live App

https://gitlogs.streamlit.app/

## Usage

1. Generate a compatible file from any Git repository:

```bash
git log --numstat --format="%H %ct %an" > gitlog.txt
```

2. Upload `gitlog.txt` in the app UI.

## Input Format (gitlog.txt)

The file consists of repeated blocks:

- Header per commit: `<40-hex-hash> <unix-timestamp> <author name>`
- Followed by any number of `--numstat` lines: `<added> <deleted> <path>`

Example:

```
<hash> <timestamp> <author>
12 3 src/foo.py
0 1 README.md
```

## Local Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deployment (Streamlit Community Cloud)

- **Main file path**: `streamlit_app.py`
- Python version: `runtime.txt`
- Dependencies: `requirements.txt`
