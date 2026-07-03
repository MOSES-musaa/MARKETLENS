def price_vs_atm(current_price, atm_price):

    if current_price > atm_price:
        return "Bullish"

    elif current_price < atm_price:
        return "Bearish"

    else:
        return "Neutral"

    #returns the sentiment based on the average implied volatility of calls and puts. 

def iv_sentiment(avg_call_iv, avg_put_iv):

    if avg_put_iv > avg_call_iv:
        return "Fear is increasing."

    elif avg_call_iv > avg_put_iv:
        return "Bullish sentiment."

    else:
        return "Neutral volatility."

    
#returns the sentiment based on the call put ratio.

def call_put_ratio_sentiment(ratio):

    if ratio > 1.2:
        return "Bullish positioning"

    elif ratio < 0.8:
        return "Bearish positioning"

    else:
        return "Balanced positioning"

    #returns a summary of the market based on the trend, implied volatility, and call/put ratio.

def market_summary(
        trend,
        iv,
        ratio):

    print("\n======= MARKET SUMMARY =======")

    print(f"Trend: {trend}")
    print(f"Volatility: {iv}")
    print(f"Options Positioning: {ratio}")