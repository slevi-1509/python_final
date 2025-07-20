from enum import Enum, auto

class Menu(Enum):
    SAVE_NEW_ENTRY = '1'
    SEARCH_BY_ID = '2'
    PRINT_AGES_AVERAGE = '3'
    PRINT_ALL_NAMES = '4'
    PRINT_ALL_IDS = '5'
    PRINT_ALL_ENTRIES = '6'
    PRINT_ENTRY_BY_INDEX = '7'
    SAVE_DATA_TO_FILE = '8'
    IMPORT_DATA_FROM_FILE = '9'
    EXIT = '0'