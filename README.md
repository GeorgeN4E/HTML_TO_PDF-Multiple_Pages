# Webpage to PDF Converter

This script converts multiple pages of a website into a single PDF document. It automatically fetches webpage titles, converts individual pages to PDF, and merges them into a cohesive document. It supports customizable templates for handling different website structures.

---

## Features
- Fetch and sanitize webpage titles for use as filenames.
- Convert individual webpage URLs to PDF.
- Merge multiple PDFs into a single document.
- Add custom templates to handle new website structures.

---

## Prerequisites
1. Python 3.x installed on your system.
2. Required Python libraries:
   - `pdfkit`
   - `requests`
   - `beautifulsoup4`
   - `PyPDF2`
3. Install `wkhtmltopdf` and configure the path in the script:
   - Download `wkhtmltopdf` from [here](https://wkhtmltopdf.org/).
   - Set the path to the executable in the script.

---

## Installation
1. Clone this repository or copy the script file.
2. Install the required libraries using:
   ```bash
   pip install pdfkit requests beautifulsoup4 PyPDF2
   ```
3. Download and install `wkhtmltopdf`. Ensure it is accessible in your system or specify the absolute path in the script.

---

## Usage
1. **Basic Example**:
   Set the `base_url` and `num_pages` variables in the script:
   ```python
   base_url = 'https://www.example.com/forum/thread'
   num_pages = 5
   ```
   Run the script:
   ```bash
   python script_name.py
   ```

2. **Customizing Templates**:
   - Templates define the URL structure for different websites.
   - Add a new template function following this format:
     ```python
     def example_website_template(base_url, page_number):
         return f"{base_url}?page={page_number}"
     ```
   - Update the `select_template_func` to include your new template:
     ```python
     if "example.com" in domain:
         return example_website_template
     ```

---

## Script Components

### Functions
- **`fetch_webpage_title(url)`**: Fetches and sanitizes the title of a webpage.
- **`convert_single_page_to_pdf(url, output_file)`**: Converts a single URL to a PDF file.
- **`merge_pdfs(input_files, output_file)`**: Merges multiple PDF files into one.
- **`convert_website_pages_to_pdf(base_url, num_pages, template_func)`**: Handles the conversion of multiple pages of a website into a single PDF document.
- **`select_template_func(base_url)`**: Selects the appropriate URL template based on the domain.

### Template Functions
- **`digital_kaos_template(base_url, page_number)`**:
  Handles pagination for the `digital-kaos.co.uk` forum.

---

## Adding New Templates
1. Create a new template function following the existing examples.
2. Add a condition for the new domain in `select_template_func`.
3. Test the new template to ensure it works correctly.

---

## Example Use Case
To convert pages from a forum thread:
1. Set the `base_url` to the first page of the thread.
2. Define the number of pages to convert with `num_pages`.
3. Ensure the correct template function is available or add a new one.

---

## Error Handling
- If the script raises `ValueError: No template available for this domain`, add a new template for the website.
- Check the path to `wkhtmltopdf` if conversion fails.

---

## Contributions
Feel free to contribute by adding new templates or improving the script. Open a pull request or raise an issue in the repository.

---

## License
This project is licensed under the MIT License.
