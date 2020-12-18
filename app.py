from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def recaptcha():
    RECAPTCHA_SITE_KEY = os.environ.get("RECAPTCHA_SITE_KEY")
    return render_template('index.html', RECAPTCHA_SITE_KEY=RECAPTCHA_SITE_KEY)


@app.route('/postform', methods=['GET', 'POST'])
def postform():
    RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')
    
    # Validate reCaptcha
    if "g-recaptcha-response" in request.form:
        recaptcha_response = request.form["g-recaptcha-response"]
        result = requests.post("https://www.google.com/recaptcha/api/"
            f"siteverify?secret={RECAPTCHA_SECRET_KEY}&response={recaptcha_response}").json()
        print(f"Recaptcha response: {result}")
        if result.get('success'):
            return f"Good recaptcha <br>{result}"
        else:
            return f"Bad captcha <br>{result}"
    else:
        return "No captcha provided"
    
