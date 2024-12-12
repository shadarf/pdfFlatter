# pip install PyPDF2

# Command line software:
import PyPDF2
import sys

def flatten_pdf(input_pdf_path, output_pdf_path):
    '''
    PDF Flattener Command-Line Application
    Overview
    This command-line application flattens a PDF file, making it editable, and saves the flattened PDF to disk. The application uses the PyPDF2 library to read and write PDF files.

    Requirements
    Python 3.x

    PyPDF2 library

    You can install the PyPDF2 library using pip:

    bash
    pip install PyPDF2
    Usage
    To use the application, run the following command in your terminal:

    bash
    python PDF_flatter.py <input_pdf_path>
    Replace <input_pdf_path> with the path to your input PDF file. The application will create a flattened version of the PDF and save it with _flat.pdf appended to the original file name.

    Example
    If your input PDF file is named 01_Fujimori_2023_AB_glioblastoma.pdf, run the following command:

    bash
    python PDF_flatter.py 01_Fujimori_2023_AB_glioblastoma.pdf
    The flattened PDF will be saved as 01_Fujimori_2023_AB_glioblastoma.pdf_flat.pdf.
        ''' 
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        writer = PyPDF2.PdfWriter()

        # Iterate through each page and add it to the writer
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)

        # Write the flattened PDF to the output file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python PDF_flatter.py <input_pdf_path>")
        sys.exit(1)

    input_pdf_path = sys.argv[1]
    output_pdf_path = f'{input_pdf_path}_flat.pdf'
    flatten_pdf(input_pdf_path, output_pdf_path)
    print(f"Flattened PDF saved as {output_pdf_path}")
