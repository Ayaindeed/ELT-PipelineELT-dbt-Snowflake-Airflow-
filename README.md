# DBT + Airflow Data Pipeline

A complete ELT pipeline implementation using dbt, Snowflake, and Apache Airflow with Astronomer Cosmos for orchestration.

## Overview

This project demonstrates a modern data engineering stack with:
- **Extract, Load, Transform (ELT)** pipeline using dbt
- **Snowflake** as the cloud data warehouse
- **Apache Airflow** for orchestration
- **Astronomer Cosmos** for dbt-Airflow integration
- **Docker** containerization for consistent deployment

## Architecture

```
Data Sources → Snowflake (Raw) → dbt (Transform) → Snowflake (Marts) → BI Tools
                                      ↑
                                  Airflow Orchestration
```

## Key Components

### 1. Snowflake RBAC Setup
- Configured warehouses, roles, schemas, databases, and users
- Proper security and access control implementation

### 2. dbt Configuration
- `dbt_project.yml` setup for project structure
- Staging and source models for data ingestion
- Fact tables and data marts for analytics
- Custom macros for reusable transformations
- Generic and singular tests for data quality

### 3. Airflow Orchestration
- Docker-based Airflow deployment using Astro CLI
- Cosmos integration for dbt task management
- Automated pipeline scheduling and monitoring

## Project Structure

```
├── dags/
│   ├── dbt_dag.py              # Main Airflow DAG
│   └── dbt/
│       └── data_pipeline/      # dbt project
│           ├── models/
│           │   ├── staging/    # Staging models
│           │   └── marts/      # Fact tables and dimensions
│           ├── macros/         # Custom dbt macros
│           ├── tests/          # Data quality tests
│           └── dbt_project.yml
├── Dockerfile                  # Custom Docker configuration
├── requirements.txt           # Python dependencies
└── README.md
```

## Setup Instructions

### Prerequisites
- Docker Desktop
- Astro CLI ([v1.34.1+](https://github.com/astronomer/astro-cli/releases))
- Snowflake account

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dbt-dag1
   ```

2. **Install Astro CLI**
   
   Download from: https://github.com/astronomer/astro-cli/releases/tag/v1.34.1
   
   Or use package managers:
   ```bash
   # macOS
   brew install astro
   
   # Windows
   winget install astronomer.astro
   ```

3. **Configure Snowflake Connection**
   
   In Airflow UI (Admin → Connections), create connection with:
   - Connection ID: `id_you_want`
   - Connection Type: `Snowflake`
   - Account: `<account_locator>.<region>.<cloud_provider>` 
   ### or use Account :   "account": "<account_locator>-<account_name>" // it didn't work for me! 
   - Username: `<your_username>`
   - Password: `<your_password>`
   - Warehouse: `<your_warehouse>`
   - Database: `<your_database>`
   - Schema: `<your_schema>`

4. **Start the environment**
   ```bash
   astro dev start
   ```

## Key Implementation Notes

### Docker Configuration
The Dockerfile includes custom setup for dbt integration:
- Creates isolated Python virtual environment for dbt
- Installs dbt-snowflake adapter
- Configures proper PATH for dbt executable
- Includes git installation for dbt dependencies

### Cosmos Integration
Uses the latest Astronomer Cosmos for seamless dbt-Airflow integration:
- Automatic DAG generation from dbt models
- Dependency management between dbt models
- Task-level monitoring and logging


## Testing

The project includes comprehensive data quality testing:
- **Generic Tests**: Built-in dbt tests (unique, not_null, relationships)
- **Singular Tests**: Custom SQL-based tests for business logic validation
- **Model Tests**: Validate transformations and calculations

## Acknowledgments

This project was built following the excellent tutorial by [Data with Marc](https://www.youtube.com/watch?v=OLXkGB7krGo&t=2071s). The tutorial provided a solid foundation for understanding the integration between dbt, Snowflake, and Airflow, which was then extended with custom Docker configurations and troubleshooting for production deployment.

## Deploy Your Project Locally
===========================

Start Airflow on your local machine by running 'astro dev start'.

This command will spin up five Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- DAG Processor: The Airflow component responsible for parsing DAGs
- API Server: The Airflow component responsible for serving the Airflow UI and API
- Triggerer: The Airflow component responsible for triggering deferred tasks
