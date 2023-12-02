# AirlinesTickets

AirlinesTickets is a Django web application with Django Rest Framework for selling plane tickets.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Acknowledgments](#acknowledgments)

## Description

AirlinesTickets is a web application built with Django and Django Rest Framework to facilitate the selling of plane
tickets. It includes features such as user authentication, ticket booking.

## Features

[//]: # (in progress)

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following software installed on your machine:

- [Python](https://www.python.org/) (version 3.8.x recommended)
    - You can download Python from the [official website](https://www.python.org/).

- [Poetry](https://python-poetry.org/) (version 1.1.x recommended)
    - Poetry is a dependency manager for Python. You can install it using the instructions provided on
      the [Poetry website](https://python-poetry.org/docs/#installation).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Yureeets/AirlineTickets-.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirlinesTickets
    ```

3. Install dependencies with Poetry:

    ```bash
    poetry install
    ```

4. Run migrations:

    ```bash
    poetry run python manage.py migrate
    ```

5. Create a superuser account:

    ```bash
    poetry run python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    poetry run python manage.py runserver
    ```

Visit `http://localhost:8000/` in your browser to access the application.

## Usage

in progress

## API Documentation

For detailed API documentation, you can use Swagger, which provides a user-friendly interface to explore and interact with the API endpoints.

To access the Swagger documentation:

1. Ensure your development server is running:

    ```bash
    poetry run python manage.py runserver
    ```

2. Open your web browser and go to:

    ```
    http://localhost:8000/swagger/
    ```
   
This will open the Swagger UI, allowing you to explore the available endpoints, make requests, and view responses interactively.

## Acknowledgments

- Thanks NULP for this opportunity.


