========
Document
========

The active containment object for layers and all other objects in the script; the basic canvas for the file.

* Access the object for the currently active document through Application.activeDocument.
* You can access other documents, or iterate through all open documents using the list in the Application.documents collection. You can access individual documents in the list by index, or use Documents.getByName() to retrieve them by name.
* Create documents programmatically using the Documents.add() method. See Document sample script and the Documents collection object for examples.

**Note**: In Adobe Photoshop, a document can also be referred to as an image or a canvas.

* The term image refers to the entire document and its contents. You can trim or crop an image. You resize an image using the resizeImage() method.
* The term canvas refers to the space in which the document sits on the screen. You can rotate or flip the canvas. You resize the canvas using the resizeCanvas() method.


----------
Properties
----------

.. property:: activeChannels
	
	The selected channels.
	
	:Permission: Read-write. 
	
	:Type: :class:`array of Channel`


.. property:: activeHistoryBrushSource
	
	The history state to use with the history brush.
	
	:Permission: Read-write. 
	
	:Type: :class:`Guide`


.. property:: activeHistoryState
	
	The selected HistoryState object.
	
	:Permission: Read-write. 
	
	:Type: :class:`Guide`


.. property:: activeLayer
	
	The selected layer.
	
	:Permission: Read-write. 
	
	:Type: :class:`ArtLayer or LayerSet`


.. property:: artLayers
	
	The art layers collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`ArtLayers`


.. property:: backgroundLayer
	
	The background layer of the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`ArtLayer`


.. property:: bitsPerChannel
	
	The number of bits per channel.
	
	:Permission: Read-write. 
	
	:Type: :class:`BitsPerChannelType`


.. property:: channels
	
	The channels collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`Channels`


.. property:: cloudDocument
	
	This document is in the cloud.
	
	:Permission: Read-only. 
	
	:Type: :class:`boolean`


.. property:: cloudWorkAreaDirectory
	
	Local directory for this cloud document.
	
	:Permission: Read-only. 
	
	:Type: :class:`alias`


.. property:: colorProfileName
	
	The name of the color profile. Valid only when colorProfileType = ColorProfile.CUSTOM or WORKING.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: colorProfileType
	
	Whether the document uses the working color profile, a custom profile, or no profile.
	
	:Permission: Read-write. 
	
	:Type: :class:`ColorProfileType`


.. property:: colorSamplers
	
	The current color samplers associated with this document.
	
	:Permission: Read-only. 
	
	:Type: :class:`ColorSamplers`


.. property:: componentChannels
	
	The color channels that make up the document; for instance, the Red, Green, and Blue channels for an RGB document.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of Channel`


.. property:: countItems
	
	The current count items. Note: For additional information about count items, see Adobe Photoshop help on the Count Tool.
	
	:Permission: Read-only. 
	
	:Type: :class:`CountItems`


.. property:: fullName
	
	The full path name of the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`File`


.. property:: guides
	
	The guides collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`Guides`


.. property:: height
	
	The height of the document (unit value).
	
	:Permission: Read-only. 
	
	:Type: :class:`UnitValue`


.. property:: histogram
	
	A histogram showing the number of pixels at each color intensity level for the composite channel. The array c ontains 256 members. Valid only when mode = DocumentMode.RGB, CMYK; or INDEXEDCOLOR.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of number`


.. property:: historyStates
	
	The history states collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`HistoryStates`


.. property:: info
	
	Metadata about the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`DocumentInfo`


.. property:: layerComps
	
	The layer compositions collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`LayerComps`


.. property:: layers
	
	The layers collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`Layers`


.. property:: layerSets
	
	The layer set collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`LayerSets`


.. property:: managed
	
	True if the document a is workgroup document.
	
	:Permission: Read-only. 
	
	:Type: :class:`boolean`


.. property:: measurementScale
	
	The measurement scale for the document. Note: The measurement scale feature is available in the Extended version only.
	
	:Permission: Read-only. 
	
	:Type: :class:`MeasurementScale`


.. property:: mode
	
	The color profile.
	
	:Permission: Read-only. 
	
	:Type: :class:`DocumentMode`


.. property:: name
	
	The document's name.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: parent
	
	The application object that contains this document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Application`


.. property:: path
	
	The path to the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`File`


.. property:: pathItems
	
	The path items collection.
	
	:Permission: Read-only. 
	
	:Type: :class:`PathItems`


.. property:: pixelAspectRatio
	
	The (custom) pixel aspect ratio to use.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0.100..10.000]`


