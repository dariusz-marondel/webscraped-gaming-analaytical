#!/usr/bin/env bash

# Activate the virtual environment
source /opt/venv/bin/activate

# Initialize the Airflow database
airflow db init

# Create an Airflow user
airflow users create \
    --role Admin \
    --username admin \
    --email admin@example.com \
    --firstname admin \
    --lastname user \
    --password admin1234

# Start the Airflow webserver
exec airflow webserver
