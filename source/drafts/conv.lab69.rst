.. _writing-precisely.conv.lab69:

------------------------------------------------------------
Convention: Lab69
------------------------------------------------------------

:version: 0.1
:revision: 2026-09-07
:written by: |author| (|email|)

.. rubric:: Purpose

Lab69 is a local schemaless storage system for experimental
data.

.. _writing-precisely.conv.lab69.definition:

Definitions
============================================================

.. glossary::
   :sorted:


   .lab69

      ~ is a special configuration file that stores
      configuration settings of the current data catalog
      (the data catalog that contains the given ~).

      ~ uses the `kile` format for storing data, see
      :ref:`writing-precisely.conv.kile`.

      .. list-table::
	 :header-rows: 1
	 :widths: 40 40 20
	 
	 * - setting
	   - purpose
	   - required?
	 * - name
	   - human-readable reference
	   - yes
	 * - attribute.catalog
	   - reference to a catalog that defines applicable
             attribute codes and names.
	   - no
	 * - attribute.separator
	   - custom field separator
	   - no
	 * - attribute.code.vocabulary
	   - custom attribute vocabulary
	   - no
	 * - attribute.code.length
	   - custom attribute length
	   - no
	 * - signature.vocabulary
	   - custom signature vocabulary
	   - no
	 * - signature.length
	   - custom signature length
	   - no
  
      .. seealso::

	 - :term:`Attribute catalog`
	 - :term:`Record signature`
	 - :term:`Attribute code length`
	 - :term:`Attribute code vocabulary`




   Data library

      ~ is a collection of data catalogs.



   Reference catalog

      ~ is a data catalog, the name of which matches the
      code of an attribute present in the containing data
      catalog.



   Attribute

      ~ is a file with the `.lab69` extension that contains
      attribute entries. As the name, attributes use the
      registered attribute codes from the attribute catalog.

      .. important::

	 Any lines not recognized as valid attribute entries are not
	 included into the attribute.

      .. seealso::

	 - :term:`Attribute code`
	 - :term:`Attribute catalog`
	 - :term:`Attribute entry`
	 - :term:`Valid attribute`


   Attribute catalog

      ~ is a special catalog that registers all applicable
      attribute names and their codes. The attribute
      catalogue must contain valid attributes. The ~ is only
      special because it is self-defining: codes and names
      of attributes are defined in the ~ itself.

      ~ is either defined in the current data catalog or the
      current data library. In a data catalog, ~ 

      .. seealso::

	 - :term:`Attribute`
	 - :term:`Attribute code`


   
   Attribute code

      ~ is a special code costructed from the characters
      that belong to the designated vocabulary. The ~ may
      only contain exactly as many characters as set up in
      the code length. Attribute codes must be stable.

   .. seealso::

      - :term:`Attribute code length`
      - :term:`Attribute code vocabulary`
      - :term:`Stable attribute code`



   Stable attribute code

      ~ is a property of the attribute code that requires
      that the attribute code must not be associated with
      any meaningful information to guarantee that there is
      never a reason to update the attribute code to catch
      up with attribute updates.

      The only property permitted for a ~ is `uniqueness`:
      no more than one attribute code may be associated with
      a single attribute. If the attribute code is `unique`
      and nothing else then there is never a reason to change
      it.

      Keep it mind that sequencial numbers are **not**
      recognized as stable because they feature the
      `ordered` property in addition to `unique`.

      .. seealso::

	 - :term:`Attribute code`



   Stable record signature

      ~ is a feature that requires the record signature **not to be**
      associated with any meaningful information to
      guarantee that there is never a reason to update the
      record identifier to catch up with data updates.

      The only property permitted for a ~ is `uniqueness`:
      no more than one record signature may be associated
      with the value of exactly one attribute entry.

      Keep it mind that sequencial numbers **do not**
      implement ~ because they have the `ordered` property.

      .. seealso::

	 - :term:`Record signature`



   Attribute code length

      ~ is the exact number of characters that may belong to
      the attribute code.

      If no custom ~ is provided then the default length
      applies respecting the value of the minimum length.

      .. seealso::
      
	 - :term:`Attribute code`
	 - :term:`Default attribute code length`
	 - :term:`Minimum attribute code length`



   Minimum attribute code length

      The attribute code must contain at least `3`
      characters from the attribute code vocabulary.

      .. seealso::

	 - :term:`Attribute code`
	 - :term:`Attribute code length`
	 - :term:`Attribute code vocabulary`


   Default attribute code length

      Matches the value of the `minimum attribute code length`
 
      .. seealso::

	 - :term:`minimum attribute code length`



   Attribute code vocabulary

      ~ is a collection of characters that may constitute
      the attribute code. If no custom ~ is provided then
      the default attribute vocabulary applies.

      .. seealso::

	 - :term:`Attribute code`
	 - :term:`Default attribute code vocabulary`



   Default attribute code vocabulary

      ~ is an attribute code vocabulary which is applied if
      the `.lab69` configuration file does not define a
      custom vocabulary.

      The ~ includes the following characters: `0698`.

      .. seealso::

	 - :term:`.lab69`
	 - :term:`Attribute code`
	 - :term:`Attribute code vocabulary`



   Data catalog

      ~ is a directory in the file system that stores
      attributes. No naming conventions are defined for
      ~s. The configuration details of the current ~ are
      stored in the special file `.lab69`.

      .. seealso::

	 - :term:`.lab69`
	 - :term:`Attribute`




   Attribute entry

      ~ is a line broken into two fields: signature and
      value. The signature is delimited from data by the field
      separator. If no custom separator is provided, the
      default separator applies.

      .. seealso::

	 - :term:`Field separator`
	 - :term:`Entry value`
	 - :term:`Record signature`




   Full record

      ~ is a collection of all attribute entries that share the same
      record signature in the current data catalog.

      .. seealso::

	 - :term:`Attribute entry`
	 - :term:`Data catalog`
	 - :term:`Record signature`



   Catalog record

      ~ is a collection of full records, where the current
      full record also includes reference records.

      .. seealso::

	 - :term:`Full record`
	 - :term:`Attribute entry`
	 - :term:`Reference record`



   Reference record

      ~ is a record signature which is used as a value of an
      attribute entry. The attribute code in this case
      matches the associated reference catalog. This
      configuration effectively implements the one-to-many
      relation from relational databases: many entries in
      the current attribute point to a record found in the
      attribute encoded in the name of the current attribute.

      .. seealso::

	 - :term:`Record signature`
	 - :term:`Entry value`



   Field separator

      ~ is one or more consecutive characters that separate the
      signature from the value in an attribute entry. All attribute
      entries must use the |t.cfs| provided in the effective
      |f.conf|.

      If |t.cfs| is not provided in the |f.conf| then the |t.dfs|
      takes effect.

      .. seealso::

	 - :term:`Attribute entry`
	 - :term:`Default field separator`
	 - :term:`.lab69`



   Default field separator

      ~ is the entry separator used with the given catalog if the
      effective |f.conf| does not define a custom separator. ~ is a
      single <space> character.

   Null value

      ~ is a special symbol or token to represent the absence of value
      in an attribute entry. Lab69 is based on the concept "nothing is
      nothing. Only nothing may represent nothing."

      In other words, null values are not supported.

      .. seealso::

	 - :term:`Attribute entry`


   Record Signature

      ~ is a unique identifier of the attribute entry. In an attribute
      entry, ~ is implemented as a sequence of characters to the left
      of the field separator. All characters in the ~ must belong to
      the signature vocabulary.

      Characters outside of the signature vocabulary are not permitted
      in the signature. Non-conforming lines are ignored
  
      The number of characters that may constitute the signature is
      determined by the signature length.

      .. seealso::

	 - :term:`Attribute entry`
	 - :term:`Signature vocabulary`

    Signature vocabulary

      ~ is a set of unique non-whitespace characters which constitue
      the record signature of an attribute entry. If no custom ~ is
      provided in the `.lab69` configuration file then the default
      signature vocabulary applies.

      .. seealso::

	- :term:`Record signature`
	- :term:`Default signature vocabulary`

    Default signature vocabulary

      ~ is a signature vocabulary which is applied if
      the `.lab69` configuration file does not define a
      custom signature vocabulary.

      The ~ includes the following characters: `dqpb`.

      .. seealso::

	 - :term:`Signature vocabulary`

    Signature length

      ~ is the number of characters from the signature vocabulary that
      the record signature must contain. If no custom ~ is provided
      then the default signature length applies.

      .. seealso::

	 - :term:`RecordSignature`
	 - :term:`Default signature length`

    Default signature length


      ~ is the value of the signature length if the effective |f.conf|
      provides no value. ~ is **12**.

      .. seealso::

	 - :term:`Signature length`

    Entry value

      ~ is a sequence of characters to the right of the |t.fs| in an
      attribute entry. It is ok for the value to include characters
      that make up the |t.fs|.

      .. seealso::

	 - :term:`Attribute entry`
	 - :term:`Field separator`



.. _writing-precisely.conv.lab69.operation:
.. _conv.lab69.op:

Operations
============================================================

.. _conv.lab69.op.data-catalog:

Data catalog
------------------------------------------------------------

.. rubric:: Create a directory on the file system.
- Name the data catalog according to the requirements of your
  project.

:reading:
- Collect all attributes.
:end:
:updating:
This operation is not applicable.
:end:
:deleting:
This operation is as trivial as deleting a directory from
the file system.
:end:

** Attribute catalog

:creating:
- Create a data catalog
- Create an attribute
- Open the 
:end:
:finding:
:end:

** Attribute

:creating:
:end:

.. include:: ./variables/common.txt
.. include:: ./variables/name.txt
