from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    greeting = f"Hello, {name}! Welcome to the Luxurious Flask Application."
    return render_template('home.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
