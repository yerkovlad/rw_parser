import json

def json_dump(input_list:list, file_name:str)->None:
    """
    Saving list with dict to json file
    ---------------------------------------------
    |list(input_list) - list with dict to save  |
    |str(file_name)   - file name to save       |
    |return           - None                    |
    ---------------------------------------------
    """
    with open(file_name, 'w', encoding='utf-8') as fl:
        json.dump(input_list, fl, indent=2, ensure_ascii=False)