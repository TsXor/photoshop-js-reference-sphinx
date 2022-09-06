================
DCS1_SaveOptions
================

Options for saving a CMYK document in DCS1 format using the Document.saveAs() method.

----------
Properties
----------

.. property:: dCS
	
	(default: DCSType.COLORCOMPOSITE).
	
	:Permission: Read-write. 
	
	:Type: :class:`DCSType`


.. property:: embedColorProfile
	
	True to embed the color profile in the document
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: encoding
	
	The type of encoding to use for document (default: SaveEncoding.BINARY).
	
	:Permission: Read-write. 
	
	:Type: :class:`SaveEncoding`


.. property:: halftoneScreen
	
	True to include halftone screen (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: interpolation
	
	True to use image interpolation (default: false)
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: preview
	
	The type of preview (default: Preview.MACOSEIGHTBIT).
	
	:Permission: Read-write. 
	
	:Type: :class:`Preview`


.. property:: transferFunction
	
	True to include the Transfer functions to compensate for dot gain between the image and film (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced DCS1_SaveOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: vectorData
	
	True to include vector data. Valid only if the document includes vector data (unrasterized text).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`

