# customer-analytics

This repository provides a small data-cleaning script and an entrypoint `app.py`.

If you encounter the "externally-managed-environment" error when running `pip install`, create and use a virtual environment.

Quick start (Debian/Ubuntu):

1. Ensure Python 3.12 and venv support are installed:

```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-distutils -y
```

2. Create and activate a virtual environment inside the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Upgrade pip inside the venv and install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

If you prefer pipx for installing `jupyter` globally, install pipx first and use `pipx install jupyter`.
