from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Share properties
class Stock(BaseModel):
    company: Optional[str] = None
    ticker: Optional[str] = None
    sector_id: Optional[int] = None
    industry_id: Optional[int] = None
    country_id: Optional[int] = None
    market_cap: Optional[float] = None
    pe_ratio: Optional[float] = None
    fwd_pe_ratio: Optional[float] = None
    price: Optional[float] = None
    volume: Optional[float] = None
    peg: Optional[float] = None
    ps_ratio: Optional[float] = None
    pb_ratio: Optional[float] = None
    pc_ratio: Optional[float] = None
    p_to_fcf_ratio: Optional[float] = None
    eps_this_year: Optional[float] = None
    eps_next_year: Optional[float] = None
    eps_past_5_year: Optional[float] = None
    eps_next_5_year: Optional[float] = None
    sales_past_5_year: Optional[float] = None
    divident: Optional[float] = None
    roa: Optional[float] = None
    roe: Optional[float] = None
    roi: Optional[float] = None
    curr_r: Optional[float] = None
    quick_r: Optional[float] = None
    debt_to_equity_ratio: Optional[float] = None
    gross_margin: Optional[float] = None
    operation_margin: Optional[float] = None
    profit_margin: Optional[float] = None
    short_ratio: Optional[float] = None
    outstanding: Optional[float] = None
    insider_own: Optional[float] = None
    inst_own: Optional[float] = None
    perf_week: Optional[float] = None
    perf_month: Optional[float] = None
    perf_qurter: Optional[float] = None
    perf_half_year: Optional[float] = None
    perf_year: Optional[float] = None
    perf_year_to_date: Optional[float] = None
    beta: Optional[float] = None
    sma20: Optional[float] = None
    sma50: Optional[float] = None
    sma200: Optional[float] = None
    rsi: Optional[float] = None
    sector: Optional[dict] = None
    industry: Optional[dict] = None
    country: Optional[dict] = None
