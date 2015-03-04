import pandas as pd
import os
import sys
import Quandl as q

rootdir = os.path.dirname(os.path.realpath(sys.argv[0]))

def read_tickers():
    ticker_path = os.path.join(rootdir,'config','tickers.txt')
    df_tickers = pd.read_csv(ticker_path,delimiter='\t',index_col=0)
    return df_tickers
    
def read_indicators():
    ind_path = os.path.join(rootdir,'config','indicators.txt')
    df_inds = pd.read_csv(ind_path,delimiter='\t',index_col=0)
    return df_inds

def build_quandl_code(ticker,indicator,dimension):
    code = "SF1/%s_%s_%s" % (ticker,indicator,dimension)
    return code

def parse_code(code):
    

df_tickers = read_tickers()
df_inds = read_indicators()
code = build_quandl_code(df_tickers.index[0],df_inds.index[0],'ARQ')
data = q.get(code)
print("Blah")