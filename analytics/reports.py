from analytics.exposure import (
    calculate_exposure,
    largest_exposure,
)

from analytics.interpretation import (
    classify_exposure,
    interpret_exposure
)


def generate_market_report(df):

    # Step 1
    result = calculate_exposure(df, "delta")

    # Step 2
    largest = largest_exposure(result, "delta")

    # Step 3
    max_exposure = result["exposure"].max()

    # Step 4
    strength = classify_exposure(
        largest["exposure"],
        max_exposure
    )

    # Step 5
    interpretation = interpret_exposure(
        largest,
        "delta"
    )

    # Step 6
    ...