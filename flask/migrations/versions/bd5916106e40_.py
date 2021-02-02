"""empty message

Revision ID: bd5916106e40
Revises: 
Create Date: 2021-02-02 00:38:47.857615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5916106e40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=28), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_token'), 'users', ['token'], unique=True)
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('water_goal', sa.Integer(), nullable=True),
    sa.Column('water_consumed', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_plant_assoc',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('plant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_id'], ['plants.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_plant_assoc')
    op.drop_table('logs')
    op.drop_index(op.f('ix_users_token'), table_name='users')
    op.drop_table('users')
    op.drop_table('plants')
    # ### end Alembic commands ###
