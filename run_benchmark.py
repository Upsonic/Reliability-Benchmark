import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from reliability_benchmark.generate_results import generate_and_save_results

generate_and_save_results()