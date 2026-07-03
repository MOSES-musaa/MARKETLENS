# MarketLens Development Log

---

## Day 1

## Goal

Prepare the development environment.

## Completed

- Installed Python
- Installed Git
- Installed PostgreSQL
- Connected pgAdmin
- Created MarketLens project
- Created Virtual Environment
- Installed project dependencies
- Created project structure

## Challenges

None

## Lessons Learned (Day 1)

- Importance of isolated Python environments
- PostgreSQL installation and configuration
- Git configuration
- Professional project organization

---

## Next Goal

Read and inspect CME options chain data.

## DEVLOG

---

### Day 5 – Rebuilding Dealer Delta Exposure (DEX)

## Date

(Insert Today's Date)

---

## Objective

Continue building the analytics engine for MarketLens by redesigning the Dealer Delta Exposure (DEX) module using professional software engineering principles instead of simply fixing existing errors.

---

## Lessons Learned

### 1. Function Contracts

A function consists of two major parts:

- Contract (Function Header)
- Implementation (Function Body)

Example:

```python
def calculate_dex(
    df: pd.DataFrame,
    contract_size: int = 100
) -> pd.DataFrame:
```

The function contract explains:

- What input is expected.
- What output will be returned.

It does not explain how the calculations are performed.

---

### 2. Type Hints

Learned how Python uses type hints to improve readability.

Examples:

```python
df: pd.DataFrame
```

expects a Pandas DataFrame.

```python
contract_size: int
```

expects an Integer.

```python
-> pd.DataFrame
```

returns a Pandas DataFrame.

Type hints document code but are not enforced by Python.

---

### 3. Immutability

Instead of modifying the original DataFrame:

```python
df["dex"] = ...
```

we first create a working copy.

```python
result = df.copy()
```

Reasons:

- Protect source data.
- Easier debugging.
- Easier rollback.
- Makes data pipelines safer.
- Prevents unintended side effects.

---

### 4. Vectorization

Instead of looping through every row:

```python
for ...
```

Pandas performs calculations across entire columns.

Example:

```python
result["dex"] = (
    result["delta"]
    * result["call_oi"]
    * contract_size
)
```

Benefits:

- Cleaner code.
- Faster execution.
- Better scalability.

---

### 5. Feature Engineering

Instead of replacing data, we enrich it.

Original Data:

- Strike
- Delta
- Call OI

Processed Data:

- Strike
- Delta
- Call OI
- DEX

New analytical features are added while preserving the original information.

---

### 6. Building calculate_dex()

Created the first production-style analytics function.

Responsibilities:

- Receive DataFrame.
- Create a safe copy.
- Calculate DEX.
- Return enriched DataFrame.

---

### 7. Function Return Types

Understood why:

```python
return result
```

is necessary.

The function contract promised to return a DataFrame.

Returning the processed copy fulfills that promise.

---

### 8. Finding Largest Dealer Delta Exposure

Algorithm:

1. Scan the DEX column.
2. Find the index of the largest value.
3. Retrieve the complete row.
4. Return the row.

Implementation:

```python
index = df["dex"].idxmax()

return df.loc[index]
```

---

### 9. Pattern Recognition

Observed that many analytics functions follow the same pattern.

Examples:

Largest Call OI

```python
idxmax()
```

Largest Put OI

```python
idxmax()
```

Largest DEX

```python
idxmax()
```

Smallest DEX

```python
idxmin()
```

Instead of memorizing code, recognize reusable patterns.

---

### 10. Software Engineering Mindset

Every function should answer three questions.

1. What goes in?

Example:

```python
df
```

1. What happens?

- Copy data
- Calculate
- Analyze

1. What comes out?

Example:

```python
pd.DataFrame
```

or

```python
pd.Series
```

Thinking this way makes functions easier to design and debug.

---

## Trading Concepts Learned

Dealer Delta Exposure depends on two things:

- Delta
- Open Interest

High Delta alone does not guarantee the highest Dealer Exposure.

Example:

Strike A

Delta = 0.90

OI = 200

DEX = Smaller

Strike B

Delta = 0.50

OI = 1800

DEX = Larger

Large Open Interest can outweigh a smaller Delta.

Dealer positioning depends on total exposure rather than Delta alone.

---

## Key Takeaways

Today I realized that software engineering is not about writing more code.

It is about designing small, reusable functions that each solve one clear problem.

I also learned that understanding patterns is more valuable than memorizing syntax.

---

## Tomorrow's Objectives

- Build greeks.py
- Understand mathematical Delta.
- Learn why Delta changes.
- Learn Gamma mathematically.
- Understand Dealer Hedging.
- Prepare MarketLens for Gamma Exposure (GEX)

## Day 7

Implemented a generic exposure engine.

### Why?

Previously we had separate functions for DEX and GEX.

This violated DRY.

The new implementation accepts any Greek as a parameter.

Concepts learned

- Vectorization
- Parameterization
- Code reuse
- High Cohesion
