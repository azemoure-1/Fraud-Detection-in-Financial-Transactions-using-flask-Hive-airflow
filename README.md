# Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow
The company “FinTech Innovations” is facing a growing challenge of fraudulent transactions which affect the trust of its customers and lead to financial losses. To respond to this problem, a fraud detection system based on the analysis of transactional data, customer data and external data is considered. 


# Rapport de Projet : Détection de Fraude en Temps Réel

## I. Introduction
### 1. Contexte du Projet
Le projet vise à développer un système de détection de fraude en quasi temps réel en utilisant des règles prédéfinies. Cela implique le développement d'API, la collecte et l'intégration des données, le stockage avec Hive, et enfin le déploiement via Airflow.


## II. Développement des API

### 2. API des Données de Transaction
Dans le cadre du projet, nous avons mis en place une API pour accéder aux données transactionnelles en temps quasi réel. Cette API expose un point d'accès à l'URL /api/transactions. En utilisant la méthode HTTP GET, les utilisateurs peuvent récupérer des données de transactions telles que l'ID de transaction, la date et l'heure, le montant, la devise, les détails du commerçant, l'ID du client et le type de transaction. Les données sont générées de manière aléatoire pour simuler des transactions réalistes.

### 3. API des Données Client
Nous avons également développé une API pour accéder aux données clients à travers le point d'accès /api/customers. En effectuant une requête GET à cette URL, les utilisateurs peuvent obtenir des informations clients telles que l'ID client, l'historique des comptes, les informations démographiques et les modèles comportementaux. Ces données sont également générées de manière synthétique pour simuler des scénarios divers.

### 4. API des Données Externes
La troisième API concerne les données externes et est accessible via /api/externalData. Elle offre la possibilité de récupérer des données externes, notamment des informations sur la liste noire, les scores de crédit et les rapports de fraude. Comme pour les autres API, ces données sont générées de manière aléatoire pour refléter des conditions variées.

Ces API constituent une partie cruciale du système global de détection de fraude, permettant la collecte en temps réel des informations nécessaires pour l'analyse et la prise de décision.

## III. Collecte et Intégration des Données

L'étape de collecte et d'intégration des données est cruciale pour assurer que les informations nécessaires à la détection de fraude sont disponibles de manière propre et structurée. Trois scripts distincts ont été développés pour traiter la collecte et l'intégration des données.

### 1. load_customers.py
Le script load_customers.py est dédié à la collecte des données clients. Il utilise l'API /api/customers que nous avons développée précédemment. Ce script récupère les informations clients telles que l'ID client, l'historique des comptes, les informations démographiques et les modèles comportementaux. Les données sont ensuite stockées dans des tables Hive pour un accès rapide et efficace.

### 2. load_transactions.py
Le script load_transactions.py est conçu pour la collecte des données transactionnelles en utilisant l'API /api/transactions. Il extrait des détails tels que l'ID de transaction, la date et l'heure, le montant, la devise, les détails du commerçant, l'ID du client et le type de transaction. Ces données sont également intégrées dans des tables Hive, garantissant une organisation optimale pour les analyses futures.

### 3. load_external_data.py
Le dernier script, load_external_data.py, gère la collecte des données externes via l'API /api/externalData. Il récupère des informations critiques telles que la liste noire, les scores de crédit et les rapports de fraude. Ces données externes sont intégrées dans le système global de stockage basé sur Hive, permettant une accessibilité rapide lors des étapes ultérieures de détection de fraude.

L'ensemble de ces scripts forme une infrastructure robuste pour la collecte, le traitement et l'intégration des données, créant ainsi une base solide pour l'analyse et la détection de fraudes en quasi temps réel.


## V. Développement du Système de Détection de Fraude Basé sur les Règles

La mise en place d'un système de détection de fraude basé sur des règles est essentielle pour identifier les activités suspectes. Quatre scripts distincts ont été développés pour implémenter différentes règles de détection de fraude.

### 1. High-Value.py
Le script High-Value.py est dédié à la détection de transactions à montant élevé. Il utilise des requêtes HiveQL pour identifier les transactions dont le montant dépasse un seuil prédéfini. Ces transactions potentiellement risquées sont ensuite marquées pour une enquête plus approfondie.

### 2. unusual_transaction.py
Le script unusual_transaction.py est conçu pour repérer les transactions inhabituelles. En utilisant des requêtes HiveQL, il identifie les transactions qui sortent du comportement habituel, par exemple, des montants inhabituels pour un client spécifique. Ces transactions atypiques sont ensuite signalées pour une analyse supplémentaire.

### 3. high_risk_customers.py
Le script high_risk_customers.py se concentre sur l'identification des clients présentant un risque élevé. Il utilise des règles prédéfinies basées sur des scores de crédit externes et des rapports de fraude pour marquer les clients à haut risque. Ces informations sont ensuite intégrées dans le système global pour une utilisation future dans d'autres étapes de détection.

### 4. suspicious_locations.py
Le dernier script, suspicious_locations.py, vise à repérer les transactions provenant de lieux inhabituels. En utilisant des requêtes HiveQL, il analyse les transactions en fonction de la localisation du commerçant et signale celles provenant de zones potentiellement risquées.

L'ensemble de ces scripts contribue à la construction d'un système de détection de fraude robuste basé sur des règles prédéfinies. Ces règles peuvent être ajustées et étendues en fonction de l'évolution des modèles de fraude et des besoins spécifiques de l'entreprise.
