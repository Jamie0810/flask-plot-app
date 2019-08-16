from flask import Flask, render_template
from plots import plots

app = Flask(__name__)
app.register_blueprint(plots)

@app.route('/')
def hello():
	return '<h1>Hello World!</h1>'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')