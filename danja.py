from flask import Flask, render_template

danja= Flask(__name__)

@danja.route('/')
@danja.route('/home')
def index():
    return render_template("index.html")

@danja.route('/vibor.html')
def about():
    return render_template("vibor.html")

@danja.route('/Rim.html')
def RimText():
    return render_template("Rim.html")


@danja.route('/Afin.html')
def AfinText():
    return render_template("Afin.html")

@danja.route('/Ankar.html')
def AnkarText():
    return render_template("Ankar.html")

if __name__ =="__main__":
    danja.run()
