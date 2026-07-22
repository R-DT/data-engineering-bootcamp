from datetime import datetime, timedelta
import airflow  # type: ignore
from airflow import DAG  # type: ignore
from airflow.providers.docker.operators.docker import DockerOperator  # type: ignore
from docker.types import Mount  # type: ignore

# 1. Define strict default operational parameters for your platform tasks
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2026, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,                      
    "retry_delay": timedelta(minutes=5) 
}

# 2. Instantiate the global Directed Acyclic Graph scheduler layout
with DAG(
    "fintech_data_platform_pipeline",
    default_args=default_args,
    description="Automated ingestion, validation, and loading pipeline for transaction records",
    schedule_interval="@daily",        
    catchup=False,
    max_active_runs=1
) as dag:

    # 3. Create the automated execution task vector using the Docker container image
    run_etl_pipeline = DockerOperator(
        task_id="execute_fintech_etl",
        image="fintech-platform:latest",  
        command="-m run",                 
        api_version="auto",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
        network_mode="docker_default",     
        mounts=[
            Mount(
                source="/var/lib/fintech/data", 
                target="/app/data", 
                type="bind"
            )
        ],
        environment={
            "DB_USER": "postgres",
            "DB_PASS": "postgres",
            "DB_HOST": "warehouse_db",     
            "DB_PORT": "5432",
            "DB_NAME": "fintech_db"
        }
    )

    # Suppress the unused expression warning for the Airflow task declaration
    _ = run_etl_pipeline  # type: ignore
