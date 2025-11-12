# NLP Cheatsheet — Hemant's Study README

> **Purpose:** A compact, memory-friendly, Krish Naik–style README that summarizes all NLP concepts you've learned so far (Tokenization → Avg Word2Vec). Each section contains short definitions, intuition, code examples (NLTK / sklearn / gensim), tips, and quick exercises so when you re-open this file you remember and understand the concept completely.

---

## Table of Contents
1. Quick setup (packages & NLTK downloads)
2. Text preprocessing
   - Tokenization
   - Lowercasing & cleaning
   - Stopword removal
   - Stemming
   - Lemmatization
3. POS Tagging
4. Named Entity Recognition (NER)
5. Text vectorization (text → numbers)
   - One-Hot Encoding
   - Bag of Words (BoW)
   - N-grams
   - TF–IDF
6. Word embeddings
   - Word Embedding intuition
   - Word2Vec (CBOW & Skip-Gram)
   - Average Word2Vec (sentence-level)
7. Common pitfalls & tips
8. Small projects / exercises
9. References & next steps

---

## 1) Quick setup

Install common packages (run once):

```bash
pip install nltk scikit-learn gensim spacy
python -m spacy download en_core_web_sm
```

NLTK downloads (inside Python):

```python
import nltk
nltk.download('punkt')                  # tokenizers
nltk.download('stopwords')              # stopword list
nltk.download('wordnet')                # lemmatizer dictionary
nltk.download('omw-1.4')                # wordnet extras
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

Keep these handy — many examples below assume these are available.

---

## 2) Text preprocessing

### Tokenization
**Definition:** Splitting raw text into smaller units (tokens): words, sentences, or subwords.

**Why:** It's the first step; everything else uses tokens.

**NLTK example:**

```python
from nltk.tokenize import word_tokenize, sent_tokenize
text = "I love learning Data Science with Krish Naik. NLP is fun!"
print(sent_tokenize(text))
print(word_tokenize(text))
```

**Tip:** Use sentence tokenization before downstream steps like NER or POS tagging so context is preserved.

---

### Lowercasing & cleaning
**Definition:** Convert text to lowercase, remove punctuation, special chars, URLs, or digits (as needed).

**Why:** Normalize text and reduce vocabulary size.

**Simple example:**

```python
import re
text = "Hello, WORLD! Visit: https://example.com"
clean = re.sub(r'http\S+|[^a-zA-Z\s]', '', text.lower()).strip()
# -> 'hello world visit'
```

**Caution:** Keep capitalization if it matters (proper nouns, NER tasks, sentiment with emphasis).

---

### Stopword removal
**Definition:** Removing high-frequency words that add little semantic value ("is", "the", "a").

**NLTK example:**

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
text = "I am learning Natural Language Processing with Hemant"
filtered = [w for w in word_tokenize(text) if w.lower() not in stop_words]
```

**Practical tip:** Customize stopwords — keep negatives like `not` when doing sentiment analysis.

---

### Stemming
**Definition:** Reduce words to a base/stem by chopping suffixes (may not produce valid words).

**Common stemmers:** Porter, Lancaster, Snowball.

**NLTK example:**

```python
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
words = word_tokenize("playing played plays study studies")
[ps.stem(w) for w in words]
# -> ['play', 'play', 'play', 'studi', 'studi']
```

**When to use:** Fast, useful for IR/search or tasks where exact dictionary form isn't needed.

---

### Lemmatization
**Definition:** Convert words to dictionary/base form (lemma) using POS tags (more accurate than stemming).

**NLTK example:**

```python
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

text = "The children are playing and studies were done"
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
lemmas = [lemmatizer.lemmatize(t, get_wordnet_pos(p)) for t, p in pos_tags]
```

**Tip:** Always use POS when you want correct lemmatization for verbs/adjectives.

---

## 3) POS Tagging (Part-of-Speech)

**Definition:** Label each token with its grammatical role (NN, VB, JJ, RB, etc.).

**Why:** Useful for lemmatization, NER improvements, syntax-aware features.

**NLTK example:**

```python
from nltk import pos_tag
from nltk.tokenize import word_tokenize
text = "Hemant loves coding in Python"
pos = pos_tag(word_tokenize(text))
print(pos)
# [('Hemant','NNP'), ('loves','VBZ'), ('coding','VBG'), ('in','IN'), ('Python','NNP')]
```

**Use:** extract only nouns or verbs as features, feed POS info to lemmatizer.

---

