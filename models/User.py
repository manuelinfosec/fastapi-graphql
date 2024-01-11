""" User Model """

# masonite-orm model User --directory models
# masonite-orm migration migration_for_user_table --create users

from masoniteorm.models import Model


class User(Model):
    """User Model"""

    pass
