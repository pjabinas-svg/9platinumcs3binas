# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](OOPAct.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Artist
Description: A person who creates, performs, or expresses original ideas through musical art. Through musical instruments, production, vocals that shape the musical piece.
## New Related Class
Class: Song
Description:  a short musical composition intended to be sung by the human voice, typically combining melody, rhythm, and lyrics
## Association
Relationship: Artist HAS-A Song
Explanation: An Artist HAS-A Song relationship means that an artist contains one or more Song object, representing ownership or creation within the system or relationship
## Multiplicity
Multiplicity: Artist 1 ───────── 0..* Song
Explanation: An Artist can have 0 song or many songs
## UML Class Relationship Diagram
![Class Relationship Diagram](images/imagesclassRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
