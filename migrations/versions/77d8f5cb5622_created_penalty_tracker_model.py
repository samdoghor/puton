"""created penalty tracker model

Revision ID: 77d8f5cb5622
Revises: efc75744f1b6
Create Date: 2024-05-06 08:25:22.491370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77d8f5cb5622'
down_revision = 'efc75744f1b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_penalties',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('is_penalty_shootout', sa.Boolean(), nullable=False),
    sa.Column('is_goal', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('game_event_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['game_event_id'], ['game_events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_penalties')
    # ### end Alembic commands ###
