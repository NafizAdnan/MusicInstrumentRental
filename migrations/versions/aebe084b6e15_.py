"""empty message

Revision ID: aebe084b6e15
Revises: c459406224bd
Create Date: 2022-12-20 19:38:49.431833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aebe084b6e15'
down_revision = 'c459406224bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'coupon', ['voucher'], ['code'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###