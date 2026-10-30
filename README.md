![Banner](banner.png)

# cred-leak-BreachAlarm-Simple
A simple command-line tool that checks a single email address against the Have I Been Pwned API to quickly determine if it has been involved in any known data breaches. - Focused on Automated searching of public code repositories (e.g., GitHub, GitLab) and paste sites (e.g., Pastebin) for leaked credentials and sensitive information related to a specified organization or technology. Aims to identify exposed API keys, passwords, and other confidential data.

## Install
`git clone https://github.com/ShadowStrikeHQ/cred-leak-breachalarm-simple`

## Usage
`./cred-leak-breachalarm-simple [params]`

The email check calls the Have I Been Pwned v3 API, which needs a paid API key. Set it in the HIBP_API_KEY environment variable before running with -e. The -o and -t modes print a placeholder notice and do not search anything.

## Parameters
- `-h`: Show help message and exit

## License
Copyright (c) ShadowStrikeHQ
