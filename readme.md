# Outseta + Flask + Flask-Login Quickstart

* I am not sure if this is all perfect. Use at your own risk. *

This repo is for quickly getting started using [Outseta](https://outseta.com) with [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

To use it, just paste your Outseta URL and keys into constants.py

### For authenticated pages
Include outseta_profile.html and pass the access_token stored in the Flask login user object to the template

See */hidden* for an example

### For unauthenticated pages
Include outseta_auth.html
