# Fintech Data Platform

A modular, Python-based data engineering project that simulates a fintech transaction platform. 

This platform serves as a production-ready portfolio asset demonstrating modern data architecture, clean code principles, and end-to-end data pipelines.

## 🛠 Features Demonstrated

*   **Transaction Generation**: Simulates a live banking ledger with realistic data anomalies.
*   **Data Validation**: Separates validation rules from business logic to inspect record health.
*   **ETL Processing**: Extracts raw feeds, repairs missing data fields, and cleans transaction rows.
*   **Analytics & Reporting**: Aggregates business KPIs and exports audit-ready reporting summaries.
*   **SQL Integration**: Prepares transactional warehouse schemas for relational target databases.
*   **Production Architecture**: Built using dependency injection, automated testing, and a custom CLI.

## 🏗 Project Structure

```text
fintech-data-platform/
├── .env.example            # Configuration blueprint for environment variables
├── pyproject.toml          # Package metadata, tool paths, and CLI script bindings
├── requirements.txt        # Pinned project library dependencies
├── LICENSE                 # Project open-source license
├── README.md               # Quickstart manual and architecture overview
├── data/                   # Local file storage folders
│   ├── raw/                # Ingested mock transactions before processing
│   ├── processed/          # Clean, schema-enforced transaction datasets
│   └── reports/            # Exported business KPI reports (JSON)
├── docs/                   # Development guides and system design records
│   ├── architecture.md
│   └── roadmap.md
├── sql/                    # Relational data warehouse layer
│   ├── schema.sql          # Table structures, data types, and database constraints
│   └── queries.sql         # SQL analytical queries for business logic
├── src/                    # Processing Engine source code
│   ├── config.py           # Application settings, directories, and Enums
│   ├── logger.py           # Centralized logging configuration
│   ├── main.py             # Pipeline orchestrator and command-line interface
│   ├── generator.py        # Generates synthetic data with random anomalies
│   ├── extractor.py        # Safe ingestion step that reads raw files
│   ├── validator.py        # Validates records against data-quality rules
│   ├── transformer.py      # Cleans, fixes, and drops invalid data rows
│   ├── analyzer.py         # Calculates transaction statistics and counts
│   └── loader.py           # Saves output datasets to target destinations
└── tests/                  # Automated unit test validation suites (pytest)
```

## ⚡ Quickstart

### 1. Environment Setup
Activate your isolated virtual environment and install the required dependencies:
```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
pip install -e .
```

### 2. Run the Data Pipeline
Execute the complete ETL workflow natively from anywhere via the custom CLI entry-point:
```bash
fintech-platform
```

### 3. Run Automated Tests
Execute the test suites to verify your transformations work perfectly:
```bash
fintech-platform -m pytest
```
