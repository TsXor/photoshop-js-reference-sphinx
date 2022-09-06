=======================
BitmapConversionOptions
=======================

Options for converting an image to bitmap mode, using Document.changeMode() with ``ChangeMode.Bitmap`` .

Convert color images to grayscale before converting the image to bitmap mode. See the ArtLayer.desaturate() method.

----------
Properties
----------

.. property:: angle
	
	The angle (in degrees) at which to orient individual dots. See shape. Valid only when method = BitmapConversionType.HALFTONESCREEN.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-180..180]`


.. property:: frequency
	
	The number of printer dots (per inch) to use. Valid only when method = BitmapConversionType.HALFTONESCREEN.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [1.0..999.99]`


.. property:: method
	
	The conversion method to use (default: BitmapConversionType.DIFFUSIONDITHER).
	
	:Permission: Read-write. 
	
	:Type: :class:`BitmapConversionType`


.. property:: patternName
	
	The name of the pattern to use. For information about pre-installed valid patterns, see Adobe Photoshop Help on the bitmap conversion command, or view the options availabe in the Custom Color drop down box after choosing the bitmap conversion command. Valid only when method = BitmapConversionType.CUSTOMPATTERN.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: resolution
	
	The output resolution in pixels per inch (default: 72.0).
	
	:Permission: Read-write. 
	
	:Type: :class:`number`


.. property:: shape
	
	The dot shape to use. Valid only when method = BitmapConversionType.HALFTONESCREEN.
	
	:Permission: Read-write. 
	
	:Type: :class:`BitmapHalfToneType`


.. property:: typename
	
	The class name of the referenced bitmapConversionOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`
