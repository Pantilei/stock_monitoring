from app.db.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Stock(Base):
    # Overview
    company = Column(
        String,
        index=True
    )
    ticker = Column(
        String,
        index=True,
        doc="Company Ticker"
    )
    sector_id = Column(
        Integer,
        ForeignKey("sector.id"),
        doc="Sector of company"
    )
    industry_id = Column(
        Integer,
        ForeignKey("industry.id"),
        doc="Industry"
    )
    country_id = Column(
        Integer,
        ForeignKey("country.id"),
        doc="Country"
    )
    market_cap = Column(
        Float,
        doc="Market capital"
    )
    # Valuation
    pe_ratio = Column(
        Float,
        doc="Price to Earning Ratio"
    )
    fwd_pe_ratio = Column(
        Float,
        doc="Forward Price to Earning Ratio"
    )
    price = Column(
        Float,
        doc="Current price of company"
    )
    volume = Column(
        Float,
        doc="Valume"
    )
    peg = Column(
        Float,
        doc="PEG ratio"
    )
    ps_ratio = Column(
        Float,
        doc="Price to Sale ratio"
    )
    pb_ratio = Column(
        Float,
        doc="Price to Book ratio"
    )
    pc_ratio = Column(
        Float,
        doc="""
            Put-Call ratio. According to some analysts, 
            a P/C ratio below 0.75 signals high levels of bullish sentiment, 
            so it's considered bearish from a contrarian viewpoint. Between 0.75 and 1.00 is neutral. 
            Above 1.00 indicates high levels of bearishness and is considered bullish by contrarians.
        """
    )
    p_to_fcf_ratio = Column(
        Float,
        doc="Price to free cash flow"
    )
    eps_this_year = Column(
        Float,
        doc="Earnings per share this year"
    )
    eps_next_year = Column(
        Float,
        doc="Earnings per share next year"
    )
    eps_past_5_year = Column(
        Float,
        doc="Earnings per share past 5 year"
    )
    eps_next_5_year = Column(
        Float,
        doc="Earnings per share next 5 year"
    )
    sales_past_5_year = Column(
        Float,
        doc="Sales past 5 year"
    )
    # Financials
    divident = Column(
        Float,
        doc="Divident persantage"
    )
    roa = Column(
        Float,
        doc="ROA - Return on Asset"
    )
    roe = Column(
        Float,
        doc="ROE - Return on Equity"
    )
    roi = Column(
        Float,
        doc="ROI - Return on Invesment"
    )
    curr_r = Column(
        Float,
        doc="Current Ratio"
    )
    quick_r = Column(
        Float,
        doc="Quick Ratio"
    )
    debt_to_equity_ratio = Column(
        Float,
        doc="Debt to Equity Ratio"
    )
    gross_margin = Column(
        Float,
        doc="Gross margin"
    )
    operation_margin = Column(
        Float,
        doc="Operation margin"
    )
    profit_margin = Column(
        Float,
        doc="Profit margin"
    )
    # Ovnership
    short_ratio = Column(
        Float,
        doc="Short ratio"
    )
    outstanding = Column(
        Float,
        doc="Number of shares outstanding(Sahres issued)"
    )
    insider_own = Column(
        Float,
        doc="Percentage of insider ownership"
    )
    inst_own = Column(
        Float,
        doc="Percentage of instance ownership"
    )
    # Performance
    perf_week = Column(
        Float,
        doc="Performance this week!"
    )
    perf_month = Column(
        Float,
        doc="Performance this month!"
    )
    perf_qurter = Column(
        Float,
        doc="Performance this quarter!"
    )
    perf_half_year = Column(
        Float,
        doc="Performance this year!"
    )
    perf_year = Column(
        Float,
        doc="Performance this year!"
    )
    perf_year_to_date = Column(
        Float,
        doc="Performance YTD(Year to date)"
    )
    # Technical
    beta = Column(
        Float, doc="Betta"
    )
    sma20 = Column(
        Float,
        doc="Simple moving average with 20 range"
    )
    sma50 = Column(
        Float,
        doc="Simple moving average with 50 range"
    )
    sma200 = Column(
        Float,
        doc="Simple moving average with 200 range"
    )
    rsi = Column(
        Float,
        doc="RSI"
    )

    sector = relationship(
        "Sector",
        back_populates="stocks",
        foreign_keys=sector_id
    )
    industry = relationship(
        "Industry",
        back_populates="stocks",
        foreign_keys=industry_id
    )
    country = relationship(
        "Country",
        back_populates="stocks",
        foreign_keys=country_id
    )
