"""empty message

Revision ID: 5fa9b83e7144
Revises: 46bb2e64cf81
Create Date: 2022-12-21 07:33:34.703298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa9b83e7144'
down_revision = '46bb2e64cf81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint('payment_ibfk_1', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.create_foreign_key('payment_ibfk_1', 'cart', ['product'], ['product'])

    # ### end Alembic commands ###