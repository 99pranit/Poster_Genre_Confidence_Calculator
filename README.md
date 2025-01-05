# Poster_Genre_Confidence_Calculator

A machine learning project that predicts the genre of a movie based on its poster and calculates confidence scores for each prediction. The dataset used is the [Kaggle IMDB Genre Dataset](https://www.kaggle.com). This tool can be used for genre classification in media curation, recommendation systems, and archival purposes.  

---

## Introduction  

The **Poster Genre Confidence Calculator** is built to classify movies into their respective genres by analyzing their posters. Using machine learning techniques, it provides confidence scores for each prediction, enabling users to assess the reliability of the classification.  

---

## Dataset  

- **Source**: [Kaggle IMDB Genre Dataset](https://www.kaggle.com)  
- **Size**: Includes metadata for thousands of movies along with their posters and genre labels.  
- **Key Features**:  
  - `Poster`: Movie poster images.  
  - `Genres`: Multi-label genres (e.g., Action, Comedy, Drama).  
  - `Year`: Release year of the movie.  

---

## Features  

- **Multi-Label Classification**:  
  - Supported movies with multiple genres using one-vs-all approach.  
- **Image Feature Extraction**:  
  - Built CNN-RNN model for poster feature extraction.  
- **Confidence Scores**:  
  - Calculated probabilities for each genre using softmax activation.  

---

## Technologies Used  

- **Programming Language**: Python  
- **Libraries and Frameworks**:  
  - TensorFlow for deep learning
  - OpenCV for image preprocessing  
  - Pandas and NumPy for data handling  
  - Matplotlib for data visualization  

---

## Result

- **Accuracy:** Achieved 88% on the validation dataset.

---

## Future Work

- Add more advanced models like transformers for multi-modal learning.

