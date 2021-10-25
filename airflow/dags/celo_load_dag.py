from __future__ import print_function

import logging

from celoetl_airflow.build_load_dag import build_load_dag
from celoetl_airflow.variables import read_load_dag_vars

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

chain_name = 'celo'

# airflow DAG
DAG = build_load_dag(
    dag_id=f'{chain_name}_load_dag',
    chain=chain_name,
    deduplicate_receipts=False,
    load_traces=True,
    load_contracts=True,
    load_tokens=True,
    is_geth_traces=True,
    **read_load_dag_vars(
        var_prefix=f'{chain_name}_',
        load_schedule_interval='30 6 * * *'
    )
)
