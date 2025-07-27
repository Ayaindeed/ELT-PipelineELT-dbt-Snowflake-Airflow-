FROM astrocrpublic.azurecr.io/runtime:3.0-6

# Create dbt virtual environment in a standard location
RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-snowflake && \
    mkdir -p /home/astro/.local/bin && \
    ln -sf /usr/local/airflow/dbt_venv/bin/dbt /home/astro/.local/bin/dbt && \
    ls -la /usr/local/airflow/dbt_venv/bin/dbt && \
    /usr/local/airflow/dbt_venv/bin/dbt --version

# Add to PATH
ENV PATH="/home/astro/.local/bin:${PATH}"

