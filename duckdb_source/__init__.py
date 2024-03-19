import duckdb
import dlt


def get_all_tables(conn):
    db_structure = conn.sql("SHOW ALL TABLES").df()
    tables = []
    for row in db_structure.itertuples():
        if row.name.startswith("_dlt"):
            continue
        tables.append(f"{row.schema}.{row.name}")
    return tables


def get_duckdb_table(database, table_name):
    # Connect to DuckDB and execute query to fetch data
    with duckdb.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        yield data


@dlt.source(max_table_nesting=0)
def duckdb_tables_source(database, table_names=None):
    if table_names is None:
        with duckdb.connect(database) as conn:
            table_names = get_all_tables(conn)
    for table_name in table_names:
        yield dlt.resource(get_duckdb_table(database, table_name), name=table_name)