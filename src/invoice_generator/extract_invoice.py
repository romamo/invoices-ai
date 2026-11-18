import sys
from pathlib import Path


def load_pdfplumber():
    try:
        import pdfplumber
    except ImportError as exc:
        raise ImportError(
            "extract-invoice requires 'pdfplumber'. "
            "Install it with: uv pip install 'invoice-generator[parsing]'"
        ) from exc
    return pdfplumber


def extract_text_from_pdf(pdf_path: Path) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")

    pdfplumber = load_pdfplumber()

    print(f"--- Extracting text from: {pdf_path.name} ---")
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            print(f"\n[Page {i + 1}]")
            text = page.extract_text()
            print(text if text else "(No text found on this page)")

            tables = page.extract_tables()
            if tables:
                print(f"\n[Page {i + 1} Tables]")
                for table in tables:
                    for row in table:
                        print(row)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: extract-invoice <path_to_pdf>", file=sys.stderr)
        sys.exit(1)

    extract_text_from_pdf(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
