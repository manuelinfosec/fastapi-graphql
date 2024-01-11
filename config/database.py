"""Required by Masonite ORM for declaration of database configurations"""

from masoniteorm.connections import ConnectionResolver


DATABASES = {
    "default": "postgres",
    "postgres": {       # set as default
        "host": "127.0.0.1",
        "driver": "postgres",
        "database": "test",
        "user": "postgres",
        "password": "test",
        "port": 5432,
        "log_queries": True,
    },
    "mysql": {},
    # Other database configurations
}

DB = ConnectionResolver().set_connection_details(DATABASES)
