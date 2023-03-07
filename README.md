# Data migration challenge

Welcome data-mig project.
This project is intented to quickly demonstrate the development process for a data engineering solution using gitflow.

## New Release - Version 2.0

I'm excited to present the new release, the version 2.0! This new release includes the following features:

- Feature 1: ETL module used to perform the migration of historical data from csv files.
- Feature 2: Data ingestion REST API

## Installation

To install the data-mig project, simply clone the repository and run the following command:

```console
pip install -r requirements.txt
```

## Usage

Please run the following command in order to perform the tests

```console
python -m unittest -v tests/TestExtract.py 
python -m unittest -v tests/TestTransform.py 
python -m unittest -v tests/TestLoad.py 
python -m unittest -v tests/TestAPI.py 
```

Further functionality will be added in the future.
