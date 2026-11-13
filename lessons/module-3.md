# Module 3: Run and save a notebook in Google Colab

## What you will learn

- Open and save a personal [notebook](../glossary.md#notebook) copy.
- Run [cells](../glossary.md#cell) in dependency order.
- Recover from a [runtime](../glossary.md#runtime) reset.

[Colab](../glossary.md#colab) lets you execute [Python](../glossary.md#python) in your browser. You work with a notebook document and a temporary runtime. You do not need a local Python installation. Start with the default CPU runtime for this course; these exercises do not require a GPU or paid plan.

## Open, copy, and run

1. Follow this lesson's **Open in Colab** link to the guided notebook.
2. Sign in to the Google account you use for coursework.
3. Choose **[File](../glossary.md#file) → Save a copy in Drive**. Give the copy a recognizable name, such as `AINS5000-M3-yourname`.
4. Read the first text cell. Select the first code cell and use its run button or **Shift+Enter**.
5. Continue from top to bottom. A number beside a cell indicates an execution; it does not prove the whole notebook ran in order.
6. Change one [input](../glossary.md#input) and rerun the affected cells. Describe the change in a text cell.
7. Confirm the copy is saved in Drive. Follow your instructor's submission instructions; saving is not submission.

The notebook may show an [output](../glossary.md#output) from a previous session. To check that it works from a clean start, use the runtime restart command and run the cells in order. Do this only after saving work. If a [variable](../glossary.md#variable) is “not defined,” look for the earlier cell that creates it rather than repeatedly rerunning the failing cell.

## A small worked example

The notebook defines `attendees = 10` and `cost_per_person = 8`, then calculates `total = attendees * cost_per_person`. Predict the total before running it. If you change attendees to 15, the total changes only when you rerun the calculation. A saved output is a record of an earlier run, not an automatically refreshed spreadsheet cell.

## Practice: recover deliberately

Save the notebook, restart the runtime, and try the calculation cell before the input cell. Observe the error. Then run the input cell followed by the calculation. Explain the dependency using ordinary language. Keep the deliberately failing experiment in a separate scratch cell or remove it before a clean final run.

When sharing a notebook, review its entire contents, including outputs. A viewer can see what was saved in the document. Do not make it public unless the activity explicitly requires that. The temporary runtime's files are separate from the shared notebook.

**Evidence of completion:** a saved notebook copy, a clean sequential run, and a brief account of the error you recovered from. See the [official Colab FAQ](https://research.google.com/colaboratory/faq.html) for storage and sharing behavior.


## Guided notebook and slides

[Open the practice in Colab](https://colab.research.google.com/github/Aurnova/ains5000-course/blob/main/notebooks/module-3-lab.ipynb) · [Notebook in this book](../notebooks/module-3-lab.ipynb) · [Study slides](../slides/module-3.ipynb)

For definitions and related graduate lessons, use the [cross-course glossary](../glossary.md).
