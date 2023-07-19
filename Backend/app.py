import PyPDF2
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods=['POST'])
def upload_files():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    ls = []
    ls.append("success")

    if not file1 or not file2:
        return 'Please upload two PDF files.', 400

    text_contents = extract_text_from_pdfs(file1, file2)
    ls.append(text_contents)
    # return text_contents
    return make_response(jsonify("s"), 200)

def extract_text_from_pdfs(file1, file2):
    pdf_text = ''
    
    for file in [file1, file2]:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

    # print(pdf_text)
    return pdf_text

if __name__ == '__main__':
    app.run()