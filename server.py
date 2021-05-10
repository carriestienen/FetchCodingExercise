from flask import Flask, redirect, url_for, request, jsonify
from textsimilarity import calculate_similarity
app = Flask(__name__)

@app.route('/classify',methods = ['POST'])
def classify():
    content = request.json
    txt1 = content['txt1']
    txt2 = content['txt2']

    result = calculate_similarity(txt1,txt2,True,True,True)
    return jsonify({"result":result})


if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')