import PyPDF2
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from preprocessing import preprocessing_using_nlp, my_variable
from pdfinfo import extract_text_from_pdfs


app = Flask(__name__)
CORS(app)



@app.route('/')
def hello_world():
    return 'Hello ask Devkinandan Jagtap for backend API Contact: jagtapdevkinandan50@gmail.com'




@app.route('/upload', methods=['POST'])
def upload_files():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    ls = {}
    ls["success"] = False

    if not file1 or not file2:
        return make_response(jsonify("Please upload two PDF files."), 400)
    
    if file1 is None or file1.mimetype != 'application/pdf':
        return make_response(jsonify("Please select a valid PDF file1"), 400)
    
    if file2 is None or file2.mimetype != 'application/pdf':
        return make_response(jsonify("Please select a valid PDF file2"), 400)

    text_contents1, author1, creation_date1, update_date1  = extract_text_from_pdfs(file1)
    text_contents2, author2, creation_date2, update_date2 = extract_text_from_pdfs(file2)

   

    
    # ls["file1"] = text_contents1
    # ls["file2"] = text_contents1
    
    # print( preprocessing_using_nlp(text_contents1, text_contents2))
    # print(my_variable)



    ls["success"] = True
    return make_response(jsonify(ls), 200)


if __name__ == '__main__':
    app.run()