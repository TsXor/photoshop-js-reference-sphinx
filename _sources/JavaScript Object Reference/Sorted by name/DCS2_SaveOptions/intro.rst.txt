================
DCS2_SaveOptions
================

Options for saving a CMYK document in DCS2 format using the Document.saveAs() method.

----------
Properties
----------

.. property:: dCS
	
	The type of composite file to create (default: DCSType.NOCOMPOSITE).
	
	:Permission: Read-write. 
	
	:Type: :class:`DCSType`


.. property:: embedColorProfile
	
	True to embed the color profile in the document.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: encoding
	
	The type of encoding to use (default: SaveEncoding.BINARY).
	
	:Permission: Read-write. 
	
	:Type: :class:`SaveEncoding`


.. property:: halftoneScreen
	
	True to include the halftone screen (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: interpolation
	
	True to use image interpolation (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: multiFileDCS
	
	True to save color channels as multiple files or a single file (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: preview
	
	The preview type (default: Preview.MACOSEIGHTBIT).
	
	:Permission: Read-write. 
	
	:Type: :class:`Preview`


.. property:: spotColors
	
	True to save spot colors.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: transferFunction
	
	True to include the Transfer functions to compensate for dot gain between the image and film (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced DCS2_SaveOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: vectorData
	
	True to include vector data. Valid only if the document includes vector data (unrasterized text).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`

