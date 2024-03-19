import dlt

from duckdb_source import duckdb_tables_source


def load_selected_tables(database, tables):
    """Function creates pipeline and load only selected tables from duckdb database.
    Please, note, that table names should be written with schemas names (ex. schema_name.table_name)
    """
    pipeline = dlt.pipeline(
        pipeline_name='duckdb', destination='filesystem', dataset_name='duckdb_data'
    )
    load_info = pipeline.run(duckdb_tables_source(database, tables))
    print(load_info)


def load_all_tables(database):
    """Function creates pipeline and load all tables from duckdb database."""
    pipeline = dlt.pipeline(
        pipeline_name='duckdb', destination='filesystem', dataset_name='duckdb_data'
    )
    load_info = pipeline.run(duckdb_tables_source(database))
    print(load_info)


if __name__ == "__main__":
    database = "mydb.duckdb"
    # load_selected_tables(database, ["schema_name.table_name"])  # load only specific table
    load_all_tables(database)  # load all tables from database
