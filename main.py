import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import time
import json
import openai 


openai.api_key = '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'  # Replace with your actual OpenAI API key


@st.cache_data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error("CSV file not found. Please check the file path.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

slokas_data = load_data("slokas.csv") 
yoga_data = load_data("yoga.csv")     

if slokas_data is not None and yoga_data is not None:
    
    model = SentenceTransformer('all-MiniLM-L6-v2')

   
    slokas_questions = slokas_data['question'].tolist()
    yoga_questions = yoga_data['question'].tolist()


    all_questions = slokas_questions + yoga_questions
    all_embeddings = model.encode(all_questions, convert_to_tensor=True)

   
    all_embeddings = np.array(all_embeddings)

    index = faiss.IndexFlatL2(all_embeddings.shape[1])  # L2 distance
    index.add(all_embeddings)  # Add embeddings to the index

    def get_translation(user_question):
        """Return the translation corresponding to the closest matching question."""
  
        start_time = time.time()

     
        user_embedding = model.encode([user_question])

        distances, indices = index.search(np.array(user_embedding), k=1) 
        closest_index = indices[0][0]

        if distances[0][0] > 0.5:  # Adjust the threshold as needed
            return json.dumps({"error": "Sorry, please ask queries on relevant topics."}), time.time() - start_time
        
       
        if closest_index < len(slokas_questions):
            # It's from the slokas dataset
            book = "Gita"
            chapter_number = int(slokas_data['chapter'].iloc[closest_index])  # Convert to int
            verse_number = int(slokas_data['verse'].iloc[closest_index])      # Convert to int
            shloka = slokas_questions[closest_index]
            translation = slokas_data['translation'].iloc[closest_index]
        else:
            # It's from the yoga dataset
            book = "PYS"
            yoga_index = closest_index - len(slokas_questions)
            chapter_number = int(yoga_data['chapter'].iloc[yoga_index])  # Convert to int
            verse_number = int(yoga_data['verse'].iloc[yoga_index])      # Convert to int
            shloka = yoga_questions[yoga_index]
            translation = yoga_data['translation'].iloc[yoga_index]

        response_data = {
            "book": book,
            "chapter_number": chapter_number,
            "verse_number": verse_number,
            "shloka": shloka,
            "translation": translation
        }

        return json.dumps(response_data, ensure_ascii=False), time.time() - start_time

   

    # Custom CSS for background image and title styling
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://your-image-url.com/background.jpg'); 
            background-size: cover;
            background-position: center;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: black; /* Change color as needed */
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<h1 class="title">SAMAY</h1>', unsafe_allow_html=True)
    st.markdown('<h5 class="title">"Spiritual Assistance and Meditation Aid for You"</h5>', unsafe_allow_html=True)

  
    user_question = st.text_input("Ask a question about the Gita or Yoga:")

    if st.button("Get Translation"):
        if user_question:
            response, response_time = get_translation(user_question)
            st.json(json.loads(response))
            st.write(f"Response time: {response_time:.2f} seconds")
        else:
            st.warning("Please enter a question.")

   
