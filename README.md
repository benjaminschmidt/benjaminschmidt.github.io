# Personal Website

The code for the personal website of Benjamin Schmidt using Django.

# Local dev setup

1. Make a copy of [mise.local.toml.template](mise.local.toml.template), call it [mise.local.toml](mise.local.toml.template). 
2. Prepare the database with:
   ```shell
   mise run db-setup
   ```
3. Start the dev server and postgres with:
   ```shell
   mise run dev
   ```
4. Optionally, you can build and run this as a container locally
   (static files won't work, and there might be networking issues with postgres):
   ```shell
   podman build . -t personal-website/personal-website
   podman run -p 8000:8000 --env-file=.env --name personal-website --network=slirp4netns personal-website/personal-website:latest
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
