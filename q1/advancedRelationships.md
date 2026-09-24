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
