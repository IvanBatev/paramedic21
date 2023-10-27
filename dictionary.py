import json
import tkinter

class DictionaryData:

    def __init__(self,dictionary_file):   
        # Reads json file and returns a full dictionary of entries
        with open(dictionary_file, encoding="utf8") as dict_file:
            self.full_dict = json.load(dict_file)
        
    def filter_full_dictionary(filters_category, filters_lections, full_dict, latin_only):
        filtered_dict = {'filtered_dictionary':[]}
        
        for entry in full_dict['dictionary']:
            for key, value in entry.items():
                if value in filters_category or value in filters_lections:
                    if latin_only.get() == 0:
                        if entry not in filtered_dict['filtered_dictionary']:
                            filtered_dict['filtered_dictionary'].append(entry)
                    else:
                        if entry not in filtered_dict['filtered_dictionary'] and entry['latin'] != "":
                            filtered_dict['filtered_dictionary'].append(entry)


        return filtered_dict

    def clear_text_field(self):
        pass


    def answer(self):
        pass