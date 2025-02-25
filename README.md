# Reliability-Benchmark

## How can I run the benchmark?

1. Clone the repository

```bash
git clone https://github.com/Upsonic/Reliability-Benchmark.git
```

2. Install the dependencies and create an environment

```bash
pip install uv
uv venv
uv sync
```

3. Run the benchmark

```bash
uv run run_benchmark.py
```

4. Compare the results

```bash
streamlit run compare_results.py
```




