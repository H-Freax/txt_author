import toolz
import re, itertools
from glob import iglob

def word_ratio(d):
    return float(d.get("a",0))/float(d.get("the",0.0001))

class PoemCleaner:
    def __init__(self):
        self.r = re.compile(r'[.,;:!-]')
    def clean_poem(self, fp):
        with open(fp,encoding='gb18030', errors='ignore') as poem:
            no_func = self.r.sub("",poem.read())
            return no_func.lower().split()

def word_is_desired(w):
    if w in ["a","the"]:
        return True
    else:
        return False

def analyze_poems(poems, cleaner):
    return word_ratio(
        toolz.frequencies(
            filter(word_is_desired,
                itertools.chain(*map(cleaner.clean_poem,poems)))
        )
    )

if __name__ == "__main__":
    cleaner = PoemCleaner()
    author1_poems = iglob("author_one/*.txt")
    author2_poems = iglob("author_two/*.txt")

    author1_ratio = analyze_poems(author1_poems, cleaner)
    author2_ratio = analyze_poems(author2_poems, cleaner)

    print("""
    Original_Poem: 0.3
    Author One:    {:.2f}
    Author Two:    {:.2f}
    """.format(author1_ratio, author2_ratio))