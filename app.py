from flask import Flask, request, redirect, render_template

app = Flask(__name__)
queue = []  # This is your queue data structure

@app.route('/')
def index():
    return render_template('index.html', queue=queue)

@app.route('/push', methods=['POST'])
def push():
    element = request.form.get('element')
    if element:
        queue.append(element)
    return redirect('/')

@app.route('/pop', methods=['POST'])
def pop():
    if queue:
        queue.pop(0)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
