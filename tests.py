import pdfkit

# Specify the path to wkhtmltopdf executable (for Windows)
config = pdfkit.configuration(wkhtmltopdf=r'D:\my files\Applications\wkhtmltopdf.exe')

# Convert an HTML file to a PDF
pdfkit.from_string('filehtml', 'output.pdf', configuration=config)
