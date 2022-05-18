"""empty message

Revision ID: de7342f0a670
Revises: e785ead267ee
Create Date: 2022-05-17 23:05:35.334499

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geometry


# revision identifiers, used by Alembic.
revision = 'de7342f0a670'
down_revision = 'e785ead267ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('spatial_ref_sys')
    op.alter_column('indian_airports', 'geo',
               existing_type=Geometry(geometry_type='POINT', from_text='ST_GeomFromEWKT', name='geometry'),
               type_=Geometry(geometry_type='POINT', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('indian_airports', 'geo',
               existing_type=Geometry(geometry_type='POINT', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'),
               type_=Geometry(geometry_type='POINT', from_text='ST_GeomFromEWKT', name='geometry'),
               existing_nullable=True)
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    # ### end Alembic commands ###
