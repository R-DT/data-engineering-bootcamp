import argparse
import sys
import pytest
from src.config import Settings
from src.logger import setup_logger
from src.generator import TransactionGenerator
from src.extractor import TransactionExtractor
from src.validator import TransactionValidator
from src.transformer import TransactionTransformer
from src.analyzer import TransactionAnalyzer
from src.loader import FileLoader

logger = setup_logger("pipeline_orchestrator")

def run_platform_pipeline() -> None:
    """Entry point for the fintech-platform CLI tool, handling both ETL runs and testing."""
    # 1. Initialize the command-line argument parser engine
    parser = argparse.ArgumentParser(
        description="Fintech Data Platform Core Ingestion and Testing CLI Tool."
    )
    
    # Add the specific '-m' or '--mode' argument flag to match your target syntax
    parser.add_argument(
        "-m", 
        "--mode", 
        type=str, 
        default="run",
        choices=["run", "pytest", "pytests"],
        help="Specify the engine operation mode: 'run' to execute ETL, 'pytest' to execute unit verification suites."
    )
    
    # Parse incoming system parameters safely
    args = parser.parse_args()

    # 2. Intercept Testing Mode
    if args.mode in ["pytest", "pytests"]:
        logger.info("=== INITIALIZING PLATFORM AUTOMATED TEST RUNNER ===")
        # Invoke pytest programmatically against your structured tests directory
        exit_code = pytest.main(["tests"])
        sys.exit(exit_code)

    # 3. Fallback to Normal ETL Pipeline Run Mode
    logger.info("=== STARTING REFACTORED FINTECH DATA PLATFORM PIPELINE ===")
    try:
        settings = Settings()
        generator = TransactionGenerator(settings)
        extractor = TransactionExtractor(settings)
        validator = TransactionValidator(settings)
        transformer = TransactionTransformer(settings)
        analyzer = TransactionAnalyzer(settings)
        loader = FileLoader(settings)

        generator.generate_transactions()
        raw_data = extractor.extract_transactions()
        validation_report = validator.validate_transactions(raw_data)
        cleaned_data = transformer.clean_transactions(raw_data, validation_report)
        metrics = analyzer.calculate_metrics(cleaned_data)
        
        loader.save_data(cleaned_data)
        loader.save_report(metrics)
        
        logger.info("=== PIPELINE RUN COMPLETE: SUCCESS ===")

    except Exception as e:
        logger.critical(f"Pipeline crashed during execution lifecycle: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    run_platform_pipeline()
