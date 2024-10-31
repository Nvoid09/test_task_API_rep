import sqlite3


db_config = {
    "saddr": "TEXT NOT NULL",
    "avgDur": "INTEGER"
}


def init_db():
    """
    Init database SQLite3.
    Name of DB: ddos_info. Name of saved table: DDoS_table.
    """
    conn = sqlite3.connect("ddos_info.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DDoS_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            saddr TEXT,
            avgDur INTEGER
        )
    """)
    conn.commit()
    conn.close()


# Save to database
def save_to_db(json_list: list):
    """
    Update database SQLite3. Save calculations result.
    Input:
        List with data {saddr: avgDur} 
    """
    conn = sqlite3.connect("ddos_info.db")
    cursor = conn.cursor()
    for el_dict in json_list:
        # Check if there is already "saddr" in the database
        cursor.execute(
            'SELECT 1 FROM DDoS_table WHERE saddr = ?',
            (el_dict["saddr"],)
        )
        is_saddr_exists = cursor.fetchone() is not None
        # Add saddr if it is not in the database
        # Otherwise, change the value of avgDur in the table with the corresponding saddr
        if not is_saddr_exists:
            cursor.execute(
                """
                    INSERT INTO DDoS_table (saddr, avgDur)
                    VALUES (?, ?)
                """,
                (el_dict["saddr"], el_dict["avgDur"])
            )
            print("INSERTED")
        else:
            cursor.execute(
                """
                    UPDATE DDoS_table SET avgDur = ? WHERE saddr = ?
                """,
                (el_dict["avgDur"], el_dict["saddr"])
            )
            print("UPDATED")
    conn.commit()
    conn.close()
