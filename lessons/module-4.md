# Module 4: Programming concepts: inputs, values, and variables

## What you will learn

- Identify [inputs](../glossary.md#input) and [outputs](../glossary.md#output).
- Use [variables](../glossary.md#variable) and basic [data types](../glossary.md#data-type).
- Explain an assignment and a calculation.

A program transforms inputs into outputs by following instructions. For an event budget, the inputs might be the number of participants and the cost of lunch. The output is the estimated lunch cost. Before writing code, describe the calculation in a sentence: multiply the number of participants by the cost per lunch.

## Name the values

A **variable** is a name referring to a value. In `participants = 12`, [Python](../glossary.md#python) associates the name `participants` with the [integer](../glossary.md#integer) 12. The equals sign assigns a value; it does not assert a mathematical equation that remains true forever. When you assign a different value later, the name refers to that new value.

Python distinguishes data types. An **integer** is a whole number, a **float** represents a number with a decimal point, a **[string](../glossary.md#string)** is text, and a **[Boolean](../glossary.md#boolean)** is `True` or `False`. `12` and `"12"` are different values: one is a number, the other is text. Quotation marks identify strings.

Use meaningful names: `lunch_cost` explains more than `x`. Names cannot contain spaces. Comments beginning with `#` explain a step for people; Python does not execute the comment as an instruction.

## Read a calculation

```python
participants = 12
lunch_cost = 7.5
estimated_cost = participants * lunch_cost
print("Lunch estimate:", estimated_cost)
```

Read it aloud: store the participant count, store the unit cost, multiply them, and display a labeled result. Predict the answer before running the [cell](../glossary.md#cell). The multiplication symbol is `*`; Python uses `/` for division and `**` for exponentiation.

## Practice: change one input

Use the [notebook](../glossary.md#notebook) to compare the lunch estimate for 12 and 18 participants. Keep the unit cost fixed. Then change only the unit cost and explain its effect. Add a comment describing the units of each input. A value of `7.5` needs context: dollars per lunch is different from hours per activity.

A computer will calculate an implausible input as readily as a plausible one. A negative participant count produces a number, but that number is not a useful event estimate. Reading outputs critically is part of programming.

## Check your understanding

Explain why `"12" + "3"` produces text rather than the number 15. What happens to `estimated_cost` if you change `participants` but never rerun the multiplication? Why are units and labels useful?

**Evidence of completion:** two controlled comparisons and a plain-language explanation of each input, calculation, and output. The [Python introduction](https://docs.python.org/3/tutorial/introduction.html) is a reference for further examples.


## Guided notebook and slides

[Open the practice in Colab](https://colab.research.google.com/github/Aurnova/ains5000-course/blob/main/notebooks/module-4-lab.ipynb) · [Notebook in this book](../notebooks/module-4-lab.ipynb) · [Study slides](../slides/module-4.ipynb)

For definitions and related graduate lessons, use the [cross-course glossary](../glossary.md).
