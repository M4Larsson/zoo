from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	author='Group 38'
	name='from the Zoo!'
	return render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    app.run()