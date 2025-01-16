import fitz


def transform_pdf_to_png(path):
    doc = fitz.open(path)
    matrix = fitz.Matrix(6, 6)

    for n in doc:
        pix = n.get_pixmap(matrix=matrix)
        pix.save(f"scout.png")


