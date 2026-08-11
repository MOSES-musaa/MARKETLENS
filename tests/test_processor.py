import pandas as pd
from core.processor import sort_by_strike,reset_data_frame_index,process_option_chain

#assessing whether option chain is sorted by strike price
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

#tests whether after sorting, the index are reset to appear well
def test_reset_dataframe_index():
    df = pd.DataFrame({
        "strike": [4000, 4025, 4035, 4050],
    },index=[5,8,12,15])

    result= reset_data_frame_index(df)
    expected = pd.DataFrame({
        "strike": [4000, 4025, 4035, 4050],
    })

    pd.testing.assert_frame_equal(result, expected)

#tests whether process_option_chain() maintains its workflow
def test_process_option_chain():
    df = pd.DataFrame({
        "strike": [4050, 4100, 4035, 4025],
    },index=[5,8,12,15])

    result= process_option_chain(df)
    expected = pd.DataFrame({
        "strike": [4025, 4035, 4050, 4100],
    })

    pd.testing.assert_frame_equal(result, expected)

#test whether original dataframe is preserved after processing the option chain
def test_process_option_chain_does_not_modify_original_dataframe():
    df = pd.DataFrame({
        "strike": [4050, 4100, 4035, 4025],
    },index=[5,8,12,15])

    original_df = df.copy(deep=True)

    process_option_chain(df)

    pd.testing.assert_frame_equal(df, original_df)

#tests whether duplicate strike prices are preserved after sorting by strike price
def test_sort_by_strikes_preserves_duplicate_strike_prices():
    df = pd.DataFrame({
        "strike": [4050, 4100, 4035, 4025, 4050],
    },index=[5,8,12,15,20])

    result= sort_by_strike(df)
    expected = pd.DataFrame({
        "strike": [4025, 4035, 4050, 4050, 4100],
    })

    pd.testing.assert_frame_equal(
        result.reset_index(drop=True),
          expected)

#tests whether row relationships are preserved after sorting by strike price
def test_sort_by_strike_preserves_row_data():
    df = pd.DataFrame({
        "strike": [4050, 4100, 4035, 4025],
        "gamma": [10, 15, 8, 12],
        "call_oi": [100, 150, 80, 120],
    },index=[5,8,12,15])

    result= sort_by_strike(df)
    expected = pd.DataFrame({
        "strike": [4025, 4035, 4050, 4100],
        "gamma": [12, 8, 10, 15],
        "call_oi": [120, 80, 100, 150]
    })

    pd.testing.assert_frame_equal(
        result.reset_index(drop=True),
          expected)

def test_process_empty_option_chain():
    df = pd.DataFrame(columns=
        ["strike", 
        "gamma", 
        "call_oi"])
    result = process_option_chain(df)
    expected = pd.DataFrame(columns=
         ["strike", 
         "gamma", 
         "call_oi"])
    pd.testing.assert_frame_equal(result, expected)

#testing whether processing protects the dataset's schema and preserves all columns.
def test_process_option_chain_preserves_all_columns():
    df = pd.DataFrame({
        "strike": [4050, 4100, 4035, 4025],
        "gamma": [10, 15, 8, 12],
        "call_oi": [100, 150, 80, 120],
        "put_oi": [200, 250, 180, 220],
        "implied_volatility": [0.2, 0.25, 0.18, 0.22]
    })

    result = process_option_chain(df)

    assert list(result.columns) ==list(df.columns)

def test_process_option_chain_returns_clean_index():
    df = pd.DataFrame({
        "strike": [4050, 4100, 4035, 4025],
    },index=[5,8,12,15])

    result = process_option_chain(df)

    assert list(result.index) == [0, 1, 2, 3]

def test_single_row_option_chain():
    df= pd.DataFrame({
        "strike": [4050],
        "gamma": [10],
        "call_oi": [100],
        "put_oi": [200],
        "implied_volatility": [0.2]
    },index=[5])

    result = process_option_chain(df)
    expected = pd.DataFrame({
        "strike": [4050],
        "gamma": [10],
        "call_oi": [100],
        "put_oi": [200],
        "implied_volatility": [0.2]
    },index=[0])

    pd.testing.assert_frame_equal(result, expected)