from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

class DataNotAvailable(Exception):
    pass
class EtymologyNotAvailable(Exception):
    pass
class DefinitionsNotAvailable(Exception):
    pass 

def fetch_word(word, language="Ancient Greek"):
   return parser.fetch(word, language)

def fetch_group_as_string(group, single_list=False):
    """
    Transforma grupo de strings em uma lista em uma só string.
    Deste modo, o arquivo .csv final não fica cheio
    de colchetes.
    """

    strings = ""
    if single_list==True:
        for i in range(len(group)): 
            strings+=group[i]
            if i < (len(group) - 1): 
                strings+="\n"
        return strings
    else:
        for i in range(len(group)):
            for j in range(len(group[i])):
                strings+=group[i][j]
                if (j == 0):
                    strings+="\n\n"
                else:
                    strings+="\n"
            if (i < len(group)-1):
                strings+="\n"

        return strings


class WordBase:
    def extract_item(self, word, selection):
        if word[0] != []:
            if word[0][selection]:
               return word[0][selection]
        else:
            raise DataNotAvailable

class Word(WordBase):
    def __init__(self, name):
        self.name = name
        self.data = fetch_word(name)
        self.definitions = self.get_definitions()
         
    def get_etymology(self):
        try:
            etymology = super().extract_item(self.data, "etymology")
            if (not etymology) or (etymology == []):
                raise EtymologyNotAvailable
            return etymology
        except EtymologyNotAvailable:
            print("{}: Etymology not available.".format(self.name)) 

    def get_definitions(self):
        try:
            definitions = super().extract_item(self.data, "definitions")
            if (not definitions) or (definitions == []):
                raise DefinitionsNotAvailable 
            return definitions 
        except DefinitionsNotAvailable:
            print("Definitions not available.")

    def get_word_class(self):
        if self.definitions is not None:
            return fetch_group_as_string([item['partOfSpeech'] for item in self.definitions], single_list=True)
        else:
            return ""

    def get_text(self):
        if self.definitions is not None:
            return fetch_group_as_string([item['text'] for item in self.definitions])
        else:
            return ""

    def get_related_words(self):
        if self.definitions is not None:
            try:
                related_words_dict = [item['relatedWords'] for item in self.definitions]
                return fetch_group_as_string(related_words_dict[0][0]["words"], single_list=True)
            except IndexError:
                return ""
        else: 
            return ""

    def get_examples(self):
        if self.definitions is not None:
            return fetch_group_as_string([item['examples'] for item in self.definitions])
        else:
            return ""