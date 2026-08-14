import pytest
from analytics.interpretation import interpret_exposure,classify_exposure

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

def test_classify_exposure_threshold_boundaries():
    assert classify_exposure(80,100) == "Very High"
    assert classify_exposure(60,100) == "High"
    assert classify_exposure(40,100) == "Moderate"
    assert classify_exposure(39,100) == "Low"

def test_classify_exposure_zero_is_low():
    assert classify_exposure(0,100) == "Low"

def test_classify_exposure_rejects_zero_max_exposure():

    with pytest.raises(ValueError) as exc_info:
        classify_exposure(0,0)

    assert str(exc_info.value) ==(
        "Cannot classify exposure when maximum exposure is zero."
    )

def test_classify_exposure_uses_absolute_exposure():
    assert classify_exposure(-80,100) == "Very High"
    assert classify_exposure(-60,100) == "High"
    assert classify_exposure(-40,100) == "Moderate"
    assert classify_exposure (-39,100) == "Low"