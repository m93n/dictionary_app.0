# Dictionary App

A simple Python-based dictionary application using SQLite and JSON for data handling.

## Features
- Add and search words.
- Store dictionary data in a SQLite database.

## Requirements
- Python 3.x
- SQLite3

## Installation
1. Clone the repository:
  ```
  git clone https://github.com/m93n/dictionary_app.0.git
  ```
   
## Usage
1. Run the app:
  ```
  python INSERT_dictionry.py
  python dictionary_app.py
  ```
2. Search for a word:
> Enter a word to retrieve its meaning

## JSON Data Import
- The app extracts dictionary data from a `data.json` file, which stores word definition pairs.
- Ensure the file follows the structure:
  ```
  {
   "word": ["definition", ...],
   "another_word": ["another_definition", ...]
  }
  ```

## Database (SQLite)
- The SQLite database (`dictionary.db`) stores the word and its definition.
- Basic SQL commands are used for adding and searching data.

## Contribution
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make changes and commit.
4. Open a pull request.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This project is licensed under the MIT License. See the [LICENSE](https://github.com/m93n/dictionary_app.0/blob/master/LICENSE) file for more details.



