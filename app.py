from flask import Flask, render_template, request
from generate_pdf import create_pdf
from mailer import send_email

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    pdf_path = create_pdf(form_data)
    send_email(
        to_address="info@sarayasansor.com",
        subject="Yeni Asansör Bilgi Formu",
        body="Form ektedir.",
        attachment_path=pdf_path
    )
    return "Form başarıyla gönderildi."

if __name__ == '__main__':
    app.run(debug=True)
