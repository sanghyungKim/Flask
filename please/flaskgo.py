from flask import Flask,render_template,request,session

app = Flask(__name__)

@app.route('/form')
def form():
    return  render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
    if  request.method == 'POST':
        if  (request.form['username'] == 'jamie'
             and    request.form['password'] == '1234'):
            session['logged_in'] = True
            session['username'] = request.form['username']
            return  request.form['username'] + " 님 환영합니다."
        else:
            return  '로그인 정보가 맞지 않습니다.'
    else:
        return '잘못된 접근'
    
app.secret_key = 'sample_secret_key'

if __name__ == '__main__':
    app.run(debug=True)