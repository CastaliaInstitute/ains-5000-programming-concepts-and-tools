# Module 5: Decisions, lists, loops, and functions

## What you will learn

- Use a [condition](../glossary.md#condition) and test its boundary.
- Repeat work over a [list](../glossary.md#list).
- Define and call a small [function](../glossary.md#function).

A repeated task is easier to understand when its steps have names and a clear order. Imagine checking whether each planned workshop fits an available room. You have a list of attendance counts, one room capacity, and a rule: flag any count above capacity.

## Make a decision

A **condition** is an expression that evaluates to true or false. An `if` statement selects instructions based on that condition. [Python](../glossary.md#python) uses indentation to show which instructions belong together.

```python
attendees = 18
capacity = 20
if attendees <= capacity:
    print("Room fits")
else:
    print("Choose a larger room")
```

Read the comparison before the [branches](../glossary.md#branch): is attendance less than or equal to capacity? Test the boundary where the two numbers are equal. In this rule, a room with exactly enough seats fits. Changing `<=` to `<` changes that decision.

## Repeat with a list and a loop

A **list** groups ordered values, such as `[12, 18, 24]`. A **[loop](../glossary.md#loop)** repeats instructions for each item. In `for attendees in attendance_counts:`, the [variable](../glossary.md#variable) takes one count at a time. A colon introduces the indented instructions that repeat. Do not copy the same block three times when one loop describes the pattern more clearly.

## Give a reusable calculation a name

A **function** groups instructions and can return a result. Its [parameters](../glossary.md#parameter) name the [inputs](../glossary.md#input) it needs.

```python
def estimated_cost(attendees, cost_per_person):
    return attendees * cost_per_person
```

Calling `estimated_cost(12, 7.5)` returns 90.0. Printing a result displays it; returning a result lets another instruction use it. A function definition alone does not run the function body.

## Practice: capacity review

Run the [notebook](../glossary.md#notebook)'s review for three workshops. Predict which one exceeds capacity. Add an attendance count of exactly 20, then explain why that case matters. Add a function that calculates a total from an attendance count and a unit cost. Keep examples small enough that you can check them by hand.

If indentation is inconsistent, Python can reject the code before it runs. Use four spaces for each block and inspect the line immediately before an indentation error. An error message identifies a place to investigate; it is not a judgment about your ability.

**Evidence of completion:** a loop that labels all workshop counts, one tested boundary case, and a function you can explain without reading its code aloud. See [Python control flow](https://docs.python.org/3/tutorial/controlflow.html).


## Guided notebook and slides

[Open the practice in Colab](https://colab.research.google.com/github/Aurnova/ains5000-course/blob/main/notebooks/module-5-lab.ipynb) · [Notebook in this book](../notebooks/module-5-lab.ipynb) · [Study slides](../slides/module-5.ipynb)

For definitions and related graduate lessons, use the [cross-course glossary](../glossary.md).
