# Celo ETL

## Overview

Celo ETL allows you to setup an ETL pipeline in Google Cloud Platform for ingesting Celo blockchain data
into BigQuery and Pub/Sub. It comes with [CLI tools](/cli) for exporting Celo data into convenient formats like CSVs and relational databases.

## Architecture

![celo_etl_architecture.svg](celo_etl_architecture.svg)

1. The nodes are run in a Kubernetes cluster.

2. [Airflow DAGs](https://airflow.apache.org/) export and load Celo data to BigQuery daily.
   Refer to [Celo ETL Airflow](/airflow) for deployment instructions.

3. Celo data is polled periodically from the nodes and pushed to Google Pub/Sub.
   Refer to [Celo ETL Streaming](/streaming) for deployment instructions.

4. Celo data is pulled from Pub/Sub, transformed and streamed to BigQuery.
   Refer to [Celo ETL Dataflow](/dataflow) for deployment instructions.

## Setting Up

1. Follow the instructions in [Celo ETL Airflow](/airflow) to deploy a Cloud Composer cluster for
   exporting and loading historical Celo data. It may take several days for the export DAG to catch up. During this
   time "load" and "verify_streaming" DAGs will fail.

2. Follow the instructions in [Celo ETL Streaming](/streaming) to deploy the Streamer component. For the value in
   `last_synced_block.txt` specify the last block number of the previous day. You can query it in BigQuery:
   `SELECT number FROM crypto_celo.blocks ORDER BY number DESC LIMIT 1`.

3. Follow the instructions in [Celo ETL Dataflow](/dataflow) to deploy the Dataflow component. Monitor
   "verify_streaming" DAG in Airflow console, once the Dataflow job catches up the latest block, the DAG will succeed.
