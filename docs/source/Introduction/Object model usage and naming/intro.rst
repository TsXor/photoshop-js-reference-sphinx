=============================
Object model usage and naming
=============================

The JavaScript API follows JavaScript naming conventions in that all classes (object types) begin with uppercase letters and have mixed case. Typically, in JavaScript, you instantiate classes using the new operator::

	new ClassName();

However, in the Photoshop Object Model, it is often not necessary to do this. Major object types are collected into collection classes; for example, a list of ``Document`` objects is contained in a ``Documents`` collection object. You then access the collection object through a corresponding collection property in its container in the object hierarchy. 

For example, the collection of all open documents is contained in the top-level Application object. You can access this through the global variable app, or simply reference its properties directly at the top level::

	app.documents[0] // get the first loaded documented
	documents[0] // this is the same

A collection property has the same name as the collection object, but begins with lowercase. For example, a ``Document`` contains a collection of ``LayerSets``, and a ``LayerSet`` contains a collection of ``ArtLayers``. To access one ``ArtLayer`` object in a set::

	var myLayer = activeDocument.layerSets[0].artLayers[0];

The collections, as in this example, can be treated as arrays, which is useful for iteration. They also provide methods to create their contained objects, and to access them by name::

	var newLayer = activeDocument.artLayers.add(); // Create a new ArtLayer object
	newLayer.name = "My Layer"; // name it for later reference
	...
	var layerRef = activeDocument.artLayers.getByName("My Layer");

Some objects, such as the Font objects contained in the app.fonts collection, are created by the application, and never by your scripts. 

Your scripts do use the JavaScript new operator to create helper objects, such as those that encapsulate a set of options for opening or saving a document in a particular format::

	var opts = new PDFOpenOptions();
	opts.page = 10;
	app.open(myPDFFile, opts);