
def get_headers(table_name, cursor_db):
    cursor_db.execute(f"Select * FROM {table_name} LIMIT 0")
    colnames = [desc[0] for desc in cursor_db.description]
    return colnames
