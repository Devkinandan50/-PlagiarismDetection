from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from Plagiarism import pdfData

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
    

    diffrence_between_pdf_data, score1, score2, common_words_and_weights = pdfData(file1, file2)
    
    ls["Cosine Score"] = score1
    ls["jaccard Score"] = score2
    ls["data"] = diffrence_between_pdf_data
    ls["common words"] = common_words_and_weights
    


    ls["success"] = "True"
    return make_response(jsonify(ls), 200)


if __name__ == '__main__':
    app.run()