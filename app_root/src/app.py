from pathlib import Path
import json
import os
import csv

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

    csv_file = os.path.abspath(os.path.join(os.path.pardir,os.path.pardir, config.get("data_path", ""), "sample.csv")) 
    print(f"CSV file path: {csv_file}")
    if not os.path.exists(csv_file) and not os.path.isfile(csv_file):
        print(f"CSV file '{csv_file}' does not exist or is not a valid file.")
    else:
        try:
            with open(csv_file, 'r') as fh:
                reader = csv.DictReader(fh)
                # print(reader.fieldnames)
                for field in reader.fieldnames:
                    print(f"|{field:<30}",end="")
                print("\n"+"-" * 50)
                for row in reader:
                    for field in reader.fieldnames:
                        print(f"|{row[field]:<30}",end="")
                    print()
        except FileNotFoundError:
            print(f"CSV file '{csv_file}' not found.")