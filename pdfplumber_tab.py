import pdfplumber
import os
import csv

INPUT_FOLDER = 'test'
PDF_FILENAME = 'offense.pdf'
OUTPUT_FOLDER = '.'

def extract_tables_with_pdfplumber():
    input_pdf_path = os.path.join(INPUT_FOLDER, PDF_FILENAME)

    if not os.path.exists(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' was not found.")
        return

    table_count = 0
    try:
        with pdfplumber.open(input_pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                extracted_tables = page.extract_tables()
                
                for table_data in extracted_tables:
                    table_count += 1
                    output_csv_filename = f"output_pdfplumber_table_{table_count}.csv"
                    output_csv_path = os.path.join(OUTPUT_FOLDER, output_csv_filename)

                    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerows(table_data)
                    
                    print(f"-> Successfully saved page {page_num + 1} table to '{output_csv_path}'")

        if table_count == 0:
            print("No tables were found in the PDF.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    extract_tables_with_pdfplumber()