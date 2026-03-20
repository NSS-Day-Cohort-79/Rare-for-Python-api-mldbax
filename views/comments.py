# get_comments_by_postId(postId)
# get_comment_by_id(pk)
# create_comment(comment_data)
# delete_comment(pk)
# update_comment(pk, comment_data)

import sqlite3
import json


def get_comments_by_post_id(post_id):
    """Run query to get all comments by post id"""
    # open a connection with the database
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""""")
