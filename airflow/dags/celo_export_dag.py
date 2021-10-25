from __future__ import print_function

from celoetl_airflow.build_export_dag import build_export_dag
from celoetl_airflow.variables import read_export_dag_vars

chain_name = 'celo'
start_date = '2020-04-22'

# airflow DAG
DAG = build_export_dag(
    dag_id=f'{chain_name}_export_dag',
    trace_export_batch_size=50,
    export_traces_toggle=True,
    extract_contracts_toggle=True,
    extract_tokens_toggle=True,
    is_geth_traces=True,
    export_format='csv',
    **read_export_dag_vars(
        var_prefix=f'{chain_name}_',
        export_schedule_interval='0 1 * * *',
        export_start_date=start_date,
        export_max_active_runs=1,
        export_max_workers=5,
        export_batch_size=10,
    )
)
