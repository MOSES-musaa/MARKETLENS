
def format_report(report: dict) -> str:

    """formats the market report for terminal display
    """
    greek = report["greek"]
    largest = report["largest"]
    smallest = report["smallest"]
    strength = report["strength"]
    interpretation = report["interpretation"]

    return f"""
==============================
        MARKETLENS
==============================

Greek: {greek.title()}

Largest Exposure
----------------
Strike     : {largest["strike"]}
Exposure   : {largest["exposure"]:.2f}

Smallest Exposure
-----------------
Strike     : {smallest["strike"]}
Exposure   : {smallest["exposure"]:.2f}

Strength
--------
{strength}

Interpretation
--------------
{interpretation}
"""