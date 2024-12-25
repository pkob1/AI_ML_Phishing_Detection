import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the features and labels from the CSV file
file_path = '/Users/papakobinaorleans-bosomtwe/Desktop/Summer 2024/AI:ML Cyber/Project/project_final/phishing_features_with_whois.csv'  # Adjust the path if necessary
df = pd.read_csv(file_path)

# Check the shape of the DataFrame
print("DataFrame shape:", df.shape)
class_distribution = df['Label'].value_counts()
print("\nClass Distribution:")
print(class_distribution)

# Define features and labels
X = df.drop(columns=['URL', 'Label'])  # Features
y = df['Label']  # Labels

# Handle any missing values (e.g., NaN in 'Domain Age (days)')
X = X.fillna(0)  # Fill NaN values with 0; you might choose a different strategy

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Naive Bayes model
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Predict with the Naive Bayes model
nb_predictions = nb_model.predict(X_test)

# Evaluate the Naive Bayes model
nb_accuracy = accuracy_score(y_test, nb_predictions)
nb_report = classification_report(y_test, nb_predictions)
print("Naive Bayes Model Accuracy:", nb_accuracy)
print("Naive Bayes Classification Report:\n", nb_report)

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict with the Random Forest model
rf_predictions = rf_model.predict(X_test)

# Evaluate the Random Forest model
rf_accuracy = accuracy_score(y_test, rf_predictions)
rf_report = classification_report(y_test, rf_predictions)
print("Random Forest Model Accuracy:", rf_accuracy)
print("Random Forest Classification Report:\n", rf_report)
