================
DICOMOpenOptions
================

Options for opening a document in DICOM format using the Application.open() method.

**Note**: This feature is available in the Extended Version only.

----------
Properties
----------

.. property:: anonymize
	
	True to make the patient information anonymous.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: columns
	
	Number of columns in n-up configuration.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: reverse
	
	True to reverse (invert) the image.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: rows
	
	The number of rows in n-up configuration.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: showOverlays
	
	True to show overlays.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced DICOMOpenOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: windowLevel
	
	The contrast of the image in Houndsfield units.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: windowWidth
	
	The brightness of the image in Houndsfield units.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`

