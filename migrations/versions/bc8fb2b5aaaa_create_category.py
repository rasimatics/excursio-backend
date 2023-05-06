"""Create category

Revision ID: bc8fb2b5aaaa
Revises: cf3388347129
Create Date: 2023-05-06 09:44:36.431462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc8fb2b5aaaa'
down_revision = 'cf3388347129'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('icon', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###