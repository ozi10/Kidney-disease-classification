import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init.py",
    f"src/{project_name}/components/__init.py",
    f"src/{project_name}/utils/__init.py",
    f"src/{project_name}/config/__init.py",
    f"src/{project_name}/config/configurator/__init.py",
    f"src/{project_name}/pipeline/__init.py",
    f"src/{project_name}/entity/__init.py",
    f"src/{project_name}/constants/__init.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory; {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info("Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filename} already exists")