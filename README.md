![A keeper's hand on a brass bell rope close up, the bell above and a shuttered window beside it, plain flags above the roof and a soft harbour behind, with no lettering anywhere](intro-banner.png)

# cred-leak-BreachAlarm-Simple

Theme: Oyster Reef Restoration Barge. Display face: BigShouldersInlineDisplay. Text face: Bitter.

![A harbourside signal station, its keeper at the one open window with a telescope, two neighbouring windows shuttered, plain red and yellow flags at the mast and a brass bell on the wall, boats soft and distant, with no lettering anywhere](banner.png)

![Animated scene](scene.svg)

![Separator](sep-heavy.svg)

![A harbourside signal station, its keeper at the one open window with a telescope, two neighbouring windows shuttered, plain red and yellow flags at the mast and a brass bell on the wall, boats soft and distant, with no lettering anywhere](banner.png)

# cred-leak-BreachAlarm-Simple
A simple command-line tool that checks a single email address against the Have I Been Pwned API to quickly determine if it has been involved in any known data breaches.


> **A PAID KEY IS REQUIRED** The version 3 service needs a paid key, supplied through the environment variable named in the README. No key value appears here.

## Install
`git clone https://github.com/ShadowGuard-AI/cred-leak-breachalarm-simple`


> **Placeholder. Searches Nothing.** The organisation and technology modes print a placeholder notice and search nothing.

## Usage
`python3 main.py (-e EMAIL | -o ORG | -t TECH)`

The email check calls the Have I Been Pwned v3 API, which needs a paid API key. Set it in the HIBP_API_KEY environment variable before running with -e. The -o and -t modes print a placeholder notice and do not search anything.


> **CLEAN AND FAILED LOOK THE SAME** A not found answer and a failed check print the same line, so that line alone cannot certify a clean address.

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


![Separator](sep-light.svg)

## Themed notes from the code

- The tool checks one email address against the Have I Been Pwned service.
- It uses version 3 of that service interface.
- It needs a paid key for that service, supplied through the environment variable named HIBP_API_KEY in the README.
- The key itself is never stated here. No key value and no sample credential of any kind appears in these themed surfaces.
- The check returns breach names only. It does not return dates, descriptions, or account details.
- The clone line in the README is correct and is shown without correction.
- The usage line shows a choice among three modes, and exactly one mode must be chosen on each run.
- The first mode takes an email address. The second mode takes an organisation name. The third mode takes a technology name.
- The second and third modes print a placeholder notice and search nothing. This is stated in the main text, not in a footnote.
- The help flag shows a help message and exits.
- The email flag takes the address to check and is one of the three required choices.
- The organisation flag takes a name to search for, subject to the placeholder limit stated above.
- The technology flag takes a technology to search for, subject to the same limit.
- An address with an invalid format ends the run with exit 1, stated as behaviour only, as a format check and nothing more.
- An empty organisation name ends the run with exit 1.
- An empty technology name ends the run with exit 1.
- A successful answer with breach names prints those names in a list.
- A not found answer prints a line saying that no breach record was returned.
- The same printed line also covers a failed check, because the code returns the same empty result for not found, for rate limiting, and for other service errors.
- A rate limit answer is logged as a warning to wait and try again.
- Other error answers are logged with their status code number, stated as a number only.
- No live run was completed in the recorded wave. The stated reasons were a missing package in that environment and the need for a paid key and network access.
- The README says to see the licence file, and the repository licence file is the MIT License.

## Buttons and headings in this theme

- Button: CHECK THIS ADDRESS
- Button: SEARCH AN ORGANISATION NAME
- Button: SEARCH A TECHNOLOGY NAME
- Heading: ONE ADDRESS CHECKED
- Heading: TAKING THE TOOL ABOARD
- Heading: THE THREE MODES
- Heading: WHAT COMES BACK
