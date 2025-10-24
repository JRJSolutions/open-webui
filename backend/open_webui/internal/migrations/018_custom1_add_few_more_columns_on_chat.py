"""Peewee migrations -- 018_custom1_add_few_more_columns_on_chat.py.

Some examples (model - class or model name):
    > Model = migrator.orm['table_name']           # Return model in current state by name
    > Model = migrator.ModelClass                  # Return model in current state by class
    > migrator.sql(sql)                            # Run custom SQL
    > migrator.run(func, *args, **kwargs)          # Run python function with the given args
    > migrator.create_model(Model)                 # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)   # Remove a model
    > migrator.add_fields(model, **fields)         # Add fields to a model
    > migrator.change_fields(model, **fields)      # Change fields
    > migrator.remove_fields(model, *field_names)  # Remove fields
    > migrator.rename_field(model, old, new)       # Rename a field
    > migrator.rename_table(model, new_name)       # Rename a table
    > migrator.add_index(model, *col_names, unique=False)  # Add an index
    > migrator.drop_index(model, *col_names)       # Drop an index
"""

from contextlib import suppress
import peewee as pw
from peewee_migrate import Migrator

# Use Postgres JSON if available; otherwise fall back to TEXT
with suppress(ImportError):
    import playhouse.postgres_ext as pw_pext


def migrate(migrator: Migrator, database: pw.Database, *, fake: bool = False):
    """Write your forward migrations here."""
    JSONField = (
        getattr(globals().get("pw_pext", None), "JSONField", None) or pw.TextField
    )

    # Add columns to "chat"
    migrator.add_fields(
        "chat",
        customUserId=pw.CharField(null=True),        # VARCHAR / TEXT
        pipe_meta=JSONField(null=True),              # JSON/TEXT (PG/SQLite)
        custom_metadata1=JSONField(null=True),
        custom_metadata2=JSONField(null=True),
        custom_metadata3=JSONField(null=True),
        custom_metadata4=JSONField(null=True),
    )

    # # Add indexes (non-unique)
    # # Peewee migrator will create sensible names for the indexes.
    # migrator.add_index("chat", "user_id")
    # migrator.add_index("chat", "customUserId")


def rollback(migrator: Migrator, database: pw.Database, *, fake: bool = False):
    """Write your rollback migrations here."""
    # Drop indexes first
    # with suppress(Exception):
    #     migrator.drop_index("chat", "customUserId")
    # with suppress(Exception):
    #     migrator.drop_index("chat", "user_id")

    # Remove columns
    migrator.remove_fields(
        "chat",
        "custom_metadata4",
        "custom_metadata3",
        "custom_metadata2",
        "custom_metadata1",
        "pipe_meta",
        "customUserId",
    )
