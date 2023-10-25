import json

class DictionaryData:
    
    def __init__(self,dictionary_file):       
        # Reads json file and returns a full dictionary of entries
        with open(dictionary_file, encoding="utf8") as dict_file:
            self.full_dict = json.load(dict_file)
        
    def create_subdictionaries(filters_category, filters_lections, full_dict):
        print(filters_category)
        print(filters_lections)
        print()
        # for entry in full_dict['dictionary']:
        #     print ()


    # def create_subdictionary(self,full_dict, criteria):
        
    #     criteria_dict = dict()
    #     for entry in full_dict['dictionary']:
    #         for key, value in entry.items():
    #             if key == 'category' and value == 'аnatomy':
    #                 criteria_dict.update(entry)
    #             elif key == 'lection' and value == '1 - Въведение в анатомията':
    #                 criteria_dict.update(entry)
        
    #     return criteria_dict


    def clear_text_field(self):
        pass


    def ask(self):
        print("Lookup")
        pass
        self.clear_text_field()


    def answer(self):
        pass