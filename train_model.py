import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\resume_ai\UpdatedResumeDataSet.csv")

X = df["Resume"]
y = df["Category"]

tfidf = TfidfVectorizer(stop_words="english")

X_vec = tfidf.fit_transform(X)

model = LogisticRegression(max_iter=1000)

model.fit(X_vec,y)

os.makedirs("models",exist_ok=True)

pickle.dump(model,open("models/model.pkl","wb"))
pickle.dump(tfidf,open("models/tfidf.pkl","wb"))


