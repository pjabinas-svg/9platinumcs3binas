# Class Attributes and Methods
## Previous Design
[OOPACT.md](OOPAct.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|+Genre| String | Public | This is a general attribute that can be accessed from outside the class|
|+Album| String | Public | This is a general attribute that can be accessed from outside the class|
|+Monthly listeners| Integer | Public | This is a general attribute that can be accessed from outside the class|
|+Name| String | Public | This is a general attribute that can be accessed from outside the class|
|-Adress| String | Private | This is a sensitive attribute that should not be accessed from outside the class|
|-Earnings| int | Private | This is a sensitive attribute that should not be accessed from outside the class|

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?