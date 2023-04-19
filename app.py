from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('layout.html')


@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    return render_template('signin.html')

@app.route('/transaction',methods=['GET','POST'])
def transaction():
    return render_template('transaction.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)