import pandas as pd
import pytest
from analytics.exposure import calculate_exposure

def test_calculate_delta_exposure():
    """delta should equal :
    delta * openInterest * contractSize"""

    df=pd.DataFrame({
        "delta":0.5,
        "call_oi": [200]
    })
    result = calculate_exposure(
        df=df, 
        greek="delta",
        contract_size=100)
    assert result.loc[0, "exposure"] == 10000

def test_preserve_original_dataframe():
    """Ensure that the original DataFrame is not modified."""
    df = pd.DataFrame({
        "delta": [0.5],
        "call_oi": [200]
    })
    original_df = df.copy(deep=True)
    calculate_exposure(df=df, greek="delta", contract_size=100)
    pd.testing.assert_frame_equal(df, original_df)

def test_adds_exposure_column():
    """Ensure that the exposure column is added to the DataFrame."""
    df = pd.DataFrame({
        "delta": [0.5],
        "call_oi": [200]
    })
    result = calculate_exposure(df=df, greek="delta", contract_size=100)
    assert "exposure" in result.columns

def test_custom_contract_size():
    """Ensure that a custom contract size is respected."""
    df = pd.DataFrame({
        "delta": [0.5],
        "call_oi": [200]
    })
    result = calculate_exposure(df=df, greek="delta", contract_size=50)
    assert result.loc[0, "exposure"] == 5000

def test_invalid_greek_raise_value_error():
    """Ensure that an invalid greek raises a ValueError."""
    df = pd.DataFrame({
        "delta": [0.5],
        "call_oi": [200]
    })
    with pytest.raises(
        ValueError,
        match="Unsupported greek"
        ):
        calculate_exposure(
            df=df, 
            greek="Theta",
            )
        
     