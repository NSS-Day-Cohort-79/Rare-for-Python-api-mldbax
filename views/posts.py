"""view for holding posts functions"""

import sqlite3
import json


def get_posts():
    """Run query to get all posts and return list of objects"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
            SELECT
                id,
                user_id,
                category_id,
                title,
                publication_date,
                image_url,
                content,
                approved
            FROM Posts
            """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        posts = []
        for row in query_results:
            posts.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_posts = json.dumps(posts)

    return serialized_posts

def retrieve_post(pk):
    """Run query to get a single post and return serialized result"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                id,
                user_id,
                category_id,
                title,
                publication_date,
                image_url,
                content,
                approved
            FROM Posts
            WHERE id = ?
            """,
            (pk,),
        )
        row = db_cursor.fetchone()
        serialized_post = json.dumps(dict(row))

    return serialized_post