# python-test
a stock exchange project in python
from pandas_datareader import data

import matplotlib.pyplot as plt
import pandas as pd
tickers = ['INFY' , 'TCS']
 from datetime import date
start = date(2015,1,1)
end = date(2015,31,12)
panel_data = data.DataReader(tickers, 'yahoo', start, end)
close = panel_data['Close']
all_weekdays = pd.date_range(start=start, end=end, freq='B')
close = close.reindex(all_weekdays)
close = close.fillna(method='ffill').
close.head(10).
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
%matplotlib inline
 my_year_month_fmt = mdates.DateFormatter('%m/%y')

data =panel_data

data.head()
 short_rolling = data.rolling(window=96).mean()
short_rolling.head(20)

