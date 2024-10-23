"""initial

Revision ID: 276efb3740e0
Revises: 00d50bc9b2de
Create Date: 2024-10-23 21:00:18.875672

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '276efb3740e0'
down_revision = '00d50bc9b2de'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
