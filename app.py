from flask import Flask, render_template, request
from llm import handle_conversation

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def text_prompt():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        handle_conversation(list(request.form.items())[0][1])
       
        return render_template("index.html", conv_hist=open("context.txt", 'r').readlines())        
if __name__ == "__main__":
    app.run(debug=True)
