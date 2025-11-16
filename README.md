# Personal Website

The code for the personal website of Benjamin Schmidt using Django.

# Local dev setup

1. Make a copy of [.env.template](.env.template), call it [.env](.env). 
2. Start postgres, run migration, and create a superuser with:
   ```shell
   podman kube play postgres.yaml --network=slirp4netns
   uv run python manage.py migrate
   uv run python manage.py createsuperuser
   ```
3. Start the dev server with:
   ```shell
   uv run python manage.py runserver
   ```
4. Optionally, you can build and run this as a container locally (static files won't work):
   ```shell
   podman build . -t benjaminschmidt.github.io/benjaminschmidt.github.io
   podman run -p 8000:8000 --env-file=.env --name benjaminschmidt.github.io --network=slirp4netns benjaminschmidt.github.io/benjaminschmidt.github.io:latest
   ```

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
