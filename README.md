# Django Honeycomb Metrics Integration

This repository contains a Django project that demonstrates how to integrate Honeycomb for collecting metrics and
observability in your Django application. Honeycomb provides powerful tools for tracking, analyzing, and visualizing
application performance and behavior.

## Requirements

To ensure a smooth setup and operation of the Django Honeycomb Metrics Integration project, make sure you have the
following requirements installed:

- **Python**: ^3.10
    - The project is developed and tested with Python 3.10. I recommend using [pyenv](https://github.com/pyenv/pyenv)
      to manage your Python versions. Pyenv provides a simple and flexible way to install and switch between different
      Python versions.

- **Poetry**:
    - Poetry is used as the dependency manager for this project. It simplifies the management of project dependencies
      and virtual environments. You can install Poetry by following the instructions on
      the [Poetry documentation](https://python-poetry.org/docs/#installation).

After installing the above requirements, proceed with the steps mentioned in the "Getting Started" section to set up and
run the project locally.

---

Please make sure to have Python 3.10 installed and set up in your environment using pyenv before continuing with the
project setup. Additionally, install Poetry to manage the project dependencies and create a virtual environment for
isolated development.

## Getting Started

### Clone the repository:

```
git clone https://github.com/victoraugusto6/django-metrics-honeycomb
cd django-metrics-honeycomb
```

### Create and activate a virtual environment using Poetry:

```
poetry shell
```

### Install the project dependencies:

```
poetry install
```

### Create a copy of the sample environment configuration:

```
cp contrib/env-sample .env
```

#### Note: Don't forget to replace HONEYCOMB_API_KEY with your actual Honeycomb API key in the .env file.
