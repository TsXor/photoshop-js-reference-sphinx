========
Document
========

The active containment object for layers and all other objects in the script; the basic canvas for the file.

* Access the object for the currently active document through Application.activeDocument.
* You can access other documents, or iterate through all open documents using the list in the Application.documents collection. You can access individual documents in the list by index, or use Documents.getByName() to retrieve them by name.
* Create documents programmatically using the Documents.add() method. See Document sample script and the Documents collection object for examples.

**Note**: In Adobe Photoshop, a document can also be referred to as an image or a canvas.

* The term image refers to the entire document and its contents. You can trim or crop an image. You resize an image using the resizeImage() method.
* The term canvas refers to the space in which the document sits on the screen. You can rotate or flip the canvas. You resize the canvas using the resizeCanvas() method.


----------
Properties
----------



-------
Methods
-------




