import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [  # Using a list instead of a set
    "src/__init__.py",  # Fixed the naming
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)  # Using makedirs instead of mkdir
        logging.info(f"Creating directory '{filedir}' for the file '{filename}'")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:  # Fixed file existence check
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"'{filename}' already exists.")
