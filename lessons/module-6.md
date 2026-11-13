# Module 6: Use a prepared GitHub Codespace

## What you will learn

- Open the intended prepared workspace.
- Recognize the editor, [file](../glossary.md#file) explorer, and [terminal](../glossary.md#terminal).
- Save work and stop the [Codespace](../glossary.md#codespaces).

A Codespace is a cloud development environment attached to a [repository](../glossary.md#repository). Its editor can display files, [notebooks](../glossary.md#notebook), a terminal, and source-control changes in one place. Use it when a course needs a complete project workspace. For a simple notebook activity, [Colab](../glossary.md#colab) remains a suitable starting point.

## Open the course workspace

1. Sign in to the [GitHub](../glossary.md#github) account with course access.
2. Open the repository specified by the activity, not a similarly named repository from a web search.
3. Choose **Code → Codespaces → Create codespace**, or use the course launch link. Review the displayed machine and billing information.
4. Wait for the prepared environment to finish starting. The configuration installs the [Python](../glossary.md#python) and notebook tools needed here.
5. In the file explorer, open `notebooks/module-6-lab.ipynb` and select its Python kernel if prompted.
6. Run its [cells](../glossary.md#cell) in order. Save the notebook before moving to another task.

A terminal is a text interface for commands. You only need three inspection commands in this lesson: `pwd` shows the working [folder](../glossary.md#folder), `ls` [lists](../glossary.md#list) its files, and `python --version` reports the available Python version. A shell command and Python code are different languages; do not paste shell instructions into a Python cell without understanding the distinction.

See GitHub's [Codespace creation guide](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository). Availability and who pays depend on your account and the repository settings. Do not add a payment method to satisfy a practice exercise; ask for an approved alternative if access is restricted.

## Understand saving versus publishing

Saving changes stores them in the Codespace. A [commit](../glossary.md#commit) records a checkpoint in its [Git](../glossary.md#git) repository. Pushing transfers commits to the remote repository you have permission to update. None of those steps automatically submits an assignment to Populi. In the next module, you will practice those separate actions in your own workspace.

## Stop when finished

Open [your Codespaces list](https://github.com/codespaces), identify the course workspace, and use its stop action. Closing the browser tab does not necessarily stop the cloud computer. Stopped workspaces can still use storage. Follow the course's cleanup instructions, and preserve work in the correct repository before deleting anything. See [the Codespace lifecycle](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle).

**Evidence of completion:** identify the open repository, run the prepared notebook, report your working folder, and explain where work is saved before a [push](../glossary.md#push). If Codespaces is unavailable, complete the notebook in Colab and document the access issue for support; your instructor decides any required alternative.


## Guided notebook and slides

[Open the practice in Colab](https://colab.research.google.com/github/Aurnova/ains5000-course/blob/main/notebooks/module-6-lab.ipynb) · [Notebook in this book](../notebooks/module-6-lab.ipynb) · [Study slides](../slides/module-6.ipynb)

For definitions and related graduate lessons, use the [cross-course glossary](../glossary.md).
