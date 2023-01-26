from flask import abort, g


def user_post(token_info):  # noqa: E501
    """Add a user

     # noqa: E501


    :rtype: str
    """


def user_get(token_info):  # noqa: E501
    """Get Information of the logged in user

     # noqa: E501


    :rtype: str
    """
    return {
        "name": "John Doe",
        "email": "john.doe@indykite.com"
    }


def user_email_get(token_info):  # noqa: E501
    """Get the email of the logged in user

     # noqa: E501


    :rtype: str
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], ["email"])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    return digital_twin['digitalTwin'].properties[0].value


def user_parents_get(token_info):  # noqa: E501
    """Get the parents of the logged in user

     # noqa: E501
    """
    return [
        {
            "name": "John Doe",
            "email": "john.doe@indykite.com"
        },
        {
            "name": "Jane Doe",
            "email": "jane.doe@indykite.com"
        }
    ]
