from flask import Flask, render_template
FAI = Flask(__name__)


@FAI.route('/')
def properties():
    return render_template('properties.html')


if __name__ == '__main__':
    FAI.run(debug=True)