.. property:: printSettings
	
	The print settings for the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`DocumentPrintSettin gs`


.. property:: quickMaskMode
	
	True if the document is in Quick Mask mode.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: resolution
	
	The document’s resolution (in pixels per inch).
	
	:Permission: Read-only. 
	
	:Type: :class:`number`


.. property:: saved
	
	True if the document has been saved since the last change.
	
	:Permission: Read-only. 
	
	:Type: :class:`boolean`


.. property:: selection
	
	The selected area of the document.
	
	:Permission: Read-only. 
	
	:Type: :class:`Selection`


.. property:: typename
	
	The class name of the Document object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: width
	
	The width of the document (unit value).
	
	:Permission: Read-only. 
	
	:Type: :class:`UnitValue`


.. property:: xmpMetadata
	
	XMP metadata for the document. Camera RAW settings for the image are stored here for example.
	
	:Permission: Read-only. 
	
	:Type: :class:`xmpMetadata`


-------
Methods
-------

.. function:: autoCount(channel, threshold)
	
	Counts the number of objects in a document. Available in the Extended Version only. Creates a CountItem object for each object counted. For additional information about how to set up objects to count, see the Count Tool in the Adobe Photoshop Help
	
	:Parameters:
		:channel: :class:`Channel`
		:threshold: :class:`number`
	
	:Returns: `undefined`


.. function:: changeMode(destinationMode[, options])
	
	Changes the color profile of the document.
	
	:Parameters:
		:destinationMode: :class:`ChangeMode`
		:options: :class:`BitmapConversionOptions or IndexedConversionOptions`
	
	:Returns: `undefined`


.. function:: close([saving])
	
	Closes the document. If any changes have been made, the script presents an alert with three options: save, do not save, prompt to save. The optional parameter specifies a selection in the alert box (default: SaveOptionsType. PROMPTTOSAVECHANGES).
	
	:Parameters:
		:saving: :class:`SaveOptions`
	
	:Returns: `undefined`


.. function:: convertProfile(destinationProfile, intent[, blackPointCompensation, dither])
	
	Changes the color profile. The destinationProfile parameter must be either a string that names the color mode or Working RGB, Working CMYK, Working Gray, Lab Color (meaning one of the working color spaces or Lab color).
	
	:Parameters:
		:destinationProfile: :class:`string`
		:intent: :class:`Intent`
		:blackPointCompensation: :class:`boolean`
		:dither: :class:`boolean`
	
	:Returns: `undefined`


.. function:: crop(bounds[, angle, width, height])
	
	Crops the document. The bounds parameter is an array of four coordinates for the region remaining after cropping, [left, top, right, bottom].
	
	:Parameters:
		:bounds: :class:`array of 4 UnitValue`
		:angle: :class:`number`
		:width: :class:`UnitValue`
		:height: :class:`UnitValue`
	
	:Returns: `undefined`


.. function:: duplicate([name, mergeLayersOnly])
	
	Creates a duplicate of the document object. The optional parameter name provides the name for the duplicated document. The optional parameter mergeLayersOnly indicates whether to only duplicate merged layers.
	
	:Parameters:
		:name: :class:`string`
		:mergeLayersOnly: :class:`boolean`
	
	:Returns: :class:`Document`


.. function:: exportDocument(exportIn[, exportAs, options])
	
	Exports the paths in the document to an Illustrator file, or exports the document to a file with Web or device viewing optimizations. This is equivalent to choosing File > Export > Paths To Illustrator, or File > Save For Web and Devices.
	
	:Parameters:
		:exportIn: :class:`File`
		:exportAs: :class:`ExportType`
		:options: :class:`ExportOptionsIllustrator or ExportOptionsSaveForWeb`
	
	:Returns: `undefined`


.. function:: flatten()
	
	Flattens all layers in the document.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: flipCanvas(direction)
	
	Flips the image within the canvas in the specified direction.
	
	:Parameters:
		:direction: :class:`Direction`
	
	:Returns: `undefined`


.. function:: importAnnotations(file)
	
	Imports annotations into the document.
	
	:Parameters:
		:file: :class:`File`
	
	:Returns: `undefined`


