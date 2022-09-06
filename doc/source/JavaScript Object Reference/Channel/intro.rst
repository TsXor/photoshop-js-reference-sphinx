=======
Channel
=======

Information about a color element in the image.

Access through the Document.channels collection. You can access an individual channel object in this list by index or by name. For example, this accesses a channel object in the active document by name and assigns an opacity value::

	var channelRef = app.activeDocument.channels.getByName("my channel");
	channelRef.opacity = 22;

A channel is analogous to a plate in the printing process that applies a single color. The document’s color mode determines the number of default channels; for example, an RGB document has three channels, red, green, and blue. A color can also have an alpha channel, which stores selections as masks, or a spot channel, which stores spot colors.

----------
Properties
----------

.. property:: color
	
	The color of the channel. Not valid when kind = ChannelType.COMPONENT.
	
	:Permission: Read-write. 
	
	:Type: :class:`SolidColor`


.. property:: histogram
	
	A histogram of the color of the channel. The array contains 256 members. Not valid when kind = ChannelType.COMPONENT. For component channel histogram values, use the histogram property of the Document object instead.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of number`


.. property:: kind
	
	The type of the channel.
	
	:Permission: Read-write. 
	
	:Type: :class:`ChannelType`


.. property:: name
	
	The name of the channel.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: opacity
	
	The opacity to use for alpha channels or the solidity to use for spot channels. Valid only when kind = ChannelType.MASKEDAREA or SELECTEDAREA.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..100]`


.. property:: parent
	
	The containing document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: typename
	
	The class name of the referenced channel object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: visible
	
	True if the channel is visible.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


-------
Methods
-------

.. function:: duplicate([targetDocument])
	
	Duplicates the channel.
	
	:Parameters:
		:targetDocument: :class:`Document`
	
	:Returns: :class:`Channel`


.. function:: merge()
	
	Merges a spot channel into the component channels.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: remove()
	
	Deletes the channel.
	
	:Parameters: `null`
	
	:Returns: `undefined`
