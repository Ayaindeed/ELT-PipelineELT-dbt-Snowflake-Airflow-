import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# Get the directory where this DAG file is located
dag_dir = os.path.dirname(os.path.abspath(__file__))
dbt_project_path = os.path.join(dag_dir, "dbt", "data_pipeline")

profile_config = ProfileConfig(
profile_name="default",
target_name="dev",
profile_mapping = SnowflakeUserPasswordProfileMapping(
    conn_id="snowflake_conn",
    profile_args={"database": "DBT_DB", "schema": "DBT_DB_DBT_SCHEMA"},
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(dbt_project_path),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt"),
    schedule="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)