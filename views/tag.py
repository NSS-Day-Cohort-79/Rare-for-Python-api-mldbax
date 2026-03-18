"""view for holding tag functions"""

import sqlite3
import json


def get_tags():
    """Run query to get all tags and return serialized list of objects"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
            SELECT
                id,
                label
            FROM Tags
            """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        tags = []
        for row in query_results:
            tags.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_tags = json.dumps(tags)

    return serialized_tags


def retrieve_tag(pk):
    """Run query to get a single tag and return serialized result"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                id,
                label
            FROM Tags
            WHERE id = ?
            """,
            (pk,),
        )
        row = db_cursor.fetchone()
        serialized_tag = json.dumps(dict(row))

    return serialized_tag
