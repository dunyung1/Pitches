"""add columns in pitch table

Revision ID: fe8faaf22e15
Revises: 5d3751edf69a
Create Date: 2019-02-12 18:31:29.759638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe8faaf22e15'
down_revision = '5d3751edf69a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mycategory', sa.String(), nullable=True),
    sa.Column('mypitch', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###