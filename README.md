# Duckdb to filesystem example

This example contains code for loading data from duckdb source to filesystem (local/s3).

## Run

To run the example:

1. Set up poetry env
    ```
    pip install poetry
    poetry install
    ```
2. Set the name of duckdb database inside `duckdb_pipeline.py`
   ```
   database = "mydb.duckdb"
   ```
3. Set up credentials for s3 inside `.dlt/secrets.toml`

   ```
   [destination.filesystem]
   bucket_url = "s3://[your_bucket_name]" # replace with your bucket name,
   
   [destination.filesystem.credentials]
   aws_access_key_id = "aws_access_key_id" # please set me up!
   aws_secret_access_key = "aws_secret_access_key" # please set me up!
   ```
   
4. If you want to turn off file compressions, set `disable_compression` to `true` inside `.dlt/config.toml`

   ```
   [normalize.data_writer]
   disable_compression=true
   ```

5. Run the pipeline

   ```
   poetry run python duckdb_pipeline.py
   ```

