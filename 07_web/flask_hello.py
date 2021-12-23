from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return '''
     <p>Hello, Flask!!</p>
     <a href="/first">Go First</a>
     <a href="/second">Go Second</a>
    '''
@app.route("/")
def first():
    return'''
     <p>first
    
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")