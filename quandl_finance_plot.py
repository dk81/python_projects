# Quandl Plots In Python

# Quandl.api_key("api_key_here")
# Ref: https://www.quandl.com/data/ZILLOW/C3821_ZHVITT-Zillow-Home-Value-Index-City-Zillow-Home-Value-Index-Top-Tier-Clarkson-NY
# https://pythonprogramming.net/using-quandl-data/
# https://www.quandl.com/data/PERTH/SLVR_USD_M-Silver-Spot-Prices-USD-Monthly
# Quick Start Guide: https://blog.quandl.com/getting-started-with-the-quandl-api

import quandl as Quandl
import matplotlib.pyplot as plt
import pandas as pd

auth_token = 'api_key_here' 

# Example One:

zillow_ny = Quandl.get("ZILLOW/C3821_ZHVITT", authtoken = auth_token)

print(zillow_ny) # Preview some rows

plt.plot(zillow_ny['Value'])

plt.title(''' Zillow\'s Home Index Of Home Prices In Clarkson, NY \n''')

plt.xlabel('\n Year')
plt.ylabel('Home Value \n')
plt.show()

# Example Two:
    
perth_silver = Quandl.get("PERTH/SLVR_USD_M", authtoken= auth_token)

# Convert to pandas dataframe:
    
silver_df = pd.DataFrame(perth_silver)

print(silver_df.head(6))
print(silver_df.tail(6))

# Bid is a price a buyer is willing to pay for:
# Ask is the price a seller is willing to accept (offer price).


plt.subplot(2, 1, 1)
plt.plot(silver_df.index, silver_df['Bid Average'])

plt.title(''' Perth Mint Monthly Prices For Silver (USD) \n''')

plt.xticks(silver_df.index[0::75],[])
plt.xlabel('\n Year')
plt.ylabel('Avg. Bid Price  \n')

plt.subplot(2, 1, 2)
plt.plot(silver_df.index, silver_df['Ask Average'])


plt.xlabel('\n Year')
plt.ylabel('Avg. Ask Price \n')

plt.show()

