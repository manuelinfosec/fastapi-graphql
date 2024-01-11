"""MigrationForUserTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForUserTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
