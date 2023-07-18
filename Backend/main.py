from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def concatenate_strings():
    data = request.get_json()
    string1 = data['string1']
    string2 = data['string2']
    result = string1 + string2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
