import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()

        for file_i in self.file_names:
            with open(file_i, encoding="utf8") as file:
                text = file.read()
                temp_list = re.split(r'[,.=!?\n; :]+', text)
                all_words[str(file_i)] = temp_list

        return all_words

    def find(self, word):
        dict_list = self.get_all_words()
        result_dict = dict()

        for file_name, word_list in dict_list.items():
            word_list_temp = [wrd.lower() for wrd in word_list]

            try:
                result_dict[str(file_name)] = (word_list.index(word.lower())) + 1
            except:
                result_dict[str(file_name)] = 'Искомого слова нет'

            del word_list_temp

        return result_dict

    def count(self, word):
        dict_list = self.get_all_words()
        result_dict = dict()

        for file_name, word_list in dict_list.items():
            word_list_temp = [wrd.lower() for wrd in word_list]
            result_dict[str(file_name)] = word_list_temp.count(word.lower())

        del word_list_temp

        return result_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
