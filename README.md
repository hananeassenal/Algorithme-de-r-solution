# Algorithme-de-r-solution
# Principe d'algorithme de résolution

Ce script Python implémente la méthode de résolution pour la logique propositionnelle. La méthode de résolution est une technique fondamentale en démonstration automatisée de théorèmes et en intelligence artificielle, utilisée pour déterminer la satisfiabilité d'une formule logique propositionnelle.

## Fonctionnalités

Le script propose les fonctionnalités suivantes :

1. **Analyse de l'Entrée de la Formule** : La fonction `parse_formula_input` analyse la formule d'entrée fournie dans le format {clause1, clause2, ...}, où chaque clause est constituée de littéraux séparés par l'opérateur ^ (ET).

2. **Négation** : La fonction `negation` calcule la négation d'une formule donnée.

3. **Conversion en Forme Clausale** : La fonction `mettre_sous_forme_de_clauses` convertit une formule donnée en une liste de clauses.

4. **Recherche des Clauses Résolvantes** : La fonction `chercher_clauses_resolvantes` recherche les clauses résolvantes en effectuant des comparaisons par paires entre les littéraux de différentes clauses.

5. **Résolution** : La fonction `resolution` implémente la méthode de résolution pour vérifier la satisfiabilité d'une formule.

6. **Test** : La fonction `test_resolution` permet aux utilisateurs de saisir des formules et de tester la méthode de résolution.

## Utilisation

### Environnement d'Exécution

- Python 3.x
- Modules nécessaires : `re` (inclus dans la bibliothèque standard de Python)

### Instructions d'Exécution

1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Téléchargez le fichier `algorithme_de_résolution.py` sur votre ordinateur.
3. Ouvrez un terminal ou une invite de commande.
4. Accédez au répertoire contenant le fichier `algorithme_de_résolution.py`.
5. Exécutez le script en utilisant la commande suivante :

   ```bash
   python algorithme_de_résolution.py
   ```

---
