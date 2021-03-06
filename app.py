# -*- coding: utf-8 -*-
# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# /!\ reloader ne doit jamais être activé sur un site en prod /!\
app.config["DEBUG"] = True

# use decorators to link the functions to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello WHAT??!"
    
# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query
    
@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"
    
@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"  # je ne sais pas pourquoi pas impossible de return value
    
# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"
    
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello {}".format(name)  #, 200 Status codeis optional, 
                                        # Flask is smart
                                        # it's convention anyway to explicitely
                                        # define Status Code for RESTful APIs
    else:
        return "Not found", 404
    
# start the development server using the run() method
if __name__ == "__main__":
    app.run()
    
