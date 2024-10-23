"""initial

Revision ID: 00d50bc9b2de
Revises: 9d09e1cb9b76
Create Date: 2024-10-23 20:18:43.811917

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '00d50bc9b2de'
down_revision = '9d09e1cb9b76'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
