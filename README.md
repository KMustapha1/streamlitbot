# streamlitbot

## Groupe:
    * TOHNGODO Maëlisse
    * TOHNGODO Inès 
    * KHELFA Moustapha


# Comment récupérer le projet et l'exécuter ?


## 1. Installer les outils nécessaires
### Tout d'abord il faut instaler Git et Python si ce n'est pas fait:

#### Git : pour télécharger le projet. Téléchargez-le ici : https://git-scm.com/.
#### Python : pour exécuter le code. Téléchargez-le ici : https://www.python.org/downloads/.

## 2. Télécharger le projet

### Ouvrez une fenêtre de Terminal (VS Code).
### Tapez la commande suivante pour télécharger le projet : 
' git clone https://github.com/KMustapha1/streamlitbot.git '
### Cela téléchargera les fichiers du projet sur votre ordinateur localement.

### Entrez dans le dossier du projet:
' cd streamlitbot '

## 3. Créer un environnement Python
### Créez un environnement en tapant:
' python -m venv stenv '
### Activez l’environnement :
#### Sur Windows :
 'stenv\Scripts\activate '
#### Sur macOS/Linux :
' source stenv/bin/activate '
#### Une fois l’environnement activé, vous verrez quelque chose comme (stenv) au niveau de votre commande.

## 4. Installer les outils nécessaires au projet

### Créez un fichier .gitignore dans votre projet streamlitbot et ajoutez les lignes suivantes et sauvegardez le fichier.
' # Python venv 
stenv
.gitignore '
### Installez les bibliothèques nécessaires avec la commande:
' pip install -r requirements.txt '
### Générer la clé API OpenAI
Une fois que vous avez créé votre compte OpenAI et que vous vous êtes connecté à votre compte sur ce lien https://platform.openai.com/, vous verrez les initiales de votre nom et l'icône de votre profil dans le coin supérieur droit du tableau de bord OpenAI. Pour générer une clé API OpenAI, appuyez sur dashboard afficher le menu déroulant. Cliquez sur l'option « les clés API » API keys.
À ce stade, vous verrez une fenêtre avec l’option « Créer une nouvelle clé secrète » Create new secret key près du centre. Cliquez sur cette option pour en obtenir une. Assurez-vous d’enregistrer cette clé API nouvellement générée dès que possible. En effet, vous ne pourrez plus voir la clé API OpenAI complète une fois la fenêtre fermée.
### Créez un nouveu dossier .streamlit dans le projet streamlitbot
### Créez un nouveu fichier secrets.toml dans le projet .streamlit
### Copiez collez les lignes de code ci-dessous dans le fichier secrets.toml :
' # .streamlit/secrets.toml
OPENAI_API_KEY = "YOUR_API_KEY" '
### Mettez à jour la valeur de "YOUR_API_KEY" avec votre clé Openai et sauvegardez le fichier.
### Ajoutez le dossier .streamlit et le fichier secrets.toml au fichier .gitignore:
' .streamlit/
secrets.toml '
### Et sauvegardez le fichier.
### Réalisez le workflow de base pour enregistrer les modifications dans votre dépôt git:
' git status
git add 
git commit -m "test chatbot"
git status
git push origin main '

### Lancez le Chatbot en tapant:
' streamlit run chatbot.py '
### Lancez le ChatbotGPT en tapant: 
' streamlit run chatbotgpt.py '

#### Une page web s'ouvrira dans votre navigateur où vous pourrez voir le Chatbot en action !
