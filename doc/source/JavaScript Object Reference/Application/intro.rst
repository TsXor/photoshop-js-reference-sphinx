===========
Application
===========

The Adobe Adobe Photoshop application object, which is the root of the object model and provides access to all other objects. This object provides application-wide information, such as application defaults and available fonts. It provides many important methods , such as those for opening files and loading documents.

To access the properties and methods, you can use the pre-defined global variable app. For example::

	var docRef = app.documents.add(800, 600, 72, "docRef", NewDocumentMode.RGB);

The properties and methods of the Application object are also available at the top level; you can omit references to the Application object altogether. For example::

	var docRef = documents.add(800, 600, 72, "docRef", NewDocumentMode.RGB);

This usage can be somewhat ambiguous; for clarity, it is recommended that you use an explicit reference to app

----------
Properties
----------

.. property:: activeDocument
	
	The frontmost document. Setting this property is equivalent to clicking an open document in the Adobe Photoshop application to bring it to the front of the screen.
	
	Tip: If there is no open document, accessing this property throws an exception.
	
	:Permission: Read-write.
	
	:Type: :class:`Document`


.. property:: backgroundColor
	
	The default background color and color style for documents.
	
	:Permission: Read-write.
	
	:Type: :class:`SolidColor`


.. property:: build
	
	Information about the application.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: cloudWorkAreaDirectory
	
	Local directory for all cloud documents.
	
	:Permission: Read-only.
	
	:Type: :class:`alias`


.. property:: colorSettings
	
	The name of the current color settings, as selected with Edit > Color Settings.
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: currentTool
	
	The name of the current tool selected.
	
	:Permission: Read-write.
	
	:Type: :class:`string`


.. property:: displayDialogs
	
	The dialog mode for the application, which controls what types of dialogs should be displayed when running scripts.
	
	:Permission: Read-write.
	
	:Type: :class:`DialogModes`


.. property:: documents
	
	The collection of open documents. This is the primary point of access for documents that are currently open in the application. The array allows you to access any open document, or to iterate through all open documents.
	
	:Permission: Read-only.
	
	:Type: :class:`Documents`


.. property:: fonts
	
	The fonts installed on this system.
	
	:Permission: Read-only.
	
	:Type: :class:`TextFonts`


.. property:: foregroundColor
	
	The default foreground color (used to paint, fill, and stroke selections).
	
	:Permission: Read-write.
	
	:Type: :class:`SolidColor`


.. property:: freeMemory
	
	The amount of unused memory available to Adobe Photoshop.
	
	:Permission: Read-only.
	
	:Type: :class:`number`


.. property:: locale
	
	The language location of the application. An Adobe locale code consists of a 2-letter ISO-639 language code and an optional 2-letter ISO 3166 country code separated by an underscore. Case is significant. For example, en_US, en_UK, ja_JP, de_DE, fr_FR.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: macintoshFileTypes
	
	A list of file image types Adobe Photoshop can open.
	
	:Permission: Read-only.
	
	:Type: :class:`array of string`


.. property:: measurementLog
	
	The log of measurements taken.
	
	:Permission: 
	
	:Type: :class:`MeasurementLog`


.. property:: name
	
	The application's name.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: notifiers
	
	The collection of notifiers currently configured (in the Scripts Events Manager menu in the Adobe Photoshop application).
	
	:Permission: Read-only.
	
	:Type: :class:`Notifiers`


.. property:: notifiersEnabled
	
	True if all notifiers are enabled.
	
	:Permission: Read-write.
	
	:Type: :class:`boolean`


.. property:: path
	
	The full path to the location of the Adobe Photoshop application.
	
	:Permission: Read-only.
	
	:Type: :class:`File`


.. property:: playbackDisplayDialogs
	
	The dialog mode for playback mode, which controls what types of dialog to display when playing back a recorded action with the Actions palette.
	
	:Permission: Read-write.
	
	:Type: :class:`DialogModes`


.. property:: playbackParameters
	
	Stores and retrieves parameters used as part of a recorded action. Can be used, for example, to control playback speed.
	
	:Permission: Read-write.
	
	:Type: :class:`ActionDescriptor`


.. property:: preferences
	
	The application preference settings (equivalent to selecting **Edit > Preferences** in the Adobe Photoshop application in Windows or **Photoshop > Preferences** in Mac OS).
	
	:Permission: Read-only.
	
	:Type: :class:`Preferences`


.. property:: preferencesFolder
	
	The full path to the Preferences folder.
	
	:Permission: Read-only.
	
	:Type: :class:`File`


.. property:: recentFiles
	
	Files in the Recent Files list.
	
	:Permission: Read-only.
	
	:Type: :class:`array of File`


.. property:: scriptingBuildDate
	
	The build date of the Scripting interface.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: scriptingVersion
	
	The version of the Scripting interface.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: systemInformation
	
	Runtime details of the application and system.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: typename
	
	The class name of the referenced app object.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: version
	
	The version of Adobe Photoshop application you are running.
	
	:Permission: Read-only.
	
	:Type: :class:`string`


