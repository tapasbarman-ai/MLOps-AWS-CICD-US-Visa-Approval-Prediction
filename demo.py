# US Visa prediction pipeline entrypoint and testing playground
import os
import sys

# Load environment variables from .env
def load_env():
    env_path = ".env"
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if "=" in line and not line.strip().startswith("#"):
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip().strip('"').strip("'")
                    print(f"Loaded env var: {key.strip()}")

load_env()

from us_visa.pipline.training_pipeline import TrainPipeline

try:
    print("Initializing training pipeline...")
    pipeline = TrainPipeline()
    print("Running training pipeline...")
    pipeline.run_pipeline()
    print("SUCCESS: Pipeline executed successfully!")
except Exception as e:
    print(f"ERROR: Pipeline execution failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)