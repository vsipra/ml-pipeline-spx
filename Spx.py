from pydantic import BaseModel
class Spx(BaseModel):
    dp: float 
    dy: float 
    ep: float 
    de: float
    svar: float
    bm: float
    ntis: float
    tbl: float
    lty: float
    ltr: float
    tms: float
    dfy: float
    dfr: float
    infl: float
