import sqlite3

def get_user_input():
    word = input("insert a word for translate: \n")
    return word


def search_in_deictionary(word):
    try:
        with sqlite3.connect("myapp.db") as conn:
            cursor = conn.cursor()
            command_select_word = f"SELECT id FROM DictionaryWord WHERE word=?"
            cursor.execute(command_select_word, (word,))
            word_id = cursor.fetchall()[0][0]

            command_select_translatoions = f"SELECT translation_text FROM DictionaryTranslation WHERE word_id={word_id}"
            cursor.execute(command_select_translatoions)
            translations = cursor.fetchall()

            print("\"\"\"")
            for translation in translations:
                print("- " + translation[0])
            
            print("\n\"\"\"")
    except:
        print("The search has no result!")



word = get_user_input()
search_in_deictionary(word)

