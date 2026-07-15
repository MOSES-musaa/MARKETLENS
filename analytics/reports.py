from analytics.exposure import (
    calculate_exposure,
    largest_exposure,
    smallest_exposure
)

from analytics.interpretation import (
    classify_exposure,
    interpret_exposure
)

def generate_market_report(df, greek):

    result = calculate_exposure(df, greek)

    largest = largest_exposure(result, greek)

    smallest = smallest_exposure(result, greek)

    max_exposure = result["exposure"].max()

    strength = classify_exposure(
        largest["exposure"] , max_exposure
    )

    interpretation = interpret_exposure(
        greek,
        strength,
        largest["strike"],
    )

    return {
    "greek": greek,
    "largest": largest,
    "smallest": smallest,
    "strength": strength,
    "interpretation": interpretation
    }