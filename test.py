import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the data from a CSV file
data = pd.read_csv('movie_reviews.csv')

# Separate the features (reviews) and the target (sentiments)
x = data['review']
y = data['sentiment']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer on the training data and transform the training data
X_train_vectorized = vectorizer.fit_transform(x_train)

# Transform the test data using the same vectorizer
X_test_vectorized = vectorizer.transform(x_test)

# Initialize the Multinomial Naive Bayes model
model = MultinomialNB()

# Train the model using the training data
model.fit(X_train_vectorized, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test_vectorized)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy: .2f}")

# Print the classification report
print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Function to predict the sentiment of a given review
def predict_sentiment(review):
    vectorized_review = vectorizer.transform([review])
    prediction = model.predict(vectorized_review)
    return "Positive" if prediction[0] == 1 else "Negative"

# List of new reviews to predict sentiments for
new_review = [
    "This movie is next level! i loved i a lot!",
    "terrible film, assal baale, waste of time and money",
    "waste of time and money",
    "it was okay, not that good and not that bad either"
]

# Predict and print sentiments for the new reviews
for review in new_review:
    print(f"Review: {review}")
    print(f"Predicted Sentiment: {predict_sentiment(review)}\n")

# Interactive loop to predict sentiments for user-entered reviews
print("Now you can enter your own reviews!")
while True:
    user_review = input("Enter a movie review ( or say 'quit' to stop it! ): ")
    if user_review.lower() == "quit":
        break
    else:
        print(f"Predicted Sentiment: {predict_sentiment(user_review)}\n")

print("thanks guys! jagratta! ede manam cheyalsindi!")
