import streamlit as st
import json
import os

st.set_page_config(layout="wide", page_title="Model Comparison")

st.title("Agent Framework Comparison")

def load_results():
    try:
        with open('results/all_products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Results file not found. Please run generate_results.py first to generate the model results.")
        st.stop()

def display_json_diff(data1, data2, path=""):
    differences = []
    if isinstance(data1, dict) and isinstance(data2, dict):
        all_keys = set(data1.keys()) | set(data2.keys())
        for key in all_keys:
            new_path = f"{path}.{key}" if path else key
            if key not in data1:
                differences.append((new_path, "Missing in first", "N/A", data2[key]))
            elif key not in data2:
                differences.append((new_path, "Missing in second", data1[key], "N/A"))
            else:
                differences.extend(display_json_diff(data1[key], data2[key], new_path))
    elif data1 != data2:
        differences.append((path, "Value mismatch", data1, data2))
    return differences

# Check if results directory exists
if not os.path.exists('results'):
    st.warning("No results directory found. Please run the following command first:")
    st.code("python generate_results.py")
    st.stop()

# Load all results
all_results = load_results()

# Product selector
st.sidebar.title("Product Selection")
selected_product = st.sidebar.selectbox(
    "Choose a product to analyze",
    list(all_results.keys())
)

# Get results for selected product
results = all_results[selected_product]

# Display product info
st.header(f"Analyzing: {selected_product}")

# Create tabs for different comparison views
tab1, tab2 = st.tabs(["Side by Side", "Differences"])

with tab1:
    # Side by side comparison
    cols = st.columns(len(results))
    for col, (model_name, result) in zip(cols, results.items()):
        with col:
            st.subheader(model_name)
            st.json(result)

with tab2:
    # Differences view
    st.subheader("Compare Models")
    col1, col2 = st.columns(2)
    with col1:
        model1 = st.selectbox("Select first model", list(results.keys()), key="model1")
    with col2:
        model2 = st.selectbox("Select second model", list(results.keys()), key="model2")
    
    if model1 and model2:
        differences = display_json_diff(results[model1], results[model2])
        if differences:
            st.write(f"Differences between {model1} and {model2}:")
            for path, diff_type, val1, val2 in differences:
                with st.expander(f"Difference in: {path}"):
                    st.write(f"**Type:** {diff_type}")
                    if diff_type == "Value mismatch":
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"{model1}:", val1)
                        with col2:
                            st.write(f"{model2}:", val2)
        else:
            st.success("No differences found between the models!")

# Add metrics/statistics section
st.sidebar.markdown("---")
st.sidebar.subheader("Statistics")
total_products = len(all_results)
total_models = len(results)
st.sidebar.metric("Total Products", total_products)
st.sidebar.metric("Models per Product", total_models)

# Add CSS to improve the visual appearance
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-bottom: 1rem;
    }
    .json-output {
        max-height: 500px;
        overflow-y: auto;
    }
    .stSidebar {
        background-color: #f0f2f6;
        padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True) 