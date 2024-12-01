init:
    rm -rf .venv
    python3.12 -m venv .venv --prompt advent_of_code
    .venv/bin/pip3 install --upgrade pip
    .venv/bin/pip3 install -r requirements.txt
    .venv/bin/pre-commit install
