==============
BMPSaveOptions
==============

Options for saving a document in BMP format using the Document.saveAs() method.

----------
Properties
----------

.. property:: alphaChannels
	
	True to save the alpha channels.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: depth
	
	The number of bits per channel.
	
	:Permission: Read-write. 
	
	:Type: :class:`BMPDepthType`


.. property:: flipRowOrder
	
	True to write the image from top to bottom (default: false). Available only when osType = OperatingSystem.WINDOWS.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: osType
	
	The target OS. (default: OperatingSystem.WINDOWS).
	
	:Permission: Read-write. 
	
	:Type: :class:`OperatingSystem`


.. property:: rleCompression
	
	True to use RLE compression. Available only when osType = OperatingSystem.WINDOWS.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced BMPSaveOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`
