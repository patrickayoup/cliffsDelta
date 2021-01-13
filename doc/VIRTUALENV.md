# How to build a virtualenv

To build a virtualenv containing the required dev dependencies:

    $ python -m venv .venv

This will create a virtualenv in the current directory in `.venv`

# How to activate your virtualenv

## Linux / OSX

    $ source .venv/bin/activate

## Windows

    $ .venv\Scripts\activate.bat

Once your environment is activated, your prompt should show the name of the venv in parentheses; for example:

    (.venv) C:\Users\...\dev\projects\cliffsDelta

# How to update pip in your virtualenv

Normally, a new virtualenv has an older version than the latest version of pip. To update to the latest, from your activated environment:

    $ pip install --upgrade pip

# How to install the dev dependencies to your virtualenv

With your virtualenv activated, run:

    $ pip install -r REQUIREMENTS.txt
