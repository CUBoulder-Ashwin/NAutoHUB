import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load new training data
data = pd.read_csv('data/generic_showtraining.csv')

# Input = intent only
X = data['intent']

# Output = cli_command
y = data['cli_command']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X).toarray()

# Encode output labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Build simple model
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(X_tfidf.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X_tfidf, y_encoded, epochs=200, verbose=1)

# Save everything
model.save('models/generic_show_command_model.h5')

with open('models/generic_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('models/generic_label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)
