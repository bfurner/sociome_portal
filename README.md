## Developer Documentation

<details>

To setup a local development environment:

* clone the repository
* change directories using `cd sociome_portal`
* create a virtual environment using `python3 -m venv sociome_portal`
* change directories using `cd sociome_portal`
* activate the vertual environment using `source bin/activate`
* install the dependencies using `pip install django-globus-portal-framework`
* create settings/local.py with client id and client secrets from Globus Developer site
* change directories using `cd ..`
* create the initial database using `python manage.py migrate`

* in order to test local deployment one can run the django app locally using `python manage.py runserver`

</details>
