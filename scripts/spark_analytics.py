import logging
from pathlib import Path
from pyspark.sql import SparkSession  # type: ignore
from pyspark.sql.functions import col, sum as _sum, avg, count  # type: ignore

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("pyspark_analytics_engine")

def run_distributed_analytics() -> None:
    logger.info("Initializing Distributed Spark Session Engine...")
    
    # Initialize local cluster context
    spark = SparkSession.builder \
        .appName("FintechPlatformSparkAnalytics") \
        .master("local[*]") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")

    try:
        base_dir = Path(__file__).resolve().parent.parent
        parquet_source = base_dir / "data" / "processed" / "cleaned_ledger.parquet"
        report_destination = base_dir / "data" / "reports" / "spark_channel_metrics.csv"

        if not parquet_source.exists():
            raise FileNotFoundError(f"Distributed Ingestion Error: Target Parquet asset not found at {parquet_source}")

        logger.info(f"Ingesting binary columnar Parquet records from data lake: {parquet_source}")
        df = spark.read.parquet(str(parquet_source))
        
        logger.info("Calculating distributed transactional metrics across payment channels...")
        channel_metrics = df.groupBy("Channel").agg(
            count("TransactionID").alias("total_transactions"),
            _sum("Amount").alias("gross_volume_usd"),
            avg("Amount").alias("average_transaction_value")
        ).orderBy(col("gross_volume_usd").desc())

        # Display calculation result summary directly to your terminal panel screen
        logger.info("Distributed Calculation Success. Result Ledger Snapshot:")
        channel_metrics.show(truncate=False)

        # WINDOWS WORKAROUND: Pull aggregated rows to driver memory and save via Pandas to bypass Hadoop winutils.exe
        logger.info("Converting calculated metrics to Pandas DataFrame for local Windows storage write...")
        pandas_report = channel_metrics.toPandas()
        
        # Ensure target folder structures exist using pathlib boundaries
        report_destination.parent.mkdir(parents=True, exist_ok=True)
        pandas_report.to_csv(report_destination, index=False)
        
        logger.info(f"PySpark Analytical Run Complete. Clean CSV report written safely to -> {report_destination}")

    except Exception as e:
        logger.error(f"PySpark processing engine encountered a critical disruption: {str(e)}", exc_info=True)
    finally:
        spark.stop()
        logger.info("Spark Session safely deactivated.")

if __name__ == "__main__":
    run_distributed_analytics()
