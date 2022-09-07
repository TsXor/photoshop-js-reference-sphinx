=============
ColorSamplers
=============

The collection of ColorSampler objects in a document. Access through the Document.colorSamplers collection property. For example::

	app.activeDocument.colorSamplers.removeAll()

----------
Properties
----------

.. property:: length
	
	The number of elements in the ColorSamplers collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: parent
	
	The containing document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced ColorSamplers object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: add(position)
	
	Creates a new color sampler object and adds it to this collection. The position parameter (x,y) represents the new horizontal and vertical locations of the moved color sampler.
	
	:Parameters:
		:position: :class:`array of UnitValue`
	
	:Returns: :class:`ColorSampler`


.. function:: removeAll()
	
	Removes all ColorSampler objects from the ColorSamplers collection.
	
	:Parameters: `null`
	
	:Returns: `undefined`
