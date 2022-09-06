==========
CountItems
==========

The collection of CountItem objects in the document.

Access through the Document.countItems collection property. For example::

	app.activeDocument.countItems.removeAll()

**Note**: This feature is available in the Extended Version only.

----------
Properties
----------

.. property:: length
	
	The number of elements in the CountItems collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: parent
	
	The containing document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced CountItems object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: add(position)
	
	Creates a new count item object and adds it to this collection. Parameter position (x,y) represents the horizontal and vertical positions, respectively, of the CountItem object.
	
	:Parameters:
		:position: :class:`array of UnitValue`
	
	:Returns: :class:`CountItem`


.. function:: getByName(name)
	
	Get the first element in the CountItems collection with the provided name.
	
	:Parameters:
		:name: :class:`string`
	
	:Returns: :class:`CountItem`


.. function:: removeAll()
	
	Removes all CountItem objects from the CountItems collection.
	
	:Parameters: `null`
	
	:Returns: `undefined`

