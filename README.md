# Personal Website (v0.1.0)

The code for the personal website of Benjamin Schmidt using Django.

DO NOT DEPLOY THIS WEBSITE WITHOUT CHANGING THE PASSWORD IN
personal_site/settings.py

# How to deploy on [PythonAnywhere](https://www.pythonanywhere.com/)

Consider to check out the official
[instructions](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) for setting up an existing project on PythonAnywhere.

1. Clone the repository with
`git clone https://github.com/benjaminschmidt/benjaminschmidt.github.io.git`.

2. Open `benjaminschmidt.github.io/personal_site/settings.py`.
    * Change the `SECRET_KEY`.
    * Add domain name to `ALLOWED_HOSTS`.
    * Add `STATIC_ROOT = "/home/bschmidt/benjaminschmidt.github.io/static/"`

3. Create a new virtual environment with `python3 -m venv venv`.

4. Activate the virtual environment with `source venv/bin/activate`.

5. Upgrade pip and install Django with
    * `python3 -m pip install --upgrade pip`
    * `python3 -m pip install Django`
    * `python3 -m pip install Pillow`

6. Go to the Django projects folder with `cd benjaminschmidt.github.io.git`.

7. Run `python3 manage.py collectstatic`

8. Run the database migrations with `python3 manage.py migrate`.

9. Create an admin user with `python3 manage.py createsuperuser`.

10. Follow the remaining
[instructions](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject)
on PythonAnywhere.

11. Once everything works go back to
`benjaminschmidt.github.io/personal_site/settings.py` and set `DEBUG = False`.


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