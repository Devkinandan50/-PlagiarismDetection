import PyPDF2
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from preprocessing import preprocessing_using_nlp, my_variable
from collectPdfData import pdfData



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
    

    pdf_text1, pdf_text2, diffrence_between_pdf_data = pdfData(file1, file2)
    
    
    
    score = preprocessing_using_nlp(pdf_text1, pdf_text2)
    # score = my_variable
    
    ls["score"] = score
    ls["all data"] = diffrence_between_pdf_data
    


    ls["success"] = True
    return make_response(jsonify(ls), 200)


if __name__ == '__main__':
    app.run()