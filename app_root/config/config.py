'''
Author: Vishwas K Singh
Email: vishwas@cloudthat.com
Module for handling and loading configuration for the app
'''
from pathlib import Path
import os
import json

TEMPLATE_FILE = "compliance_report_template.html"
OUTPUT_PDF_FILE = "compliance_report.pdf"
OUTPUT_HTML_FILE = "compliance_report.html"


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
    
def set_path(data_dir:str,template_dir:str,output_dir:str) -> tuple:
    '''
    Sets data_path, template_path & output_path
    Returns data_path, template, output_html, output_pdf 
    '''
    base_path = Path(os.path.abspath(__file__)).parent.parent
    data_path = base_path / data_dir
    template = base_path / template_dir / TEMPLATE_FILE
    output_pdf = base_path / output_dir / OUTPUT_PDF_FILE
    output_html = base_path / output_dir / OUTPUT_HTML_FILE

    return data_path, template, output_html, output_pdf