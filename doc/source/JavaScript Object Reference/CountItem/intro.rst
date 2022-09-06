=========
CountItem
=========

A counted item in a document. Access through the Document.countItems collection. See the Document.autoCount() method.

**Note**: This feature is available in the Extended Version only.

For additional information about count items, see Adobe Photoshop help on the Count Tool.

----------
Properties
----------

.. property:: position
	
	The position of the count item in the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of UnitValue`


.. property:: parent
	
	The containing document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced CountItem object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: remove()
	
	Deletes the CountItem object.
	
	:Parameters: `null`
	
	:Returns: `undefined`
