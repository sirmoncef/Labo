from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.http import HttpResponse

def generate_ticket_pdf(appointment, ticket_number):
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Draw ticket content
    p.setFont("Helvetica-Bold", 18)
    p.drawString(1 * inch, height - 1 * inch, "Medical Laboratory Ticket")
    p.line(1 * inch, height - 1.2 * inch, width - 1 * inch, height - 1.2 * inch)

    p.setFont("Helvetica", 12)
    y_position = height - 2 * inch
    p.drawString(1 * inch, y_position, f"Ticket Number: {ticket_number}")
    p.drawString(1 * inch, y_position - 0.5 * inch, f"Patient: {appointment.first_name} {appointment.last_name}")
    p.drawString(1 * inch, y_position - 1 * inch, f"Date: {appointment.date.strftime('%Y-%m-%d')}")
    p.drawString(1 * inch, y_position - 1.5 * inch, f"Time: {appointment.time.strftime('%H:%M')}")
    p.drawString(1 * inch, y_position - 2 * inch, f"Phone: {appointment.phonenumber}")

    # Add barcode (optional)
    # You'll need to install python-barcode package for this
    # from barcode import Code128
    # from barcode.writer import ImageWriter
    # code = Code128(str(ticket_number), writer=ImageWriter())
    # code.save("barcode")
    # p.drawImage("barcode.png", 1*inch, y_position - 3*inch, width=2*inch, preserveAspectRatio=True)

    # Add footer
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(1 * inch, 0.5 * inch, "Thank you for choosing our laboratory services!")

    # Close the PDF object cleanly
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so browsers present
    # the option to save the file
    buffer.seek(0)
    return buffer