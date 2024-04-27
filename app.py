from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ece418')
def home():
    return 'Final Project Hunter and Gustavo'

@app.route('/ece418/baseline')
def baseline():
    return render_template('baseline.html')

@app.route('/ece418/progressive')
def progressive():
    return render_template('progressive.html')

@app.route('/ece418/hierarchical')
def hierarchical():
    return render_template('hierarchical.html')


if __name__ == '__main__':
    app.run(debug=True)
