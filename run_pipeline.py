import sys
import os

# Append the absolute path of the fintech platform to the runtime system path
current_dir = os.path.dirname(os.path.abspath(__file__))
platform_path = os.path.join(current_dir, "fintech-data-platform")
sys.path.append(platform_path)

# Execute the core orchestration function directly
from src.main import run_platform_pipeline

if __name__ == "__main__":
    run_platform_pipeline()
