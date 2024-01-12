"""MigrationForCommentTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForCommentTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("comments") as table:
            table.increments("id")
            table.integer(
                "user_id"
            ).unsigned().nullable()  # ID of the user that made the comment
            table.foreign("user_id").references("id").on(
                "users"
            )  # Foreignkey the `user_id` column to ID on users
            table.integer(
                "post_id"
            ).unsigned().nullable()  # ID of the post with the comment
            table.text("body")  # Comment's content

            table.timestamps()  # `updated_at` and `created_at`

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("comments")
