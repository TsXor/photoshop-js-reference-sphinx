================
ActionDescriptor
================

This object provides a dictionary-style mechanism for storing data as key-value pairs. It can be used for low-level access into Photoshop. See an example of this usage in ‘Selection sample script’ on page 170.

Many configuration files use serialized action descriptors to represent their data. It is used, for example, to encapsulate playback options in Application.playbackParameters, and is returned by Application.getCustomOptions().

----------
Properties
----------

.. property:: count
	
	The number of keys contained in the descriptor.
	
	:Permission: Read-only
	
	:Type: :class:`number`


.. property:: typename
	
	The class name of the referenced :class:`ActionDescriptor` object.
	
	:Permission: Read-only
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: clear()

        Clears the descriptor.

        :Parameters: `null`

        :Returns: `undefined`


.. function:: erase(key)

        Erases a key from the descriptor.

        :Parameters:
                :key: :class:`number`

        :Returns: `undefined`


.. function:: fromStream(value)

        Creates a descriptor from a stream of bytes; for reading from disk.

        :Parameters:
                :value: :class:`string`

        :Returns: `undefined`


.. function:: getBoolean(key)

        Gets the value of a key of type boolean.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`boolean`


.. function:: getClass(key)

        Gets the value of a key of type class.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getData(key)

        Gets raw byte data as a string value.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`string`


.. function:: getDouble(key)

        Gets the value of a key of type double.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getEnumerationType(key)

        Gets the enumeration type of a key.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getEnumerationValue(key)

        Gets the enumeration value of a key.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getInteger(key)

        Gets the value of a key of type integer.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getKey(index)

        Gets the ID of the Nth key, provided by index.

        :Parameters:
                :index: :class:`number`

        :Returns: :class:`number`


.. function:: getLargeInteger(key)

        Gets the value of a key of type large integer.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getList(key)

        Gets the value of a key of type list.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`ActionList`


.. function:: getObjectType(key)

        Gets the class ID of an object in a key of type object.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getObjectValue(key)

        Gets the value of a key of type object.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`ActionDescriptor`


.. function:: getPath(key)

        Gets the value of a key of type File.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`File`


.. function:: getReference(key)

        Gets the value of a key of type ActionReference.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`ActionReference`


.. function:: getString(key)

        Gets the value of a key of type string.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`string`


.. function:: getType(key)

        Gets the type of a key.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`DescValueType`


.. function:: getUnitDoubleType(key)

        Gets the unit type of a key of type UnitDouble.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: getUnitDoubleValue(key)

        Gets the value of a key of type UnitDouble.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`number`


.. function:: hasKey(key)

        Checks whether the descriptor contains the provided key.

        :Parameters:
                :key: :class:`number`

        :Returns: :class:`boolean`


.. function:: isEqual(otherDesc)

        Determines whether the descriptor is the same as another descriptor.

        :Parameters:
                :otherDesc: :class:`ActionDescriptor`

        :Returns: :class:`boolean`


.. function:: putBoolean(key,value)

        Sets the value for a key whose type is boolean.

        :Parameters:
                :key: :class:`number`
                :value: :class:`boolean`

        :Returns: `undefined`


.. function:: putClass(key,value)

        Sets the value for a key whose type is class.

        :Parameters:
                :key: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putData(key,value)

        Puts raw byte data as a string value.

        :Parameters:
                :key: :class:`number`
                :value: :class:`string`

        :Returns: `undefined`


.. function:: putDouble(key,value)

        Sets the value for a key whose type is double.

        :Parameters:
                :key: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putEnumerated(key,enumType,value)

        Sets the enumeration type and value for a key.

        :Parameters:
                :key: :class:`number`
                :enumType: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putInteger(key,value)

        Sets the value for a key whose type is integer.

        :Parameters:
                :key: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putLargeInteger(key,value)

        Sets the value for a key whose type is large integer.

        :Parameters:
                :key: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putList(key,value)

        Sets the value for a key whose type is an ActionList object.

        :Parameters:
                :key: :class:`number`
                :value: :class:`ActionList`

        :Returns: `undefined`


.. function:: putObject(key,classID,value)

        Sets the value for a key whose type is an object, represented by an Action Descriptor.

        :Parameters:
                :key: :class:`number`
                :classID: :class:`number`
                :value: :class:`ActionDescriptor`

        :Returns: `undefined`


.. function:: putPath(key,value)

        Sets the value for a key whose type is path.

        :Parameters:
                :key: :class:`number`
                :value: :class:`File`

        :Returns: `undefined`


.. function:: putReference(key,value)

        Sets the value for a key whose type is an object reference.

        :Parameters:
                :key: :class:`number`
                :value: :class:`ActionReference`

        :Returns: `undefined`


.. function:: putString(key,value)

        Sets the value for a key whose type is string.

        :Parameters:
                :key: :class:`number`
                :value: :class:`string`

        :Returns: `undefined`


.. function:: putUnitDouble(key,unitID,value)

        Sets the value for a key whose type is a unit value formatted as a double.

        :Parameters:
                :key: :class:`number`
                :unitID: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: toStream()

        Gets the entire descriptor as a stream of bytes, for writing to disk.

        :Parameters: `null`

        :Returns: :class:`string`


