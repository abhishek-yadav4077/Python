#Importing
from flask import Flask, render_template


# Interaction
web = Flask(__name__)

# Mapping
#www.youtube.com
@web.route('/')
@web.route('/register')

# Inputs
def homepage():
    return render_template('register.html')

# Main
if __name__ == "__main__":
    web.run(debug=True)

