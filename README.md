# `mailer`

A simple command line interface (CLI) for sending emails using SMTP.

## Installation

Please install this via `git`:

```bash
pip install git+https://github.com/LiHRaM/mailer.git
```

## Usage

This application can be run from the command line with the command `mailer`, followed by the necessary options.

The application accepts the following options:

- `--to`: The email address to send the email to (required).
- `--subject`: The subject of the email (required).
- `--username`: The SMTP username (required). Can also be set with the `SMTP_USERNAME` environment variable.
- `--password`: The SMTP password (required). Can also be set with the `SMTP_PASSWORD` environment variable. You will be prompted to enter it securely.
- `--body`: The body of the email. This option is mutually exclusive with `--body-path`.
- `--body-path`: A path to a text file containing the body of the email. This option is mutually exclusive with `--body`.
- `--server`: The SMTP server to use. Defaults to `smtp.gmail.com`.
- `--port`: The SMTP port to use. Defaults to `587`.

## Example

To send an email:

```bash
export SMTP_USERNAME=yourusername@gmail.com
mailer --to receiver@example.com --subject "Hello" --body "This is the body of the email."
```

When you run this command, you will be prompted to enter your SMTP password.

## License

[MIT](./LICENSE.md)
