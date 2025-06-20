[![Python CI/CD](https://github.com/svereshagin/DRWEBQUEST/actions/workflows/python-ci.yml/badge.svg)](https://github.com/svereshagin/DRWEBQUEST/actions/workflows/python-ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)


# DRWEBQUEST - In-Memory Database with Transaction Support

Python implementation of a test task for Dr.Web.  
A console application representing an in-memory database with transaction support.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command Reference](#command-reference)
- [Examples](#examples)
- [Technical Implementation](#technical-implementation)
- [Limitations](#limitations)

## Features
- Key-value storage in memory
- Transaction support with nesting
- Atomic commit/rollback operations
- Fast value counting and searching

## Installation

### Prerequisites
- Python 3.12+

### Installation Steps
```bash
# For Linux/Windows:
pip install -r requirements.txt

# For MacOS:
pip3 install -r requirements.txt
```

## Usage
```bash
# Linux/Windows:
python main.py

# MacOS:
python3 main.py
```

## Command Reference

| Command    | Syntax               | Description                                  |
|------------|----------------------|----------------------------------------------|
| SET        | `SET <key> <value>`  | Stores the value for specified key           |
| GET        | `GET <key>`          | Retrieves value for key or NULL              |
| UNSET      | `UNSET <key>`        | Removes the key from storage                 |
| COUNTS     | `COUNTS <value>`     | Returns count of keys with specified value   |
| FIND       | `FIND <value>`       | Returns all keys with specified value        |
| BEGIN      | `BEGIN`              | Starts new transaction block                 |
| ROLLBACK   | `ROLLBACK`           | Cancels current transaction changes          |
| COMMIT     | `COMMIT`             | Applies current transaction changes          |
| END        | `END`                | Terminates the application                   |

## Examples

### Basic Operations
```bash
> SET user:1 "John Doe"
> GET user:1
"John Doe"
> COUNTS "John Doe"
1
> FIND "John Doe"
user:1
> UNSET user:1
> GET user:1
NULL
```

### Transaction Handling
```bash
> BEGIN
> SET balance 100
> BEGIN
> SET balance 150
> GET balance
150
> ROLLBACK
> GET balance
100
> COMMIT
> GET balance
100
```

## Technical Implementation
- **Data Storage**: Python dictionary with defaultdict for value counting
- **Transactions**: Stack-based change tracking with rollback capability
- **Input Processing**: Line-based command parsing with EOF support
- **Performance**: O(1) for GET/SET/UNSET operations

## Limitations
- No persistent storage between sessions
- No support for spaces in keys/values
- Single-threaded implementation
- No network access or remote connections


# TODO
2. Зависимости проекта: В решении присутствуют сторонние библиотеки, которые не добавляют существенной ценности к решению задачи. Код успешно работает без использования typer, что указывает на избыточность данной зависимости.

3. Функциональные ошибки:
- Некорректная работа с транзакциями (неправильное поведение после COMMIT)
- Ошибки в обработке команд (COUNTS вместо COUNT)
- Отсутствие обработки EOFError
- Некорректная работа команды UNSET

4. Архитектурные решения: Код демонстрирует избыточную сложность для поставленной задачи, что затрудняет его понимание и поддержку.
