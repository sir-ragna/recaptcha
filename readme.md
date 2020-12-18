
# reCaptcha Example Code

## Set-up environment

The environment.

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.flaskenv` file if you like automatic reloads.

```sh
# file: .flaskenv
FLASK_ENV="development"
``` 

### reCaptcha keys

Create your reCaptcha keys: https://www.google.com/recaptcha/admin/

As site url enter `127.0.0.1` for your development environment.

You get a **SITE KEY** and a **SECRET KEY**. Add them in your `.flaskenv` file.

```sh
# file: .flaskenv
FLASK_ENV="development"
RECAPTCHA_SITE_KEY="<insert your sitekey here>"
RECAPTCHA_SECRET_KEY="<insert your secret key here>"
```

## Running

Activate the virtual environment and run flask.

```sh
source venv/bin/activate
flask run
```
