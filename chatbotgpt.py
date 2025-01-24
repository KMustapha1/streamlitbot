import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

 # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            max_tokens = 200,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

#PARTIE 2
import streamlit as st

# Selectbox pour choisir un modèle GPT
model = st.selectbox(
    "Choisissez un modèle GPT :",  # Titre du selectbox
    [
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-instruct",
        "gpt-3.5-turbo-1106",
        "gpt-3.5-turbo-0125",
    ]  # Options disponibles
)

# Affichage du modèle sélectionné
st.write(f"Vous avez sélectionné le modèle : {model}")


#Création slider
import streamlit as st
import openai


# Ajouter un slider pour choisir le nombre maximum de jetons
max_tokens = st.slider(
    "Choisissez le nombre maximum de jetons générés :",  # Titre du slider
    min_value=0,  # Valeur minimale
    max_value=500,  # Valeur maximale
    value=100,  # Valeur par défaut
    step=10  # Incrément du slider
)

# Afficher le modèle et le nombre de jetons choisis
st.write(f"Modèle sélectionné : {model}")
st.write(f"Le nombre maximum de jetons sélectionné est : {max_tokens}")

# Ajouter une zone de texte pour saisir une question
user_input = st.text_input("Entrez votre question ici :")

# Si une question est saisie, appeler l'API OpenAI
if st.button("Envoyer"):
    if user_input:
        try:
            # Requête à l'API OpenAI avec les valeurs sélectionnées
            response = openai.ChatCompletion.create(
                model=model,  # Modèle sélectionné avec le selectbox
                messages=[{"role": "user", "content": user_input}],
                max_tokens=max_tokens,  # Valeur sélectionnée avec le slider
            )
            # Afficher la réponse de l'API
            st.write("Réponse du modèle :")
            st.write(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"Erreur : {e}")
    else:
        st.warning("Veuillez entrer une question avant d'envoyer.")
