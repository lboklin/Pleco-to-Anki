from pleco.Bookmarks import Bookmarks
from pleco.definition_helpers import *

import time

# TODO: Add dependencies to requirements.txt
# TODO: Add tests
# TODO: wrap project in Anki add-on

def main():

    bookmarks = Bookmarks(FILE_NAME)

    if REFORMAT_PINYIN:
        bookmarks.reformat_pinyin()

    bookmarks.build_english_and_definition_fields()

    if SPOONFED_EXAMPLES:
        print('Adding Spoonfed examples...')
        start_time = time.time()
        bookmarks.add_spoonfed_sentences()
        end_time = time.time()
        print('Runtime of Spoonfed lookups: ' + str(round(end_time - start_time, 1)) + 's')

    bookmarks.export_to_csv()

if __name__ == "__main__":
    main()