from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/baseline')
def baseline():
    return render_template('baseline.html')

@app.route('/progressive')
def progressive():
    return render_template('progressive.html')

@app.route('/hierarchical')
def hierarchical():
    return render_template('hierarchical.html')


if __name__ == '__main__':
    app.run(debug=True)
