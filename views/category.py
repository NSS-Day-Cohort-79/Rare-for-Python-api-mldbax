"""view for holding category functions"""

import sqlite3
import json


def get_categories():
    """Run query to get all categories and return list of objects"""
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
            FROM Categories
            """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        categories = []
        for row in query_results:
            categories.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_categories = json.dumps(categories)

    return serialized_categories


def retrieve_category(pk):
    pass
