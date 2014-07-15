# ----- Flask Hello World ------- #

# import the Flask class from the flask module
from flask import Flask

# create the oplication object 
app = Flask(__name__)

# use decorators to links the function to a url 
@app.route("/")
@app.route("/hello")

# define the view use the function, which returns the string
def HelloWorld():
	return "Hello World!"

# start the development server using run() method
if __name__ == "__main__":
	app.run()