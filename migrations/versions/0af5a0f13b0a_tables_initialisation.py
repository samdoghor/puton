"""tables initialisation

Revision ID: 0af5a0f13b0a
Revises: 
Create Date: 2024-03-24 21:34:53.349697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af5a0f13b0a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seasons',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('season', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seasons')
    # ### end Alembic commands ###