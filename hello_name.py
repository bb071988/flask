from flask import Flask

app = Flask(__name__)

# we can have many routes.  Ask Sam about passing in these variables.  Presently setting them in main

@app.route("/hello")
def say_hi():
    return "Hello World!"

# @app.route("/hello/<name>")
# def hi_person(name):
#     return "Hello {}!".format(name.title())

# @app.route("/htmlhello/<htmlName>")
# def hello_person(htmlName):
#     html = """
#         <h1>
#             Hello {}!
#         </h1>
#         <p>
#             Here's a picture of a kitten.  Awww...
#         </p>
#         <img src="http://placekitten.com/g/200/300">
#     """
#     return html.format(name.title())

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/robert")
def whatsUp():
    return "Whats up"

#hi_person("bob")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    name = "bob"
    htmlName = "Robert"
    upName = "robert"