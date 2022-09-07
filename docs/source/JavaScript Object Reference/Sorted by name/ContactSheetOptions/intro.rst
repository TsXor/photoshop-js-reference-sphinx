===================
ContactSheetOptions
===================

Options for creating a contact sheet with the Application.makeContactSheet() method.

----------
Properties
----------

.. property:: acrossFirst
	
	True to place the images horizontally (left to right, then top to bottom) first (default: true).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: bestFit
	
	True to rotate images for the best fit (default: false).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: caption
	
	True to use the filename as a caption for the image (default: true).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: columnCount
	
	The number of columns to include (default: 5).
	
	:Permission: Read-write. 
	
	:Type: :class:`number[1..100]`


.. property:: flatten
	
	True to flatten all layers in the final document (default: true).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: font
	
	The font used for the caption (default: GalleryFontType.ARIAL).
	
	:Permission: Read-write. 
	
	:Type: :class:`GalleryFontType`


.. property:: fontSize
	
	The font size to use for the caption (default: 12).
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: height
	
	The height (in pixels) of the resulting document (default: 720).
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..29000]`


.. property:: horizontal
	
	The horizontal spacing (in pixels) between images (default: 1).
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: mode
	
	The document color mode (default: NewDocumentMode.RGB).
	
	:Permission: Read-write. 
	
	:Type: :class:`NewDocumentMode`


.. property:: resolution
	
	The resolution of the document in pixels per inch (default: 72.0).
	
	:Permission: Read-write. 
	
	:Type: :class:`number [35..1200]`


.. property:: rowCount
	
	The number of rows to use (default: 6).
	
	:Permission: Read-write. 
	
	:Type: :class:`number [1..100]`


.. property:: typename
	
	The class name of the referenced contactSheetOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: useAutoSpacing
	
	True to auto space the images (default: true).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: vertical
	
	The vertical spacing (in pixels) between images (default: 1). Valid only when useAutoSpacing = false.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..29000]`


.. property:: width
	
	The width (in pixels) of the resulting document (default: 576).
	
	:Permission: Read-write. 
	
	:Type: :class:`number [100..29000]`
