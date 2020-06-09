import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import spacy
from langdetect import DetectorFactory, detect
from nltk import FreqDist
from nltk.corpus import stopwords
from wordcloud import STOPWORDS, WordCloud

nlp = spacy.load('en', disable=['parser', 'ner'])
stop_words = stopwords.words('english')

DetectorFactory.seed = 42

def create_final_dataset(
    df1: pd.DataFrame, df2: pd.DataFrame, df3: pd.DataFrame
) -> pd.DataFrame:
    """Merge three datasets using outer joins and drop any
    missing values.

    Args:
        df1 (pd.Dataframe): dataframe containing reviews and book IDs
        df2 (pd.Dataframe): dataframe containing book authors, titles and ISBNs
        df3 (pd.Dataframe): dataframe containing book genre information

    Returns:
        A complete dataset will all relevant book information
    """
    df1.pop("stars")
    df1["user"] = df1.user.fillna("unknown")
    df1 = df1.dropna()

    # combine first two dataframes
    book_info_reviews = pd.merge(df1, df2, on="id", how="outer")
    book_info_reviews = book_info_reviews.dropna()

    df3.pop("goodreads_shelves")
    df3["book_genres"] = (
        df3.book_genres.str.replace("[", "")
        .str.replace("]", "")
        .str.replace("'", "")
        .str.replace(" ", "")
    )
    categories = df3.book_genres.str.split(",", expand=True)
    categories.columns = ["genre_1", "genre_2", "genre_3"]
    df3["book_genres"] = categories.genre_1

    # combine remaining dataframes
    book_info_reviews_genres = pd.merge(book_info_reviews, df3, on="id", how="outer")
    book_info_reviews_genres = book_info_reviews_genres.dropna()
    book_info_reviews_genres = book_info_reviews_genres[
        [
            "reviews",
            "n_helpful",
            "time",
            "user",
            "id",
            "book_title",
            "author",
            "isbn_x",
            "book_genres",
        ]
    ]
    return book_info_reviews_genres.rename(columns={"isbn_x": "isbn"})


def detect_language(text: str) -> str:
    """ Use Google Translate API to detect
    the language in a string

    Args:
        text (str): text whose language needs
            to be determined

    Returns:
        The language code corresponding to the
            language the text is in. If a language
            can't be detected, returns None.
    """
    try:
        return detect(text)
    except Exception:
        return ""


def generate_wordcloud(df: pd.DataFrame, book_genre: str) -> None:
    """Removes stopwords then creates a wordcloud from book reviews

    Args:
        book_genre (str): book genre reviews correspond to
    """
    stopwords = set(STOPWORDS)
    stopwords.update(['one', 'much', 'still', 'novel', 'book', 'even', 'though', 'really', 'now', 'come', 
                      'work', 'thing', 'way', 'rather', 'made', 'will', 'bit', 'left', 'make', 'read',
                      'think', 'book', 'find', 'know', 'lot', 'found', 'another', 'page', 'first', 'part', 'take', 
                      'thing', 'many', 'give', 'make', 'quite', 'although', 'see', 'yet'])
    text = " ".join(review for review in df.reviews[df.book_genres == book_genre])

    wordcloud = WordCloud(stopwords=stopwords, background_color='white', width=800, height=400, max_words=100).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(book_genre)
    plt.axis('off')
    return None


def generate_word_counts_fig(x, terms = 30):
    all_words = ' '.join([text for text in x])
    all_words = all_words.split()

    fdist = FreqDist(all_words)
    words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})

    # selecting top 20 most frequent words
    d = words_df.nlargest(columns="count", n = terms) 
    plt.figure(figsize=(20,5))
    ax = sns.barplot(data=d, x= "word", y = "count")
    ax.set(ylabel='Count')


def remove_stopwords(rev):
    rev_new = " ".join([i for i in rev if i not in stop_words])
    return rev_new


def lemmatize_text(texts, tags=['NOUN', 'ADJ']):
    output = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        output.append([token.lemma_ for token in doc if token.pos_ in tags])
    return output


def plot_word_frequency(reviews):
    reviews = reviews.str.replace("n\'t", " not")
    reviews = reviews.str.replace("[^a-zA-Z#]", " ")
    reviews = reviews.apply(lambda x: ' '.join([w for w in x.split() if len(w) > 2]))
    reviews = [remove_stopwords(r.split()) for r in reviews]
    reviews = [r.lower() for r in reviews]

    tokenized_reviews = pd.Series(reviews).apply(lambda x: x.split())
    lemma_reviews = lemmatize_text(tokenized_reviews)
    clean_reviews = []
    for i in range(len(lemma_reviews)):
        clean_reviews.append(' '.join(lemma_reviews[i]))

    clean_series = pd.Series(clean_reviews)
    return generate_word_counts_fig(clean_series)
