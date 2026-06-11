from pathlib import Path
import json
import os
from .loading import load_data

def load_config(config_path: Path) -> dict:
    '''
    Loads the configuration from the given JSON file path and returns it as a dictionary.
    '''
    try:
        with open(config_path, 'r') as fh:
            config = json.load(fh)
            return config
    except FileNotFoundError:
        print(f"Configuration file '{config_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the configuration file '{config_path}'.")
        return {}
    

if __name__ == "__main__":
    config_path = Path(__file__).parent.parent/"config"/"env.json"
    # config_path = os.path.abspath(os.path.join(os.path.pardir, "config", "env.json"))
    print(f"Loading configuration from: {config_path}")

    if not config_path.exists():
        print(f"Configuration file '{config_path}' does not exist.")
    else:
        config = load_config(config_path)
        if config:
            print("Configuration loaded successfully:")
            print(json.dumps(config, indent=4))
        else:
            print("Failed to load configuration.")
    
    data_dir = config.get("data_dir", "data")
    data_path = Path(__file__).parent.parent / data_dir
    print(f"Data directory path: {data_dir}")
    if not data_path.exists():
        print(f"Data directory '{data_path}' does not exist.")
    else:
        print(f"Data directory '{data_path}' exists.")

    app_inventory_path = data_path / "cap_app_inventory.csv"
    app_df = load_data(app_inventory_path)
    if app_df is not None:
        print("Data loaded successfully:")
        print(app_df.head())
    else:
        print("Failed to load data.")

    compiance_path = data_path / "cap_compliance_status.csv"
    compiance_df = load_data(compiance_path)
    if compiance_df is not None:
        print("Data loaded successfully:")
        print(compiance_df.head())
    else:
        print("Failed to load data.")