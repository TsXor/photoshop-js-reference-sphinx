=====================
DocumentPrintSettings
=====================

The print settings for a document.

----------
Properties
----------

.. property:: backgroundColor
	
	Background color of page.
	
	:Permission: Read-write. 
	
	:Type: :class:`SolidColor`


.. property:: bleedWidth
	
	Bleed width
	
	:Permission: Read-write. 
	
	:Type: :class:`UnitValue`


.. property:: caption
	
	Print the caption found in FileInfo.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: centerCropMarks
	
	Print center crop marks.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: colorBars
	
	Print color calibration bars.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: copies
	
	Number of copies to print.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: cornerCropMarks
	
	Print corner crop marks.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: colorHandling
	
	Color handling.
	
	:Permission: Read-only. 
	
	:Type: :class:`PrintColorHandling`


.. property:: activePrinter
	
	The currently active printer.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: flip
	
	Flip the image horizontally.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: hardProof
	
	Print a hard proof.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: interpolate
	
	Read-write.
	
	:Permission: 
	
	:Type: :class:`boolean`


.. property:: labels
	
	Prints the document title.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: mapBlack
	
	Map blacks.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: negative
	
	Invert the image colors.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: renderIntent
	
	Color conversion intent when print space is different from the source space.
	
	:Permission: Read-write. 
	
	:Type: :class:`Intent`


.. property:: posX
	
	The x position of the image on page.
	
	:Permission: Read-only. 
	
	:Type: :class:`UnitValue`


.. property:: posY
	
	The y position of the image on page.
	
	:Permission: Read-only. 
	
	:Type: :class:`UnitValue`


.. property:: printBorder
	
	The width of the print border.
	
	:Permission: Read-write. 
	
	:Type: :class:`UnitValue`


.. property:: printerName
	
	Name of the printer.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: printSpace
	
	color space for printer. Can be nothing (meaning same as source); 'Working RGB', 'Working CMYK', 'Working Gray', 'Lab Color' (meaning one of the working spaces or Lab color); or a string specifying a specific colorspace (default is same as source)
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: registrationMarks
	
	Print registration marks.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: scale
	
	Scale of image on page.
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: vectorData
	
	Include vector data.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


-------
Methods
-------

.. function:: setPagePosition(docPosition, posX, posY, scale)
	
	Set the position of the image on the page.
	
	:Parameters:
		:docPosition: :class:`DocPositionStyle`
		:posX: :class:`UnitValue`
		:posY: :class:`UnitValue`
		:scale: :class:`number`
	
	:Returns: `undefined`

