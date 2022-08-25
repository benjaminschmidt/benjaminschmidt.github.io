# Personal Website (v0.1.0)

The code for the personal website of Benjamin Schmidt. Written with Django.

DO NOT DEPLOY THIS WEBSITE WITHOUT CHANGING THE PASSWORD IN
personal_site/settings.py

# How to deploy on server

1. Clone the repository with `git clone https://github.com/benjaminschmidt/personal_site.git`.

2. Go to `personal_site/personal_site/settings.py` and change the `SECRET_KEY`.

3. Create a new virtual environment with `python3 -m venv venv`.

4. Activate the virtual environment with `source venv/bin/activate`.

5. Upgrade stuff and install Django with
    * `python3 -m pip install --upgrade pip`
    * `python3 -m pip install Django` 


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