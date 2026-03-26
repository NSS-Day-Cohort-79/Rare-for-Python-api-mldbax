import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import login_user, create_user
from views import (
    get_categories,
    retrieve_category,
    create_category,
    update_category,
    delete_category,
)
from views import get_posts, retrieve_post, get_approved_posts, create_post, update_post

from views import get_tags, retrieve_tag, create_tag, update_tag, delete_tag

from views import retrieve_comments, create_comment

from views import add_post_tag


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for shipping ships"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "categories":
            if url["pk"] != 0:
                response_body = retrieve_category(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = get_categories()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "tags":
            if url["pk"] != 0:
                response_body = retrieve_tag(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            else:
                response_body = get_tags()
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "posts":
            if url["pk"] != 0:
                response_body = retrieve_post(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = get_posts()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "approved-posts":

            response_body = get_approved_posts()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "post-comments":
            if url["pk"] != 0:
                response_body = retrieve_comments(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_PUT(self):
        """Handle PUT requests from a client"""

        # Parse the URL and get the primary key
        url = self.parse_url(self.path)
        pk = url["pk"]

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "categories":
            if pk != 0:
                successfully_updated = update_category(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
        elif url["requested_resource"] == "tags":
            if pk != 0:
                successfully_updated = update_tag(pk, request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
        # CD - Added endpoint for updating posts
        elif url["requested_resource"] == "posts":
            if pk != 0:
                successfully_updated = update_post(request_body)
                if successfully_updated:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )

        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )

    def do_DELETE(self):
        """Handle DELETE requests from a client"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "categories":
            if pk != 0:
                successfully_deleted = delete_category(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )
        elif url["requested_resource"] == "tags":
            if pk != 0:
                successfully_deleted = delete_tag(pk)
                if successfully_deleted:
                    return self.response(
                        "", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value
                    )
                return self.response(
                    "Requested resource not found",
                    status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
                )
        else:
            return self.response(
                "Not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def do_POST(self):
        """Handle POST requests from a client"""
        # Parse the URL
        url = self.parse_url(self.path)

        # Get the request body JSON for the new data
        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "categories":
            new_category_id = create_category(request_body)
            if new_category_id:
                return self.response(
                    "",
                    status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                )
        elif url["requested_resource"] == "tags":
            new_tag_id = create_tag(request_body)
            if new_tag_id:
                return self.response(
                    "",
                    status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
                )
        elif url["requested_resource"] == "register":
            new_token = create_user(request_body)
            if new_token:
                return self.response(new_token, status.HTTP_201_SUCCESS_CREATED.value)

        elif url["requested_resource"] == "login":
            set_token = login_user(request_body)
            if set_token:
                return self.response(set_token, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "posts":
            new_id = create_post(request_body)
            if new_id:
                return self.response(new_id, status.HTTP_201_SUCCESS_CREATED.value)

        elif url["requested_resource"] == "post-tags":
            new_id = add_post_tag(request_body)
            if new_id:
                return self.response(new_id, status.HTTP_201_SUCCESS_CREATED.value)

        elif url["requested_resource"] == "comments":
            new_comment_id = create_comment(request_body)
            if new_comment_id:
                return self.response(
                    new_comment_id,
                    status.HTTP_201_SUCCESS_CREATED.value,
                )

        else:
            return self.response(
                "oops", status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value
            )


# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
