import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from os import path
import csv,sqlite3,pandas


ch = 'AV2ZAVZMSXGEN20H'
#teste alteracao

pd.set_option('display.max_rows',None)
tms = TimeSeries(key=ch, output_format='pandas')
data,meta_data = tms.get_intraday(symbol='B3SA3.SAO', interval= '60min', outputsize = 'compact')
datab,meta_datab = tms.get_intraday(symbol='PETR4.SAO', interval= '60min', outputsize = 'compact')


df = pd.DataFrame(data)

print(df)

# antes de rodar não se esqueça de alterar o caminho para uma pasta desejada 

df.to_csv('alpha.csv',header=3)

#cria conexao banco - ok

#sql_conn = sqlite3.connect("\\Users\\vaio\\Desktop\\pandas\\beta.db")
sql_conn = sqlite3.connect("beta.db")

#salva no csv - ok
df = pd.read_csv("alpha.csv", delimiter = ',')

#insere no banco - ok
df.to_sql(name = 'convest', con = sql_conn, if_exists = 'append', index = 1)

sql_conn.commit()
sql_conn.close()
