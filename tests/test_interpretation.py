import pytest
from analytics.interpretation import interpret_exposure

def test_interpret_exposure_handles_moderate_strength():
   result = interpret_exposure(
       "gamma",
       "Moderate",
       "120"
   )
   assert result is not None
   assert "120" in result
   assert "Moderate" in result

def test_interpret_exposure_handles_lowest_strength():
    result = interpret_exposure(
        "gamma",
         "Low",
         "60"
    )
    assert result is not None
    assert "60" in result
    assert "Low" in result

def test_interpret_exposure_rejects_unsupported_greek():
    with pytest.raises(ValueError) as exc_info:
        interpret_exposure(
            "vega",
            "High",
            "120"
        )
    assert str(exc_info.value) == (
        "No Interpretation template available for greek 'vega'."
    )
    