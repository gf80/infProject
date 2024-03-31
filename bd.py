import sqlite3


def connect_to_bd(bd_name):
    conn = sqlite3.connect(bd_name)
    cursor = conn.cursor()
    return conn, cursor


def fetch_data(cursor, table_name, columns='*', condition=None):
    query = f"SELECT {columns} FROM {table_name}"
    if condition:
        query += f" WHERE {condition}"
    cursor.execute(query)
    return cursor.fetchall()


def fetch_related_data(cursor, table1, table2, join_condition, columns='*', condition=None):
    query = f"SELECT {columns} FROM {table1} INNER JOIN {table2} ON {join_condition}"
    if condition:
        query += f" WHERE {condition}"
    cursor.execute(query)
    return cursor.fetchall()


def create_table(cursor: sqlite3.Connection, table_name: str, columns: str):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
    print(f"table {table_name} was created!")

def create_record(cursor: sqlite3.Connection, table_name: str, values: tuple):
    cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(values))})", values)


def update_record(cursor, table_name, set_values, condition):
    cursor.execute(f"UPDATE {table_name} SET {set_values} WHERE {condition}")


def delete_record(cursor, table_name, condition):
    cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")


def drop_table(cursor, table_name):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")


def close_connection(conn):
    conn.commit()
    conn.close()


