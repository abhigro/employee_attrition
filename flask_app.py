#import a liberary
from flask import Flask,render_template,request
import joblib

#instance of an app
app=Flask(__name__)

#loading the model

#global attr

model=joblib.load("attrition.pkl")
attr=joblib.load("attribute.pkl")
#encode=joblib.load("encoding.pkl")

@app.route('/' )
def hello():
    return render_template("form.html")
@app.route('/submit', methods=["POST"])
def form_data():
    dic={}
    for i in attr:
        if (i!="Attrition"):
            dic[i]=int(request.form.get(i))
    

    pred=model.predict([list(dic.values())])
    print(pred)
    
    if pred[0]==1:
        out="probable to leave"
    else:
        out="not probable to leave"
    return render_template("index.html",data=f'person is {out}')



#run the app
if __name__=="__main__":
    app.run(debug=True)
