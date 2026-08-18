import pandas as pd
import pytest
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

def test_generate_market_report_returns_correct_smallest_exposure():
    df = pd.DataFrame({
        "strike": [100, 105, 110],
        "gamma": [0.1, 0.2, 0.3],
        "call_oi": [1000, 1500, 2000],
    })

    result = generate_market_report(df, "gamma")

    assert result["smallest"]["strike"] == 100
    assert result["smallest"]["exposure"] == 10000

def test_generate_market_report_classifies_largest_exposure():
    df = pd.DataFrame({
        "strike": [100, 105, 110],
        "gamma": [0.1, 0.2, 0.3],
        "call_oi": [1000, 1500, 2000],
    })

    result = generate_market_report(df, "gamma")

    assert result["strength"] == "Very High"

def test_generate_market_report_interprets_largest_exposure():
    df = pd.DataFrame({
        "strike": [100, 105, 110],
        "gamma": [0.1, 0.2, 0.3],
        "call_oi": [1000, 1500, 2000],
    })

    result = generate_market_report(df, "gamma")

    assert result["interpretation"] is not None
    assert "110" in result["interpretation"]
    assert "High" in result["interpretation"]


def test_generate_market_report_rejects_unsupported_greek():
    df = pd.DataFrame({
        "strike" : [100,110,120],
        "gamma" :[0.1,0.2,0.3],
        "call_oi":[1000,1500,2000]
    })

    with pytest.raises(ValueError) as exc_info:
        generate_market_report(df, "vega")

        assert str(exc_info.value) ==(
            "Unsupported greek 'vega'."
            "Supported greeks are :delta, gamma"
        )

def test_generate_market_report_returns_complete_report():
    df= pd.DataFrame({
        "strike":[110,120,130,140],
        "gamma":[0.1,0.25,0.15,0.30],
        "call_oi":[100,200,300,400]
    })

    result = generate_market_report(df, "gamma")

    assert result ["greek"]=="gamma"
    assert result ["largest"] is not None
    assert result ["smallest"] is not None
    assert result ["strength"] is not None
    assert result ["interpretation"] is not None

def test_generate_market_report_identifies_the_largest_exposure():
    df = pd.DataFrame({
        "strike":[110,120,130,150],
        "gamma":[0.25,0.30,0.15,0.20],
        "call_oi":[1000,2000,3000,4000]
    })

    result= generate_market_report(df,"gamma")

    assert result ["largest"]["strike"]== 150
    assert result ["largest"]["exposure"]== 80000

def test_generate_market_report_identifies_the_smallest_exposure():
    df =pd.DataFrame({
        "strike":[110,120,130],
        "gamma":[0.10,0.20,0.30],
        "call_oi":[1000,2000,3000]
    })

    result = generate_market_report(df,"gamma")

    assert result ["smallest"]["strike"]==110
    assert result ["smallest"]["exposure"]== 10000

