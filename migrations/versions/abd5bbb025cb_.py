"""empty message

Revision ID: abd5bbb025cb
Revises: caa07ffab522
Create Date: 2022-12-20 18:48:33.525449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd5bbb025cb'
down_revision = 'caa07ffab522'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_constraint('order_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'payment', ['product'], ['product'])

    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('voucher', sa.String(length=15), nullable=True))
        batch_op.create_foreign_key(None, 'coupon', ['voucher'], ['code'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('voucher')

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('order_ibfk_1', 'instrument', ['product'], ['id'])

    # ### end Alembic commands ###