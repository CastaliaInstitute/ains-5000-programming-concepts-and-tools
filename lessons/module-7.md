# Module 7: Save, share, submit, and troubleshoot

## What you will learn

- Distinguish saving, committing, pushing, and submitting.
- Inspect a change before sharing.
- Describe an error with enough context for help.

A reliable workflow keeps the original instructions, your working copy, and your submission distinguishable. Before sharing, ask: which [file](../glossary.md#file) did I edit, which version did I save, who can read it, and what does the assignment ask me to submit?

## Save a checkpoint in GitHub

Use your personal practice [repository](../glossary.md#repository) or the private classroom repository assigned to you. In [Codespaces](../glossary.md#codespaces), save the file, open Source Control, inspect the changed lines, stage only the intended files, and make a [commit](../glossary.md#commit) with a message such as `Label the workshop cost output`. [Push](../glossary.md#push) or sync when you are ready to transfer that checkpoint to [GitHub](../glossary.md#github). If asked to publish a [branch](../glossary.md#branch), use the repository your instructor specified. Do not grant repository access to an unfamiliar application to fix a routine push error.

Inspect the repository on GitHub after pushing. Find the changed file and latest commit. This readback distinguishes “I clicked save” from “the remote repository has my work.” A [pull request](../glossary.md#pull-request) is a request to review changes; it is needed only when the activity asks for one.

## Share a Colab notebook carefully

Use your saved Drive copy, review text and [outputs](../glossary.md#output), and set access for the intended recipient. Open the link using the permitted checking method to confirm the recipient can view it. A private [notebook](../glossary.md#notebook) link can be valid while inaccessible to your instructor. A public link may expose more information than the assignment requires. Follow the course's sharing rule rather than changing visibility by guesswork.

## Recover from a Python error

Read the final line of a [traceback](../glossary.md#traceback) first. `NameError` often means a [variable](../glossary.md#variable) was not created in this [runtime](../glossary.md#runtime). `TypeError` can mean an operation received the wrong type, such as text where a number was expected. `SyntaxError` can indicate a missing colon or quotation mark. Check the named line and the line immediately before it. Make one change, rerun, and describe what happened.

In the lab, `int("12")` converts numeric text to an [integer](../glossary.md#integer). It does not convert every possible [string](../glossary.md#string). Real [input](../glossary.md#input) [validation](../glossary.md#validation) is a separate task; try a deliberately invalid value in a scratch [cell](../glossary.md#cell), observe the error, and restore the clean example.

## Ask for useful help

Include the course and module, the tool, the step, the exact error message, and what you already tried. Remove secrets and private records from screenshots. “It does not work” gives support little to investigate; “Module 7 in [Colab](../glossary.md#colab): NameError after restarting, calculation cell ran before inputs” describes a recoverable problem.

**Evidence of completion:** a visible saved checkpoint or saved Drive copy, a sharing/submission checklist, and one clear support request. Your instructor's submission route remains authoritative.


## Guided notebook and slides

[Open the practice in Colab](https://colab.research.google.com/github/Aurnova/ains5000-course/blob/main/notebooks/module-7-lab.ipynb) · [Notebook in this book](../notebooks/module-7-lab.ipynb) · [Study slides](../slides/module-7.ipynb)

For definitions and related graduate lessons, use the [cross-course glossary](../glossary.md).
