import pdfkit
import requests
from bs4 import BeautifulSoup
import os
from PyPDF2 import PdfMerger
import re
from urllib.parse import urlparse

# Function to fetch and sanitize the title of the webpage
def fetch_webpage_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip()
    # Remove invalid characters for Windows filenames
    title = re.sub(r'[\/:*?"<>|]', '-', title)
    return title

# Function to convert a single URL to PDF
def convert_single_page_to_pdf(url, output_file):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Adjust this path
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url, output_file, configuration=config)

# Function to merge multiple PDFs into one
def merge_pdfs(input_files, output_file):
    merger = PdfMerger()
    for pdf in input_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

# Main function to handle everything
def convert_website_pages_to_pdf(base_url, num_pages, template_func):
    temp_files = []
    
    # Fetch and sanitize the title from the first page
    first_page_url = template_func(base_url, 1)
    pdf_title = fetch_webpage_title(first_page_url)
    
    # Convert each page to a separate PDF
    for i in range(1, num_pages + 1):
        page_url = template_func(base_url, i)
        temp_pdf = f"temp_page{i}.pdf"
        convert_single_page_to_pdf(page_url, temp_pdf)
        temp_files.append(temp_pdf)
    
    # Merge all the PDFs into one
    output_file = f"{pdf_title}.pdf"
    merge_pdfs(temp_files, output_file)
    
    # Clean up temporary files
    for temp_file in temp_files:
        os.remove(temp_file)

# Template functions for different websites
def digital_kaos_template(base_url, page_number):
    return f"{base_url}/page{page_number}"

# Add more template functions for other websites here

# Function to select the appropriate template based on domain
def select_template_func(base_url):
    domain = urlparse(base_url).netloc
    if "digital-kaos.co.uk" in domain:
        return digital_kaos_template
    # Add more conditions for other domains here
    else:
        raise ValueError("No template available for this domain")

# Example usage
base_url = 'https://www.digital-kaos.co.uk/forums/showthread.php/495654-new-tuning-edc17-guide'
num_pages = 3

#base_url= input("Base url: ")
#num_pages= input("Number of pages: ")
# Select the appropriate template function
template_func = select_template_func(base_url)

# Convert the website pages to a PDF
convert_website_pages_to_pdf(base_url, num_pages, template_func)
