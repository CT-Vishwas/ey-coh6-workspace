from jinja2 import Environment, FileSystemLoader
from dataclasses import dataclass
from playwright.sync_api import sync_playwright
import base64
from pathlib import Path


@dataclass
class ReportData:
    company_title: str
    status_counts: dict
    department_scores: dict
    generation_time: str
    reporter_name: str
    chart: str # Default path for the chart image

def image_to_base64(img_file:Path):
    # Open the file in binary read mode and encode it
    try: 
        with open(img_file, "rb") as image_file:
            # Read the file and encode to base64 bytes, then decode to a UTF-8 string
            img_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        return img_base64
    except FileNotFoundError:
        print(f"{img_file} NOT FOUND")
def create_compliance_report(report_data: ReportData, template=None, report_path=None, report_pdf=None) -> None:
    # 2. Set up the Jinja2 template environment
    env = Environment(loader=FileSystemLoader(template.parent))
    template = env.get_template(template.name)
    # 3. Render template with our data context
    print("Rendering the compliance report template...")
    # print(f"Report Data: {type(report_data)}, {report_data}")
    html_out = template.render(report_data.__dict__)

    file_url = report_path.as_uri()

    # render HTML to a HTML File
    with open(report_path, "w") as f:
        f.write(html_out)


    with sync_playwright() as p:
        # Launch Chromium (set headed=True to see the UI)
        browser = p.chromium.launch(headless=False)
        
        # Open a new isolated browser context and page
        page = browser.new_page()
        
        # Navigate to a report
        page.goto(file_url)
        print(f"Page Title: {page.title()}")
        page.emulate_media(media="screen")
        page.pdf(path=report_pdf,
                 landscape=False,
                 format="A5",  # Options: 'A4', 'Letter', 'Legal', etc.
                 print_background=True,  # Crucial! Keeps Tailwind background colors intact
                 margin={
                    "top": "0.5in",
                    "bottom": "0.5in",
                    "left": "0.5in",
                    "right": "0.5in",
                },
                 )
        # Always clean up and close the browser
        browser.close()


if __name__ == "__main__":
    # create_compliance_report()
    print(image_to_base64('compliance_scores.png'))