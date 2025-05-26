from weasyprint import HTML
import tempfile

def create_pdf(form_data):
    html_content = f"""
    <html>
    <body>
        <h2>Asansör Bilgi Formu</h2>
        <ul>
            {''.join(f'<li><strong>{key}</strong>: {value}</li>' for key, value in form_data.items())}
        </ul>
    </body>
    </html>
    """
    tmp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    HTML(string=html_content).write_pdf(tmp_pdf.name)
    return tmp_pdf.name
