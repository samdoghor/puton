"""fix: update datatype for season start and end date

Revision ID: 6455f4b8c5c5
Revises: 6727c7277cbc
Create Date: 2024-03-30 17:01:54.071862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6455f4b8c5c5'
down_revision = '6727c7277cbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seasons', schema=None) as batch_op:
        batch_op.alter_column('start_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
        batch_op.alter_column('end_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
        batch_op.drop_column('year')
        batch_op.drop_column('season')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seasons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('season', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.alter_column('end_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
        batch_op.alter_column('start_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)

    # ### end Alembic commands ###
