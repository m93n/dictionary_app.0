import sqlite3
import json
from pathlib import Path

current_path = str(Path().absolute())
data = Path(current_path + "\data.json").read_text()

dictionries = json.loads(data)

with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    command_Insert_word = "INSERT INTO DictionaryWord VALUES(?,?)"
    command_Insert_translation = "INSERT INTO DictionaryTranslation VALUES(?,?,?)"

    command_table_word = """
        CREATE TABLE if NOT EXISTS "DictionaryWord" (
            "id"	INTEGER,
            "word"	TEXT NOT NULL,
            PRIMARY KEY("id")
        );
    """

    command_table_translation = """
        CREATE TABLE if NOT EXISTS "DictionaryTranslation" (
            "id"	INTEGER,
            "translation_text"	TEXT NOT NULL,
            "word_id"	INTEGER,
            FOREIGN KEY("word_id") REFERENCES "DictionaryWord"
        );
    """

    cursor.execute(command_table_word)
    cursor.execute(command_table_translation)

    word_id = 1
    translation_id = 1

    for word in dictionries:

        #insrt word to db
        cursor.execute(command_Insert_word, (word_id, word))
        
        for translation in dictionries[word]:

            #insert translation to db
            cursor.execute(command_Insert_translation, (translation_id, translation, word_id))

            translation_id += 1
        
        word_id += 1

    conn.commit()
        
