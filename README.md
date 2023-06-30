# PasswordGuesser

Cours de POO - MDS -  M1 Dev

## Description

Dans ce code, j'utilise différentes méthodes pour générer des mots de passe.
L'utilisateur rentre des mots de base et des dates.
De plus, il peux choisir différentes options :

-   LeetSpeak : Remplacer certaines lettres par des chiffres
    -   Elias => Eli4s, 3l14s, 31145, ...
-   Majuscule :
    -   Mettre la première lettre en majuscule
    -   Mettre toutes les lettres en majuscule
-   Minuscule : Mettre toutes les lettres en minuscule
-   Retrait des accents
-   Caractères spéciaux :
    -   Tous les caractères spéciaux ou seulement les plus communs
-   Dates :
    -   Les mois sont remplacés par leur nom en français, anglais ou les deux.
    -   Utilisation de l'année sur 2 ou 4 chiffres

Le tout est combiné et permuté pour obtenir une liste de mots de passe.

## Installation

```bash
git clone https://github.com/BmrElias/PasswordGuesser.git
cd PasswordGuesser/app
```

## Usage

Le [fichier run.py](app/run.py) ne contient qu'une seule ligne (une de plus pour réaliser un import du main).

```bash
python run.py
```

ou

```bash
python3 run.py
```

## Techniques de POO

-   **Polymorphisme**

    -   Le polymorphisme est une caractéristique de la programmation orientée objet (POO) qui permet à une méthode ou une classe d'avoir plusieurs formes. Cela signifie qu'une même méthode ou classe peut se comporter différemment en fonction de son contexte.

    -   L'interface [GeneratorInterface](app/generator_interface.py) définit une méthode [generate()](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/generator_interface.py#L6) que chaque classe qui l'implémente (par exemple, [PrimaryWordsGenerator](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/primary_word_generator.py#L15) et [LeetSpeakGenerator](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/leet_speak_generator.py#L10) doit définir, chacune avec un comportement différent. C'est une forme de polymorphisme.

-   **Encapsulation**

    -   L'encapsulation est le mécanisme qui regroupe les données (attributs) et les méthodes qui manipulent ces données en une seule unité, appelée classe. C'est une façon de cacher les détails de mise en œuvre et de protéger les données d'un accès direct.

    -   Les détails de l'implémentation de chaque classe sont cachés à l'utilisateur de la classe. Par exemple, dans la classe [Date](app/date_generator.py), la façon dont le format de la date est converti est cachée à l'utilisateur de cette classe, qui n'a qu'à appeler la méthode `get_formatted_date()` (exemple dans [Main](https://github.com/BmrElias/PasswordGuesser/blob/9d3b7e4c0516e89ce95d15bd93db99d6083391c8/app/main.py#L55C34-L55C52)) pour obtenir une date formatée.

-   **Composition**

    -   La composition est un type de relation entre les classes où une classe est utilisée comme attribut dans une autre classe. C'est une façon de combiner des objets simples pour créer des objets plus complexes.

    -   La classe [Main](app/main.py) utilise la composition en intégrant plusieurs autres classes (CombinationsGenerator, Date, LeetSpeakGenerator, etc.) pour réaliser ses tâches.

-   **Héritage**

    -   L'héritage est une caractéristique de la POO qui permet de créer une nouvelle classe à partir d'une classe existante. La nouvelle classe hérite des attributs et méthodes de la classe parente, et peut également ajouter de nouveaux attributs et méthodes ou redéfinir ceux de la classe parente.

    -   Bien que cet exemple ne montre pas un exemple direct d'héritage (c'est-à-dire une classe qui hérite d'une autre classe), il utilise l'héritage de classes intégrées comme [ABC](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/generator_interface.py#L4) pour créer des interfaces.

-   **Interface**

    -   Une interface est une définition de méthodes sans implémentation qui peuvent être implémentées par n'importe quelle classe. Les interfaces sont utilisées pour définir un contrat pour les classes, garantissant que certaines méthodes seront présentes dans une classe qui implémente l'interface.

    -   [GeneratorInterface](app/generator_interface.py) sert de contrat pour d'autres classes à implémenter. C'est une interface en programmation orientée objet.

-   **Méthodes et attributs d'objets**

    -   En POO, chaque objet d'une classe a ses propres attributs (qui sont essentiellement des variables associées à l'objet) et des méthodes (qui sont essentiellement des fonctions associées à l'objet). Ces attributs et méthodes peuvent être utilisés pour manipuler l'état de l'objet.

    -   La plupart des classes utilisent des méthodes et des attributs d'objets. Par exemple, dans la classe [Main](app/main.py), [run()](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/main.py#L20) est une méthode d'instance et `base_words, date_values, primary_words` sont des attributs d'instance.

-   **Méthodes et attributs statiques**

    -   Les méthodes et attributs statiques sont définis au niveau de la classe, et non au niveau de l'instance. Les méthodes statiques ne peuvent pas accéder ou modifier les attributs d'instance, tandis que les attributs statiques sont partagés par toutes les instances de la classe.

    -   [CombinationsGenerator](app/combinations_generator.py) utilise des méthodes statiques, comme [combinations_with_replacement()](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/combinations_generator.py#L3) et [permutations_with_replacement()](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/combinations_generator.py#L14). Les méthodes statiques sont des méthodes qui appartiennent à la classe et non à une instance de la classe. Elles sont généralement utilisées pour créer des méthodes utilitaires. De même, la classe [SpecialCharacters](app/special_characters.py) utilise une méthode statique [add_special_characters()](https://github.com/BmrElias/PasswordGuesser/blob/b0de661119e95673ddaa07a253fd9e31e66f7879/app/special_characters.py#L3).

-   **Méthodes et attributs de classe**

    -   Les méthodes et attributs de classe sont similaires aux méthodes et attributs statiques, mais ils sont associés à la classe plutôt qu'à une instance de la classe. Les méthodes de classe peuvent accéder ou modifier les attributs de la classe, tandis que les attributs de classe sont partagés par toutes les instances de la classe.

    -   [Exemple](app/test_class.py)
