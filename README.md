# Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow
The company “FinTech Innovations” is facing a growing challenge of fraudulent transactions which affect the trust of its customers and lead to financial losses. To respond to this problem, a fraud detection system based on the analysis of transactional data, customer data and external data is considered. 



![012273c16f07dbce9a146f3c46add2e3](https://github.com/azemoure-1/Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow/assets/113553607/413318bb-afc8-4b1b-bc27-852dbf48b91c)





# Rapport de Projet : Détection de Fraude en Temps Réel

## I. Introduction
### 1. Contexte du Projet
Le projet vise à développer un système de détection de fraude en quasi temps réel en utilisant des règles prédéfinies. Cela implique le développement d'API, la collecte et l'intégration des données, le stockage avec Hive, et enfin le déploiement via Airflow.


## II. Développement des API

### 2. API des Données de Transaction
Dans le cadre du projet, nous avons mis en place une API pour accéder aux données transactionnelles en temps quasi réel. Cette API expose un point d'accès à l'URL /api/transactions. En utilisant la méthode HTTP GET, les utilisateurs peuvent récupérer des données de transactions telles que l'ID de transaction, la date et l'heure, le montant, la devise, les détails du commerçant, l'ID du client et le type de transaction. Les données sont générées de manière aléatoire pour simuler des transactions réalistes.


![Capture d'écran 2023-12-06 141557](https://github.com/azemoure-1/Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow/assets/113553607/b4101865-a1c1-4791-a931-d39018fa3928)


### 3. API des Données Client
Nous avons également développé une API pour accéder aux données clients à travers le point d'accès /api/customers. En effectuant une requête GET à cette URL, les utilisateurs peuvent obtenir des informations clients telles que l'ID client, l'historique des comptes, les informations démographiques et les modèles comportementaux. Ces données sont également générées de manière synthétique pour simuler des scénarios divers.

![Capture d'écran 2023-12-06 141405](https://github.com/azemoure-1/Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow/assets/113553607/2339b3e3-d57b-465a-ac8e-c1698177db70)


### 4. API des Données Externes
La troisième API concerne les données externes et est accessible via /api/externalData. Elle offre la possibilité de récupérer des données externes, notamment des informations sur la liste noire, les scores de crédit et les rapports de fraude. Comme pour les autres API, ces données sont générées de manière aléatoire pour refléter des conditions variées.


![Capture d'écran 2023-12-06 141708](https://github.com/azemoure-1/Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow/assets/113553607/597879f1-d32e-41d2-b5d6-c6c19b34ad27)


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

## VI. Gestion des Données (Data Governance)

La gouvernance des données est une composante essentielle de notre projet de détection de fraude en temps réel. Elle garantit la qualité, la sécurité et l'intégrité des données tout au long du processus, depuis leur collecte jusqu'à leur utilisation dans le système de détection. Voici comment nous avons abordé la gouvernance des données :

### 1. Qualité des Données
Nous avons mis en place des mécanismes pour garantir la qualité des données collectées. Cela inclut des contrôles de validation lors de la collecte initiale, des vérifications de cohérence pendant l'intégration, et des audits réguliers pour identifier et corriger les anomalies.

### 2. Intégrité des Données
L'intégrité des données est assurée par des mécanismes de contrôle de version, des checksums, et des procédures de sauvegarde régulières. Ces pratiques garantissent que les données sont toujours complètes et fiables, même en cas de défaillance du système.

### 3. Conformité Réglementaire
Nous avons intégré des mesures de conformité réglementaire dans notre gestion des données pour nous assurer que toutes les activités respectent les lois et réglementations en vigueur. Cela inclut le respect des normes de protection des données personnelles et d'autres exigences légales.

### 4. Documentation
Un aspect crucial de la gouvernance des données est la documentation exhaustive. Nous avons créé une documentation claire sur les sources de données, les transformations effectuées, les règles de détection de fraude, et d'autres aspects du système. Cela facilite la traçabilité et la compréhension du flux des données.

La gouvernance des données est un processus continu, avec des revues régulières et des mises à jour pour s'adapter aux évolutions technologiques et aux changements dans l'environnement réglementaire.


## VII. Conformité au RGPD (Règlement Général sur la Protection des Données)

La conformité au RGPD est une composante fondamentale de notre approche pour garantir la sécurité des données et respecter les droits des individus. Voici comment notre projet s'aligne sur les principes clés du RGPD :

### 1. Consentement et Transparence
Nous avons mis en place des mécanismes de consentement clairs pour la collecte et l'utilisation des données. Les utilisateurs sont informés de manière transparente sur la finalité de la collecte, les types de données traitées, et leurs droits en vertu du RGPD.

### 2. Minimisation des Données
Nous adoptons une approche de minimisation des données, ne collectant que les informations strictement nécessaires à des fins spécifiques. Cela réduit le risque de traitement excessif et garantit que seules les données pertinentes sont traitées.

### 3. Sécurité des Données
La sécurité des données est au cœur de notre projet. Nous avons mis en place des mesures de sécurité robustes pour protéger les données contre tout accès non autorisé, notamment le chiffrement des données, la gestion des accès, et des protocoles de sécurité avancés.

### 4. Notification des Données
En cas de violation de données à caractère personnel, nous avons mis en place des procédures de notification conformes aux exigences du RGPD. Les autorités compétentes et les individus concernés seront informés dans les délais prescrits par la réglementation.

## VI. DAG Airflow

Le déploiement de notre solution de détection de fraude repose sur l'utilisation d'un DAG (Directed Acyclic Graph) Airflow. Ce DAG est conçu pour orchestrer de manière efficace et planifiée le processus complet, du début à la fin, comprenant la collecte de données, le traitement et la génération d'alertes.

Le DAG Airflow est configuré pour exécuter les différents scripts de collecte de données (`load_customers.py`, `load_transactions.py`, `load_external_data.py`) à des intervalles réguliers. Il assure également le déclenchement des scripts de détection de fraude basés sur des règles (`High-Value.py`, `unusual_transaction.py`, `high_risk_customers.py`, `suspicious_locations.py`).

L'utilisation d'Airflow offre plusieurs avantages, tels que la gestion simplifiée des dépendances entre les tâches, la planification flexible des workflows, et la surveillance détaillée des exécutions. De plus, le DAG facilite l'intégration avec d'autres outils et systèmes, contribuant ainsi à une solution robuste et évolutive.


![airflow_dag](https://github.com/azemoure-1/Fraud-Detection-in-Financial-Transactions-using-flask-Hive-airflow/assets/113553607/941dc347-dfe7-47ad-a5cb-f82fb70a8614)


## VII. Conclusion

En conclusion, ce projet de détection de fraude en quasi temps réel a été élaboré en tenant compte des principaux aspects du cycle de vie des données, de la collecte à l'analyse en passant par le stockage. Les API développées permettent une récupération dynamique des données, tandis que les scripts de collecte et d'intégration garantissent la disponibilité de données propres et structurées.

Le système de détection de fraude basé sur des règles met en œuvre différentes stratégies pour identifier les activités suspectes, offrant ainsi une première ligne de défense contre la fraude. La conformité au RGPD et les pratiques de gouvernance des données renforcent la sécurité et la responsabilité dans le traitement des informations personnelles.

Enfin, le déploiement via Airflow assure une exécution régulière et automatisée du processus, permettant ainsi une surveillance proactive et une intervention rapide en cas d'incident. Ce projet représente une solution holistique qui peut évoluer en fonction des besoins changeants du paysage de la fraude et des exigences de l'entreprise.
