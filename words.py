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

class WordBase:
    def extract_item(self, word, selection):
        if word[0] != []:
            if word[0][selection]:
               return word[0][selection]
        else:
            raise DataNotAvailable

class Word(WordBase):
    def __init__(self, name):
        self.data = fetch_word(name)
        self.definitions = self.get_definitions()
         
    def get_etymology(self):
        try:
            etymology = super().extract_item(self.data, "etymology")
            if (not etymology) or (etymology == []):
                raise EtymologyNotAvailable
            return etymology
        except EtymologyNotAvailable:
            print("Etymology not available.") 

    def get_definitions(self):
        try:
            definitions = super().extract_item(self.data, "definitions")
            if (not definitions) or (definitions == []):
                raise DefinitionsNotAvailable 
            return definitions 
        except DefinitionsNotAvailable:
            print("Definitions not available.")

    def get_word_class(self):
        return self.definitions[0]['partOfSpeech']

    def get_text(self):
        return self.definitions[0]['text']

    def get_related_words(self):
        return self.definitions[0]['relatedWords'] 

    def get_examples(self):
        return self.definitions[0]['examples'] 