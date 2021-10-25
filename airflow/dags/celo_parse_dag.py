from __future__ import print_function

from glob import glob
import logging
import os

from celoetl_airflow.build_parse_dag import build_parse_dag
from celoetl_airflow.variables import read_parse_dag_vars

chain_name = 'celo'

DAGS_FOLDER = os.environ.get('DAGS_FOLDER', '/home/airflow/gcs/dags')
table_definitions_folder = os.path.join(DAGS_FOLDER, f'resources/stages/parse/table_definitions_{chain_name}/*')

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

for folder in glob(table_definitions_folder):
    dataset = folder.split('/')[-1]

    dag_id = f'{chain_name}_parse_{dataset}_dag'
    logging.info(folder)
    logging.info(dataset)
    globals()[dag_id] = build_parse_dag(
        dag_id=dag_id,
        chain_name=chain_name,
        dataset_folder=folder,
        source_project_id='nansen-public-data',
        source_dataset_name=f'crypto_{chain_name}',
        internal_project_id='blockchain-etl-internal',
        **read_parse_dag_vars(
            var_prefix=f'{chain_name}_',
            dataset=dataset,
            schedule_interval='30 8 * * *'
        )
    )
