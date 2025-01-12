# SAMAY

# SAMAY: Spiritual Assistance and Meditation Aid for You

## Overview
SAMAY is a Streamlit application designed to provide users with translations and insights related to the Gita and Yoga. By leveraging advanced natural language processing techniques, the application allows users to ask questions and receive relevant translations from a curated dataset of slokas and yoga principles.

## Features
- **Semantic Search**: Utilizes Sentence Transformers and FAISS for efficient retrieval of relevant translations based on user queries.
- **User -Friendly Interface**: Built with Streamlit for an interactive and intuitive user experience.
- **Dynamic Query Handling**: Supports user input and provides contextual translations.
- **Customizable**: Easily extendable to include additional features such as user feedback and integration with language models.

## Technologies Used
- **Python**: The primary programming language for the application.
- **Streamlit**: For building the web application interface.
- **Sentence Transformers**: For generating semantic embeddings of questions.
- **FAISS**: For efficient similarity search in high-dimensional spaces.
- **Pandas**: For data manipulation and loading CSV files.
- **OpenAI API**: (Optional) For future integration with language models.

## Installation
To run this application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/samay.git
   cd samay





   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt
OPENAI_API_KEY=your_openai_api_key
Ensure you have the slokas.csv and yoga.csv files in the same directory as the script.
streamlit run app.py




### Notes:
- **Replace placeholders**: Make sure to replace `yourusername` and `your_openai_api_key` with your actual GitHub username and OpenAI API key.
- **Add a License**: If you haven't already, consider adding a license file to your repository.
- **Requirements File**: Create a `requirements.txt` file that lists all the dependencies your project needs. You can generate this file using:
  ```bash
  pip freeze > requirements.txt
