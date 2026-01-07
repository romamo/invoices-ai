import sys
from pathlib import Path
import subprocess

def ensure_pdfplumber():
    try:
        import pdfplumber
        return pdfplumber
    except ImportError:
        print("This feature requires 'pdfplumber'.")
        choice = input("Install pdfplumber support now? [y/N] ").lower()
        if choice == 'y':
            print("Installing pdfplumber...")
            subprocess.run(["uv", "pip", "install", "pdfplumber"], check=True)
            print("pdlplumber installed. Importing...")
            import pdfplumber
            return pdfplumber
        else:
            print("Aborted.")
            sys.exit(1)

def extract_text_from_pdf(pdf_path):
    path = Path(pdf_path)
    if not path.exists():
        print(f"Error: File not found at {path}")
        return

    pdfplumber = ensure_pdfplumber()

    print(f"--- Extracting text from: {path.name} ---")
    try:
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                print(f"\n[Page {i+1}]")
                text = page.extract_text()
                if text:
                    print(text)
                else:
                    print("(No text found on this page)")
                    
                # Also try to extract tables if any
                tables = page.extract_tables()
                if tables:
                    print(f"\n[Page {i+1} Tables]")
                    for table in tables:
                        for row in table:
                            print(row)
    except Exception as e:
        print(f"Error reading PDF: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: extract-invoice <path_to_pdf>")
        sys.exit(1)
    
    extract_text_from_pdf(sys.argv[1])

if __name__ == "__main__":
    main()
