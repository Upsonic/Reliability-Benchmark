# Reliability-Benchmark

## 📊 Results

LLM output reliability is critical, particularly for numerical operations and action execution. Upsonic addresses this through a multi-layered reliability system, enabling control agents and verification rounds to ensure output accuracy.

Upsonic is a reliability-focused framework. The results in the table were generated with a small dataset. They show success rates in the transformation of JSON keys. No hard-coded changes were made to the frameworks during testing; only the existing features of each framework were activated and run. GPT-4o was used in the tests.

10 transfers were performed for each section. The numbers show the error count. So if it says 7, it means 7 out of 10 were done **incorrectly**. The table has been created based on initial results. We are expanding the dataset. The tests will become more reliable after creating a larger test set. Reliability benchmark [repo](https://github.com/Upsonic/Reliability-Benchmark)


| Name     | Reliability Score % | ASIN Code | HS Code | CIS Code | Marketing URL | Usage URL | Warranty Time | Policy Link | Policy Description |
|-----------|--------------------|-----------|---------|----------|---------------|-----------|---------------|-------------|----------------|
 **Upsonic**   |**99.3**      |0         |1       |0        |0             |0         |0             |0           |0                   |
| **CrewAI**    |**87.5**       |0         |3       |2        |1             |1         |0             |1           |2                   |
| **Langgraph** |**6.3**      |10        |10      |7        |10            |8         |10            |10          |10                  |


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




