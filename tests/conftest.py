import random

import pytest
from faker import Faker
from masoniteorm.migrations import Migration

from models.Comment import Comment
from models.Post import Post
from models.User import User

fake = Faker()


@pytest.fixture(autouse=True)
def setup_database():
    config_path = "config/test_config.py"

    migrator = Migration(config_path=config_path)
    migrator.create_table_if_not_exists()

    migrator.refresh()


@pytest.fixture
def user():
    user = User()
    user.name = fake.name()
    user.address = fake.address()
    user.phone_number = 123456789
    user.sex = random.choice(["male", "female"])
    user.email = fake.email()

    user.save()
    return user


@pytest.fixture
def post(user):
    post = Post()
    post.title = fake.word().capitalize()
    post.body = fake.text()
    post.user_id = user.id
    post.save()

    user.attach("posts", post)
    return post


@pytest.fixture
def comment(user, post):
    comment = Comment()
    comment.body = fake.sentence()
    comment.user_id = user.id
    comment.post_id = post.id

    comment.save()

    user.attach("comments", comment)
    post.attach("comments", comment)

    return comment
