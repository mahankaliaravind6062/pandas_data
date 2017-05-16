import string

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer, EnglishStemmer
from sklearn.base import TransformerMixin
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfHelper(TransformerMixin):
    def __init__(self, path_to_tf=None, lang="french", stemmer=False, stop_words=False,
                 remove_integer=True, min_df=0.1, max_df=0.9):
        self.args = {}
        if path_to_tf:
            self.tfidf = joblib.load(path_to_tf)
        else:
            self.tfidf = None
        if stop_words:
            self.stopwords = stopwords.words('french')
            self.args["stop_words"] = self.stopwords
        if stemmer:
            self.stemmers = {
                "french": FrenchStemmer,
                "english": EnglishStemmer
            }
            self.args["tokenizer"] = self.tokenize

        self.args["min_df"] = min_df
        self.args["max_df"] = max_df
        self.lang = lang
        self.remove_integer = remove_integer

    def add_tfidf_on_dataframe(self, df_, column_desciption, suffix="", **args):
        """

        :param df_:
        :param column_desciption:
        :param suffix:
        :param args:
        :return:
        """
        if not self.tfidf:
            self.tfidf = TfidfVectorizer(args)
        df_tf_idf = pd.DataFrame(self.tfidf.fit_transform(df_[column_desciption]).toarray(),
                                 columns=[suffix + elt for elt in self.tfidf.get_feature_names()])
        return df_.join(df_tf_idf)

    def transform(self, X, **transform_params):
        """

        :param X:
        :param transform_params:
        :return:
        """
        return self.add_tfidf_on_dataframe(X)

    def fit(self, X, y=None, **fit_params):
        return self

    def tokenize(self, text):
        """

        :param text:
        :return:
        """
        stemmer = self.stemmers[self.lang]()
        text = "".join([ch for ch in text if ch not in string.punctuation])
        tokens = nltk.word_tokenize(text)
        stems = self.stem_tokens(tokens, stemmer)
        return stems

    def stem_tokens(self, tokens, stemmer):
        """

        :param tokens:
        :param stemmer:
        :return:
        """
        stemmed = []
        is_not_integer = lambda s: not s.isdigit()
        for item in tokens:
            stemmed.append(stemmer.stem(item))
        if self.remove_integer:
            return list(filter(is_not_integer, stemmed))
        else:
            return stemmed


if __name__ == "__main__":
    df = pd.DataFrame({'A': [1, 2, 3, 4],
                       'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                       'E': ["tester train train, train tester test",
                             "train train trainer train", "test test test",
                             "train train"],
                       'F': 'foo'})
    tf = TfidfHelper()
    print(tf.add_tfidf_on_dataframe(df, column_desciption="E", suffix="tf_"))
