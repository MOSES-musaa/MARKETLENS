import pandas as pd
from analytics.reports import generate_market_report

def test_generate_market_report_returns_expected_report():
    df= pd.DataFrame({
        "strike": [100, 105, 110],
        "gamma": [0.1, 0.2, 0.3],
        "call_oi": [1000, 1500, 2000],
    })

    result = generate_market_report(df, "gamma")

    assert result["greek"] == "gamma"

    assert result["largest"]["strike"] == 110
    assert result["largest"]["exposure"] == 60000

    assert result["smallest"]["strike"] == 100
    assert result["smallest"]["exposure"] == 10000

    assert result["strength"] == "Very High"
    assert result["interpretation"] is not None