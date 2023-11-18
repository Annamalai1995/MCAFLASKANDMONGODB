from flask import Flask,make_response,render_template,request
app=Flask(__name__)

@app.route("/")
def Hello():
    return make_response("<h1>I am Annamalai</h1>")


@app.route("/pages1")
def tempfirst():
    return  render_template("first.html")

@app.route("/jin/<int:value>")
def callJinja(value):
    return render_template("jinja.html",number=value);

@app.route("/repeat")
def callLoop():
    myList=['Spring Boot','Flask','DJnago','Node','Hibernate']
    return render_template("loop.html",myFrame=myList)


@app.route("/decide/<float:income>")
def decision(income):
    return render_template("decisionmaking.html",ctc=income)

@app.route("/skills")
def showTable():
    myList=[
        {"front":"Thymeleaf","back":"SpringBoot","data":"Oracle","server":"apache tomcat"},
        {"front":"Jinja","back":"Flask","data":"MongoDB","server":"WSGI"},
        {"front":"React","back":"DJango","data":"MySQL","server":"WSGI"},
        {"front":"Vite","back":"Express","data":"MongoDB","server":"Node"},
    ]
    return render_template("table.html",stack=myList)

@app.route("/send",methods=['GET','POST'])
def performSignUp():
    if request.method=="GET":
        return render_template("bootforms.html")
    else:
        firstName=request.form['fname']
        lastName=request.form['lname']
        email=request.form['mail']
        contact=request.form['mobile']
        print(firstName,lastName,contact,email)
        return render_template("bootforms.html",msg=firstName+" account created")





if __name__=="__main__":
    app.run(debug=True,port=2711)