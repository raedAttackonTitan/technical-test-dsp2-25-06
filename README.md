# technical-test-25-06


# 🧾 AccountClient – Python API Client

`AccountClient` est un client Python simple pour interagir avec un service REST de la gestion de comptes bancaires, utilisant `requests` pour les appels HTTP et `pydantic` pour la validation automatique des données.

---

## 🚀 Fonctionnalités

-   Authentification via OAuth2 (`/oauth/token`)
-   Récupération de l’identité utilisateur (`/stet/identity`)
-   Liste des comptes bancaires (`/stet/account`)
-   Consultation des balances par comptes (`/stet/account/{account_id}/balance`)
-   Récupération des transactions (`/stet/account/{account_id}/transaction`)
-   Validation stricte des entrées et sorties grâce à [Pydantic](https://docs.pydantic.dev/)

---

## 📦 Installation

```bash
 uv pip install .

````

## BUILD 

build

```bash
 docker build -t account-client .
```


## RUN 

build

```bash
  docker run --rm account-client
```


