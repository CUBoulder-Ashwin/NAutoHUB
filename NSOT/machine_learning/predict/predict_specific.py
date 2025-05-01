import os
import pickle
import tensorflow as tf

# Get the absolute directory where THIS script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Point to the models folder
models_dir = os.path.join(current_dir, "..", "..", "machine_learning", "models")

# Load TF-IDF Vectorizer
with open(os.path.join(models_dir, "show_type_vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

# Load Label Encoder
with open(os.path.join(models_dir, "show_type_label_encoder.pkl"), "rb") as f:
    label_encoder = pickle.load(f)

# Load trained model
model = tf.keras.models.load_model(os.path.join(models_dir, "show_type_model.h5"))


def predict_specific_output(user_input):
    """Predicts either show_type or config_template based on intent."""
    vectorized_input = vectorizer.transform([user_input]).toarray()
    prediction = model.predict(vectorized_input)
    predicted_label = label_encoder.inverse_transform([prediction.argmax()])[0]
    return predicted_label


# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    prediction = predict_specific_output(user_query)
    print(f"Predicted Output: {prediction}")
