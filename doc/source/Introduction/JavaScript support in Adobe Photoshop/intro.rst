=====================================
JavaScript support in Adobe Photoshop
=====================================

For a JavaScript file to be recognized by Photoshop as a valid script file, it must use either a ``.js`` or a ``.jsx`` extension. 

On the Mac OS, there is no difference in the way scripts with the two extensions function. On Windows, if the script files is opened from inside Photoshop, there is no difference between using the ``.js`` and ``.jsx`` extension. However, if the script is launched by double-clicking on it, a script with the ``.js`` extension is interpreted with the Microsoft JScript engine, and it cannot launch Adobe Photoshop. For Windows, using the ``.jsx`` extension is preferrable, since it interprets the script with the ExtendScript engine.

All of the Adobe Creative Cloud applications, including Adobe Photoshop, use ExtendScript, Adobe’s extended implementation of JavaScript. ExtendScript files are distinguished by the ``.jsx`` extension. ExtendScript offers all standard JavaScript features, plus additional features and utilities, such as:

* A debugging environment (the ExtendScript Toolkit)
* A localization utility
* Tools that allow you to combine scripts and direct them to particular applications
* Platform-independent file and folder representation 

Many of the JavaScript objects and methods use objects defined in ExtendScript, such as the ``File`` object, the ``Folder`` object, and the ``UnitValue`` object. For that reason, using the ``.jsx`` extension for your script files is preferable.

For details of these and additional features, see the JavaScript Tools Guide. This document is installed with Creative Cloud applications at these locations:

* In Windows: ``C:\Program Files\Adobe\Adobe Utilities\ExtendScript Toolkit CC\SDK``
* In Mac OS: ``Applications/Utilities/Adobe Utilities/ExtendScript Toolkit CC/SDK``

The latest versions of this document and of the ExtendScript Tookit, can also be downloaded from Adobe Developer Center, http://www.adobe.com/devnet/

-----------------
Executing scripts
-----------------

The Adobe Photoshop interface includes a Scripts menu (**File > Scripts**) which provides quick and easy access to your JavaScripts. Scripts can be listed directly as menu items that run when you select them, or you can navigate to and run any JavaScript in your file system.

If Adobe Photoshop encounters an error during script execution, it displays the error message.

^^^^^^^^^^^^^^^^^^
Installing scripts
^^^^^^^^^^^^^^^^^^

To install a JavaScript in the Scripts menu, place it in the Scripts folder (**Photoshop/Presets/Scripts**). The names of the scripts in the Scripts folder, without the file name extension, will be displayed in the Scripts menu. Any number of scripts may be installed in the Scripts menu.

Scripts added to the Scripts folder while Adobe Photoshop is running will not appear in the Scripts menu until the next time you launch the application.

All scripts found in the Scripts folder and sub-folders are displayed at the top level of the **File > Scripts** menu. The addition of sub-folders does not add a hierarchical organization to the Scripts menu.

^^^^^^^^^^^^^^^^^^^^^^^
Executing other scripts
^^^^^^^^^^^^^^^^^^^^^^^

The **Browse** item at the end of the **Scripts** menu (**File > Scripts > Browse**) allows you to execute scripts which are not installed in the Scripts folder. You can also use Browse to select scripts installed in the Scripts folder after the application was last launched. 

Selecting **Browse** displays a file browser dialog which allows you to select a script file for execution. Only ``.js`` or ``.jsx`` files are displayed in the browse dialog. When you select a script file, it is executed the same way as an installed script.

---------------
Startup scripts
---------------

On startup, Adobe Photoshop executes all .jsx files that it finds in the startup folders. 

* On Windows, the startup folder for user-defined scripts is: ``C:\Program Files\Common Files\Adobe\Startup Scripts CC\Adobe Photoshop``
* On Mac OS, the startup folder for user-defined scripts is: ``~/Library/Application Support/Adobe/Startup Scripts CC/Adobe Photoshop``

If a script is meant to be executed only by Adobe Photoshop, it must include code such as the following::

	if( BridgeTalk.appName == "photoshop" ) {
		//continue executing script
	}

For additional details, see the *JavaScript Tools Guide*.