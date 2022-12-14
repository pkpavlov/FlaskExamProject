"""initial migration

Revision ID: e2c877a4e410
Revises: 
Create Date: 2022-07-23 13:43:38.699905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e2c877a4e410"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "StoreUser",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=20), nullable=False),
        sa.Column("last_name", sa.String(length=20), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=60), nullable=False),
        sa.Column("phone", sa.String(length=14), nullable=False),
        sa.Column(
            "role",
            sa.Enum(
                "employee",
                "store_user",
                "admin",
                "accountant",
                "warehouseman",
                name="userrole",
            ),
            nullable=False,
        ),
        sa.Column("nickname", sa.String(length=20), nullable=False),
        sa.Column("address", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "employees",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=20), nullable=False),
        sa.Column("last_name", sa.String(length=20), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=60), nullable=False),
        sa.Column("phone", sa.String(length=14), nullable=False),
        sa.Column(
            "role",
            sa.Enum(
                "employee",
                "store_user",
                "admin",
                "accountant",
                "warehouseman",
                name="userrole",
            ),
            nullable=False,
        ),
        sa.Column("iban", sa.String(length=50), nullable=False),
        sa.Column("salary", sa.Float(), nullable=False),
        sa.Column("vacation", sa.Integer(), nullable=False),
        sa.Column(
            "create_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "store",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_name", sa.String(length=100), nullable=False),
        sa.Column("serial_number", sa.String(length=30), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("delivery_price", sa.Integer(), nullable=False),
        sa.Column("sell_price", sa.Integer(), nullable=False),
        sa.Column("dealer_price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "task",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "finished_on",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("used_parts", sa.String(length=255), nullable=False),
        sa.Column("employ_comments", sa.String(length=255), nullable=False),
        sa.Column(
            "state",
            sa.Enum("in_progress", "done", "cancelled", "on_hold", name="taskstate"),
            nullable=False,
        ),
        sa.Column("employee_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["employees.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task")
    op.drop_table("store")
    op.drop_table("employees")
    op.drop_table("StoreUser")
    # ### end Alembic commands ###
