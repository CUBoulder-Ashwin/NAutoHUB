import os
import pickle
import tensorflow as tf

# Get the absolute directory where THIS script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Point to the models folder
models_dir = os.path.join(current_dir, "..", "..", "machine_learning", "models")

# Load TF-IDF vectorizer and label encoder
with open(os.path.join(models_dir, "generic_vectorizer.pkl"), "rb") as f:
    generic_vectorizer = pickle.load(f)

with open(os.path.join(models_dir, "generic_label_encoder.pkl"), "rb") as f:
    generic_label_encoder = pickle.load(f)

# Load trained model
generic_model = tf.keras.models.load_model(
    os.path.join(models_dir, "generic_show_command_model.h5")
)


def predict_generic_show_command(intent_only):
    """Predicts CLI command based only on extracted intent."""
    intent_tfidf = generic_vectorizer.transform([intent_only]).toarray()
    prediction = generic_model.predict(intent_tfidf)
    predicted_command = generic_label_encoder.inverse_transform([prediction.argmax()])[
        0
    ]
    return predicted_command
