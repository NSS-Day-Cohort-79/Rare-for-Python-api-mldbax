# get_comments_by_postId(postId) - view
# get_comment_by_id(pk) - edit
# create_comment(comment_data) - create
# delete_comment(pk) - delete
# update_comment(pk, comment_data) - edit


import sqlite3
import json
from datetime import datetime


def retrieve_comments(post_id):
    """Run query to get all comments by post id"""
    # open a connection with the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
            SELECT 
                c.id,
                c.post_id,
                c.subject, 
                c.content, 
                c.created_on,
                c.author_id,
                p.title, 
                u.first_name,
                u.last_name
            FROM Comments c 
            JOIN Users u 
            ON u.id = c.author_id
            JOIN Posts p
            ON c.post_id = p.id
            WHERE c.post_id = ?
            ORDER BY c.created_on DESC
            """,
            (post_id,),
        )
        query_results = db_cursor.fetchall()
        comments = []
        for row in query_results:
            user = {
                "authorId": row["author_id"],
                "firstName": row["first_name"],
                "lastName": row["last_name"],
            }
            post = {"postId": row["post_id"], "title": row["title"]}
            comment = {
                "id": row["id"],
                "subject": row["subject"],
                "content": row["content"],
                "createdOn": row["created_on"],
                "post": post,
                "author": user,
            }
            comments.append(comment)

        serialized_comments = json.dumps(comments)
    return serialized_comments


def create_comment(comment_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
            INSERT INTO Comments (
            post_id, 
            author_id, 
            subject, 
            content, 
            created_on
            ) VALUES (
            ?,?,?,?,?
            )
            """,
            (
                comment_data["postId"],
                comment_data["authorId"],
                comment_data["subject"],
                comment_data["content"],
                datetime.now(),
            ),
        )
        new_comment_id = db_cursor.lastrowid
        return json.dumps(new_comment_id)


def update_comment(comment_id, comment_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
            UPDATE Comments
            SET 
            subject = ?,
            content = ?
            WHERE id = ?
            """,
            (comment_data["subject"], comment_data["content"], comment_id),
        )
        rows_affected = db_cursor.rowcount
    return True if rows_affected > 0 else False
