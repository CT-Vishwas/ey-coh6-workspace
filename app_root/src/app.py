from pathlib import Path
import json
import os
from .loading import load_data
import pandas as pd
import matplotlib.pyplot as plt
from .reporting import create_compliance_report, ReportData, image_to_base64
from config import load_config, set_path

CONFIG_PATH = Path(__file__) / "env.json"
APP_FILE = "cap_app_inventory.csv"
COMPLIANCE_STATUS_FILE = "cap_compliance_status.csv"
GAP_LOG_FILE ="cap_gap_logs.csv"
STAKE_HOLDERS_FILE = "cap_stake_holders.csv"


if __name__ == "__main__":
    print(f"Loading configuration from: {CONFIG_PATH}")
    config = {}
    if not CONFIG_PATH.exists():
        print(f"Configuration file '{CONFIG_PATH}' does not exist.")
    else:
        config = load_config(CONFIG_PATH)
        if config:
            print("Configuration loaded successfully:")
            print(json.dumps(config, indent=4))
        else:
            print("Failed to load configuration.")

    data_path, template, output_html, output_pdf = set_path(config.get("data_dir","data"),config.get("template_dir","template"),config.get("outputs_dir","outputs"))

    # Loading the data
    app_inventory_path = data_path / APP_FILE
    app_df = load_data(app_inventory_path)
    if app_df is not None:
        print("Data loaded successfully:")
        print(app_df.head())
    else:
        print("Failed to load data.")

    compliance_path = data_path / COMPLIANCE_STATUS_FILE
    compliance_df = load_data(compliance_path)
    if compliance_df is not None:
        print("Data loaded successfully:")
        print(compliance_df.head())
    else:
        print("Failed to load data.")

    # 2. Doing Analysis
    # Combine using innerjoin
    print("merged_df: ")
    merged_df = pd.merge(app_df, compliance_df, how="inner")
    print(merged_df.head())


    compliance_statuses = merged_df['Status'].value_counts()
    print(compliance_statuses)

    print(merged_df.info())
    merged_df['Compliance_Score'] = pd.to_numeric(merged_df['Compliance_Score'].str.replace("%",""))
    print(merged_df.info())


    plt.figure(figsize=(8, 8))
    merged_df.groupby('Department')['Compliance_Score'].mean().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Compliance Score by Department')
    plt.ylabel('')
    plt.savefig(output_html.parent / 'average_compliance_score_by_department.png')

    # 3. Generated a report
    try:
        report_data = ReportData(
            company_title="Company Title",
            status_counts=compliance_statuses.to_dict(),
            department_scores=merged_df.groupby('Department')['Compliance_Score'].mean().to_dict(),
            generation_time=pd.Timestamp.now().strftime("%Y-%m-%d %I:%M %p"),
            reporter_name="Reporter",
            chart= image_to_base64(output_html.parent / 'average_compliance_score_by_department.png')
        )
        create_compliance_report(report_data, template=template, report_path=output_html, report_pdf=output_pdf)
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")