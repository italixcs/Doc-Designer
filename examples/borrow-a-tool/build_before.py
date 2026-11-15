"""Build the deliberately basic public redesign fixture; requires python-docx."""
from pathlib import Path
from docx import Document
from docx.shared import Mm, Pt

BASE = Path(__file__).resolve().parent


def main():
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Mm(210), Mm(297)
    section.top_margin = section.bottom_margin = Mm(22)
    section.left_margin = section.right_margin = Mm(22)
    normal = doc.styles["Normal"]
    normal.font.name, normal.font.size = "Liberation Sans", Pt(11)
    normal.paragraph_format.space_after = Pt(8)
    normal.paragraph_format.line_spacing = 1.12
    for border in doc.styles.element.xpath(".//w:pBdr"):
        border.getparent().remove(border)
    doc.core_properties.author = "Doc designer example"
    doc.core_properties.last_modified_by = "Doc designer example"
    doc.core_properties.title = "Borrow a tool"
    doc.core_properties.subject = "Fictional public redesign fixture"
    doc.core_properties.comments = ""
    doc.add_heading("Borrow a tool", 0)
    doc.add_paragraph("A quick guide to the fictional Northbank Tool Library")
    doc.add_heading("Opening hours", 1)
    doc.add_paragraph("Wednesday: 16:00–19:00. Saturday: 10:00–13:00.")
    doc.add_heading("Join and borrow", 1)
    doc.add_paragraph("Membership is free. Ask at the desk to join. Members may borrow one item at a time.")
    doc.add_paragraph("Choose an available tool. The desk records the item and its return date. Check the return date before leaving.")
    doc.add_heading("Loan periods", 1)
    table = doc.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    for cell, text in zip(table.rows[0].cells, ["Item", "Loan period", "Included"]):
        cell.text = text
    for row in [
        ["Cordless drill", "7 days", "Drill, battery, charger"],
        ["Hand saw", "14 days", "Saw and blade cover"],
        ["Repair kit", "7 days", "Kit and contents checklist"],
    ]:
        for cell, text in zip(table.add_row().cells, row):
            cell.text = text
    doc.add_heading("Return your tool", 1)
    doc.add_paragraph("Bring the item back during opening hours. Return it clean and with all included parts.")
    doc.add_paragraph("If you expect to be late, contact the desk before the return date.")
    doc.add_heading("Before you leave", 1)
    doc.add_paragraph("Check the return date before leaving.")
    doc.save(BASE / "before.docx")


if __name__ == "__main__":
    main()
