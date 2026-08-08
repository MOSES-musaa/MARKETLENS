import pandas as pd
from core.processor import sort_by_strike

def test_option_chain_is_sorted_by_strike():
    df =pd.DataFrame({
        "strike": [100, 90, 110, 95],
    })

    # Process the option chain
    result= sort_by_strike(df)

    expected = pd.DataFrame({
        "strike": [90, 95, 100, 110],
    })

    pd.testing.assert_frame_equal(
        result.reset_index(drop=True),
        expected)   
    