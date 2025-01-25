import streamlit as st
import openai

# Configurez votre clé API depuis les secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Titre de l'application
st.title("Clone de ChatGPT avec Streamlit")

# Initialiser l'état des sessions
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# **Partie 1 : Sélection du modèle via un selectbox**
st.sidebar.header("Configuration")
st.sidebar.subheader("Modèle GPT")
model = st.sidebar.selectbox(
    "Choisissez un modèle GPT :",
    ["gpt-3.5-turbo", "gpt-3.5-turbo-instruct", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125"],
    index=0
)
st.session_state["openai_model"] = model

# Affichage du modèle sélectionné
st.sidebar.write(f"Modèle sélectionné : {model}")

# **Partie 2 : Slider pour le nombre maximum de jetons**
st.sidebar.subheader("Paramètres de réponse")
max_tokens = st.sidebar.slider(
    "Choisissez le nombre maximum de jetons générés :",
    min_value=0,
    max_value=500,
    value=100,
    step=10
)

# **Partie 3 : Chat interactif**
st.header("Chat interactif")

# Affichage de l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if user_input := st.chat_input("Posez une question :"):
    # Ajouter le message utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Affichage du message utilisateur
    with st.chat_message("user"):
        st.markdown(user_input)

    # Réponse du modèle
    with st.chat_message("assistant"):
        try:
            # Envoyer la requête à OpenAI
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in st.session_state.messages
                ],
                max_tokens=max_tokens,
            )
            response_content = response["choices"][0]["message"]["content"]

            # Ajouter la réponse à l'historique
            st.session_state.messages.append({"role": "assistant", "content": response_content})

            # Afficher la réponse dans l'interface utilisateur
            st.markdown(response_content)
        except Exception as e:
            st.error(f"Erreur lors de la communication avec l'API : {e}")
