import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import tensorflow as tf

# Load data
data = pd.read_csv('data/specific_data.csv')

X = data['intent']
y = data['specific_data']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X).toarray()

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split (optional - or just train fully)
# X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y_encoded, test_size=0.2)

# Build simple model
model = Sequential([
    Input(shape=(X_tfidf.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_tfidf, y_encoded, epochs=200, verbose=1)

# Save everything
model.save('models/show_type_model.h5')

with open('models/show_type_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('models/show_type_label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)
