=========
ArtLayers
=========

The collection of ArtLayer objects in a document or layer set.

Access through the Document.artLayers or LayerSet.artLayers collection. For example::

	var layerRef = docRef.artLayers.add()


----------
Properties
----------

.. property:: length
	
	The number of elements in the artLayers collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: parent
	
	The object's container.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced artLayers object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: add()
	
	Creates a new art layer in the document and adds the new object to this collection.
	
	:Parameters: `null`
	
	:Returns: :class:`ArtLayer`


.. function:: getByName(name)
	
	Get the first element in the artLayers collection with the provided name.
	
	:Parameters:
		:name: :class:`string`
	
	:Returns: :class:`ArtLayer`


.. function:: removeAll()
	
	Removes all elements from the artLayers collection.
	
	:Parameters: `null`
	
	:Returns: `undefined`

