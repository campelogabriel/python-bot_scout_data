import fitz


def transform_pdf_to_png(path):
    doc = fitz.open(path)

    for n in doc:
        pix = n.get_pixmap()
        pix.save(f"scout.png")