## 4) Named Entity Recognition (NER)

**Definition:** Identify and classify proper nouns in text into types: PERSON, ORG, GPE, DATE, MONEY, etc.

**NLTK (baseline) example:**

```python
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
text = "Elon Musk founded SpaceX in 2002 in the United States."
tokens = word_tokenize(text)
pos = pos_tag(tokens)
ner_tree = ne_chunk(pos)
ner_tree.pprint()
```

**spaCy (recommended for production):**

```python
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Elon Musk founded SpaceX in 2002 in the United States.")
for ent in doc.ents:
    print(ent.text, ent.label_)
```

**Tip:** spaCy gives higher-quality, fast NER out-of-the-box; use NLTK for learning and visualization.

---

## 5) Text vectorization (text → numbers)

### One-Hot Encoding
**Definition:** Each category/word turned into a binary vector with 1 at that word's index and 0 elsewhere.

**scikit-learn example:**

```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np
enc = OneHotEncoder(sparse_output=False)
colors = np.array([['Red'], ['Blue'], ['Green']])
enc.fit_transform(colors)
```

**Limitation:** High dimensionality; not suitable for large vocabularies.

---

### Bag of Words (BoW)
**Definition:** Represent document as a vector of word counts over the vocabulary (ignores order).

**sklearn example:**

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    "I love Data Science",
    "I love Machine Learning",
    "Data Science is fun"
]
cv = CountVectorizer()
X = cv.fit_transform(corpus)
print(cv.get_feature_names_out())
print(X.toarray())
```

**Use:** Simple baseline for classification and clustering. Combine with N-grams to include short context.

---

### N-grams
**Definition:** Sequences of N consecutive words (unigram, bigram, trigram). Capture short local order.

**sklearn usage (unigrams + bigrams):**

```python
cv = CountVectorizer(ngram_range=(1,2))
X = cv.fit_transform(corpus)
print(cv.get_feature_names_out())
```

**Tip:** Use (1,2) or (1,3) for many tasks. Beware feature explosion.

---

### TF–IDF
**Definition:** Weight words by Term Frequency (TF) and Inverse Document Frequency (IDF) → importance per corpus.

**sklearn example:**

```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
print(X_tfidf.toarray())
```

**Pros:** Reduces weight of common words. Works well with linear models.
**Cons:** Ignores context; high-dimensional sparse vectors.

---

## 6) Word embeddings

### Word Embedding Intuition
**Definition:** Dense, low-dimensional vectors for words where semantic relationships map to geometric relationships (similar words are nearby).

**Key idea:** Distributional hypothesis — "you shall know a word by the company it keeps".

---

### Word2Vec (CBOW & Skip-Gram)
**Definition:** Neural models that learn word embeddings by predicting target from context (CBOW) or context from target (Skip-Gram).

**Gensim example (train fast):**

```python
from gensim.models import Word2Vec
sentences = [
    ["i","love","data","science"],
    ["data","science","is","fun"],
    ["i","enjoy","machine","learning"],
]
# Skip-Gram (sg=1), CBOW (sg=0)
model_sg = Word2Vec(sentences, vector_size=50, window=2, min_count=1, sg=1)
model_cb = Word2Vec(sentences, vector_size=50, window=2, min_count=1, sg=0)
# vector for word
vec_data = model_sg.wv['data']
# most similar
print(model_sg.wv.most_similar('learning'))
```

**Parameter notes:**
- `vector_size` (embedding dim): 50–300 common
- `window`: context window size (2–5 typical)
- `min_count`: ignore rare words below this count
- `sg`: 1 -> skip-gram, 0 -> CBOW

**CBOW vs Skip-Gram:**
- CBOW: faster, better for small datasets, predicts target from context.
- Skip-Gram: slower, better for rare words & large datasets, predicts context from target.

**Common vector trick:** `king - man + woman ≈ queen`

---

### Average Word2Vec (sentence/document representation)
**Definition:** Compute the mean (average) of word vectors in a sentence/document to get one fixed-size vector.

**Why:** ML models require fixed-size inputs; averaging is simple and effective baseline.

**Example:**

```python
import numpy as np

def avg_word2vec(sentence_tokens, model):
    vecs = [model.wv[w] for w in sentence_tokens if w in model.wv]
    if len(vecs)==0:
        return np.zeros(model.vector_size)
    return np.mean(vecs, axis=0)
```

**Pros:** Fast, simple, works well for many tasks.
**Cons:** Loses word order and fine-grained context (negations, sequence info).

---






