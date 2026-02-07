from pathlib import Path
from pypdf import PdfReader, PdfWriter

local = Path(__file__).parent

arquivos = [
    local / "Documento1.pdf",
    local / "Documento2.pdf",
]

writer = PdfWriter()

for nome in arquivos:
    reader = PdfReader(nome)
    for page in reader.pages:
        writer.add_page(page)

with open(local / "resultado.pdf", "wb") as f:
    writer.write(f)