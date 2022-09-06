===============
ActionReference
===============

This object provides information about what the action is refering to. For example, when referring to the name of something you might use keyName. The reference would also need to know what name you are referring to. In this case you could use classDocument for the name of the document or classLayer for the name of the layer. It can be used for low-level access into Photoshop.Contains data associated with an ActionDescriptor. 

----------
Properties
----------

.. property:: typename
	
	The class name of the referenced :class:`ActionReference` object.
	
	:Permission: Read-only
	
	:Type: :class:`string`


-------
Methods
-------

.. function:: getContainer()

        Gets a reference contained in this reference.
        
        Container references provide additional pieces to the reference. This looks like another reference, but it is actually part of the same reference.

        :Parameters: `null`

        :Returns: :class:`ActionReference`


.. function:: getDesiredClass()

        Gets a number representing the class of the object.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: getEnumeratedType()

        Gets the enumeration type.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: getEnumeratedValue()

        Gets the enumeration value.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: getForm()

        Gets the form of this action reference.

        :Parameters: `null`

        :Returns: :class:`ReferenceFormType`


.. function:: getIdentifier()

        Gets the identifier value for a reference whose form is identifier.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: getIndex()

        Gets the index value for a reference in a list or array.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: getName()

        Gets the name of a reference.

        :Parameters: `null`

        :Returns: :class:`string`


.. function:: getOffset()

        Gets the offset of the object’s index value.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: getProperty()

        Gets the property ID value.

        :Parameters: `null`

        :Returns: :class:`number`


.. function:: putClass(desiredClass)

        Puts a new class form and class type into the reference.

        :Parameters:
                :desiredClass: :class:`number`

        :Returns: `undefined`


.. function:: putEnumerated(desiredClass,enumType,value)

        Puts an enumeration type and ID into a reference along with the desired class for the reference.

        :Parameters:
                :desiredClass: :class:`number`
                :enumType: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putIdentifier(desiredClass,value)

        Puts a new identifier and value into the reference.

        :Parameters:
                :desiredClass: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putIndex(desiredClass,value)

        Puts a new index and value into the reference.

        :Parameters:
                :desiredClass: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putName(desiredClass,value)

        Puts a new name and value into the reference.

        :Parameters:
                :desiredClass: :class:`number`
                :value: :class:`string`

        :Returns: `undefined`


.. function:: putOffset(desiredClass,value)

        Puts a new offset and value into the reference.

        :Parameters:
                :desiredClass: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`


.. function:: putProperty(desiredClass,value)

        Puts a new property and value into the reference.

        :Parameters:
                :desiredClass: :class:`number`
                :value: :class:`number`

        :Returns: `undefined`

