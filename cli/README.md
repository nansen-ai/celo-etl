# Celo ETL CLI


Celo ETL lets you convert blockchain data into convenient formats like CSVs and relational databases.

## Quickstart

Install Celo ETL CLI:

```bash
pip3 install celo-etl
```

Export blocks, actions and logs ([Schema](../docs/schema.md), [Reference](../docs/commands.md)):

```bash
> celoetl export_blocks --start-block 1 --end-block 500000 \
--output-dir output --provider-uri grpcs://api.mainnet.celo.one:443
```

---

Stream blocks, actions and logs to console ([Reference](../docs/commands.md#stream)):

```bash
> pip3 install celo-etl[streaming]
> celoetl stream --start-block 500000 -e block,action,log --log-file log.txt \
--provider-uri grpcs://api.mainnet.celo.one:443
```

For the latest version, check out the repo and call 
```bash
> pip3 install -e . 
> python3 celoetl.py
```

## Running Tests

```bash
> pip3 install -e .[dev,streaming]
> export CELOETL_PROVIDER_URI=grpcs://api.mainnet.celo.one:443
> pytest -vv
```

### Running Tox Tests

```bash
> pip3 install tox
> tox
```

## Running in Docker

1. Install Docker https://docs.docker.com/install/

2. Build a docker image
        
        > docker build -t celo-etl:latest .
        > docker image ls
        
3. Run a container out of the image

        > docker run -v $HOME/output:/celo-etl/output celo-etl:latest export_blocks -s 1 -e 5499999 -b 1000 -o out

4. Run streaming to console or Pub/Sub

        > docker build -t celo-etl:latest -f Dockerfile .
        > echo "Stream to console"
        > docker run celo-etl:latest stream --start-block 500000 --log-file log.txt
        > echo "Stream to Pub/Sub"
        > docker run -v /path_to_credentials_file/:/celo-etl/ --env GOOGLE_APPLICATION_CREDENTIALS=/celo-etl/credentials_file.json celo-etl:latest stream --start-block 500000 --output projects/<your-project>/topics/mainnet

