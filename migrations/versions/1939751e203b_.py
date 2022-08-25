"""empty message

Revision ID: 1939751e203b
Revises: 665c3735b4eb
Create Date: 2022-08-06 15:40:53.891056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1939751e203b"
down_revision = "665c3735b4eb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "task",
        sa.Column(
            "create_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
    )
    op.drop_column("task", "created_on")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "task",
        sa.Column(
            "created_on",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("task", "create_on")
    # ### end Alembic commands ###
