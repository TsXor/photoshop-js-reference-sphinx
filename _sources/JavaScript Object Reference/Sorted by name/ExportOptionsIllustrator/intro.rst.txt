========================
ExportOptionsIllustrator
========================

Options for exporting PathItem objects to an Adobe Illustrator® file using using the Document.exportDocument() method. These options are the options that you can provide when you choose **File > Export > Paths To Illustrator**.

----------
Properties
----------

.. property:: path
	
	The type of path to export (default: IllustratorPathType.DOCUMENTBOUNDS).
	
	:Permission: Read-write. 
	
	:Type: :class:`IllustratorPathType`


.. property:: pathName
	
	The name of the path to export. Valid only when path = IllustratorPathType.NAMEDPATH.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: typename
	
	The class name of the referenced exportOptionsIllustrator object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`

