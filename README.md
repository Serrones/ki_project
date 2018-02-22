# KI_PROJECT

Single Web Application built with Python Flask Framework


# Virtual Environment

We strongly recommend that you create a virtual environment in your computer before installing anything!!

For more information about venv:

https://docs.python.org/3/library/venv.html


# Requirements

Flask==0.12.2

Jinja2==2.10

ki-project==0.0.0

requirements==0.1

pytest==3.4.1

After cloning this repository in your computer's virtual environment, run the following command:

** Dont't forget to activate your venv!!!! **

`pip install requirements.txt`


# What is ki_project?

`ki_project` is a very basic single page web application built in Python language, and for this project, it has choosen Flask, a micro web framework which give us the freedom of building a web application regardless the size or complexity.
This project, with just one view, one template and no database, is a perfect example of minimal web application that can be built with few code lines, simplicity and, best of all, tidy and clean scripts!!

# The goal

`ki_project` displays a randomic deck's list returned by the API:


`https://github.com/martincarrera/clash-royale-api`


# api_wrapper

`api_wrapper` is a python package built for this project, but we can add more
functions according with its use in other projects that work with API requests.
For this project, we have just one function (Don't worry!! `ki_project` has just
one view and one template)


# Running ki_project

commandline --> ki_project root

export FLASK_APP=ki_project  

export FLASK_DEBUG=true

flask run


# Using ki_project

By default, when you access `http://127.0.0.1:5000/`, it already delivers a page with decks being displayed 2 cards by row.
If you press the `New Deck` button, the page will be reloaded and another randomic deck group will be displayed the same way. 


# Test

Something that is untested is broken.

Even in a project like this, with a minimal structure, we must test the funcionalities
to avoid any setting problems or even bugs

# running tests in ki_project

commandline --> ki_project root

`py.test`

or

`python setup.py test`
