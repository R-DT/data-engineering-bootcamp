# Module 01 - Banking Transaction Analyzer Pipeline

An transactional pipeline application built for Moniepoint data infrastructure tracks. This module ingests mock core system ledger entries, sanitizes corrupted attributes, normalizes operational time-series data vectors, and publishes structured performance profiles.

## Technologies Used
- Python 3.11+
- Isolated Workspace Environment (`venv`)
- Pandas Vector Data Structures
- NumPy Numerical Engines

## Project Structure
```text
week01-python/
├── README.md                  # Project documentation profile
├── banking_analyzer.py        # Complete ETL pipeline script execution core
├── raw_moniepoint_transactions.csv # Automatically generated messy source
├── clean_transactions.csv     # Validated data warehouse target artifact
└── summary.csv                # Aggregated key financial matrix data
```

## How to Install & Run

1. Open your terminal at your repository root level and verify your environment container is running:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. Execute the self-contained pipeline application execution block:
   ```powershell
   python week01-python/banking_analyzer.py
   ```

## Future Technical Improvements
- Integrate `SQLAlchemy` mapping components to push the production DataFrame directly into a staging database target instead of flat `.csv` local disk targets.
- Abstract transformation steps into explicit testing modules using `pytest` hooks.
