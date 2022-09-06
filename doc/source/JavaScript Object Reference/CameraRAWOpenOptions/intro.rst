====================
CameraRAWOpenOptions
====================

Options for opening a document in Camera RAW format using the Application.open() method.

----------
Properties
----------

.. property:: bitsPerChannel
	
	The number of bits per channel.
	
	:Permission: Read-write. 
	
	:Type: :class:`BitsPerChannelType`


.. property:: blueHue
	
	The blue hue of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: blueSaturation
	
	The blue saturation of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: brightness
	
	The brightness of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..150]`


.. property:: chromaticAberrationBY
	
	The chromatic aberration B/Y of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: chromaticAberrationRC
	
	The chromatic aberration R/C of the shot
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: colorNoiseReduction
	
	The color noise reduction of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..100]`


.. property:: colorSpace
	
	The colorspace for the image.
	
	:Permission: Read-write. 
	
	:Type: :class:`ColorSpaceType`


.. property:: contrast
	
	The contrast of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-50..100]`


.. property:: exposure
	
	The exposure of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-4.0..4.0]`


.. property:: greenHue
	
	The green hue of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: greenSaturation
	
	The green saturation of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: luminanceSmoothing
	
	The luminance smoothing of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..100]`


.. property:: redHue
	
	The red hue of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: redSaturation
	
	The red saturation of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: resolution
	
	The resolution of the document in pixels per inch.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [1..999]`


.. property:: saturation
	
	The saturation of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: settings
	
	The global settings for all Camera RAW options. Default: CameraRAWSettingsType.CAMERA.
	
	:Permission: Read-write. 
	
	:Type: :class:`CameraRAWSettingsType`


.. property:: shadows
	
	The shadows of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..100]`


.. property:: shadowTint
	
	The shadow tint of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: sharpness
	
	The sharpness of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0..100]`


.. property:: size
	
	The size of the new document.
	
	:Permission: Read-write. 
	
	:Type: :class:`CameraRAWSize`


.. property:: temperature
	
	The temperature of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [2000..50000]`


.. property:: tint
	
	The tint of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-150..150]`


.. property:: typename
	
	The class name of the referenced cameraRAWOpenOptions object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: vignettingAmount
	
	The vignetting amount of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: vignettingMidpoint
	
	The vignetting mid point of the shot.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [-100..100]`


.. property:: whiteBalance
	
	The white balance options for the image. These are lighting conditions that affect color balance.
	
	:Permission: Read-write. 
	
	:Type: :class:`WhiteBalanceType`
