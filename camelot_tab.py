import camelot
import os

INPUT_FOLDER = 'test'
PDF_FILENAME = 'AnimalSounds.pdf'
OUTPUT_FOLDER = '.'

def extract_tables_with_camelot():
    input_pdf_path = os.path.join(INPUT_FOLDER, PDF_FILENAME)

    if not os.path.exists(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' was not found.")
        return

    try:
        tables = camelot.read_pdf(input_pdf_path, pages='all', flavor='stream')

        if not tables:
            print("No tables found in the PDF.")
            return

        for i, table in enumerate(tables):
            output_csv_filename = f"output_camelot_table_{i + 1}.csv"
            output_csv_path = os.path.join(OUTPUT_FOLDER, output_csv_filename)
            table.to_csv(output_csv_path)
            print(f"-> Successfully saved '{output_csv_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    extract_tables_with_camelot()