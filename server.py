from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')
    return b'200'


if __name__ == '__main__':
    app.run(debug=True)

