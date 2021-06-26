# Outseta + Flask + Flask-Login Quickstart

This repo is for quickly getting started using [Outseta](https://outseta.com) with [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

To use it, just paste your Outseta URL and keys into constants.py

### For authenticated pages
Include outseta_profile.html and pass the access_token stored in the Flask login user object to the template

See */hidden* for an example

### For on authenticated pages
Include outseta_auth.html
