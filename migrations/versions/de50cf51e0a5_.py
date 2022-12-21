"""empty message

Revision ID: de50cf51e0a5
Revises: 5fa9b83e7144
Create Date: 2022-12-21 08:03:04.917301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de50cf51e0a5'
down_revision = '5fa9b83e7144'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint('payment_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'cart', ['product'], ['product'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('payment_ibfk_2', 'cart', ['cart_id'], ['id'])

    # ### end Alembic commands ###
