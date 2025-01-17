from flask import Flask, request, jsonify

from chat import get_response
app = Flask(__name__)

@app.get('/')
def hello_world():
    return 'Hello!'

@app.post("/predict")
def pred():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True ,host='0.0.0.0',port='3000')

# if __name__ == "__main__":
#     app.run(debug=true)