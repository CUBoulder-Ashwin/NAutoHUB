from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def homePage():
    return render_template('homepage.html')

@app.route('/photography', methods = ['POST', 'GET'])
def testPage():
    x=0
    while(True):
        x +=1
        return render_template('photography.html', msg = x)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=80)