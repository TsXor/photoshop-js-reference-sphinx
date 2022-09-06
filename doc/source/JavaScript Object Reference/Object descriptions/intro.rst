===================
Object descriptions
===================

Object properties and methods are described in separate tables for each object. The following sections describe the conventions used in these descriptions.

-------------------
Properties notation
-------------------

The Properties table for an object lists the following:

* The properties defined in each object.
* The value type for each property.

When the value type is a constant or another object, the value is a hypertext link to the listing for that constant or object. 

* The property’s input status: read-only or read-write.
* A description that explains what the property does. 

(a chart here)

For constants, like ``DialogModes`` in the sample, click the link to go to the table that shows allowed values. 
Constants are represented by objects, and allowed values are properties of those objects. Specify a constant value in the form *ConstantName.VALUE.* For example::

	app.displayDialogs = DialogModes.ERROR;

----------------
Methods notation
----------------

The Methods table for an object lists the following:

* The method name.
* The parameters list.
* The parameter value types, on lines corresponding to each parameter.
* Return value type
* A description of what the method does, and further descriptions of parameters, if needed. 

(a chart here)

When a parameter type or return value is a constant or another object, the value is a hypertext link to the listing for that constant or object.

Parameters can be required or optional. Optional parameters are indicated in the table by square brackets ([]). In the example, the first parameters, bounds, is required. The remaining parameters are all optional. 

You must pass a value for each required parameter. You can leave out optional parameters if there are no remaining values to pass; however, if you wish to use the default value for any optional parameter that is not the last one specified, pass undefined as a placeholder. You must enter the values in the order they are listed, so that the JavaScript compiler knows which value you are entering. 

For example, the following passes only the required parameter (using a previously-defined variable for the bounding region)::

	app.activeDocument.crop( myRegion );

The following skips the angle parameter, specifies the width value, and omits the final height value::

	var myWidth = new UnitValue( "500 pixels" );
	app.executeAction( myRegion,undefined,myWidth );

---------------------
But something changed
---------------------

However, in this doc, functions will be documented the way sphinx does, not charts.

You see that (a chart here) above? In this doc they should be:

^^^^^^^^^^^^^^^^^^^^^
Property description:
^^^^^^^^^^^^^^^^^^^^^

.. property:: displayDialogs
	
	The dialog mode for the application, which controls what types of dialogs should be displayed when running scripts.
	
	:Permission: Read-write
	
	:Type: :class:`DialogModes`

^^^^^^^^^^^^^^^^^^^^^
Function description:
^^^^^^^^^^^^^^^^^^^^^

.. function:: crop(bounds[, angle, width, height])
	
	Crops the document. 
	
	:Parameters:
		:bounds: array of 4 :class:`UnitValue`: for the region remaining after cropping, [left, top, right, bottom]
		:angle: number
		:width: :class:`UnitValue`
		:height: :class:`UnitValue`
	
	:Returns: `undefined`