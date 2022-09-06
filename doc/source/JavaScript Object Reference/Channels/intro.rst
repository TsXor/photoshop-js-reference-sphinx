========
Channels
========

The collection of Channel objects in a document.

Access through the Document.channels collection property. For example::

	var channelRef = app.activeDocument.channels.add()

----------
Properties
----------

.. property:: length
	
	The number of elements in the channels collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: parent
	
	The containing document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced channels object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: add()
	
	Creates a new channel object and adds it to this collection.
	
	:Parameters: `null`
	
	:Returns: :class:`Channel`


.. function:: getByName(name)
	
	Get the first element in the channels collection with the provided name.
	
	:Parameters:
		:name: :class:`string`
	
	:Returns: :class:`Channel`


.. function:: removeAll()
	
	Removes all alpha channel objects from the channels collection.
	
	:Parameters: `null`
	
	:Returns: `undefined`
