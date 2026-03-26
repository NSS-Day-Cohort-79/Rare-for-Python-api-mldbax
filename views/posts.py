"""view for holding posts functions"""

import sqlite3
import json
from datetime import datetime


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
            user = {"firstName": row["first_name"], "lastName": row["last_name"]}
            category = {"label": row["label"]}
            post = {
                "id": row["post_id"],
                "user": user,
                "category": category,
                "title": row["title"],
                "publicationDate": row["publication_date"],
                "imageUrl": row["image_url"],
                "content": row["content"],
                "approved": row["approved"],
            }
            posts.append(post)

        # Serialize Python list to JSON encoded string
        serialized_posts = json.dumps(posts)

    return serialized_posts


def get_user_posts(user_id):
    """Run query to get all posts by a specific user and return list of objects"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                p.id post_id,
                p.user_id,
                p.category_id,
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
            WHERE p.user_id = ?
            ORDER BY p.publication_date DESC
            """,
            (user_id,),
        )
        query_results = db_cursor.fetchall()

        posts = []
        for row in query_results:
            user = {"firstName": row["first_name"], "lastName": row["last_name"]}
            category = {"label": row["label"]}
            post = {
                "id": row["post_id"],
                "userId": row["user_id"],
                "user": user,
                "categoryId": row["category_id"],
                "category": category,
                "title": row["title"],
                "publicationDate": row["publication_date"],
                "imageUrl": row["image_url"],
                "content": row["content"],
                "approved": row["approved"],
            }
            posts.append(post)

        serialized_posts = json.dumps(posts)

    return serialized_posts


def get_approved_posts():
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
            WHERE p.approved = 1 AND p.publication_date <= datetime('now')
            ORDER BY p.publication_date DESC
            """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        approved_posts = []
        for row in query_results:
            user = {"firstName": row["first_name"], "lastName": row["last_name"]}
            category = {"label": row["label"]}
            post = {
                "id": row["post_id"],
                "user": user,
                "category": category,
                "title": row["title"],
                "publicationDate": row["publication_date"],
                "imageUrl": row["image_url"],
                "content": row["content"],
                "approved": row["approved"],
            }
            approved_posts.append(post)

        # Serialize Python list to JSON encoded string
        serialized_posts = json.dumps(approved_posts)

    return serialized_posts


def retrieve_post(pk):
    """Run query to get a single post and return serialized result"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Expand user_id to get author name AND expand category_id to get category name
        # CD - Added user_id and category_id to SELECT
        db_cursor.execute(
            """
            SELECT
                p.id post_id,
                p.user_id,
                p.category_id,
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
        # CD - Added category and userID, changed to camel case
        row = query_results
        post = {
            "id": row["post_id"],
            "userId": row["user_id"],
            "user": {"firstName": row["first_name"], "lastName": row["last_name"]},
            "categoryId": row["category_id"],
            "category": {"label": row["label"]},
            "title": row["title"],
            "publicationDate": row["publication_date"],
            "imageUrl": row["image_url"],
            "content": row["content"],
            "approved": row["approved"],
        }
        serialized_post = json.dumps(post)

    return serialized_post


def create_post(newPostObj):
    """Adds a post to the database

    Args:
        newPostObj (dictionary): The dictionary passed to the posts post request

    Returns:
        json string: Contains the id of the newly created post
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Posts (
              'user_id', 
              'category_id', 
              'title', 
              'publication_date', 
              'image_url', 
              'content', 
              'approved'
            )
            VALUES (
              ?, 
              ?, 
              ?,
              ?,
              ?,
              ?,
              ?
            );
            """,
            (
                newPostObj["userId"],
                newPostObj["categoryId"],
                newPostObj["title"],
                datetime.now(),
                newPostObj["imageUrl"],
                newPostObj["content"],
                1,
            ),
        )

        id = db_cursor.lastrowid

        return json.dumps({"id": id})


def update_post(post_obj):
    """Updates an existing post in the database

    Args:
        postObj (dictionary): The dictionary passed to the posts PUT request

    Returns:
        json string: Contains the id of the updated post
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Posts 
                SET
                    user_id = ?, 
                    category_id = ?, 
                    title = ?,
                    publication_date = ?, 
                    image_url = ?, 
                    content = ?, 
                    approved = ?
                WHERE id = ?            
            """,
            (
                post_obj["userId"],
                post_obj["categoryId"],
                post_obj["title"],
                post_obj["publicationDate"],
                post_obj["imageUrl"],
                post_obj["content"],
                post_obj["approved"],
                post_obj["id"],
            ),
        )

        id = db_cursor.lastrowid

        return json.dumps({"id": id})


def delete_post(post_id):
    """Delete a post from the database"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            DELETE FROM Posts
            WHERE id = ?
            """,
            (post_id),
        )

        return json.dumps({"message": "Post deleted successfully"})
