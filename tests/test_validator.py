import pandas as pd
import pytest
from core.validator import validate_option_chain

#tests whether a valid option chain passes validation without raising an error
def test_valid_option_chain_passes():
    df =pd.DataFrame({
        "delta":[0.5],
        "gamma":[0.02],
        "call_oi":[200],
        "put_oi":[150],
        "implied_volatility":[0.25],
    })

    required_columns=[
        "delta",
        "gamma",
        "call_oi", 
        "put_oi", 
        "implied_volatility"
        ]
    result = validate_option_chain(
        df, 
        required_columns
        )
    pd.testing.assert_frame_equal(result, df)

#tests whether a missing required column raises a ValueError when validated
def test_missing_required_column_raises_error():
    df = pd.DataFrame({
        "delta":[0.5],
        "call_oi":[200],
        "put_oi":[150],
        "implied_volatility":[0.25],
    })

    required_columns=[
        "delta",
        "gamma",
        "call_oi", 
        "put_oi", 
        "implied_volatility",
        ]
    
    with pytest.raises(ValueError) as exc_info:
        validate_option_chain(
            df, 
            required_columns
            )
    assert str(exc_info.value) == "Option chain is missing required columns: gamma"

#tests whether an empty option chain raises a ValueError when validated
def test_empty_option_chain_raises_value_error():
    df = pd.DataFrame()
    
    required_columns=[
        "delta",
        "gamma",
        "call_oi", 
        "put_oi", 
        "implied_volatility"
        ]
    
    with pytest.raises(ValueError) as exc_info:
        validate_option_chain(
            df, 
            required_columns
            )
    assert str(exc_info.value) == "Option chain is empty"

#tests whether multiple missing required columns raises a ValueError when validated
def test_multiple_missing_required_columns_raises_error():
    df = pd.DataFrame({
        "delta":[0.5],
        "call_oi":[200],
        "put_oi":[150],
    })

    required_columns=[
        "delta",
        "gamma",
        "call_oi", 
        "put_oi", 
        "implied_volatility",
        ]
    
    with pytest.raises(ValueError) as exc_info:
        validate_option_chain(
            df, 
            required_columns
            )
    assert str(exc_info.value) == "Option chain is missing required columns: gamma, implied_volatility"

#tests whether our validator does not modify the original dataframe when it passes validation
def test_validator_does_not_modify_dataframe():
    df = pd.DataFrame({
        "delta":[0.5],
        "gamma":[0.02],
        "call_oi":[200],
        "put_oi":[150],
        "implied_volatility":[0.25],
    })

    required_columns=[
        "delta",
        "gamma",
        "call_oi", 
        "put_oi", 
        "implied_volatility"
        ]
    
    original_df = df.copy()
    validate_option_chain(
        df, 
        required_columns
        )
    pd.testing.assert_frame_equal(df, original_df)