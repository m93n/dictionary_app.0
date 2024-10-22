# Dictionary App

A simple Python-based dictionary application using SQLite and JSON for data handling.

## Features
- Add, search, and delete words.
- Store dictionary data in a SQLite database.
- JSON extraction for data import.

## Requirements
- Python 3.x
- SQLite3

## Installation
1. Clone the repository:
  ```
  git clone https://github.com/m93n/dictionary_app.0.git
  ```
2. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
   
## Usage
1. Run the app:
  ```
  python main.py
  ```
2. Search for a word:
>Enter a word to retrieve its meaning

## JSON Data Import
- The app extracts dictionary data from a `data.json` file, which stores word definition pairs.
- Ensure the file follows the structure:
  ```
  {
   "word": "definition",
   "another_word": "another_definition"
  }
  ```

## Database (SQLite)
- The SQLite database (`dictionary.db`) stores the word and its definition.
- Basic SQL commands are used for adding and searching data.
- Example for querying the database:
  ```
  SELECT * FROM words WHERE word='example';
  ```

## Testing
1. Run unit tests:
  ```
  python -m unittest discover
  ```

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make changes and commit.
4. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.




