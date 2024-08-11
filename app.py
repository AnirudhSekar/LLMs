from flask import Flask, render_template, request, jsonify
from llm import handle_conversation

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def text_prompt():
    conv_hist = []
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        bot_response = handle_conversation(list(request.form.items())[0][1])
        conv_hist.append([list(request.form.items())[0][1], bot_response])
       
        return render_template("index.html", conv_hist=open("context.txt", 'r').readlines())        
if __name__ == "__main__":
    app.run(debug=True)