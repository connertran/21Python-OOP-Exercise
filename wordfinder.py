from random import randint
"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("word2.txt")
    4 words read

    >>> wf.random() in ["hi", "one", "two", "three"]
    True

    >>> wf.random() in ["hi", "one", "two", "three"]
    True

    >>> wf.random() in ["hi", "one", "two", "three"]
    True
    """
    def __init__(self, file_name):
        """searching for file
        file_name has to be in this form: python-oo-practice/[file_name]"""
        self.file = file_name
        self.words_list = []
        self.read_lines_from_file()
        
        print(f'{self.get_words_count()} words read')

    def read_lines_from_file(self):
        with open(self.file) as file:
            self.words_list = [line.strip() for line in file]

    def get_words_count(self):
        """To check how many items are in the list"""
        return len(self.words_list)

    def random(self):
        """using randint from random to chose a random item from the list"""
        list_length = self.get_words_count()
        random_index = randint(0, list_length - 1)
        return self.words_list[random_index]


class SpecialWordFinder(WordFinder):
    """Machine for finding random words from dictionary.
    This is a subclass of class WordFinder
    This class doesn't read comments or empty lines
    
    >>> swf = SpecialWordFinder("word3withcomments.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    def read_lines_from_file(self):
        with open(self.file) as file:
            self.words_list = [line.strip() for line in file if line.strip() and line[0] != '#']
        
wf = WordFinder("word2.txt")
print(wf.random() in ["hi", "one", "two", "three"])
print(wf.random())
print(wf.random())
print(wf.random())
swf = SpecialWordFinder("word3withcomments.txt")
print(swf.random() in ["kale", "parsnips", "apple", "mango"])
print(swf.random())
print(swf.random())
print(swf.random())
