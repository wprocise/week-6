# Week 5

This week's lab is meant to introduce you to APIs and Multiprocessing. Often, these two concepts go well together, but on their own, each are powerful tools for gathering data. Further, Multiprocessing is quite helpful for speeding up routines on large datasets which can be done in parallel. In particular, we'll cover the following topics:

- Accessing an API
- API Wrappers
- Python Scripts
- Multiprocessing

## Setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. **Upload** the .env file shared with you on Canvas. This is needed to run the lab notebook.
4. Once you're ready, [commit and push](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes) your final changes to your repository. *Note: You can also make quick edits using the [GitHub Dev Editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor).*

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: week-5
dependencies:
  - python=3.11
  - pip
  - pip:
    - ipykernel  # for Jupyter Notebook
    - streamlit
    - seaborn
    - pandas
    - numpy
    - python-dotenv
    - requests
    - tqdm
```

*Note: you are welcome to install more packages in your codespace, but they will not be used by the autograder.*