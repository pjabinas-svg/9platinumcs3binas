# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: `Person`
Child: `Artist`
Explanation: An `Artist` **IS-A** `Person` . In here, `Artist` inherits the attributes (`name`, `age`) and methods (`get_info()`) of the `Person` class. It also has its own specialized attributes like `genre` and methods to manage tracks.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation (Weak HAS-A)
Explanation: An `Artist` **has-a** list of `Song` objects. This is modeled as Aggregation because a `Song` object can be instantiated independently of a `Artist` object (created outside the artist and passed to the artist via `add_song()`), so deleting the artist will not destroy the song object.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
1. I chose Artist as the child class of Person because an artist IS-A person in essence. Each artist has the basic human properties of name and age, and the musical properties of genre and a list of songs. The modeling of Artist as a subclass of child correctly captures this real-world hierarchy.
2. Inheritance removed the necessity to re-define common personal attributes and behaviors within Artist. The attributes name and age are directly taken from Person by calling super().__init__(name, age). Artist's get_info() method also re-used super().get_info() for the standard name & age string, rather than re-writing that formatting logic.
3. Artist and Song are related by Aggregation (a weak HAS-A relationship). The Song lifecycle is independent of an Artist because the Song instances are created outside the class and passed in using add_song(song). If you destroy or delete an Artist object, the Song instances still exist in memory, independently.
4. Part III. The Simple Association is a general link or peer-to-peer relationship in which two objects communicate with each other temporarily. The Aggregation relationship in this example is a structured, directed container-contained relationship in which one class (Artist) explicitly contains and manages a collection of the other class (Song) as part of its internal state.
5. The design follows the DRY principle, which means Don’t Repeat Yourself. I keep all shared identity logic inside the Person class of copying it into many identity-based classes. When I change the way personal information is stored I only have to update the Person class. That change automatically goes to the Artist class through inheritance so I do not have to update places in the codebase.