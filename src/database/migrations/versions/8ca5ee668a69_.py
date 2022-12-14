"""empty message

Revision ID: 8ca5ee668a69
Revises: 
Create Date: 2022-11-22 09:41:36.051141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca5ee668a69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('num_code', sa.Integer(), nullable=True),
    sa.Column('char_code', sa.String(length=15), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('nominal', sa.Integer(), nullable=True),
    sa.Column('value', sa.Numeric(precision=10, scale=4), nullable=True),
    sa.Column('date_req', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('code', 'date_req')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currencies')
    # ### end Alembic commands ###