.. function:: mergeVisibleLayers()
	
	Flattens all visible layers in the document.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: paste([intoSelection])
	
	Pastes the contents of the clipboard into the document. If the optional argument is set to true and a selection is active, the contents are pasted into the selection.
	
	:Parameters:
		:intoSelection: :class:`boolean`
	
	:Returns: :class:`ArtLayer`


.. function:: print([sourceSpace, printSpace, intent, blackPointCompensation])
	
	Prints the document. printSpace specifies the color space for the printer. Valid values are nothing (that is, the same as the source); or Working RGB, Working CMYK, Working Gray, Lab Color (meaning one of the working color spaces or Lab color); or a string specifying a specific colorspace (default is same as source).
	
	:Parameters:
		:sourceSpace: :class:`SourceSpaceType`
		:printSpace: :class:`string`
		:intent: :class:`Intent`
		:blackPointCompensation: :class:`boolean`
	
	:Returns: `undefined`


.. function:: printOneCopy()
	
	Print one copy of the document.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: rasterizeAllLayers()
	
	Rasterizes all layers.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: recordMeasurements([source, dataPoints])
	
	Record measurements of document.
	
	:Parameters:
		:source: :class:`MeasurementSource`
		:dataPoints: :class:`array of string`
	
	:Returns: `undefined`


.. function:: resizeCanvas([width, height, anchor])
	
	Changes the size of the canvas to display more or less of the image but does not change the image size. See resizeImage.
	
	:Parameters:
		:width: :class:`UnitValue`
		:height: :class:`UnitValue`
		:anchor: :class:`AnchorPosition`
	
	:Returns: `undefined`


.. function:: resizeImage([width, height, resolution, resampleMethod, amount])
	
	Changes the size of the image. The amount parameter controls the amount of noise value when using preserve details (Range: 0 - 100).
	
	:Parameters:
		:width: :class:`UnitValue`
		:height: :class:`UnitValue`
		:resolution: :class:`number`
		:resampleMethod: :class:`ResampleMethod`
		:amount: :class:`number`
	
	:Returns: `undefined`


.. function:: revealAll()
	
	Expands the document to show clipped sections.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: rotateCanvas(angle)
	
	Rotates the canvas (including the image) in clockwise direction.
	
	:Parameters:
		:angle: :class:`number`
	
	:Returns: `undefined`


.. function:: save()
	
	Saves the document.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: saveAs(saveIn[, options, asCopy, extensionType])
	
	Saves the document in a specific format. Specify the save options appropriate to the format by passing one of these objects: BMPSaveOptions DCS1_SaveOptions DCS2_SaveOptions EPSSaveOptions GIFSaveOptions JPEGSaveOptions PDFSaveOptions PhotoshopSaveOptions PICTFileSaveOptions PICTResourceSaveOptions PixarSaveOptions PNGSaveOptions RawSaveOptions SGIRGBSaveOptions TargaSaveOptions TiffSaveOptions
	
	:Parameters:
		:saveIn: :class:`File`
		:options: :class:`object (see description)`
		:asCopy: :class:`boolean`
		:extensionType: :class:`Extension`
	
	:Returns: `undefined`


.. function:: splitChannels()
	
	Splits the document channels into separate images.
	
	:Parameters: `null`
	
	:Returns: :class:`array of Document`


.. function:: suspendHistory(historyString, javaScriptString)
	
	Provides a single entry in history states for the entire script provided by javaScriptString. Allows a single undo for all actions taken in the script. The historyString parameter provides the string to use for the history state. The javaScriptString parameter provides a string of JavaScript code to excute while history is suspended.
	
	:Parameters:
		:historyString: :class:`string`
		:javaScriptString: :class:`string`
	
	:Returns: `undefined`


.. function:: trap(width)
	
	Applies trapping to a CMYK document. Valid only when docRef.mode = DocumentMode.CMYK.
	
	:Parameters:
		:width: :class:`number`
	
	:Returns: `undefined`


.. function:: trim([type, top, left, bottom, right])
	
	Trims the transparent area around the image on the specified sides of the canvas. Default is true for all Boolean parameters.
	
	:Parameters:
		:type: :class:`TrimType`
		:top: :class:`boolean`
		:left: :class:`boolean`
		:bottom: :class:`boolean`
		:right: :class:`boolean`
	
	:Returns: `undefined`

