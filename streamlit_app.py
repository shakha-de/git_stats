import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Git Repository Analytics",
    layout="wide",
)

st.title("📊 Git Repository Analytics")
st.caption("Analyse von `git log --numstat --format=\"%H %ct %an\"`")

# ---------- Upload ----------
uploaded_file = st.file_uploader(
    "gitlog.txt hochladen",
    type="txt"
)

if not uploaded_file:
    st.info("⬆️ Bitte lade eine gitlog.txt Datei hoch")
    st.stop()

# ---------- Parsing ----------
commits = []
current = None

for raw_line in uploaded_file:
    line = raw_line.decode("utf-8").strip()
    if not line:
        continue

    parts = line.split()

    # Commit header
    if len(parts) >= 3 and len(parts[0]) == 40:
        if current:
            commits.append(current)
        current = {
            "hash": parts[0],
            "timestamp": int(parts[1]),
            "author": " ".join(parts[2:]),
            "added": 0,
            "deleted": 0,
        }

    # Numstat
    elif current and parts[0].isdigit() and parts[1].isdigit():
        current["added"] += int(parts[0])
        current["deleted"] += int(parts[1])

if current:
    commits.append(current)

df = pd.DataFrame(commits)
df["date"] = pd.to_datetime(df["timestamp"], unit="s")
df["net"] = df["added"] - df["deleted"]

# ---------- Sidebar ----------
st.sidebar.header("🔎 Filter")

authors = st.sidebar.multiselect(
    "Autor:innen",
    sorted(df["author"].unique()),
    default=sorted(df["author"].unique())
)

date_range = st.sidebar.date_input(
    "Zeitraum",
    (df["date"].min().date(), df["date"].max().date())
)

filtered = df[
    (df["author"].isin(authors)) &
    (df["date"].dt.date >= date_range[0]) &
    (df["date"].dt.date <= date_range[1])
]

# ---------- KPIs ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Commits", len(filtered))
c2.metric("Lines Added", int(filtered["added"].sum()))
c3.metric("Lines Deleted", int(filtered["deleted"].sum()))
c4.metric("Net Growth", int(filtered["net"].sum()))

st.divider()

# ---------- Commits over Time ----------
st.subheader("📈 Commits über Zeit")

commits_per_day = (
    filtered
    .groupby(filtered["date"].dt.date)
    .size()
    .rename("Commits")
)

st.line_chart(commits_per_day)

# ---------- Lines Changed ----------
st.subheader("🧮 Code-Änderungen")

lines_per_day = (
    filtered
    .groupby(filtered["date"].dt.date)[["added", "deleted"]]
    .sum()
)

st.area_chart(lines_per_day)

# ---------- Activity by Author ----------
st.subheader("👩‍💻 Aktivität pro Autor")

author_stats = (
    filtered
    .groupby("author")[["added", "deleted"]]
    .sum()
    .sort_values(by="added", ascending=False)
)

st.bar_chart(author_stats)

# ---------- Cumulative Growth ----------
st.subheader("📈 Kumulatives Code-Wachstum")

growth = filtered.sort_values("date")
growth["cumulative_net"] = growth["net"].cumsum()

st.line_chart(
    growth.set_index("date")["cumulative_net"]
)

# ---------- Raw Data ----------
with st.expander("📄 Rohdaten anzeigen"):
    st.dataframe(filtered)
