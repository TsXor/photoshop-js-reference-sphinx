========
ArtLayer
========

An object within a document that contains the visual elements of the image (equivalent to a layer in the Adobe Photoshop application).

Access an art layer in a document through the Document.artLayers collection. You can access a layer by name; for example::

	var layerRef = app.activeDocument.artLayers.getByName("my layer");
	layerRef.allLocked = true;

Access the art layers in a layer set through the LayerSet.artLayers collection in the parent set.

----------
Properties
----------

.. property:: allLocked
	
	True to completely lock the contents and settings of this layer.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: blendMode
	
	The blending mode.
	
	:Permission: Read-write. 
	
	:Type: :class:`BlendMode`


.. property:: bounds
	
	An array of coordinates that describes the bounding rectangle of the layer.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of UnitValue`


.. property:: boundsNoEffects
	
	An array of coordinates that describes the bounding rectangle of the layer not including effects.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of UnitValue`


.. property:: fillOpacity
	
	The interior opacity of the layer, a percentage value.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0.0..100]`


.. property:: filterMaskDensity
	
	The density of the filter mask (between 0.0 and 250.0)
	
	:Permission: Read-write. 
	
	:Type: :class:`double`


.. property:: filterMaskFeather
	
	The feather of the filter mask (between 0.0 and 250.0)
	
	:Permission: Read-write. 
	
	:Type: :class:`double`


.. property:: grouped
	
	True if this layer is grouped with the layer beneath it.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: isBackgroundLayer
	
	True if this is the background layer of the document. A document can have only one background layer. If there is no background layer, setting this to true causes this to become the background layer.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: kind
	
	Sets the type (such as 'text layer') for an empty layer. Valid only when the layer is empty and when isBackgroundLayer is false. See isBackgroundLayer. You can use the kind property to make a background layer a normal layer; however, to make a layer a background layer, you must set isBackgroundLayer to true.
	
	:Permission: Read-write. 
	
	:Type: :class:`LayerKind`


.. property:: layerMaskDensity
	
	The density of the layer mask (between 0.0 and 100.0)
	
	:Permission: Read-write. 
	
	:Type: :class:`double`


.. property:: layerMaskFeather
	
	The feather of the layer mask (between 0.0 and 250.0)
	
	:Permission: Read-write. 
	
	:Type: :class:`double`


.. property:: linkedLayers
	
	The layers linked to this layer. See ArtLayer.link.
	
	:Permission: Read-only. 
	
	:Type: :class:`array of ArtLayer or LayerSet`


.. property:: name
	
	The name.
	
	:Permission: Read-write. 
	
	:Type: :class:`string`


.. property:: opacity
	
	The master opacity of the layer, a percentage value.
	
	:Permission: Read-write. 
	
	:Type: :class:`number [0.0..100.0].`


.. property:: parent
	
	The object's container.
	
	:Permission: Read-only. 
	
	:Type: :class:`Document`


.. property:: pixelsLocked
	
	True if the pixels in the layer’s image cannot be edited using the paintbrush tool.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: positionLocked
	
	True if the pixels in the layer’s image cannot be moved within the layer.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: textItem
	
	The text item that is associated with the layer. Valid only when kind = LayerKind.TEXT.
	
	:Permission: Read-only. 
	
	:Type: :class:`TextItem`


.. property:: transparentPixelsLocked
	
	True if editing is confined to the opaque portions of the layer.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: typename
	
	The class name of the referenced artLayer object.
	
	:Permission: Read-only. 
	
	:Type: :class:`string`


.. property:: vectorMaskDensity
	
	The density of the vector mask (between 0.0 and 250.0)
	
	:Permission: Read-write. 
	
	:Type: :class:`double`


.. property:: vectorMaskFeather
	
	The feather of the vector mask (between 0.0 and 250.0)
	
	:Permission: Read-write. 
	
	:Type: :class:`double`


.. property:: visible
	
	True if the layer is visible.
	
	:Permission: Read-write. 
	
	:Type: :class:`boolean`


.. property:: xmpMetadata
	
	Metadata for the layer.
	
	:Permission: Read-write. 
	
	:Type: :class:`xmpMetadata`


-------
Methods
-------

.. function:: adjustBrightnessContrast(brightness, contrast)
	
	Adjusts the brightness in the range [-100..100] and contrast [-100..100].
	
	:Parameters:
		:brightness: :class:`number`
		:contrast: :class:`number`
	
	:Returns: `undefined`


.. function:: adjustColorBalance([shadows, midtones, highlights, preserveLuminosity])
	
	Adjusts the color balance of the layer’s component channels. For shadows, midtones, and highlights, the array must include three values in the range [-100..100], which represent cyan or red, magenta or green, and yellow or blue, when the document mode is CMYK or RGB. See Document.mode.
	
	:Parameters:
		:shadows: :class:`array of number`
		:midtones: :class:`array of number`
		:highlights: :class:`array of number`
		:preserveLuminosity: :class:`boolean`
	
	:Returns: `undefined`


.. function:: adjustCurves(curveShape)
	
	Adjusts the tonal range of the selected channel using up to fourteen points. Each value in the curveShape array is a point pair, an array of an x and y integer value.
	
	:Parameters:
		:curveShape: :class:`array of array of number`
	
	:Returns: `undefined`


.. function:: adjustLevels(inputRangeStart, inputRangeEnd, inputRangeGamma, outputRangeStart, outputRangeEnd)
	
	Adjusts the levels of the selected channels
	
	:Parameters:
		:inputRangeStart: :class:`number[0..253]`
		:inputRangeEnd: :class:`number[(start+2)..255]`
		:inputRangeGamma: :class:`number[0.10..9.99]`
		:outputRangeStart: :class:`number[0..253]`
		:outputRangeEnd: :class:`number[(start+2)..255]`
	
	:Returns: `undefined`


.. function:: applyAddNoise(amount, distribution, monochromatic)
	
	Applies the Add Noise filter amount is a percentage value.
	
	:Parameters:
		:amount: :class:`number[0.1..400]`
		:distribution: :class:`NoiseDistribution`
		:monochromatic: :class:`boolean`
	
	:Returns: `undefined`


.. function:: applyAverage()
	
	Applies the Average filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyBlur()
	
	Applies the Blur filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyBlurMore()
	
	Applies the Blur More filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyClouds()
	
	Applies the Clouds filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyCustomFilter(characteristics, scale, offset)
	
	Applies a custom filter. The characteristics array has 25 members. See Adobe Photoshop Help for specific instructions.
	
	:Parameters:
		:characteristics: :class:`array of number`
		:scale: :class:`number`
		:offset: :class:`number`
	
	:Returns: `undefined`


.. function:: applyDeInterlace(eliminateFields, createFields)
	
	Applies the De-Interlace filter.
	
	:Parameters:
		:eliminateFields: :class:`EliminateFields`
		:createFields: :class:`CreateFields`
	
	:Returns: `undefined`


.. function:: applyDespeckle()
	
	Applies the Despeckle filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyDifferenceClouds()
	
	Applies the Difference Clouds filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyDiffuseGlow(graininess, glowAmount, clearAmount)
	
	Applies the Diffuse Glow filter.
	
	:Parameters:
		:graininess: :class:`number[0..10]`
		:glowAmount: :class:`number[0..20]`
		:clearAmount: :class:`number[0..20]`
	
	:Returns: `undefined`


.. function:: applyDisplace(horizontalScale, verticalScale, displacement, undefinedareas, displacementMapFiles)
	
	Applies the Displace filter using the specified horizontal and vertical scale, mapping type, treatment of undistorted areas, and path to the distortion image map.
	
	:Parameters:
		:horizontalScale: :class:`number[-999..999]`
		:verticalScale: :class:`number[-999..999]`
		:displacement: :class:`DisplacementMapType`
		:undefinedareas: :class:`UndefinedAreas`
		:displacementMapFiles: :class:`File`
	
	:Returns: `undefined`


.. function:: applyDustAndScratches(radius, threshold)
	
	Applies the Dust & Scratches filter.
	
	:Parameters:
		:radius: :class:`number[1..100]`
		:threshold: :class:`number[0..255]`
	
	:Returns: `undefined`


.. function:: applyGaussianBlur(radius)
	
	Applies the Gaussian Blur filter within the specified radius (in pixels)
	
	:Parameters:
		:radius: :class:`number[0.1..250.0]`
	
	:Returns: `undefined`


.. function:: applyGlassEffect(distortion, smoothness, scaling[, invert, texture, textureFile])
	
	Applies the Glass filter. scaling is a percentage value.
	
	:Parameters:
		:distortion: :class:`number[0..20]`
		:smoothness: :class:`number[1..15]`
		:scaling: :class:`number[50..200]`
		:invert: :class:`boolean`
		:texture: :class:`TextureType`
		:textureFile: :class:`File`
	
	:Returns: `undefined`


.. function:: applyHighPass(radius)
	
	Applies the High Pass filter within the specified radius.
	
	:Parameters:
		:radius: :class:`number[0.1..250.0]`
	
	:Returns: `undefined`


.. function:: applyLensBlur([source, focalDistance, invertDepthMap, shape, radius, bladeCurvature, rotation, brightness, threshold, amount, distribution, monochromatic])
	
	Applies the Lens Blur filter. source: The source for the depth map (default: DepthMapSource.NONE) focalDistance : The blur focal distance for the depth map (default: 0). invertDepthMask : True if the depth map is inverted (default: false). shape: The shape of the iris (default: Geometry.HEXAGON) radius: The radius of the iris (default: 15). bladeCurvature: The blade curvature of the iris (default: 0). rotation: The rotation of the iris (default: 0) brightness: The brightness for the specular highlights (default: 0). threshold: The threshold for the specular highlights (default: 0). amount: The amount of noise (default: 0) distribution: The distribution value for the noise (default: NoiseDistribution.UNIFORM). monochromatic: True if the noise is monochromatic (default: false).
	
	:Parameters:
		:source: :class:`DepthMapSource`
		:focalDistance: :class:`number`
		:invertDepthMap: :class:`boolean`
		:shape: :class:`Geometry`
		:radius: :class:`number`
		:bladeCurvature: :class:`number`
		:rotation: :class:`number`
		:brightness: :class:`number`
		:threshold: :class:`number`
		:amount: :class:`number`
		:distribution: :class:`NoiseDistribution`
		:monochromatic: :class:`boolean`
	
	:Returns: `undefined`


.. function:: applyLensFlare(brightness, flareCenter, lensType)
	
	Applies the Lens Flare filter with the specified brightness (0 - 300, as a percentage), the x and y coordinates (unit value) of the flare center, and the lens type.
	
	:Parameters:
		:brightness: :class:`number`
		:flareCenter: :class:`array(UnitValue)`
		:lensType: :class:`LensType`
	
	:Returns: `undefined`


.. function:: applyMaximum(radius)
	
	Applies the Maximum filter within the specified radius (in pixels).
	
	:Parameters:
		:radius: :class:`number[1..100]`
	
	:Returns: `undefined`


.. function:: applyMedianNoise(radius)
	
	Applies the Median Noise filter within the specified radius (in pixels).
	
	:Parameters:
		:radius: :class:`number[1..100]`
	
	:Returns: `undefined`


.. function:: applyMinimum(radius)
	
	Applies the Minimum filter within the specified radius (in pixels) (1 - 100).
	
	:Parameters:
		:radius: :class:`number[1..100]`
	
	:Returns: `undefined`


.. function:: applyMotionBlur(angle, radius)
	
	Applies the Motion Blur filter.
	
	:Parameters:
		:angle: :class:`number[-360..360]`
		:radius: :class:`number[1..999]`
	
	:Returns: `undefined`


.. function:: applyNTSC()
	
	Applies the NTSC colors filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyOceanRipple(size, magnitude)
	
	Applies the Ocean Ripple filter.
	
	:Parameters:
		:size: :class:`number[1..15]`
		:magnitude: :class:`number[0..20]`
	
	:Returns: `undefined`


.. function:: applyOffset(horizontal, vertical, undefinedAreas)
	
	Moves the layer the specified amount horizontally and vertically (min/max amounts depend on layer size), leaving an undefined area at the layer’s original location.
	
	:Parameters:
		:horizontal: :class:`UnitValue`
		:vertical: :class:`UnitValue`
		:undefinedAreas: :class:`OffsetUndefinedAreas`
	
	:Returns: `undefined`


.. function:: applyPinch(amount)
	
	Applies the Pinch filter. amount is a percentage value.
	
	:Parameters:
		:amount: :class:`number[-100..100]`
	
	:Returns: `undefined`


.. function:: applyPolarCoordinates(conversion)
	
	Applies the Polar Coordinates filter.
	
	:Parameters:
		:conversion: :class:`PolarConversionType`
	
	:Returns: `undefined`


.. function:: applyRadialBlur(amount, blurMethod, blurQuality[, blurCenter])
	
	Applies the Radial Blur filter in the specified amount, using either a spin or zoom effect and the specified quality. The parameter blurCenter is the position (unit value).
	
	:Parameters:
		:amount: :class:`number[1..100]`
		:blurMethod: :class:`RadialBlurMethod`
		:blurQuality: :class:`RadialBlurQuality`
		:blurCenter: :class:`UnitValue`
	
	:Returns: `undefined`


.. function:: applyRipple(amount, size)
	
	Applies the Ripple filter in the specified amount, throughout the image and in the specified size.
	
	:Parameters:
		:amount: :class:`number[-999..999]`
		:size: :class:`RippleSize`
	
	:Returns: `undefined`


.. function:: applySharpen()
	
	Applies the Sharpen filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applySharpenEdges()
	
	Applies the Sharpen Edges filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applySharpenMore()
	
	Applies the Sharpen More filter.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: applyShear(curve, undefinedAreas)
	
	Applies the Shear filter. The curve defines a curve with [2..255] points. Each value in the curve array is a point pair, an array of an x and y integer value.
	
	:Parameters:
		:curve: :class:`array of array of number`
		:undefinedAreas: :class:`UndefinedAreas`
	
	:Returns: `undefined`


.. function:: applySmartBlur(radius, threshold, blurQuality, mode)
	
	Applies the Smart Blur filter.
	
	:Parameters:
		:radius: :class:`number[0.1..100.0]`
		:threshold: :class:`number[0.1..100.0]`
		:blurQuality: :class:`SmartBlurQuality`
		:mode: :class:`SmartBlurMode`
	
	:Returns: `undefined`


.. function:: applySpherize(amount, mode)
	
	Applies the Spherize filter. amount is a percentage value.
	
	:Parameters:
		:amount: :class:`number[-100..100]`
		:mode: :class:`SpherizeMode`
	
	:Returns: `undefined`


.. function:: applyStyle(styleName)
	
	Applies the specified style to the layer. You must use a style from the Styles list in the Layer Styles Palette.
	
	:Parameters:
		:styleName: :class:`string`
	
	:Returns: `undefined`


.. function:: applyTextureFill(textureFile)
	
	Applies the Texture Fill filter.
	
	:Parameters:
		:textureFile: :class:`File`
	
	:Returns: `undefined`


.. function:: applyTwirl(angle)
	
	Applies the Twirl filter.
	
	:Parameters:
		:angle: :class:`number[-999..999]`
	
	:Returns: `undefined`


.. function:: applyUnSharpMask(amount, radius, threshold)
	
	Applies the Unsharp Mask filter. (amount is a percentage value.
	
	:Parameters:
		:amount: :class:`number[1..500]`
		:radius: :class:`number[0.1..250.0]`
		:threshold: :class:`number[0..255]`
	
	:Returns: `undefined`


.. function:: applyWave(generatorNumber, minimumWavelength, maximumWavelength, minimumAmplitude, maximumAmplitude, horizontalScale, verticalScale, waveType, undefinedAreas, randomSeed)
	
	Applies the Wave filter. Scale factors are percentage values.
	
	:Parameters:
		:generatorNumber: :class:`number[1..999]`
		:minimumWavelength: :class:`number[1..998]`
		:maximumWavelength: :class:`number[2..min+1]`
		:minimumAmplitude: :class:`number[1..998]`
		:maximumAmplitude: :class:`number[2..min+1]`
		:horizontalScale: :class:`number[1..100]`
		:verticalScale: :class:`number[1..100]`
		:waveType: :class:`WaveType`
		:undefinedAreas: :class:`UndefinedAreas`
		:randomSeed: :class:`number`
	
	:Returns: `undefined`


.. function:: applyZigZag(amount, ridges, style)
	
	Applies the Zigzag filter.
	
	:Parameters:
		:amount: :class:`number[-100..100]`
		:ridges: :class:`number[0..20]`
		:style: :class:`ZigZagType`
	
	:Returns: `undefined`


.. function:: autoContrast()
	
	Adjusts the contrast of the selected channels automatically.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: autoLevels()
	
	Adjusts the levels of the selected channels using the auto levels option.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: clear()
	
	Cuts the layer without moving it to the clipboard.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: copy([merge])
	
	Copies the layer to the clipboard. When the optional argument is set to true, a merged copy is performed (that is, all visible layers are copied to the clipboard).
	
	:Parameters:
		:merge: :class:`boolean`
	
	:Returns: `undefined`


.. function:: cut()
	
	Cuts the layer to the clipboard.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: desaturate()
	
	Converts a color image to a grayscale image in the current color mode by assigning equal values of each component color to each pixel.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: duplicate([relativeObject, insertionLocation])
	
	Creates a duplicate of the object on the screen.
	
	:Parameters:
		:relativeObject: :class:`ArtLayer or LayerSet`
		:insertionLocation: :class:`ElementPlacement`
	
	:Returns: :class:`ArtLayer or LayerSet`


.. function:: equalize()
	
	Redistributes the brightness values of pixels in an image to more evenly represent the entire range of brightness levels within the image.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: invert()
	
	Inverts the colors in the layer by converting the brightness value of each pixel in the channels to the inverse value on the 256-step color-values scale.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: link(with)
	
	Links the layer with the specified layer.
	
	:Parameters:
		:with: :class:`ArtLayer or LayerSet`
	
	:Returns: `undefined`


.. function:: merge()
	
	Merges the layer down, removing the layer from the document; returns a reference to the art layer that this layer is merged into.
	
	:Parameters: `null`
	
	:Returns: :class:`ArtLayer`


.. function:: mixChannels(outputChannels[, monochrome])
	
	Modifies a targeted (output) color channel using a mix of the existing color channels in the image. The outputChannels parameter is an array of channel specifications. For each component channel, specify a list of adjustment values in the range [-200..200] followed by a 'constant' value [-200..200].) When monochrome = true, the maximum number of channel value specifications is 1. Valid only when docRef.mode = DocumentMode.RGB or CMYK. RGB arrays must include four values. CMYK arrays must include five values.
	
	:Parameters:
		:outputChannels: :class:`array of array of number`
		:monochrome: :class:`boolean`
	
	:Returns: `undefined`


.. function:: move(relativeObject, insertionLocation)
	
	Moves the layer relative to the object specified in parameters. For art layers, only the constant values ElementPlacement. PLACEBEFORE and PLACEAFTER are valid. For layer sets, only the constant values ElementPlacement. PLACEBEFORE and INSIDE are valid.
	
	:Parameters:
		:relativeObject: :class:`ArtLayer or LayerSet`
		:insertionLocation: :class:`ElementPlacement`
	
	:Returns: `undefined`


.. function:: photoFilter([fillColor, density, preserveLuminosity])
	
	Adjust the layer’s color balance and temperature as if a color filter had been applied. density is a percentage value.
	
	:Parameters:
		:fillColor: :class:`SolidColor`
		:density: :class:`number[1..100]`
		:preserveLuminosity: :class:`boolean`
	
	:Returns: `undefined`


.. function:: posterize(levels)
	
	Specifies the number of tonal levels for each channel and then maps pixels to the closest matching level.
	
	:Parameters:
		:levels: :class:`number[2..225]`
	
	:Returns: `undefined`


.. function:: rasterize(target)
	
	Converts the targeted contents in the layer into a flat, raster image.
	
	:Parameters:
		:target: :class:`RasterizeType`
	
	:Returns: `undefined`


.. function:: remove()
	
	Deletes the object.
	
	:Parameters: `null`
	
	:Returns: `undefined`


.. function:: resize([horizontal, vertical, anchor])
	
	Resizes the layer to the specified dimensions (as a percentage of its current size) and places it in the specified position.
	
	:Parameters:
		:horizontal: :class:`number`
		:vertical: :class:`number`
		:anchor: :class:`AnchorPosition`
	
	:Returns: `undefined`


.. function:: rotate(angle[, anchor])
	
	Rotates rotates the layer around the specified anchor point (default: MIDDLECENTER).
	
	:Parameters:
		:angle: :class:`number`
		:anchor: :class:`AnchorPosition`
	
	:Returns: `undefined`


.. function:: selectiveColor(selectionMethod[, reds, yellows, greens, cyans, blues, magentas, whites, neutrals, blacks])
	
	Modifies the amount of a process color in a specified primary color without affecting the other primary colors. Each color array must have four values.
	
	:Parameters:
		:selectionMethod: :class:`AdjustmentReference`
		:reds: :class:`array of number`
		:yellows: :class:`array of number`
		:greens: :class:`array of number`
		:cyans: :class:`array of number`
		:blues: :class:`array of number`
		:magentas: :class:`array of number`
		:whites: :class:`array of number`
		:neutrals: :class:`array of number`
		:blacks: :class:`array of number`
	
	:Returns: `undefined`


.. function:: shadowHighlight([shadowAmount, shadowWidth, shadowRadius, highlightAmount, highlightWidth, highlightRadius, colorCorrection, midtoneContrast, blackClip, whiteClip])
	
	Adjusts the range of tones in the image’s shadows and highlights. Amounts and widths are percentage values. Radius values are in pixels.
	
	:Parameters:
		:shadowAmount: :class:`number[0..100]`
		:shadowWidth: :class:`number[0.100]`
		:shadowRadius: :class:`number[0..2500]`
		:highlightAmount: :class:`number[0..100]`
		:highlightWidth: :class:`number[0..100]`
		:highlightRadius: :class:`number[0..2500]`
		:colorCorrection: :class:`number[-100..100]`
		:midtoneContrast: :class:`number[-100..100]`
		:blackClip: :class:`number[0.000..50.000]`
		:whiteClip: :class:`number[0.000..50.000]`
	
	:Returns: `undefined`


.. function:: threshold(level)
	
	Converts grayscale or color images to high-contrast, B/W images by converting pixels lighter than the specified threshold to white and pixels darker than the threshold to black.
	
	:Parameters:
		:level: :class:`number[1..255]`
	
	:Returns: `undefined`


.. function:: translate([deltaX, deltaY])
	
	Moves the layer the specified amount (in the given unit) relative to its current position.
	
	:Parameters:
		:deltaX: :class:`UnitValue`
		:deltaY: :class:`UnitValue`
	
	:Returns: `undefined`


.. function:: unlink()
	
	Unlinks the layer.
	
	:Parameters: `null`
	
	:Returns: `undefined`

