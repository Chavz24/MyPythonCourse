from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import blue


canvas = Canvas('PP_Hello.pdf', pagesize=LETTER)
canvas.setFont('Times-Roman',30)
canvas.setFillColor(blue)
canvas.drawString(1*inch,10*inch, 'Hello World')

canvas.save()
