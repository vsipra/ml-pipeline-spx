# -*- coding: utf-8 -*-
"""
@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
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