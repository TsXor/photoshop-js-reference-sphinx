============
DocumentInfo
============

Metadata about a ``document`` object.

Access through the Document.info property. For example, the following sets the ``author``, ``caption``, and
``copyrighted`` properties::

	var docRef = open(fileList[i])
	// set the file info
	docRef.info.author = "Mr. Adobe programmer"
	docRef.info.caption = "Adobe Photo shoot"
	docRef.info.copyrighted = CopyrightedType.COPYRIGHTEDWORK

These values can be set interactively by choosing **File > File Info**.


----------
Properties
----------

.. property:: author
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: authorPosition
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: caption
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: captionWriter
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: category
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: city
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: copyrighted
	
	The copyrighted status.
	
	:Permission: Read-write. 
	
	:Type: :class:`CopyrightedType`


.. property:: copyrightNotice
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: country
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: creationDate
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: credit
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: exif
	
	Camera data that includes camera settings used when the image was taken. Each array member is a tag pair, an array of [tag, tag_data]; for example, [ "camera" "Cannon"].
	
	:Permission: Read-only. 
	
	:Type: :class:`array of array [tag data]`


.. property:: headline
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: instructions
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: jobName
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: keywords
	
	A list of keywords that can identify the document or its contents.
	
	:Permission: Read-write. 
	
	:Type: :class:`array of string`


.. property:: ownerUrl
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: parent
	
	The info object's container.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: provinceState
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: source
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: supplementalCategories
	
	:Permission: Read-write.
	
	:Type: :class:`array of string`


.. property:: title
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: transmissionReference
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: typename
	
	The class name of the referenced info object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: urgency
	
	:Permission: Read-write.
	
	:Type: :class:`Urgency`

