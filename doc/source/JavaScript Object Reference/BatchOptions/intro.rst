============
BatchOptions
============

Options for running a batch operation using the Application.batch() method.

JavaScript only supports folders as sources for batch commands. Specify the batch source folder as the ``inputFiles`` parameter of the Application.batch() method.

----------
Properties
----------

.. property:: destination
	
	The type of destination for the processed files (default: ``BatchDestinationType.NODESTINATION``).
	
	:Permission: Read-write. 
	
	:Type: :class:`BatchDestinationType`


.. property:: destinationFolder
	
	The folder location for the processed files. Valid only when destination = ``BatchDestinationType.FOLDER``.
	
	:Permission: Read-write. 
	
	:Type: :class:`Folder`


.. property:: errorFile
	
	The file in which to log errors encountered. To display errors on the screen (and stop batch processing when errors occur) leave blank.
	
	:Permission: Read-write. 
	
	:Type: :class:`File`


.. property:: fileNaming
	
	A list of file naming options (maximum: 6). Valid only when destination = ``BatchDestinationType.FOLDER``.
	
	:Permission: Read-write. 
	
	:Type: :class:`array of FileNamingType`


.. property:: macintoshCompatible
	
	True to make the final file names Macintosh compatible (default: ``true``). Valid only when destination = ``BatchDestinationType.FOLDER``.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: overrideOpen
	
	True to override action open commands (default: ``false``).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: overrideSave
	
	True to override save as action steps with the specified destination (default: ``false``). Valid only when destination = ``BatchDestinationType.FOLDER`` or ``SAVEANDCLOSE``.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: startingSerial
	
	The starting serial number to use in naming files (default: 1). Valid only when destination = ``BatchDestinationType.FOLDER``.
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: suppressOpen
	
	True to suppress the file open options dialogs (default: ``false``).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: suppressProfile
	
	True to suppress the color profile warnings (default: ``false``).
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced ``batchOptions`` object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: unixCompatible
	
	True to make the final file name Unix compatible (default: ``true``). Valid only when destination = ``BatchDestinationType.FOLDER``.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: windowsCompatible
	
	True to make the final file names Windows compatible (default: ``true``). Valid only when destination = ``BatchDestinationType.FOLDER``.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`

