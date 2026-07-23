from collectors.csv_loader import load_csv
from core.validator import validate_dataframe
from analytics.option_chain import (
    total_call_open_interest,
    total_put_open_interest,
    largest_call_wall,
    largest_put_wall,
    atm_strike,
)
from analytics.metrics import (
    call_put_ratio,
    average_call_iv,
    average_put_iv,
    highest_iv_strike,
)
from analytics.market_bias import (
    price_vs_atm,
    iv_sentiment,
    call_put_ratio_sentiment,
    market_summary,
)

from analytics.reports import generate_market_report
from analytics.presentation import format_report

SUPPORTED_GREEKS = ["delta", "gamma", "theta", "vega", "rho"]

def main():
    file_path = "Data/raw/sample_gold_options.csv"

    df = load_csv(file_path)
    print("\nColumns in DataFrame:")
    print(df.columns.tolist())

    validate_dataframe(df)

    print("\nPreview")
    print(df.head())

    print("\n========== OPTION CHAIN ANALYSIS ==========")

    print(f"Total Call OI: {total_call_open_interest(df)}")
    print(f"Total Put OI: {total_put_open_interest(df)}")

    print("\nLargest Call Wall")
    print(largest_call_wall(df))

    print("\nLargest Put Wall")
    print(largest_put_wall(df))

    print("\nATM Strike")
    print(atm_strike(df, 4092))
    trend = price_vs_atm(
    3988,
    4000
)

    iv = iv_sentiment(
    average_call_iv(df),
    average_put_iv(df)
)

    ratio = call_put_ratio_sentiment(
    call_put_ratio(df)
)

    market_summary(
    trend,
    iv,
    ratio
)

    print("\n========== MARKET METRICS ==========")

    print(f"Call / Put Ratio: {call_put_ratio(df)}")

    print(f"Average Call IV: {average_call_iv(df)}%")

    print(f"Average Put IV: {average_put_iv(df)}%")

    print("\nHighest IV Strike")

    print(highest_iv_strike(df))

    for greek in SUPPORTED_GREEKS:
        try:
            report = generate_market_report(df, greek)
            print(format_report(report))
        except Exception as e:
            print(f"Error generating report for {greek}: {e}")

if __name__ == "__main__":
    main()


