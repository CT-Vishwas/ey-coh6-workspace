from pathlib import Path
import json
import os
from .loading import load_data
import pandas as pd
import matplotlib.pyplot as plt
from .reporting import create_compliance_report, ReportData

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

    # Loading the data
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

    # 2. Doing Analysis
    # Combine using innerjoin
    print("merged_df: ")
    merged_df = pd.merge(app_df, compiance_df, how="inner")
    print(merged_df.head())


    compliance_statuses = merged_df['Status'].value_counts()
    print(compliance_statuses)

    print(merged_df.info())
    merged_df['Compliance_Score'] = pd.to_numeric(merged_df['Compliance_Score'].str.replace("%",""))
    print(merged_df.info())


    scores = merged_df[["Department","Compliance_Score"]]
    scores.plot(kind="pie", y="Compliance_Score")
    plt.savefig("./outputs/compliance_scores.png")


    plt.figure(figsize=(8, 8))
    merged_df.groupby('Department')['Compliance_Score'].mean().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Compliance Score by Department')
    plt.ylabel('')
    plt.savefig('./outputs/average_compliance_score_by_department.png')

    # 3. Generated a report
    try:
        report_data = ReportData(
            company_title="Company Title",
            status_counts=compliance_statuses.to_dict(),
            department_scores=merged_df.groupby('Department')['Compliance_Score'].mean().to_dict(),
            generation_time=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            reporter_name="Reporter"
        )
        create_compliance_report(report_data)
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")