# Week 6

This week's lab is meant to introduce you to some useful tools for gathering data. We will also cover a few more in-depth Python techniques such as classes and running scripts.

In particular, we'll cover the following topics:

- Accessing an API
- Python Scripts
- Classes
- Multiprocessing

## Setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. This week, you will be saving a **.env** file that will be *ignored* by git. For this reason, you might find it safest to [clone](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_clone-a-repository-locally) your fork of the weekly repository, and work locally on VS Code instead of on a codespace.
   - *Note: if you do this, you'll need to [create an environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) using the **environment.yml** text, below.*
3. (Optional) You are still welcome to [create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository; just make sure to save your **.env** file somewhere safe in case you need to restart the codespace.
4. Save (or upload) the .env file shared with you on Canvas. This is needed to run the lab notebook.
5. Once you're ready, [commit and push](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes) your final changes to your repository. *Note: You can also make quick edits using the [GitHub Dev Editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor).*

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: week-6
dependencies:
  - python=3.11
  - pip
  - pip:
    - ipykernel  # for Jupyter Notebook
    - streamlit
    - seaborn
    - pandas
    - joblib
    - numpy
    - python-dotenv
    - requests
    - tqdm
```

*Note: you are welcome to install more packages in your codespace, but they will not be used by the autograder.*