from flask import Flask, request, jsonify, render_template
from speech_to_text import listen
from db_communicator import authenticate, insert, search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/listen', methods=["POST"])
def record():
    text = listen()
    return jsonify({"results": text})

@app.route('/api/authenticate', methods=['POST'])
def login():
      data = request.json
      username = data['user']
      password = data['pass']
      res = authenticate(username, password)
      return jsonify({"result": res})

@app.route('/api/insert', methods=['POST'])
def insertTranscript():
     data = request.json
     djs = data['speakers']
     showname = data['shownm']
     results = data['txt']
     res = insert(djs, showname, results)
     return jsonify({"results": res})

@app.route('/search')
def openSearch():
     return render_template('search.html')

@app.route('/search/api/searchdb', methods=['POST'])
def searchdb():
     data = request.json
     input = data['input']
     res = search(input)
     return jsonify({"results": res})

if __name__ == '__main__':
    app.run(debug=True)