"""
AI Programming Project – Naive Bayes Classifier
University of North Dakota – AI Course | Spring 2025

Title: Predicting Hit Songs Using Naive Bayes
Total Points: 100 (+10 bonus points)

This is the main assignment script. You must complete each step where "YOUR CODE HERE" is indicated.
Use the provided helper modules (dataset_utils.py and naive_bayes_model.py) to assist you.
The NaiveBayesContinuous model is based on our course’s GitHub repository:
https://github.com/aimacode/aima-python
"""

# ---------------------------------------------------------------
# STEP 1 [10 pts]: Load the Dataset
# ---------------------------------------------------------------
# - Load the CSV file 'spotify_hits.csv' (located in the 'data' folder)
#   into a pandas DataFrame.
# - Hint: Use the load_dataset() function from dataset_utils.py.
# YOUR CODE HERE:
# import necessary modules and load the dataset.
data =  None  # YOUR CODE HERE


# ---------------------------------------------------------------
# STEP 2 [10 pts]: Create a Binary Target Column
# ---------------------------------------------------------------
# - Create a new column 'hit' from 'popularity'.
# - A song is a hit if popularity ≥ 70; otherwise, it is not a hit.
# YOUR CODE HERE:
# Create the 'hit' column using a conditional operation.
# data['hit'] = YOUR CODE HERE


# ---------------------------------------------------------------
# STEP 3 [10 pts]: Preprocess the Dataset
# ---------------------------------------------------------------
# - Prepare the dataset for training by:
#   1. Keeping only numeric columns.
#   2. Removing rows with missing values.
# - Hint: Use select_dtypes() and dropna().
# YOUR CODE HERE:
# Preprocess the dataset.
# data = YOUR CODE HERE


# ---------------------------------------------------------------
# STEP 4 [10 pts]: Train/Test Split
# ---------------------------------------------------------------
# - Split the dataset into training (80%) and testing (20%) sets.
# - Hint: Use the split_dataset() function from dataset_utils.py.
# YOUR CODE HERE:
# Split the dataset.
# train_df, test_df = YOUR CODE HERE


# ---------------------------------------------------------------
# STEP 5 [20 pts]: Train the Naive Bayes Model
# ---------------------------------------------------------------
# - Wrap the training DataFrame using the DataSet class (from dataset_utils.py) 
#   with 'hit' as the target.
# - Train the NaiveBayesContinuous model (from naive_bayes_model.py) using the training DataSet.
# YOUR CODE HERE:
# Create the DataSet object and train the model.
# from naive_bayes_model import NaiveBayesContinuous
# train_dataset = YOUR CODE HERE
# model = YOUR CODE HERE


# ---------------------------------------------------------------
# STEP 6 [15 pts]: Make Predictions and Evaluate
# ---------------------------------------------------------------
# - For each song in the test set, extract its features (all columns except 'hit') as a dictionary.
# - Use the trained model to predict the label.
# - Compare the prediction to the true 'hit' value and compute the overall accuracy.
# YOUR CODE HERE:
# Write your loop to predict and calculate accuracy.
# correct = YOUR CODE HERE
# total = YOUR CODE HERE
# for ... in test_df.iterrows():
#     features = YOUR CODE HERE
#     true_label = YOUR CODE HERE
#     predicted_label = YOUR CODE HERE
#     if predicted_label equals true_label:
#         update your counter
# accuracy = YOUR CODE HERE
# print("Model accuracy: ", accuracy)


# ---------------------------------------------------------------
# STEP 7 [15 pts]: Answer Conceptual Questions
# ---------------------------------------------------------------
# For each question, assign your answer (as a capital letter "A", "B", "C", or "D")
# to the corresponding variable.
#
# Q1 [5 pts]: Which features are most likely to influence whether a song is a hit?
#   A. track_id and duration_ms
#   B. danceability, energy, and loudness
#   C. popularity and tempo
#   D. artist name and genre
q1_answer = ""  # YOUR ANSWER HERE

# Q2 [5 pts]: What assumption does the Naive Bayes model make about the input features?
#   A. They follow a uniform distribution.
#   B. They are normally distributed.
#   C. They are independent given the target class.
#   D. They are weighted by importance.
q2_answer = ""  # YOUR ANSWER HERE

# Q3 [5 pts]: What is a likely difference if a decision tree is used instead of Naive Bayes?
#   A. The model will assume independence of features.
#   B. The model will assign probabilities instead of decision rules.
#   C. The model will create splits based on feature thresholds.
#   D. The model will always perform worse.
q3_answer = ""  # YOUR ANSWER HERE


# ---------------------------------------------------------------
# BONUS SECTION: Advanced Analysis [10 bonus pts]
# ---------------------------------------------------------------
# BONUS Task 1 [6 pts]:
# - Compute and display a confusion matrix comparing the true labels to your model's predictions.
# - Hint: You may use sklearn.metrics.confusion_matrix.
# YOUR CODE HERE:
# (Optional) Compute and print the confusion matrix.
# BONUS Task 2 [4 pts]:
# - Experiment with different thresholds for defining a hit (e.g., popularity ≥ 65, 75, or 80).
# - Determine which threshold gives the best model accuracy.
# - Report your best threshold and the corresponding accuracy.
best_threshold = 70  # YOUR BEST THRESHOLD HERE
best_accuracy = 0.0  # YOUR BEST ACCURACY HERE (update after testing)
