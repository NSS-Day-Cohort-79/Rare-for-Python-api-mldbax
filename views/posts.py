"""view for holding posts functions"""

import sqlite3
import json


def get_posts():
    """Run query to get all posts and return list of objects"""
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Expand user_id to get author name AND expand category_id to get category name

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
            SELECT
                p.id post_id,
                p.title,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved,
                u.first_name, 
                u.last_name,
                c.label 
            FROM Posts p
            JOIN Users u ON u.id = p.user_id
            JOIN Categories c ON c.id = p.category_id
            ORDER BY p.publication_date DESC
            """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        posts = []
        for row in query_results:
            user = {"first_name": row["first_name"], "last_name": row["last_name"]}
            category = {"label": row["label"]}
            post = {
                "id": row["post_id"],
                "user": user,
                "category": category,
                "title": row["title"],
                "publication_date": row["publication_date"],
                "image_url": row["image_url"],
                "content": row["content"],
                "approved": row["approved"],
            }
            posts.append(post)

        # Serialize Python list to JSON encoded string
        serialized_posts = json.dumps(posts)

    return serialized_posts


def retrieve_post(pk):
    """Run query to get a single post and return serialized result"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Expand user_id to get author name AND expand category_id to get category name
        db_cursor.execute(
            """
            SELECT
                p.id post_id,
                p.title,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved,
                u.first_name, 
                u.last_name,
                c.label 
            FROM Posts p
            JOIN Users u ON u.id = p.user_id
            JOIN Categories c ON c.id = p.category_id
            WHERE p.id = ?
            """,
            (pk,),
        )
        query_results = db_cursor.fetchone()
        print(dict(query_results))

        # Expanded single post
        row = query_results
        post = {
            "id": row["post_id"],
            "user": {"first_name": row["first_name"], "last_name": row["last_name"]},
            "category": {"label": row["label"]},
            "title": row["title"],
            "publication_date": row["publication_date"],
            "image_url": row["image_url"],
            "content": row["content"],
            "approved": row["approved"],
        }
        serialized_post = json.dumps(post)

    return serialized_post
