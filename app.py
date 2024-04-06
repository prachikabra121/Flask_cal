from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/welcome")
def welcome():
    return "welcome to Indore"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return " Person is passed and score is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "person is fail and score is " + str(score)


@app.route('/calculate',methods = ["Post","GET"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else :
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        avg_marks =(maths +science + history) /3
        result =""

        if avg_marks >=50:
            result = "success"  
        else:
            result = "fail"

        return redirect(url_for(result,score = avg_marks))

       # return render_template('result.html',results= avg_marks)


if __name__ =='__main__':
    app.run(debug = True)