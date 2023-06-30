# PasswordGuesser

Cours POO MDS M1 Dev

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

    -   Le polymorphisme est une caractéristique de la POO qui permet à une classe ou à une méthode d'avoir plusieurs formes. En pratique, cela signifie qu'une seule interface peut être utilisée pour représenter différents types de données.

    -   L'interface [GeneratorInterface](app/generator_interface.py) définit une méthode [generate()](https://github.com/BmrElias/PasswordGuesser/blob/c2ccb0e92369867015c521bde9832b20c7fe51b6/app/generator_interface.py#L6C6-L6C6) que chaque classe qui l'implémente (par exemple, [PrimaryWordsGenerator](app/primary_word_generator.py) et [LeetSpeakGenerator](app/leet_speak_generator.py)) doit définir, chacune avec un comportement différent. C'est une forme de polymorphisme.

-   **Encapsulation**

    -   L'encapsulation est le mécanisme qui permet de restreindre l'accès direct à certains composants d'un objet et de protéger les données internes de l'objet. C'est une manière de regrouper les données (attributs) et les méthodes qui les manipulent.

    -   Les détails de l'implémentation de chaque classe sont cachés à l'utilisateur de la classe. Par exemple, dans la classe [Date](app/date_generator.py), la façon dont le format de la date est converti est cachée à l'utilisateur de cette classe, qui n'a qu'à appeler la méthode `get_formatted_date()` pour obtenir une date formatée.

-   **Composition**

    -   La composition est un type de relation entre les classes où une classe est utilisée comme attribut dans une autre classe. C'est une façon de combiner des objets simples pour créer des objets plus complexes.

    -   La classe [Main](app/main.py) utilise la composition en intégrant plusieurs autres classes (CombinationsGenerator, Date, LeetSpeakGenerator, etc.) pour réaliser ses tâches.

-   **Héritage**

    -   L'héritage est une caractéristique de la POO qui permet de créer une nouvelle classe à partir d'une classe existante. La nouvelle classe hérite des attributs et méthodes de la classe parente, et peut également ajouter de nouveaux attributs et méthodes ou redéfinir ceux de la classe parente.

    -   Bien que cet exemple ne montre pas un exemple direct d'héritage (c'est-à-dire une classe qui hérite d'une autre classe), il utilise l'héritage de classes intégrées comme ABC pour créer des interfaces.

-   **Interface**

    -   Une interface est une définition de méthodes sans implémentation qui peuvent être implémentées par n'importe quelle classe. Les interfaces sont utilisées pour définir un contrat pour les classes, garantissant que certaines méthodes seront présentes dans une classe qui implémente l'interface.

    -   [GeneratorInterface](app/generator_interface.py) sert de contrat pour d'autres classes à implémenter. C'est une interface en programmation orientée objet.

-   **Méthodes et attributs d'objets**

    -   En POO, chaque objet d'une classe a ses propres attributs (qui sont essentiellement des variables associées à l'objet) et des méthodes (qui sont essentiellement des fonctions associées à l'objet). Ces attributs et méthodes peuvent être utilisés pour manipuler l'état de l'objet.

    -   La plupart des classes utilisent des méthodes et des attributs d'objets. Par exemple, dans la classe [Main](app/main.py), run() est une méthode d'instance et base_words, date_values, primary_words sont des attributs d'instance.

-   **Méthodes et attributs statiques**

    -   Les méthodes et attributs statiques sont définis au niveau de la classe, et non au niveau de l'instance. Les méthodes statiques ne peuvent pas accéder ou modifier les attributs d'instance, tandis que les attributs statiques sont partagés par toutes les instances de la classe.

    -   [CombinationsGenerator](app/combinations_generator.py) utilise des méthodes statiques, comme generate_combinations(), combinations_with_replacement(), etc. Les méthodes statiques sont des méthodes qui appartiennent à la classe et non à une instance de la classe. Elles sont généralement utilisées pour créer des méthodes utilitaires. De même, la classe [SpecialCharacters](app/special_characters.py) utilise une méthode statique add_special_characters().

-   **Méthodes et attributs de classe**

    -   Les méthodes et attributs de classe sont similaires aux méthodes et attributs statiques, mais ils sont associés à la classe plutôt qu'à une instance de la classe. Les méthodes de classe peuvent accéder ou modifier les attributs de la classe, tandis que les attributs de classe sont partagés par toutes les instances de la classe.

    -   [Exemple](app/test_class.py)
