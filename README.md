# AirBnB Clone Python Console

This is the command-line interface (CLI) component of the AirBnB Clone project for ALX Software Engineering curriculum. The CLI allows users to interact with the AirBnB Clone's data and functionality through various commands.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
- [Commands](#commands-and-usage)

## Description

The AirBnB Clone Python Console is a CLI application that provides a command-line interface for managing and interacting with different models in the AirBnB Clone project. It allows users to create, show, update, and delete instances of various models, all within a command-line environment.

## Features

- Create new instances of different models.
- Show information about a specific instance.
- Update attributes of existing instances.
- Delete instances.
- List all instances or instances of a specific model type.  

The available model types are:

- **BaseModel**
- **City**
- **Place**
- **Review**
- **State**
- **User**

## Getting Started

To use the AirBnB Clone Python Console, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `console.py` file using Python:

## Commands and Usage

Upon launching the console, you'll be greeted with a prompt `(hbnb)`. You can enter various commands to interact with the AirBnB Clone's data. Here are some example commands:

- `create [MODEL_TYPE]`: Create a new instance of the specified model.
- `show [MODEL_TYPE] [ID]`: Show details about a specific instance.
- `update [MODEL_TYPE] [ID] [ATTRIBUTE] "[NEW_VALUE]"`: Update an attribute of an instance.
- `destroy [MODEL_TYPE] [ID]`: Delete a specific instance.
- `all [MODEL_TYPE]`: List all instances or instances of a specific model type.
- `quit`: Exit the console.

For more details on available commands, you can use the `help` command followed by the specific command name or just `help` to see all available commands.
