"""empty message

Revision ID: e157ee29908d
Revises: 
Create Date: 2019-12-13 11:18:47.302000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e157ee29908d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('opbeans_flask_customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=1000), nullable=True),
    sa.Column('company_name', sa.String(length=1000), nullable=True),
    sa.Column('email', sa.String(length=1000), nullable=True),
    sa.Column('address', sa.String(length=1000), nullable=True),
    sa.Column('postal_code', sa.String(length=1000), nullable=True),
    sa.Column('city', sa.String(length=1000), nullable=True),
    sa.Column('country', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opbeans_flask_producttype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('opbeans_flask_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['opbeans_flask_customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opbeans_flask_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=1000), nullable=True),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('product_type_id', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('selling_price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_type_id'], ['opbeans_flask_producttype.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sku')
    )
    op.create_table('opbeans_flask_orderline',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['opbeans_flask_order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['opbeans_flask_product.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('opbeans_flask_orderline')
    op.drop_table('opbeans_flask_product')
    op.drop_table('opbeans_flask_order')
    op.drop_table('opbeans_flask_producttype')
    op.drop_table('opbeans_flask_customer')
    # ### end Alembic commands ###
