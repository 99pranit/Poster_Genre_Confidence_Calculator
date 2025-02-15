# Poster_Genre_Confidence_Calculator

A machine learning project that predicts the genre of a movie based on its poster and calculates confidence scores for each prediction. The dataset used is the [Kaggle IMDB Genre Dataset](https://www.kaggle.com). This tool can be used for genre classification in media curation, recommendation systems, and archival purposes.  

---

## Introduction  

The **Poster Genre Confidence Calculator** is built to classify movies into their respective genres by analyzing their posters. Using machine learning techniques, it provides confidence scores for each prediction, enabling users to assess the reliability of the classification.  

---

## Dataset  

- **Source**: (https://www.kaggle.com/code/krutarthhd/genre-prediction-from-the-movie-poster/input)
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
  - TensorFlow for deep learning and image preprocessing
  - Pillow for image preprocessing  
  - Pandas and NumPy for data handling  
  - Matplotlib for data visualization  

---

## Result

- **Accuracy:** Achieved 90% on the validation dataset.

---

## Future Work

- Add more advanced models like transformers for multi-modal learning.

---

## 📌 Installation

### Clone the Repository  
**Bash:**
git clone https://github.com/99pranit/Poster_Genre_Confidence_Calculator.git   

Note: The TensorFlow model was not uploaded due to memory constraints.

Steps to Set Up:
1. Download the dataset from [Kaggle](https://www.kaggle.com/code/krutarthhd/genre-prediction-from-the-movie-poster/input) and save it in Poster_Genre_Confidence_Calculator/notebook.
2. Open uploaded final_modelling.ipynb.
3. Copy and paste the model into Poster_Genre_Confidence_Calculator/genre_predict_app.
     
cd movie_poster_genre

### Install Dependencies (Without Docker)

- Install required dependencies:  
  pip install -r requirements.txt

- Run the Streamlit App (Without Docker):  
  streamlit run app.py

- Open http://localhost:8501 in your browser.

### 🐳 Deploy with Docker

- Build the Docker Image:  
  docker build -t genre-classifier .

- Run the Container:  
  docker run -p 8501:8501 genre-classifier

- Open http://localhost:8501 to access the Movie Poster Genre Classifier web app

## 💡 Contributions

Feel free to fork, contribute, or raise issues! PRs are welcome.

📧 Contact: 99pranitd@gmail.com
🔗 Linkedin: www.linkedin.com/in/pranit-das-87739a230

