# SauceDemo Test Automation Framework

A Python + Selenium + pytest test automation framework built against
[SauceDemo](https://www.saucedemo.com), a public demo e-commerce site made
for practicing test automation. This was my first end-to-end automation
project, built from scratch to learn real testing practices — not just
Selenium syntax, but how an actual test framework is structured, run, and
maintained.

## What it tests

27 automated tests covering the full shopping journey:

- **Login** — valid login, locked-out user, empty/invalid field combinations (parametrized)
- **Products** — page load, product names, prices, sorting (A-Z, Z-A, price low-high, high-low)
- **Cart** — adding/removing single and multiple items, cart count accuracy, continue shopping
- **Checkout** — full purchase flow end-to-end, required-field validation, and a calculation test that independently sums item prices and verifies the displayed subtotal/tax/total actually match
- **Session security** — logout, and confirming the browser back button doesn't bypass login after logout

Both positive and negative paths are covered throughout, not just happy-path clicking.

## Tech stack

- **Selenium WebDriver** — browser automation
- **pytest** — test runner (fixtures, markers, parametrization)
- **Page Object Model** — all locators/actions live in `pages/`, never in test files
- **PyYAML** — config-driven base URL and test users
- **pytest-html** — HTML test reports
- **Python `logging`** — timestamped action logs, written to console + file
- **GitHub Actions** — CI runs the smoke suite on every push/PR

## Project structure
'''
saucedemo-tests/
├── conftest.py # driver fixture, screenshot-on-failure hook
├── pytest.ini # markers, addopts, pythonpath
├── config.yaml # base URL, test user credentials
├── requirements.txt
├── pages/
│ ├── base_page.py # shared explicit-wait helpers + logging
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── tests/
│ ├── test_login.py
│ ├── test_products.py
│ ├── test_cart.py
│ └── test_checkout.py
├── utils/
│ ├── config_reader.py
│ ├── logger.py
│ ├── test_data.py
│ └── helpers.py
├── reports/
│ ├── report.html # generated on every run
│ ├── screenshots/ # auto-captured on test failure
│ └── logs/test_run.log # timestamped action log
└── .github/workflows/ # CI config'''

## Setup

```bash
git clone https://github.com/dhanishthayyil/saucedemo-tests.git
cd saucedemo-tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running tests

```bash
pytest -v              # run everything
pytest -m smoke        # fast subset, what CI runs on every push
pytest -m regression   # full regression suite
```

After a run, check:
- `reports/report.html` — visual pass/fail report
- `reports/screenshots/` — auto-saved screenshots for any failed test
- `reports/logs/test_run.log` — step-by-step action log for every run

## CI/CD

GitHub Actions runs the smoke suite automatically on every push and pull
request to `main`, on a fresh Ubuntu machine with Chrome installed on the
fly. The HTML report is uploaded as a workflow artifact either way, so a
failure is debuggable without re-running anything locally.

## Challenges I hit (and actually learned from)

This was my first real project, and most of the learning happened while
debugging, not while writing new code:

- Early on, pytest kept reporting **"collected 0 items"** with no error at
  all, which was more confusing than an actual crash. Eventually traced it
  to a test file that had silently saved empty — pytest doesn't treat an
  empty file as an error, it just has nothing to collect. Now I always
  double-check a file's line count (`wc -l`) if pytest goes suspiciously quiet.
- Hit a real `ImportError` because a `pages/` folder was missing
  `__init__.py`, so Python couldn't see it as a package. Small file, easy to
  forget, breaks everything downstream.
- Had a few `AttributeError`s from copy-pasting new methods into a page
  object but only partially replacing the file — the class was missing
  locators the new test depended on. Fixed by always re-checking the full
  file content (`cat`) after a big paste, not just assuming it landed right.
- When I moved tests into a `tests/` folder, imports broke again — needed
  `pythonpath = .` in `pytest.ini` so pytest could still resolve
  `from pages.login_page import LoginPage` from a subfolder.
- Learned the difference between **config values** (URL, credentials — things
  that vary per environment) and **test logic** (assertions — the actual
  claims a test makes). Only the former belongs in `config.yaml`.
- Learned explicit waits (`WebDriverWait` + `expected_conditions`) are more
  reliable than relying on implicit waits or nothing at all, especially once
  I added logging and could actually see how long each step was taking.

## What I'd add next

- Cross-browser runs (Firefox, WebKit) in CI, not just Chrome
- API-level test setup to seed cart state faster instead of clicking through the UI every time
- Visual regression testing on the product listing page
- A Playwright version of the same suite, to compare against Selenium directly