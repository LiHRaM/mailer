import smtplib
from email.mime.text import MIMEText
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated


def send_email(
    to: str,
    subject: str,
    body: str,
    smtp_server: str,
    smtp_port: int,
    smtp_username: str,
    smtp_password: str,
):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_username
    msg["To"] = to

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()


def main(
    to: str,
    subject: str,
    username: Annotated[str, typer.Option(envvar="SMTP_USERNAME")],
    password: Annotated[
        str, typer.Option(envvar="SMTP_PASSWORD", prompt=True, hide_input=True)
    ],
    body: Optional[str] = None,
    body_path: Annotated[
        Optional[Path],
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
            allow_dash=True,
            path_type=str,
        ),
    ] = None,
    server: str = "smtp.gmail.com",
    port: int = 587,
):
    if body_path:
        with open(body_path, "r") as f:
            body = f.read()

    if not body:
        raise typer.BadParameter("Must provide either body or body_path")

    send_email(to, subject, body, server, port, username, password)

def run():
    typer.run(main)

# Use `python src/main.py --help` to see the help message.
if __name__ == "__main__":
    run()
