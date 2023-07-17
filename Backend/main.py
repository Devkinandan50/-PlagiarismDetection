from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    # Check if the request contains two PDF files
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'message': 'Two PDF files are required.'}), 400
    
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Check if the file extensions are PDF
    if not file1.filename.endswith('.pdf') or not file2.filename.endswith('.pdf'):
        return jsonify({'message': 'Both files should be in PDF format.'}), 400

    # Process the files (you can add your own logic here)

    # Return a success response
    return jsonify({'message': 'Files uploaded successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
