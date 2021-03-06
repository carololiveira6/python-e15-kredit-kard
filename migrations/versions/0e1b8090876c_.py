"""empty message

Revision ID: 0e1b8090876c
Revises: 
Create Date: 2021-07-16 17:15:44.655054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e1b8090876c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('credit_cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expire_date', sa.String(length=30), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('security_code', sa.String(length=3), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('credit_cards')
    op.drop_table('users')
    # ### end Alembic commands ###
