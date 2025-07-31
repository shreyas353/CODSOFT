import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk, messagebox

# Sample movie data
data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight',
        'Pulp Fiction', 'Fight Club', 'The Prestige', 'Memento',
        'The Shawshank Redemption', 'Forrest Gump'
    ],
    'genre': [
        'Sci-Fi Action', 'Sci-Fi Thriller', 'Sci-Fi Drama', 'Action Crime',
        'Crime Drama', 'Drama Thriller', 'Mystery Drama', 'Mystery Thriller',
        'Drama', 'Comedy Drama'
    ],
    'keywords': [
        'hacker reality future', 'dream heist subconscious', 'space time blackhole',
        'batman joker chaos', 'mob hitmen redemption', 'underground fight club',
        'magic rivalry illusion', 'memory loss revenge', 'prison escape hope',
        'life journey simplicity'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Combine features
def combine_features(row):
    return f"{row['genre']} {row['keywords']}"

df['combined'] = df.apply(combine_features, axis=1)

# Vectorize text
vectorizer = CountVectorizer().fit_transform(df['combined'])
similarity = cosine_similarity(vectorizer)

# Get movie index
def get_index(title):
    for i, t in enumerate(df['title']):
        if title.lower() in t.lower():
            return i
    return None

# Recommendation function
def recommend(title, n=5):
    idx = get_index(title)
    if idx is None:
        return []
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    return [df['title'][i[0]] for i in scores]

# GUI
def get_recommendations():
    selected_movie = movie_var.get()
    if not selected_movie:
        messagebox.showwarning("Input Error", "Please select or enter a movie.")
        return
    result = recommend(selected_movie)
    if result:
        result_var.set("\n".join(result))
    else:
        result_var.set("Movie not found. Try another.")

root = tk.Tk()
root.title("Movie Recommender")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Select or type a movie:", font=("Arial", 13)).pack(pady=10)
movie_var = tk.StringVar()
movie_dropdown = ttk.Combobox(root, textvariable=movie_var, values=list(df['title']), font=("Arial", 12), width=30)
movie_dropdown.pack()

tk.Button(root, text="Recommend", font=("Arial", 12), command=get_recommendations).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, text="Recommendations:", font=("Arial", 13)).pack()
tk.Label(root, textvariable=result_var, font=("Arial", 12), justify="left", wraplength=350).pack(pady=10)

root.mainloop()