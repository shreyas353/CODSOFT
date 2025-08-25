import tkinter as tk
from tkinter import ttk, messagebox
import math

# Book data
titles = [
    'Harry Potter', 'The Lord of the Rings', 'The Da Vinci Code',
    'To Kill a Mockingbird', 'The Great Gatsby',
    '1984', 'Pride and Prejudice', 'Moby Dick',
    'War and Peace', 'The Alchemist'
]

genres = [
    'Fantasy Magic', 'Fantasy Adventure', 'Mystery Thriller',
    'Classic Drama', 'Classic Romance',
    'Dystopian Political', 'Romance Classic', 'Adventure Sea',
    'Historical War', 'Philosophy Adventure'
]

keywords = [
    'wizard magic school', 'ring power journey',
    'murder mystery symbols', 'justice childhood racism',
    'wealth love tragedy', 'totalitarian society control',
    'love manners society', 'whale captain revenge',
    'russia napoleon family', 'dreams destiny spirituality'
]

# Combine features
combined_data = [f"{genres[i]} {keywords[i]}" for i in range(len(titles))]

# Tokenize vocabulary
def build_vocabulary(data):
    vocab = set()
    for doc in data:
        for word in doc.lower().split():
            vocab.add(word)
    return sorted(list(vocab))

vocab = build_vocabulary(combined_data)

# Convert text to vector
def text_to_vector(text):
    words = text.lower().split()
    vector = [words.count(word) for word in vocab]
    return vector

# Cosine similarity
def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (mag1 * mag2) if mag1 and mag2 else 0.0

vectors = [text_to_vector(doc) for doc in combined_data]

def get_index(title):
    for i, t in enumerate(titles):
        if title.lower() in t.lower():
            return i
    return None

def recommend(title, n=5):
    idx = get_index(title)
    if idx is None:
        return []
    target_vec = vectors[idx]
    scores = []
    for i, vec in enumerate(vectors):
        if i != idx:
            sim = cosine_similarity(target_vec, vec)
            scores.append((i, sim))
    scores.sort(key=lambda x: x[1], reverse=True)
    return [titles[i] for i, _ in scores[:n]]

# GUI
def get_recommendations():
    selected_book = book_var.get()
    if not selected_book:
        messagebox.showwarning("Input Error", "Please select or enter a book.")
        return
    result = recommend(selected_book)
    if result:
        result_var.set("\n".join(result))
    else:
        result_var.set("Book not found. Try another.")

root = tk.Tk()
root.title("Book Recommender")

# Make window full screen
root.state("zoomed")  # For Windows
# root.attributes("-fullscreen", True)  # Alternative, works on all OS

# Heading
tk.Label(root, text="📚 Book Recommendation System", font=("Arial", 20, "bold")).pack(pady=20)

# Input field
book_var = tk.StringVar()
tk.Label(root, text="Select or type a book:", font=("Arial", 15)).pack(pady=10)
book_dropdown = ttk.Combobox(root, textvariable=book_var, values=titles, font=("Arial", 14), width=50)
book_dropdown.pack(pady=5)

# Button
tk.Button(root, text="🔍 Recommend", font=("Arial", 14, "bold"), command=get_recommendations, bg="lightblue").pack(pady=20)

# Results
result_var = tk.StringVar()
tk.Label(root, text="Recommendations:", font=("Arial", 15, "underline")).pack(pady=10)
tk.Label(root, textvariable=result_var, font=("Arial", 14), justify="left", wraplength=1000).pack(pady=10)

root.mainloop()
