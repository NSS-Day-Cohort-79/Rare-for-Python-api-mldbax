"""view for holding post tags functions"""

import sqlite3
import json


def get_post_tags_by_post_id(post_id):
    """Gets all post tags entries for given post id

    Args:
        post_id (int): int of the post id to search for

    Returns:
        list of tags for the searched post id
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            SELECT
                pt.id,
                pt.post_id,
                pt.tag_id,
                t.label
            FROM PostTags pt
            JOIN Tags t on t.id = pt.tag_id
            WHERE post_id = ?
            """,
            (post_id,),
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        post_tags = []
        for row in query_results:
            post_tags.append(
                {
                    "id": row["id"],
                    "postId": row["post_id"],
                    "tagId": row["tag_id"],
                    "tag": {"id": row["tag_id"], "label": row["label"]},
                }
            )

    return post_tags


def add_post_tag(new_post_tag):
    """Creates a new entry for given post_tag

    Args:
        new_post_tag (dictionary): dictionary containing information for new post tag

    Returns:
        id of created post_tag
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO PostTags VALUES (null, ?, ?)
            """,
            (new_post_tag["postId"], new_post_tag["tagId"]),
        )

        id = db_cursor.lastrowid

        return json.dumps({"id": id})
