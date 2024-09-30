from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/photography', methods=['POST', 'GET'])
def testPage():
    return render_template('photography.html')

@app.route('/stream')
def stream():
    def event_stream():
        x = 0
        while True:
            x += 1
            yield f'data: {x}\n\n'
            time.sleep(1)  # Simulating data push every second
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True)
