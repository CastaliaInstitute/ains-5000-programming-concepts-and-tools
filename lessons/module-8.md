# Module 8: Use AI help and complete your readiness project

## What you will learn

- Ask a specific setup or code question.
- Check an AI answer against evidence.
- Complete and explain a small programming task.

[Gemini](../glossary.md#gemini) in [Colab](../glossary.md#colab) and [Copilot Chat](../glossary.md#copilot) in [Codespaces](../glossary.md#codespaces) can explain a setup step, discuss a code fragment, or suggest a way to investigate an error. They can also give incorrect instructions. Treat an answer as a suggestion to check against the course materials and the behavior you observe.

## Ask a bounded question

In Colab, open the built-in Gemini chat panel using the sparkle icon when your account is eligible. In Codespaces, open Copilot Chat when your [GitHub](../glossary.md#github) account has access. The prepared [repository](../glossary.md#repository) requests the extensions; that does not grant a Copilot subscription. Both tools may be restricted by institution settings. No paid assistant or API key is required for this course. You can complete the reasoning activity using the supplied example answer if an assistant is unavailable.

Try: “Explain what the [variables](../glossary.md#variable) in this workshop budget [cell](../glossary.md#cell) mean. Use plain language. Do not change files or execute code. Ask me to predict the result before giving it.” Include the relevant non-sensitive cell, because an assistant may not have the entire course context. Colab chat does not automatically know a syllabus on another website. See the [Colab FAQ](https://research.google.com/colaboratory/faq.html) and the toolkit's [Copilot guide](https://github.com/CastaliaInstitute/ains-student-toolkit/blob/main/tutorials/codespaces.md#ask-the-toolkit-with-copilot-chat).

## Evaluate the response

Compare the proposed explanation to the [input](../glossary.md#input) values, the code, and your observed [output](../glossary.md#output). If a response says that saving a [notebook](../glossary.md#notebook) submits it to Populi, reject that claim and check the assignment instructions. If a response suggests changing permissions or installing an unfamiliar package, stop and identify why that would be needed. Generated code still needs a small, understandable check.

Never provide passwords, API keys, patient records, student records, or private assessment material. For assessed work, follow your instructor's permitted-use rule and record how an assistant helped. An assistant should support your reasoning; you must be able to explain the final artifact yourself.

## Readiness project: plan a workshop budget

Choose synthetic values for attendance, cost per attendee, and the total available budget. Create a notebook that:

1. Explains the event and labels the inputs and their units.
2. Defines a [function](../glossary.md#function) that returns total estimated cost.
3. Uses a [condition](../glossary.md#condition) to label the estimate as within or over budget.
4. Uses a [loop](../glossary.md#loop) to compare at least three attendance scenarios.
5. Includes a boundary case where cost equals budget.
6. Reports outputs clearly, explains one limitation, and records any AI help.
7. Runs from a fresh [runtime](../glossary.md#runtime) and is saved and submitted through the required route.

Do not use real participant records. The starter notebook demonstrates a function but leaves your scenario design and explanation to you. Use the [assessment rubric](../assessment.md) to review your work before submission.

**Evidence of completion:** the notebook and a short reflection explaining an input change, a boundary case, an error you recovered from, and how you checked any AI suggestion.


## Guided notebook and slides

[Open the practice in Colab](https://colab.research.google.com/github/Aurnova/ains5000-course/blob/main/notebooks/module-8-lab.ipynb) · [Notebook in this book](../notebooks/module-8-lab.ipynb) · [Study slides](../slides/module-8.ipynb)

For definitions and related graduate lessons, use the [cross-course glossary](../glossary.md).
