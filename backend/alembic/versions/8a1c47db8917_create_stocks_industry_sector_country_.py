"""Create stocks, industry, sector, country tables

Revision ID: 8a1c47db8917
Revises: f6df97eadc17
Create Date: 2022-02-19 23:42:46.215568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a1c47db8917'
down_revision = 'f6df97eadc17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_country_id'), 'country', ['id'], unique=False)
    op.create_index(op.f('ix_country_name'), 'country', ['name'], unique=False)
    op.create_table('sector',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sector_id'), 'sector', ['id'], unique=False)
    op.create_index(op.f('ix_sector_name'), 'sector', ['name'], unique=False)
    op.create_table('industry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sector_id', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.ForeignKeyConstraint(['sector_id'], ['sector.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_industry_id'), 'industry', ['id'], unique=False)
    op.create_index(op.f('ix_industry_name'), 'industry', ['name'], unique=False)
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('sector_id', sa.Integer(), nullable=True),
    sa.Column('industry_id', sa.Integer(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('market_cap', sa.Float(), nullable=True),
    sa.Column('pe_ratio', sa.Float(), nullable=True),
    sa.Column('fwd_pe_ratio', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('peg', sa.Float(), nullable=True),
    sa.Column('ps_ratio', sa.Float(), nullable=True),
    sa.Column('pb_ratio', sa.Float(), nullable=True),
    sa.Column('pc_ratio', sa.Float(), nullable=True),
    sa.Column('p_to_fcf_ratio', sa.Float(), nullable=True),
    sa.Column('eps_this_year', sa.Float(), nullable=True),
    sa.Column('eps_next_year', sa.Float(), nullable=True),
    sa.Column('eps_past_5_year', sa.Float(), nullable=True),
    sa.Column('eps_next_5_year', sa.Float(), nullable=True),
    sa.Column('sales_past_5_year', sa.Float(), nullable=True),
    sa.Column('divident', sa.Float(), nullable=True),
    sa.Column('roa', sa.Float(), nullable=True),
    sa.Column('roe', sa.Float(), nullable=True),
    sa.Column('roi', sa.Float(), nullable=True),
    sa.Column('curr_r', sa.Float(), nullable=True),
    sa.Column('quick_r', sa.Float(), nullable=True),
    sa.Column('debt_to_equity_ratio', sa.Float(), nullable=True),
    sa.Column('gross_margin', sa.Float(), nullable=True),
    sa.Column('operation_margin', sa.Float(), nullable=True),
    sa.Column('profit_margin', sa.Float(), nullable=True),
    sa.Column('short_ratio', sa.Float(), nullable=True),
    sa.Column('outstanding', sa.Float(), nullable=True),
    sa.Column('insider_own', sa.Float(), nullable=True),
    sa.Column('inst_own', sa.Float(), nullable=True),
    sa.Column('perf_week', sa.Float(), nullable=True),
    sa.Column('perf_month', sa.Float(), nullable=True),
    sa.Column('perf_qurter', sa.Float(), nullable=True),
    sa.Column('perf_half_year', sa.Float(), nullable=True),
    sa.Column('perf_year', sa.Float(), nullable=True),
    sa.Column('perf_year_to_date', sa.Float(), nullable=True),
    sa.Column('beta', sa.Float(), nullable=True),
    sa.Column('sma20', sa.Float(), nullable=True),
    sa.Column('sma50', sa.Float(), nullable=True),
    sa.Column('sma200', sa.Float(), nullable=True),
    sa.Column('rsi', sa.Float(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['industry_id'], ['industry.id'], ),
    sa.ForeignKeyConstraint(['sector_id'], ['sector.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_company'), 'stock', ['company'], unique=False)
    op.create_index(op.f('ix_stock_id'), 'stock', ['id'], unique=False)
    op.create_index(op.f('ix_stock_ticker'), 'stock', ['ticker'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stock_ticker'), table_name='stock')
    op.drop_index(op.f('ix_stock_id'), table_name='stock')
    op.drop_index(op.f('ix_stock_company'), table_name='stock')
    op.drop_table('stock')
    op.drop_index(op.f('ix_industry_name'), table_name='industry')
    op.drop_index(op.f('ix_industry_id'), table_name='industry')
    op.drop_table('industry')
    op.drop_index(op.f('ix_sector_name'), table_name='sector')
    op.drop_index(op.f('ix_sector_id'), table_name='sector')
    op.drop_table('sector')
    op.drop_index(op.f('ix_country_name'), table_name='country')
    op.drop_index(op.f('ix_country_id'), table_name='country')
    op.drop_table('country')
    # ### end Alembic commands ###