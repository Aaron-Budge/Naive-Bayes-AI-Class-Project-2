# 🎧 Naive Bayes Spotify Classifier

**Programming Project Assignment: CSCI 384 AI**

This project applies **Naive Bayes classification** to a real-world dataset containing audio features of Spotify songs, with the goal of predicting whether a song is a **hit** based on its measurable characteristics.

This is a structured, step-by-step programming project designed to guide you through the complete process of implementing and evaluating a Naive Bayes classifier on real-world data. Each section in the script builds on the previous one—from loading and cleaning the dataset, to model training, prediction, and evaluation—allowing you to apply core AI concepts in a hands-on and practical way.

---

## 📚 What You'll Practice

- Naive Bayes classification using Gaussian (continuous) probability
- Transforming a continuous target (popularity) into a binary classification problem
- Data cleaning and preprocessing (numeric feature selection, handling missing values)
- Splitting data into training and test sets
- Model evaluation using classification accuracy and confusion matrix
- (Optional) Model experimentation with dynamic threshold tuning

---

## 📁 Folder Structure

| Folder / File                | Description                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| `data/spotify_hits.csv`      | Dataset of Spotify songs (510 instances, 12 features)           |
| `src/naive_bayes_project.py` | Main script to complete and submit                              |
| `src/naive_bayes_model.py`   | Provided model implementation for NaiveBayesContinuous          |
| `src/dataset_utils.py`       | Functions for loading data, splitting, and Gaussian calculation |

---

## 📊 Dataset Overview

The dataset is a preprocessed snapshot of Spotify songs with various audio features.

**Dataset Information**

- Number of songs: 510
- Number of features: 12
- Target column (original): popularity (continuous)

**Feature Columns**

```python
['genre', 'artist_name', 'acousticness', 'danceability', 'duration_ms',
 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness',
 'tempo', 'valence']
```

**Missing Values (before cleaning)**

| Feature      | Missing |
| ------------ | ------- |
| acousticness | 1       |
| danceability | 4       |
| liveness     | 1       |
| speechiness  | 2       |
| valence      | 2       |

**Original Target (`popularity`) Unique Values**

`[0, 1, 3, 5, 6, 7, 8, 9, 10, ..., 93]`

---

## 🚀 How to Start

1. **Clone or download** this repository.
2. Navigate to the `src/` folder.
3. Open the file: `naive_bayes_project.py` and complete the sections marked `# YOUR CODE HERE`.
4. Run the script using Python: `python naive_bayes_project.py`

---

## 📦 Dependencies

This project uses basic Python packages:

- `pandas`
- `numpy`
- `sklearn`

You can install them with:

```bash
pip install pandas numpy scikit-learn
```
