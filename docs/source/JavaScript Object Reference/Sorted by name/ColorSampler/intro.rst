============
ColorSampler
============

A color sampler for a document. Access through the Document.colorSamplers collection. For example::

	var colorSamplerRef = app.activeDocument.colorSamplers[0];
	var currentColor = colorSamplerRef.color;

**Note**: For additional information about color samplers, see Adobe Photoshop help on the Color SamplerTool.


----------
Properties
----------

.. property:: color
	
	The color of the color sampler.
	
	:Permission: Read-only. 
	
	:Type: :class:`SolidColor`


.. property:: position
	
	The position of the color sampler in the document. The array (x,y) represents the horizontal and vertical location of the count item.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of UnitValue`


.. property:: parent
	
	The containing document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced ColorSampler object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: move(position)
	
	Moves the color sampler to a new location in the document. The position parameter (x,y) represents the new horizontal and vertical locations of the moved color sampler.
	
	:Parameters:
		:position: :class:`array of UnitValue`
	
	:Returns: `undefined`


.. function:: remove()
	
	Deletes the ColorSampler object.
	
	:Parameters: `null`
	
	:Returns: `undefined`
