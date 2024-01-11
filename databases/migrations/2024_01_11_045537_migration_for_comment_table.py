"""MigrationForCommentTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForCommentTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("comments") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("comments")
