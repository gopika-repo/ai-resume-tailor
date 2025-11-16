from flask import Flask

# Create an instance of the Flask app
app = Flask(__name__)

# Define a "route" for the home page
@app.route('/')
def home():
    return "Hello from the AI Resume Tailor Backend!"

# This makes the app runnable with "python app.py"
if __name__ == '__main__':
    app.run(debug=True)