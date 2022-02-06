from flask import Flask, render_template,redirect,session,request
app = Flask(__name__)
app.secret_key = 'Lamelo Ball'
@app.route('/')  
def hello_world():
    return render_template('index.html')
@app.route('/users', methods=['POST'])
def info():
    print(request.form['name'])
    session['name']=request.form['name']
    print(request.form['dojo'])
    session['dojo'] = request.form['dojo']
    print(request.form['lang'])
    session['lang'] = request.form['lang']
    print(request.form['Comment'])
    session['Comment'] = request.form['Comment']
    return redirect('/result')

@app.route('/result')
def final():
    return render_template('result.html')
if __name__=="__main__":
    app.run(debug=True)