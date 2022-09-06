==========
ActionList
==========

This object provides an array-style mechanism for storing data. It can be used for low-level access into Photoshop.

This object is ideal when storing data of the same type. All items in the list must be of the same type.

You can use the "put" methods, such as putBoolean(), to append new elements, and can clear the entire list using clear(), but cannot otherwise modify the list.

Note: The ``ActionList`` object is part of the Action Manager functionality. For details on using the Action Manager, see the *Photoshop Scripting Guide*.

----------
Properties
----------

.. property:: count
	
	The number of commands that comprise the action.
	
	:Permission: Read-only
	
	:Type: :class:`number`


.. property:: typename
	
	The class name of the referenced :class:`ActionList` object.
	
	:Permission: Read-only
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: clear()

        Clears the list.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: getBoolean(index)

        Gets the value of a list element of type boolean.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`boolean`


.. function:: getClass(index)

        Gets the value of a list element of type class.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getData(index)

        Gets raw byte data as a string value.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`string`


.. function:: getDouble(index)

        Gets the value of a list element of type double.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getEnumerationType(index)

        Gets the enumeration type of a list element.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getEnumerationValue(index)

        Gets the enumeration value of a list element.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getInteger(index)

        Gets the value of a list element of type integer.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getLargeInteger(index)

        Gets the value of a list element of type large integer.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getList(index)

        Gets the value of a list element of type list.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`ActionList`


.. function:: getObjectType(index)

        Gets the class ID of a list element of type object.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getObjectValue(index)

        Gets the value of a list element of type object.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`ActionDescriptor`


.. function:: getPath(index)

        Gets the value of a list element of type File.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`File`


.. function:: getReference(index)

        Gets the value of a list element of type ActionReference.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`ActionReference`


.. function:: getString(index)

        Gets the value of a list element of type string.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`string`


.. function:: getType(index)

        Gets the type of a list element.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`DescValueType`


.. function:: getUnitDoubleType(index)

        Gets the unit value type of a list element of type Double.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getUnitDoubleValue(index)

        Gets the unit value of a list element of type double.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: putBoolean(value)

        Appends a new value, true or false.

        :Parameters:
                :value: :class:`boolean`

        :Returns: `undefined`


.. function:: putClass(value)

        Appends a new value, a class or data type.

        :Parameters:
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putData(value)

        Appends a new value, a string containing raw byte data.

        :Parameters:
                :value: :class:`string`

        :Returns: `undefined`


.. function:: putDouble(value)

        Appends a new value, a double.

        :Parameters:
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putEnumerated(enumType,value)

        Appends a new value, an enumerated (constant) value.

        :Parameters:
                :enumType: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putInteger(value)

        Appends a new value, an integer.

        :Parameters:
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putLargeInteger(value)

        Appends a new value, a large integer.

        :Parameters:
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putList(value)

        Appends a new value, a nested action list.

        :Parameters:
                :value: :class:`ActionList`

        :Returns: `undefined`


.. function:: putObject(classID,value)

        Appends a new value, an object.

        :Parameters:
                :classID: :class:`number`
                :value: :class:`ActionDescriptor`

        :Returns: `undefined`


.. function:: putPath(value)

        Appends a new value, a path.

        :Parameters:
                :value: :class:`File`

        :Returns: `undefined`


.. function:: putReference(value)

        Appends a new value, a reference to an object created in the script.

        :Parameters:
                :value: :class:`ActionReference`

        :Returns: `undefined`


.. function:: putString(value)

        Appends a new value, a string.

        :Parameters:
                :value: :class:`string`

        :Returns: `undefined`


.. function:: putUnitDouble(classID,value)

        Appends a new value, a unit/value pair.

        :Parameters:
                :classID: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`
