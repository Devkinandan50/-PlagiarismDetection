# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/upload', methods=['POST'])
# def concatenate_strings():
#     data = request.get_json()
#     string1 = data['string1']
#     string2 = data['string2']
#     result = string1 + string2
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)


import PyPDF2
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_files():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return 'Please upload two PDF files.', 400

    text_contents = extract_text_from_pdfs(file1, file2)
    return text_contents

def extract_text_from_pdfs(file1, file2):
    pdf_text = ''
    ls = []

    ls.append("success")


    for file in [file1, file2]:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

    # ls.append(pdf_text)
    print(pdf_text)

    # return pdf_text
    return make_response(jsonify("s"), 200)

if __name__ == '__main__':
    app.run()