.. property:: windowsFileTypes
	
	A list of file image extensions Adobe Photoshop can open.
	
	:Permission: Read-only.
	
	:Type: :class:`array of string`


-------
Methods
-------

.. function:: batch(inputFiles, action, from[, options])

        Runs the batch automation routine (similar to the **File > Automate > Batch** command).

        :Parameters:
                :inputFiles: :class:`array of File` - specifies the sources for the files to be manipulated by the batch command
                :action: :class:`string`
                :from: :class:`string`
                :options: :class:`BatchOptions`

        :Returns: :class:`string`


.. function:: beep()

        Causes a "beep" sound.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: bringToFront()

        Makes Adobe Photoshop the active (front-most) application.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: changeProgressText(progressString)

        Changes the text that appears in the progress window.

        :Parameters:
                :progressString: :class:`string` - the string to show in the progress window

        :Returns: `undefined`


.. function:: charIDToTypeID(charID)

        Converts from a four character code (character ID) to a runtime ID.

        :Parameters:
                :charID: :class:`string`

        :Returns: :class:`number`


.. function:: compareWithNumbers(first, second)

        :Parameters:
                :first: :class:`string`
                :second: :class:`string`

        :Returns: :class:`number` - 

                0: They are equal.

                Less than 0: Either the value of the first character that does not match is lower in the compared string, or all compared characters match but the compared string is shorter. 

                Greater than 0: Either the value of the first character that does not match is greater in the compared string, or all compared characters match but the compared string is longer. When a number is encountered it is converted from a string to a number. For example, A1, A2, A10 would be the sorting order, instead of A1, A10, A2 with the normal sort routine.


.. function:: doAction(action, from)

        Plays an action from the Actions palette.

        :Parameters:
                :action: :class:`string` - the name of the action
                :from: :class:`string` - the name of the action set

        :Returns: `undefined`


.. function:: doForcedProgress(progressString, javaScriptString)

        Performs a task with a progress bar. Forces progress bar to display, ignoring the normal heuristics that keep it from showing unnecessarily (for example, during very short tasks). Other progress APIs must be called periodically to update the progress bar and allow canceling.

        :Parameters:
                :progressString: :class:`string` - the string to show in the progress window
                :javaScriptString: :class:`string` - the string to execute

        :Returns: `undefined`


.. function:: doProgress(progressString, javaScriptString)

        Performs a task with a progress bar. Other progress APIs must be called periodically to update the progress bar and allow canceling.

        :Parameters:
                :progressString: :class:`string` - the string to show in the progress window
                :javaScriptString: :class:`string` - the string to execute

        :Returns: `undefined`


.. function:: doProgressSegmentTask(segmentLength, done, total, javaScriptString)

        Sections-off a portion of the unused progress bar for execution of a subtask. Returns false on cancel. This method should be used when iterating a list of tasks with unequal run times.

        :Parameters:
                :segmentLength: :class:`number` - the length of the current task
                :done: :class:`number` - the total length of all completed tasks
                :total: :class:`number` - the total length of all tasks
                :javaScriptString: :class:`string` - the string to execute

        :Returns: :class:`boolean`


.. function:: doProgressSubTask(index, limit, javaScriptString)

        Sections-off a portion of the unused progress bar for execution of a subtask. Returns false on cancel. This method should be used when iterating a list of tasks with equal run times.

        :Parameters:
                :index: :class:`number` - the 0-based index of the current task
                :limit: :class:`number` - the total number of tasks
                :javaScriptString: :class:`string` - the string to execute

        :Returns: :class:`boolean`


.. function:: doProgressTask(taskLength, javaScriptString)

        Sections-off a portion of the unused progress bar for execution of a subtask.

        :Parameters:
                :taskLength: :class:`number` - the amount of the unused progress bar to section-off between 0.0 and 1.0
                :javaScriptString: :class:`string` - the string to execute

        :Returns: :class:`boolean` - false on cancel


.. function:: eraseCustomOptions(key)

        Erases the user object with specified ID value from the Photoshop registry.

        :Parameters:
                :key: :class:`string`

        :Returns: `undefined`


.. function:: executeAction(eventID[, descriptor, displayDialogs])

        Plays an Action Manager event.

        :Parameters:
                :eventID: :class:`number`
                :descriptor: :class:`ActionDescriptor`
                :displayDialogs: :class:`DialogModes`

        :Returns: :class:`ActionDescriptor`


.. function:: executeActionGet(reference)

        Obtains information about a predefined or recorded action.

        :Parameters:
                :reference: :class:`ActionReference`

        :Returns: :class:`ActionDescriptor`


.. function:: featureEnabled(name)

        Determines whether the feature specified by name is enabled. The following features are supported as values for name: "photoshop/extended" "photoshop/standard" "photoshop/trial"

        :Parameters:
                :name: :class:`string`

        :Returns: :class:`boolean`


.. function:: getCustomOptions(key)

        Retreives user objects in the Photoshop registry for the ID with value key.

        :Parameters:
                :key: :class:`string`

        :Returns: :class:`ActionDescriptor`


