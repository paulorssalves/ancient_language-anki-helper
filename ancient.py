from words import Word 
import pandas as pd


if __name__ == "__main__":
    f = pd.read_csv("logoi.csv", header=None, 
                    names=["word(s)"])

    head = f.head(20)

    for cell in head.iteritems():
        for word in cell[1]:

            current = Word(word)

            words_data = {
                "names":current.name,
                "etymologies":current.get_etymology(),
                "word_class":current.get_word_class(),
                "text":current.get_text(),
                "related_words":current.get_related_words(),
                "examples":current.get_examples()
            }

            words_dataframe = pd.DataFrame.from_dict(words_data, orient="index")
            words_dataframe = words_dataframe.transpose()
            words_dataframe.to_csv("out.csv",encoding="utf-8",mode="a",header=False, index=False)