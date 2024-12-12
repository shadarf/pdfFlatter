# PDF Flattener Command-Line Application

## Overview

This command-line application flattens a PDF file, making it editable, and saves the flattened PDF to disk. The application uses the PyPDF2 library to read and write PDF files.

**Requirements**

```
Python 3.x

PyPDF2 library
```

You can install the PyPDF2 library using pip:

`pip install PyPDF2`

**Usage**

To use the application, run the following command in your terminal:


`python PDF_flatter.py <input_pdf_path>`

Replace <input_pdf_path> with the path to your input PDF file. The application will create a flattened version of the PDF and save it with _flat.pdf appended to the original file name.

**Example** 

If your input PDF file is named 01_Fujimori_2023_AB_glioblastoma.pdf, run the following command:

```
python PDF_flatter.py 01_Fujimori_2023_AB_glioblastoma.pdf
```
The flattened PDF will be saved as 01_Fujimori_2023_AB_glioblastoma.pdf_flat.pdf.

**License**
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.
