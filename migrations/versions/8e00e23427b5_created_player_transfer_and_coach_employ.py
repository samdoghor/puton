"""created player transfer and coach employ

Revision ID: 8e00e23427b5
Revises: aed5af862616
Create Date: 2024-04-13 22:34:46.381072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e00e23427b5'
down_revision = 'aed5af862616'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.drop_constraint('coaches_team_id_fkey', type_='foreignkey')
        batch_op.drop_column('team_id')

    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.drop_constraint('teams_league_id_fkey', type_='foreignkey')
        batch_op.drop_column('league_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('league_id', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('teams_league_id_fkey', 'leagues', ['league_id'], ['id'])

    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.add_column(sa.Column('team_id', sa.UUID(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('coaches_team_id_fkey', 'teams', ['team_id'], ['id'])

    # ### end Alembic commands ###
