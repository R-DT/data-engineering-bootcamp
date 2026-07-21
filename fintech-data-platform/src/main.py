import logging
import sys
from .generator import TransactionGenerator
from .extractor import TransactionExtractor
from .transformer import TransactionTransformer
from .analyzer import TransactionAnalyzer
from .loader import TransactionLoader


# Configure standard production-level global tracking format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("pipeline_orchestrator")

def run_platform_pipeline():
    logger.info("=== STARTING FINTECH DATA PLATFORM PIPELINE ===")
    
    try:
        # 1. Initialize components
        generator = TransactionGenerator()
        extractor = TransactionExtractor()
        transformer = TransactionTransformer()
        analyzer = TransactionAnalyzer()
        loader = TransactionLoader()

        # 2. Run execution sequence
        raw_path = generator.generate()
        raw_data = extractor.extract()
        cleaned_data = transformer.clean(raw_data)
        metrics = analyzer.calculate_metrics(cleaned_data)
        
        loader.save_processed_data(cleaned_data)
        loader.save_analytics_report(metrics)
        
        logger.info("=== PIPELINE RUN COMPLETE: SUCCESS ===")

    except Exception as e:
        logger.critical(f"Pipeline crashed during execution lifecycle: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    run_platform_pipeline()
