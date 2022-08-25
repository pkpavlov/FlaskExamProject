"""empty message

Revision ID: e1a77fc7ceb2
Revises: f7a584397b3e
Create Date: 2022-08-06 15:35:22.578415

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "e1a77fc7ceb2"
down_revision = "f7a584397b3e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "task",
        "created_on",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "task",
        "finished_on",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "task",
        "finished_on",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
        existing_server_default=sa.text("now()"),
    )
    op.alter_column(
        "task",
        "created_on",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
        existing_server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###
