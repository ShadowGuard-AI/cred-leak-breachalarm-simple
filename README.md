![Banner](banner.png)

# cred-leak-BreachAlarm-Simple
A simple command-line tool that checks a single email address against the Have I Been Pwned API to quickly determine if it has been involved in any known data breaches.

## Install
`git clone https://github.com/ShadowGuard-AI/cred-leak-breachalarm-simple`

## Usage
`python3 main.py (-e EMAIL | -o ORG | -t TECH)`

The email check calls the Have I Been Pwned v3 API, which needs a paid API key. Set it in the HIBP_API_KEY environment variable before running with -e. The -o and -t modes print a placeholder notice and do not search anything.

## Parameters
- `-h`: Show help message and exit
- `-e`, `--email`: Email address to check against Have I Been Pwned. Exactly one of `-e`, `-o`, and `-t` is required.
- `-o`, `--org`: Organization name to search for.
- `-t`, `--tech`: Technology to search for.

## Verified behavior
- The parameter list above is taken from the argument parser in `main.py`, and `main.py` passes `py_compile`.
- A live run was not completed in this wave: the `aiohttp` package is not installed here and installs are not permitted in this wave, and the email check would also need a paid HIBP API key and network access to that API. Install `aiohttp` from `requirements.txt` and set HIBP_API_KEY before running with `-e`.

## License
See LICENSE.
