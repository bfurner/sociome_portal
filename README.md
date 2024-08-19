## Developer Documentation

<details>

To setup a local development environment:

* clone the repository
* change directories using `cd sociome_portal`
* create a virtual environment using `python3 -m venv sociome_portal`
* change directories using `cd sociome_portal`
* activate the vertual environment using `source bin/activate`
* install the dependencies using `pip install django-globus-portal-framework`
* Go to the Globus Developer Site and retrieve client is and client secrets
* Make sure `http://localhost:8000/complete/globus/` is added to the redirect`
* create settings/local.py with `SOCIAL_AUTH_GLOBUS_KEY` and `SOCIAL_AUTH_GLOBUS_SECRET` from Globus Developer site
  ```
  from sociome_portal.settings.base import *
  
  # Your portal credentials for a Globus Auth Flow
  SOCIAL_AUTH_GLOBUS_KEY = ""
  SOCIAL_AUTH_GLOBUS_SECRET = ""
  DEBUG = True
  SECRET_KEY =""
  STATIC_ROOT = "/usr/local/var/www/static/"
  ```
* change directories using `cd ..`
* create the initial database using `python manage.py migrate`

* in order to test local deployment one can run the django app locally using `python manage.py runserver`

</details>
