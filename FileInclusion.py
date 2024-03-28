import os

# pre spustenie musime mat dane subory a vytvorenu cestu
ALLOWED_FUNC = {'djikstra.py', 'sort.py', 'fibonaci.py'}
BASE_DIRECTORY = '/path/to/secure/func/'

def load_template_safe(filename):
    # kontrola ci sa filename nachadza v zozname povolenych funkcii
    if filename in ALLOWED_FUNC:
        filepath = os.path.join(BASE_DIRECTORY, filename)
        # podmienka kontroluje ci sa subor nachadza vramci based directory
        if os.path.commonpath([BASE_DIRECTORY]) == os.path.commonpath([BASE_DIRECTORY, filepath]):
            try:
                with open(filepath, 'r') as file:
                    return file.read()
            except IOError:
                return "Function not found."
    return "Access denied."


content = load_template_safe('djikstra.py')
