# spread-analysis
Kaggle project for historical analysis of NFL spread data.


## Setup


After cloning this repo and navigating to it, create the environment using:

```
conda env create -f environment.yml
```

Then activate the environment using:

```
conda activate spread-analysis
```

If you have not yet setup API access for Kaggle, refer to https://pypi.org/project/kagglehub/'s **Usage** section for setting up the API token. Once done, the following scripts can be run from the main repo folder to reproduce everything:

```
python scripts/01-download_raw.py
```
