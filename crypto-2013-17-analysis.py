
# coding: utf-8

# In[60]:

#Price chart 
#Render plot in line
get_ipython().magic('matplotlib inline')

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.api as sm
from sklearn import linear_model


pd.set_option('display.mpl_style', 'default') # makes graphs pretty

#pd.matplotlib.pyplot.mpl.use


#plt.xscale('ln')

#reading csv parsing dates indexinf
read= pd.read_csv(r'C:\Users\Abdullah Yusuf\Desktop\crypto-markets.csv', encoding='latin1',                   parse_dates=['date'], dayfirst=False, index_col='date')

stock= pd.read_csv(r'C:\Users\Abdullah Yusuf\Desktop\all_stocks_5yr.csv', encoding='latin1',                   parse_dates=['date'], dayfirst=False)

stockcry= pd.read_csv(r'C:\Users\Abdullah Yusuf\Desktop\crypto-markets.csv', encoding='latin1',                   parse_dates=['date'], dayfirst=False,)




# In[52]:

#selecting and plotting crypto prices
plt.rcParams['figure.figsize']=(15,30)

btc = read[read['symbol'].str.match('BTC')].loc['2016-01-01':'2018-01-01']
plt.subplot(6,1,1)
plt.title('Bitcoin closing prices')
btc['close'].plot()

eth=read[read['symbol'].str.match('ETH')].loc['2016-01-01':'2018-01-01']
plt.subplot(6,1,2)
plt.title('Ether closing prices')
eth['close'].plot()

xrp=read[read['symbol'].str.match('XRP')].loc['2016-01-01':'2018-01-01']
plt.subplot(6,1,3)
plt.title('Ripple closing prices')
xrp['close'].plot()

poet=read[read['symbol'].str.match('POE')].loc['2016-01-01':'2018-01-01']
plt.subplot(6,1,4)
plt.title('Po.et closing prices')
poet['close'].plot()

tron=read[read['symbol'].str.match('TRX')].loc['2016-01-01':'2018-01-01']
plt.subplot(6,1,5)
plt.title('Tron closing prices')
tron['close'].plot()

mon=read[read['symbol'].str.match('XMR')].loc['2016-01-01':'2018-01-01']
plt.subplot(6,1,6)
plt.title('Monero closing prices')
mon['close'].plot()

print(btc.iloc[:3])
print(eth.iloc[:3])


# In[67]:

#bitcoin delta function 

plt.rcParams['figure.figsize']=(15,5)
btc_delta = read[read['symbol'].str.match('BTC')].loc['2013-01-01':'2018-01-01']

#creates delta column
btc_delta['dP'] = (btc_delta['high']/btc_delta['low'])#/(btc_delta['close']/btc_delta['open']) 
print(btc_delta.iloc[:3])
btc_delta['dP'].plot()

cry_2013= btc_delta.loc['2013-02-08' : '2014-01-01']
cry_2014= btc_delta.loc['2014-01-01' : '2015-01-01']
cry_2015= btc_delta.loc['2015-01-01' : '2016-01-01']
cry_2016= btc_delta.loc['2016-01-01' : '2017-01-01']
cry_2017= btc_delta.loc['2017-01-01' : '2018-01-01']


# In[68]:

#stock delta func.
stock['delta']=stock['high']/stock['low']
print(stock.iloc[:3])


smry=stock.groupby('date').mean()
print(smry.iloc[:3])

stock.set_index('date')
stock['delta'].plot()

stk_2013= smry.loc['2013-02-08' : '2014-01-01']
stk_2014= smry.loc['2014-01-01' : '2015-01-01']
stk_2015= smry.loc['2015-01-01' : '2016-01-01']
stk_2016= smry.loc['2016-01-01' : '2017-01-01']
stk_2017= smry.loc['2017-01-01' : '2018-01-01']


# In[69]:

#agg crypto delta func.
stockcry['delta']=stockcry['high']/stockcry['low']
#print(stock.iloc[:3])


smrya=stockcry.groupby('date').mean()
print(smrya.iloc[:3])

#stockcry.set_index('date')
stockcry['delta'].plot()

crya_2013= smrya.loc['2013-02-08' : '2014-01-01']
crya_2014= smrya.loc['2014-01-01' : '2015-01-01']
crya_2015= smrya.loc['2015-01-01' : '2016-01-01']
crya_2016= smrya.loc['2016-01-01' : '2017-01-01']
crya_2017= smrya.loc['2017-01-01' : '2018-01-01']


# In[32]:

X = btc["close"].iloc[:600]/btc["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #].loc['2016-01-01':'2017-01-01']
y = eth["close"].iloc[:600]/eth["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #.loc['2016-01-01':'2017-01-01']

X=list(X)
y=list(y)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()

#lm = linear_model.LinearRegression()
#model = lm.fit(X,y)

#predictions = lm.predict(X)
#print(predictions)[0:5]

#lm.score(X,y)


# In[79]:

X = stk_2013["close"].iloc[:225] #/btc["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #].loc['2016-01-01':'2017-01-01']
y = cry_2013["close"].iloc[:225] #/eth["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #.loc['2016-01-01':'2017-01-01']

X=list(X)
y=list(y)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()


# In[84]:

X = stk_2014["close"].iloc[:250] #/btc["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #].loc['2016-01-01':'2017-01-01']
y = cry_2014["close"].iloc[:250] #/eth["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #.loc['2016-01-01':'2017-01-01']

X=list(X)
y=list(y)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()


# In[85]:

X = stk_2015["close"].iloc[:250] #/btc["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #].loc['2016-01-01':'2017-01-01']
y = cry_2015["close"].iloc[:250] #/eth["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #.loc['2016-01-01':'2017-01-01']

X=list(X)
y=list(y)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()


# In[86]:

X = stk_2016["close"].iloc[:250] #/btc["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #].loc['2016-01-01':'2017-01-01']
y = cry_2016["close"].iloc[:250] #/eth["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #.loc['2016-01-01':'2017-01-01']

X=list(X)
y=list(y)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()


# In[87]:

X = stk_2017["close"].iloc[:250] #/btc["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #].loc['2016-01-01':'2017-01-01']
y = cry_2017["close"].iloc[:250] #/eth["open"].iloc[:600] #.loc['2017-01-01':'2017-02-01'] #.loc['2016-01-01':'2017-01-01']

X=list(X)
y=list(y)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()


# In[ ]:



