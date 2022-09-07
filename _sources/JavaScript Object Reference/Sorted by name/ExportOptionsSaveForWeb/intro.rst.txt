=======================
ExportOptionsSaveForWeb
=======================

Options for optimizing a document for the web or devices using the Document.exportDocument() method. These are the options that you can provide when you choose **File > Save For Web and Devices**.

----------
Properties
----------

.. property:: blur
	
	Applies blur to the image to reduce artifacts (default: 0.0).
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: colorReduction
	
	The color reduction algorithm (default: ColorReductionType.SELECTIVE).
	
	:Permission: Read-write. 
	
	:Type: :class:`ColorReductionType`


.. property:: colors
	
	The number of colors in the palette (default: 256).
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: dither
	
	The type of dither (default: Dither.DIFFUSION).
	
	:Permission: Read-write. 
	
	:Type: :class:`Dither`


.. property:: ditherAmount
	
	The amount of dither (default: 100). Valid only when dither = Dither.DIFFUSION.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: format
	
	The file format to use (default: SaveDocumentType.COMPUSERVEGIF). Note: For this property, only COMPUSERVEGIF, JPEG, PNG-8, PNG-24, and BMP are supported.
	
	:Permission: Read-write. 
	
	:Type: :class:`SaveDocumentType`


.. property:: includeProfile
	
	True to include the document’s embedded color profile (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: interlaced
	
	True to download in multiple passes; progressive (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: lossy
	
	The amount of lossiness allowed (default: 0).
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: matteColor
	
	The colors to blend transparent pixels against.
	
	:Permission: Read-write. 
	
	:Type: :class:`RGBColor`


.. property:: optimized
	
	True to create smaller but less compatible files (default: true). Valid only when format = SaveDocumentType.JPEG.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: PNG8
	
	Indicates the number of bits; true = 8, false = 24 (default: true). Valid only when format = SaveDocumentType.PNG.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`

