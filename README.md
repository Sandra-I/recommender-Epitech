# Recommender_2021_31

### API

Installer toutes les dépendances nécessaires à l'utilisation de l'API

```
$ pip install anyio asgiref click colorama fastapi h11 idna joblib nltk numpy pandas pycodestyle pydantic python-dateutil pytz regex six sniffio starlette toml tqdm typing-extensions uvicorn watchgod websockets google-auth-oauthlib google-api-python-client
```

`̀``
$ pip install -U scikit-learn
```

Pour lancer le serveur FastAPI, depuis le dossier recommender-service/ :

```
$ uvicorn main:app --reload
```

Consulter l'API Swagger http://localhost:8000/docs

### Web App

Installer les dépendances nécessaires pour l'application web, depuis le dossier web-dashboard/ :

```
$ npm install
```

Pour lancer l'interface web, depuis le dossier web-dashboard/ :

```
$ npm run serve
```

Accéder à l'interface web depuis l'adresse http://localhost:8080/