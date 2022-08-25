"""add transaction table

Revision ID: 5e2793b346f3
Revises: c6d0eea48485
Create Date: 2022-08-14 14:15:33.507529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5e2793b346f3"
down_revision = "c6d0eea48485"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("quote_id", sa.String(length=255), nullable=False),
        sa.Column("recipient_id", sa.String(length=255), nullable=False),
        sa.Column("transfer_di", sa.String(length=255), nullable=False),
        sa.Column("target_account_id", sa.String(length=100), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("employee_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["employees.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transactions")
    # ### end Alembic commands ###
