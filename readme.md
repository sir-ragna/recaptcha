
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

To enable IPv6 listening on IPv6 use `--host=::1` for localhost only.
Use `--host=::` to enable everyone to contact you both over IPv4 and IPv6.

```sh
flask run --host=::
```

When someone connects over IPv4 the address will be prefixed with `::FFFF:`.
For example:

```log
::ffff:127.0.0.1 - - [19/Dec/2020 10:10:48] "GET / HTTP/1.1" 200 -
::ffff:127.0.0.1 - - [19/Dec/2020 10:10:48] "GET /favicon.ico HTTP/1.1" 404 -
```

# BUG?

In Firefox the using the IPv4 embed in IPv6 method the reCaptcha seems to break.

How to reproduce:

- Make sure you have `127.0.0.1` in your captcha list
- Start your server with both IPv4 and IPv6 support `flask run --host=::`
- Embed `127.0.0.1` in your IPv6 address and browse to `http://[::ffff:7f00:1]:5000/`
- Click on the submit button
- The submit button will become grey and eventually the following text will show: _Could not connect to the reCAPTCHA service. Please check your internet connection and reload to get a reCAPTCHA challenge._

This does not seem to happen in Chromium.

I compared _Firefox 84.0(64-bit) for Manjaro Linux_ and _Chromium 87.0.4280.66 (Official Build) Arch Linux (64-bit)_

It is unclear to me whether this is a Firefox or a reCaptcha issue.

