from __future__ import print_function

import logging

from celoetl_airflow.build_partition_dag import build_partition_dag

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

chain_name = 'celo'

# airflow DAG
DAG = build_partition_dag(
    dag_id=f'{chain_name}_partition_dag',
    partitioned_project_id='blockchain-etl-internal',
    partitioned_dataset_name=f'crypto_{chain_name}_partitioned',
    public_project_id='nansen-public-data',
    public_dataset_name=f'crypto_{chain_name}',
    load_dag_id=f'{chain_name}_load_dag',
    schedule_interval='0 8 * * *',
)
