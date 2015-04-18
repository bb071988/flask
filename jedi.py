# Your Jedi name is the first three letters of your last name, followed by the first two letters of your first name. So visiting /jedi/beyonce/knowles should tell you that your Jedi #name is "knobe".

from flask import Flask


app = Flask(__name__)

@app.route("/<first_name>/<last_name>")
def nameEngine(first_name,last_name):
    html = """
    <h1> My name is {} {}<h1>
    <h2> but my Jedi Name is {}{}<h2>
    """
    return html.format(first_name, last_name, first_name[:3], last_name[:2])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    first_name = "bob"
    last_name = "braico"
    


