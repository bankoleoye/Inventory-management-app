
import sys

from app.users.models import User


def create_dummy_users_command():
    """Create dummy users"""

    users_exist = User.query.count()
    if users_exist:
        sys.stdout.write("create_dummy_users(): Users already exist \n")
        return

    users = [
        {
            "firstname": "Sam",
            "lastname": "Ethan",
            "email": "samethan@example.com",
            "password": "1234ABDCEF",
        },
        {
            "firstname": "Sim",
            "lastname": "Emma",
            "email": "samiemma@example.com",
            "password": "InitialPassword",
        },
    ]

    # create dummy users
    for user in users:
        reg_user = User(**user)
        reg_user.save()

    sys.stdout.write("create_dummy_users(): Users created \n")
