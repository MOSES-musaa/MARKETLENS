
import pandas as pd
import pytest
from analytics.exposure import calculate_exposure, largest_exposure, smallest_exposure

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
        
"""EXPOSURE RELATED TESTS"""
def test_largest_exposure_returns_row_with_highest_exposure():
    """Ensure that the largest_exposure function returns the row with the highest exposure."""
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [200_000, 300_000, 100_000]
    })

    result = largest_exposure(df,)

    expected = pd.Series({
        "strike": 4100,
        "exposure": 300_000
    },)

    pd.testing.assert_series_equal(
        result[["strike", "exposure"]],
          expected,
          check_names=False)

def test_largest_exposure_returns_highest_exposure():
    df= pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [200_000, 300_000, 100_000]
    })
    result = largest_exposure(df)
    assert result["strike"] == 4100
    assert result["exposure"] == 300_000

def test_smallest_exposure_returns_row_smallest_exposure():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [200_000, 300_000, 100_000]
    })  
    result = smallest_exposure(df)
    assert result["strike"] == 4050
    assert result["exposure"] == 100_000

def test_smallest_exposure_handles_negative_values():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [200_000, -300_000, 100_000]
    })

    result = smallest_exposure(df)

    assert result["strike"] == 4100
    assert result["exposure"] == -300_000

def test_largest_exposure_returns_first_occurrence_of_max_exposure():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050, 4200],
        "exposure": [200_000, 300_000, 300_000, 100_000]
    })

    result = largest_exposure(df)

    assert result["strike"] == 4100
    assert result["exposure"] == 300_000

def test_smallest_exposure_returns_first_occurrence_of_min_exposure():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050, 4200],
        "exposure": [200_000, 100_000, 100_000, 300_000]
    })

    result = smallest_exposure(df)

    assert result["strike"] == 4100
    assert result["exposure"] == 100_000

def test_smallest_exposure_handles_zero():
    df= pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure":[500_000,0,200_000],
    })
    result = smallest_exposure(df)
    assert result["strike"] == 4100
    assert result["exposure"] == 0

def test_smallest_exposure_ignores_nan_values():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [200_000, float('nan'), 100_000]
    })

    result = smallest_exposure(df)

    assert result["strike"] == 4050
    assert result["exposure"] == 100_000

def test_smallest_exposure_rejects_all_nan_values():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [float('nan'), float('nan'), float('nan')]
    })

    with pytest.raises(ValueError) as exc_info:
        smallest_exposure(df)

        assert str(exc_info.value) == "cannot determine smallest exposure."
        " All exposure values are missing."

def test_largest_exposure_rejects_all_nan_values():
    df = pd.DataFrame({
        "strike": [4000, 4100, 4050],
        "exposure": [float('nan'), float('nan'), float('nan')]
    })

    with pytest.raises(ValueError) as exc_info:
        largest_exposure(df)

        assert str(exc_info.value) == "cannot determine largest exposure."
        " All exposure values are missing."