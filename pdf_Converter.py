from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    c = canvas.Canvas(output_file, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

input_file = 'input.txt'
output_file = 'output.pdf'
text_to_pdf(input_file, output_file)
