"""Load raw data from kaggle and save to csv.

Option will exist to initially check if the file exists and only redownload if it doesn't.
"""

import pandas as pd
import os
import sys
import shutil
import kagglehub
from pathlib import Path

def import_raw_data(datapath: str = "data/raw/"):
    path = Path(kagglehub.dataset_download("tobycrabtree/nfl-scores-and-betting-data"))
    if not os.path.exists(datapath):
        os.makedirs(datapath)
    for filepath in path.iterdir():
        if filepath.is_file():
            shutil.move(filepath,datapath)

if __name__ == "__main__":
    import_raw_data()