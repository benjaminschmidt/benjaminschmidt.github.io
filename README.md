# Personal Website (v1.0.2)

The code for the personal website of Benjamin Schmidt using Django.

DO NOT DEPLOY THIS WEBSITE WITHOUT CHANGING THE PASSWORD IN
personal_site/settings.py

# How to deploy on [PythonAnywhere](https://www.pythonanywhere.com/)

Consider to check out the official
[instructions](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) for setting up an existing project on PythonAnywhere.

1. Open a new bash console and clone the repository with
`git clone https://github.com/benjaminschmidt/benjaminschmidt.github.io.git mysite`.

2. Open `mysite/personal_site/settings.py`.
    * Change the `SECRET_KEY`.
    * Add `'myusername.pythonanywhere.com'` to `ALLOWED_HOSTS`.

3. Create a new virtual environment with `python3 -m venv venv`.

4. Activate the virtual environment with `source venv/bin/activate`.

5. Upgrade pip and install Django and Pillow with
    * `python3 -m pip install --upgrade pip`
    * `python3 -m pip install Django`
    * `python3 -m pip install Pillow`

6. Go to the Django projects folder with `cd mysite`.

7. Run `python3 manage.py collectstatic` to collect all the static files.

8. Run the database migrations with `python3 manage.py migrate`.

9. Create an admin user with `python3 manage.py createsuperuser`.

10. Create a new web app.
    * Use `Manual configuration` and `Python 3.9`.
    * Add the full path to the source `/home/myusername/mysite`.
    * Choose the virtualenv to `/home/myusername/venv`.
    * Add a static files url `/static/` and path `/home/myusername/mysite/static/`

11. Open `/var/www/myusername_pythonanywhere_com_wsgi.py` and replace its
content by
    ```
    import os
    import sys

    path = '/home/myusername/mysite'
    if path not in sys.path:
        sys.path.insert(0, path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'personal_site.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```

12. Reload the website at the top of the settings page.

13. Go to the admin interface at `https://myusername.pythonanywhere.com/admin/`
and add all the information you want. The minimum to get the website to work is
to add a `myself` entry.

14. Once everything works go back to
`mysite/personal_site/settings.py` and set `DEBUG = False`.


# Credits

* The envelope icon under information/static/information/mail-icon.pgn is
licensed under CC0 1.0 Universal (CC0 1.0) and was downloaded from
https://www.iconsdb.com/black-icons/email-icon.html.

* Information about the license of the GitHub logo under
information/static/information/github.pgn can be found on
https://github.com/logos.

* Information about the license of the LinkedIn logo under
information/static/information/linkedin.pgn can be found on
https://brand.linkedin.com/downloads.