.. function:: isQuicktimeAvailable()

        Returns true if Quicktime is installed.

        :Parameters: `null`

        :Returns: :class:`boolean`


.. function:: load(document)

        Loads a support file (as opposed to a Photoshop image document) from the specified location.

        :Parameters:
                :document: :class:`File`

        :Returns: `undefined`


.. function:: makeContactSheet(inputFiles[, options])

        DEPRECATED for Adobe Photoshop CS4.

        :Parameters:
                :inputFiles: :class:`array of File`
                :options: :class:`ContactSheetOptions`

        :Returns: :class:`string`


.. function:: makePDFPresentation(inputFiles, outputFiles[, options])

        DEPRECATED for Adobe Photoshop CS4.

        :Parameters:
                :inputFiles: :class:`array of File`
                :outputFiles: :class:`File`
                :options: :class:`PresentationOptions`

        :Returns: :class:`string`


.. function:: makePhotoGallery(inputFolder, outputFolder[, options])

        DEPRECATED for Adobe Photoshop CS4.

        :Parameters:
                :inputFolder: :class:`File`
                :outputFolder: :class:`File`
                :options: :class:`GalleryOptions`

        :Returns: :class:`string`


.. function:: makePhotomerge(inputFiles)

        DEPRECATED for Adobe Photoshop.

        Use provided script::

                runphotomergeFromScript = true;
                $.evalFile( app.path + "Presets/Scripts/Photomerge.jsx")
                photomerge.createPanorama( fileList, displayDialog );

        Merges multiple files into one, with user interaction required.

        :Parameters:
                :inputFiles: :class:`array of File`

        :Returns: :class:`string`


.. function:: makePicturePackage(inputFiles[, options])

        DEPRECATED for Adobe Photoshop CS4.

        :Parameters:
                :inputFiles: :class:`array of File`
                :options: :class:`PicturePackageOptions`

        :Returns: :class:`string`


.. function:: open(document[, as, asSmartObject])

        Opens the specified document. Use the optional as parameter to specify the file format using the constants in OpenDocumentType; or, you can specify a file format together with its open options using these objects: :class:`CameraRAWOpenOptions` :class:`DICOMOpenOptions` :class:`EPSOpenOptions` :class:`PDFOpenOptions` :class:`PhotoCDOpenOptions` :class:`RawFormatOpenOptions`. Use the optional parameter asSmartObject (default: false) to create a smart object around the opened document. See the Application sample scripts for an example of using the File object in the open method.

        :Parameters:
                :document: :class:`File`
                :as: :class:`object or OpenDocumentType`
                :asSmartObject: :class:`boolean`

        :Returns: :class:`Document`


.. function:: openDialog()

        Invokes the Photoshop Open dialog box for the user to select files.

        :Parameters: `null`

        :Returns: :class:`array of File` - an array of File objects for the files selected in the dialog


.. function:: purge(target)

        Purges one or more caches.

        :Parameters:
                :target: :class:`PurgeTarget`

        :Returns: `undefined`


.. function:: putCustomOptions(key, customObject[, persistent])

        Saves a customized settings object in the Photoshop registry.

        :Parameters:
                :key: :class:`string`: the unique identifier for your custom settings
                :customObject: :class:`ActionDescriptor`: the object to save in the registry
                :persistent: :class:`boolean`: indicates whether the object should persist once the script has finished

        :Returns: `undefined`


.. function:: refresh()

        Pauses the script while the application refreshes. Use to slow down execution and show the results to the user as the script runs. Use carefully; your script runs much more slowly when using this method.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: refreshFonts()

        Force the font list to get updated.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: runMenuItem(menuID)

        Run a menu item given the menu ID.

        :Parameters:
                :menuID: :class:`number`

        :Returns: `undefined`


.. function:: showColorPicker()

        :Parameters: `null`

        :Returns: :class:`boolean` - false if dialog is cancelled, true otherwise


.. function:: stringIDToTypeID(stringID)

        Converts from a string ID to a runtime ID.

        :Parameters:
                :stringID: :class:`string`

        :Returns: :class:`number`


.. function:: togglePalettes()

        Toggle palette visibility.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: toolSupportsBrushes(tool)

        :Parameters:
                :tool: :class:`string`

        :Returns: :class:`boolean` - true if the specified tool supports brushes, false otherwise


.. function:: toolSupportsBrushPresets(tool)

        :Parameters:
                :tool: :class:`string`

        :Returns: :class:`boolean` - true if the brush supports presets


.. function:: typeIDToCharID(typeID)

        Converts from a runtime ID to a character ID.

        :Parameters:
                :typeID: :class:`number`

        :Returns: :class:`string`


.. function:: typeIDToStringID(typeID)

        Converts from a runtime ID to a string ID.

        :Parameters:
                :typeID: :class:`number`

        :Returns: :class:`string`


.. function:: updateProgress(done, total)

        Updates the progress bar started by doProgress method. This method should be used for manual non-task based progress updating.

        :Parameters:
                :done: :class:`number`: the number of tasks completed
                :total: :class:`number`: the total number of tasks

        :Returns: :class:`boolean` - false on cancel
