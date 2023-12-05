from flask import Flask

# Create Flask application
# app = Flask(__name__)
app = Flask(__name__, template_folder='C:/Users/HP/OneDrive/Desktop/DEVPUTERS/Learning/Back-End-Development-Pictures/static/templates')

from backend import routes