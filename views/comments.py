# get_comments_by_postId(postId) - view
# get_comment_by_id(pk) - edit
# create_comment(comment_data) - create
# delete_comment(pk) - delete
# update_comment(pk, comment_data) - edit


import sqlite3
import json


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
                u.username 
            FROM Comments c 
            JOIN Users u 
            ON u.id = c.author_id
            WHERE c.post_id = ?
            ORDER BY c.created_on DESC
            """,
            (post_id,),
        )
        query_results = db_cursor.fetchall()
        comments = []
        for row in query_results:
            user = {"author_id": row["author_id"], "username": row["username"]}
            comment = {
                "id": row["id"],
                "post_id": row["post_id"],
                "subject": row["subject"],
                "content": row["content"],
                "created_on": row["created_on"],
                "author": user,
            }
            comments.append(comment)

        serialized_comments = json.dumps(comments)
    return serialized_comments
