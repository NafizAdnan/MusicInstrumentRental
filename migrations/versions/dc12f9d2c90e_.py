"""empty message

Revision ID: dc12f9d2c90e
Revises: de50cf51e0a5
Create Date: 2022-12-21 15:11:07.304108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc12f9d2c90e'
down_revision = 'de50cf51e0a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint('payment_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'instrument', ['product'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('payment_ibfk_1', 'cart', ['product'], ['product'])

    # ### end Alembic commands ###