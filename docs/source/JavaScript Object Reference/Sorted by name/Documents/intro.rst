=========
Documents
=========

The collection of open Document objects.

Access this list through the Application.documents collection property, which is available through the app global variable, or directly at the top level. For example, the following adds a new document to the collection::

	app.documents.add(800, 500, 72, "myDocument", NewDocumentMode.RGB)

—or— ::

	documents.add(800, 500, 72, "myDocument", NewDocumentMode.RGB)

----------
Properties
----------

.. property:: length
	
	The number of elements in the documents collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: parent
	
	The containing application.
	
	:Permission: Read-only. 
	
	:Type: :class:`Application`


.. property:: typename
	
	The class name of the referenced documents object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: add([width, height, resolution, name, mode, initialFill, pixelAspectRatio, bitsPerChannel, colorProfileName])
	
	Creates a new document object and adds it to this collection. pixelAspectRatio: Default is 1.0, a square aspect ratio. bitsPerChannelType: Default is BitsPerChannelType.EIGHT.
	
	:Parameters:
		:width: :class:`UnitValue`
		:height: :class:`UnitValue`
		:resolution: :class:`number`
		:name: :class:`string`
		:mode: :class:`NewDocumentMode`
		:initialFill: :class:`DocumentFill`
		:pixelAspectRatio: :class:`number[0.1..10.00]`
		:bitsPerChannel: :class:`BitsPerChannelType`
		:colorProfileName: :class:`string`
	
	:Returns: :class:`Document`


.. function:: getByName(name)
	
	Gets the first element in the documents collection with the provided name
	
	:Parameters:
		:name: :class:`string`
	
	:Returns: :class:`Document`

