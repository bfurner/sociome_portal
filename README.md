## Developer Documentation

<details>

To setup a local development environment:

* clone the repository
* change directories using `cd itmdatacommons`
* initiate uv project using `uv init --no-workspace`
* create a virtual environment using `uv venv`
* activate the vertual environment using `source .venv/bin/activate`
* install the dependencies using `uv add django-globus-portal-framework`
* Go to the Globus Developer Site and retrieve client ID and client secrets
* Make sure `http://localhost:8000/complete/globus/` is added to the redirect`
* create settings/local.py with `SOCIAL_AUTH_GLOBUS_KEY` and `SOCIAL_AUTH_GLOBUS_SECRET` from Globus Developer site
  ```
  from itmdatacommons.settings.base import *
  
  # Your portal credentials for a Globus Auth Flow
  SOCIAL_AUTH_GLOBUS_KEY = ""
  SOCIAL_AUTH_GLOBUS_SECRET = ""
  DEBUG = True
  SECRET_KEY =""
  STATIC_ROOT = "/usr/local/var/www/static/"
  ```
* change directories using `cd ..`
* create the initial database using `uv run python manage.py migrate`

* in order to test local deployment one can run the django app locally using `uv run python manage.py runserver`

</details>
