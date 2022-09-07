==============
EPSSaveOptions
==============

Options for saving a document in EPS format using the Document.saveAs() method.

----------
Properties
----------

.. property:: embedColorProfile
	
	True to embed the color profile in this document.
	
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


.. property:: preview
	
	The preview type.
	
	:Permission: Read-write. 
	
	:Type: :class:`Preview`


.. property:: psColorManagement
	
	True to use Postscript color management (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: transferFunction
	
	True to include the Transfer functions to compensate for dot gain between the image and film (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: transparentWhites
	
	True to display white areas as transparent. Valid only when document.mode = DocumentMode.BITMAP. See also changeMode().
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced EPSSaveOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: vectorData
	
	True to include vector data. Valid only if the document includes vector data (text).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`

