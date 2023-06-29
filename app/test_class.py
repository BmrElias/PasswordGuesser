class MyClass:
    # C'est un attribut de classe
    class_attribute = "I am a class attribute"

    @classmethod
    def my_class_method(cls):
        # C'est une méthode de classe, elle a accès aux attributs et méthodes de la classe
        return cls.class_attribute


# Utilisation de l'attribut de classe
print(MyClass.class_attribute)  # Output: "I am a class attribute"

# Utilisation de la méthode de classe
print(MyClass.my_class_method())  # Output: "I am a class attribute"

# Les attributs de classe sont partagés par toutes les instances
instance1 = MyClass()
instance2 = MyClass()

print(instance1.class_attribute)  # Output: "I am a class attribute"
print(instance2.class_attribute)  # Output: "I am a class attribute"

# Si nous changeons l'attribut de classe, il change pour toutes les instances
MyClass.class_attribute = "I am a changed class attribute"

print(instance1.class_attribute)  # Output: "I am a changed class attribute"
print(instance2.class_attribute)  # Output: "I am a changed class attribute"
