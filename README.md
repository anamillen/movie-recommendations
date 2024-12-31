# Movie Recommendation System

## Overview
This project is a **Movie Recommendation System** built with **Streamlit** for the web interface and a machine learning model for suggesting content-based movie recommendations. 
Users can select a movie they like, and the system will recommend similar movies based on the pre-trained model.

---

## Hosted Version
Access the hosted version of this app here:
[Movie Recommendation System](https://movierecommendationssyst.streamlit.app/)

---

## How It Works
1. **Input**: The user selects a movie from a dropdown list.
2. **Model**: A pre-trained model calculates the similarity between movies using a similarity matrix.
3. **Output**: The top 5 similar movies are displayed as recommendations.

---

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/anamillen/movie-recommendations
   cd movie-recommendations 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add the necessary files (`movies.pkl` and `similarity.pkl`) to the project directory.

---

## Usage
### Run the Application
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser at `http://localhost:8501`.

### Interact with the App
- Select a movie from the dropdown menu.
- Click **"Recommend"** to see the top 5 recommended movies.

---

---

## Data Sources
The original data comes from the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The preprocessed data for this project is stored in `movies.pkl` and `similarity.pkl`. Make sure these files are present in the project directory.

---

## Example Output
### Input
- Selected Movie: **"The Matrix"**

### Output
- Recommended Movies:
  - **"The Matrix Reloaded"**
  - **"The Matrix Revolutions"**
  - **"Inception"**
  - **"Interstellar"**
  - **"Avatar"**

---

## Contributing
Feel free to fork the repository and make improvements. Pull requests are welcome!

---

## Contact
For any questions or feedback, please contact:
- **Name**: Anastasia Millen
- **Email**: anastasiia.millen@gmail.com
