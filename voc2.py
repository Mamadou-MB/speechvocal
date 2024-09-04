import speech_recognition as sr
import streamlit as st 
import os
#=============================================================================================================================================================================
# Ajoutez d'autres API si nécessaire
api_options = ["Google Web Speech API", "Sphinx (Offline)", "Recognizer API"]  
selected_api = st.selectbox("Sélectionnez l'API de reconnaissance vocale", api_options)

# Choix de la langue
language_options = {
    "Français": "fr-FR",
    "Anglais": "en-US",
    "Espagnol": "es-ES"
   
}
selected_language = st.selectbox("Choisissez la langue", list(language_options.keys()))

#=============================================================================================================================================================================

# Configuration de la reconnaissance vocale
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Variables de contrôle pour la pause et reprise
pause = st.button("Pause")
resume = st.button("Reprendre")
transcription = ""

#=============================================================================================================================================================================

# Fonction pour la transcription de la parole
def transcribe_speech(api_name, lang):
    global transcription
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            st.write("Parlez maintenant...")
            audio = recognizer.listen(source)
        
        if api_name == "Google Web Speech API":
            transcription = recognizer.recognize_google(audio, language=lang)
        elif api_name == "Sphinx (Offline)":
            transcription = recognizer.recognize_sphinx(audio, language=lang)
        elif api_name == "Recognizer API":
            transcription = recognizer.recognize_bing(audio, language=lang)  # Exemple, ajoutez les clés API nécessaires

        st.write("Transcription:", transcription)

    except sr.RequestError as e:
        st.error(f"Erreur de l'API de reconnaissance vocale: {e}")
    except sr.UnknownValueError:
        st.error("L'API de reconnaissance vocale n'a pas pu comprendre l'audio.")
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue: {e}")

#================================================================================================================================================================        
        
# Fonction pour enregistrer la transcription dans un fichier
def save_transcription(text):
    with open("transcription.txt", "w") as file:
        file.write(text)
    st.success("Transcription enregistrée dans 'transcription.txt'")

#=================================================================================================================================================================    
    
# Démarrer la reconnaissance vocale
if st.button("Démarrer"):
    transcribe_speech(selected_api, language_options[selected_language])

    
#=============================================================================================================================================================================

# Enregistrer la transcription dans un fichier
if transcription:
    if st.button("Enregistrer la transcription"):
        save_transcription(transcription)
#=============================================================================================================================================================================

# Pause et Reprise du processus
if pause:
    st.write("Reconnaissance vocale en pause...")
if resume:
    st.write("Reprise de la reconnaissance vocale...")
    
    
    
    



