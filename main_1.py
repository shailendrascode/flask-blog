from flask import Flask, jsonify , render_template
app = Flask(__name__)

print("Learning flask")
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/about')
def about():
    uid1 = "shailendra"
    return render_template('about.html',name = uid1)

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    ans = a + b
    result = {
        "num1":a,
        "num2":b,
        "sum":ans
    }

    return jsonify(result)


@app.route('/bootstrap_page')
def bootstrap_page():
    return render_template('bootstrap.html')

if __name__ == '__main__':
    app.run(debug=True)
