import firebase
from firebase import credentials, auth

config = {
    "apiKey": "AIzaSyBywehNS3M-CJesqTEr-jlx1fsNk6Xgxg",
    "authDomain": "idpets-8146a.firebaseapp.com",
    "databaseURL": "",
    "projectId": "idpets-8146a",
    "storageBucket": "idpets-8146a.appspot.com",
    "messagingSenderId": "1057470492257",
    "appId": "1:1057470492257:web:1afd755d6303ba2ce28420"
}

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase.initialize_app(cred)

def iniciar_sesion(email, password):
    try:
        user = auth.get_user_by_email(email)
        print('Usuario inició sesión con éxito:', user.uid)
    except:
        print('Error durante inicio de sesión')

def cerrar_sesion(user):
    try:
        auth.current_user = user
        auth.refresh(user['refreshToken'])
        print('Usuario cerró sesión con éxito')
    except:
        print('Error durante cierre de sesión')