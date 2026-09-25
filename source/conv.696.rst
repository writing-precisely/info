.. _writing-precisely.conv.696:

------------------------------------------------------------
Local Information Storage Model
------------------------------------------------------------

.. highlights:: Purpose

   This convention defines |this|. It is a schemaless model
   for storing information the structure of which is not
   fully known in advance and should be expected to change
   or be redefined over time.



Methods
============================================================

Storing information
------------------------------------------------------------

1. A :term:`data library <Data library (conv. 696)>` contains
   :term:`data catalogs <Data catalog (conv. 696)>`.
2. A data catalog contains
   :term:`attributes <Attribute (conv. 696)>`. Within a data
   catalog, a
   :term:`record signature <Record signature (conv. 696)>`
   identifies no more than one record.
3. An attribute contains
   :term:`attribute entries <Attribute entry (conv. 696)>`.
   An attribute entry has two
   :term:`components <Attribute entry component (conv. 696)>`,
   a record signature and an
   :term:`entry value <Entry value (conv. 696)>`, separated by
   the :term:`component separator <Component separator (conv. 696)>`.
   Within an attribute, a record signature appears in no more
   than one attribute entry.
4. An attribute is named by an
   :term:`attribute code <Attribute code (conv. 696)>`
   registered in an
   :term:`attribute catalog <Attribute catalog (conv. 696)>`.
5. A connection between records is itself a record, stored in
   a :term:`reference catalog <Reference catalog (conv. 696)>`.
   The entry values of its
   :term:`reference attributes <Reference attribute (conv. 696)>`
   are record signatures from the connected data catalogs.

Constructing a record
------------------------------------------------------------

1. Take the
   :term:`record signature <Record signature (conv. 696)>` and
   the :term:`data catalog <Data catalog (conv. 696)>` that
   contains the record.
2. In each :term:`attribute <Attribute (conv. 696)>` of the
   data catalog, find the
   :term:`attribute entry <Attribute entry (conv. 696)>` with
   that record signature.
3. Resolve the
   :term:`attribute code <Attribute code (conv. 696)>` of each
   attribute to its
   :term:`attribute name <Attribute name (conv. 696)>` by
   :term:`attribute code resolution <Attribute code resolution (conv. 696)>`.
4. Map each attribute name to the
   :term:`entry value <Entry value (conv. 696)>` found in that
   attribute. The result is the
   :term:`full record <Full record (conv. 696)>`.

Resolving an attribute code
------------------------------------------------------------

1. Start at the :term:`data catalog <Data catalog (conv. 696)>`
   that contains the
   :term:`attribute <Attribute (conv. 696)>`.
2. If the
   :term:`data catalog meta data <Data catalog meta data (conv. 696)>`
   at the current level name an
   :term:`attribute catalog <Attribute catalog (conv. 696)>`
   that registers the
   :term:`attribute code <Attribute code (conv. 696)>`, take
   the :term:`attribute name <Attribute name (conv. 696)>`
   from it and stop.
3. Otherwise, move to the containing
   :term:`data library <Data library (conv. 696)>` and repeat
   step 2.
4. If no containing data library remains, the attribute code
   is not registered.


Definitions
============================================================

.. glossary::
   :sorted:

   Attribute (conv. 696)

      ~ is a file in a data catalog that contains attribute
      entries. ~ is named by an attribute code. Within an ~, a
      record signature appears in no more than one attribute
      entry.

      .. admonition:: Reasoning

         The perspective leaves open whether a record signature
         may appear more than once in an ~. This convention
         restricts it: an ~ holds one entry value per record,
         so a full record maps each attribute name to exactly
         one entry value. Several values for one record, such
         as several dealers for one car model, are expressed
         through a reference catalog.

      .. seealso::

         - :term:`Attribute code (conv. 696)`
         - :term:`Attribute entry (conv. 696)`
         - :term:`Attribute name (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Entry value (conv. 696)`
         - :term:`Full record (conv. 696)`
         - :term:`Record signature (conv. 696)`
         - :term:`Reference catalog (conv. 696)`



   Attribute catalog (conv. 696)

      ~ is a data catalog that registers attribute codes
      together with their attribute names. ~ is only special
      because it is self-defining: the attribute codes and
      attribute names of its own attributes are registered in
      the ~ itself. Which ~ applies to a data catalog is stated
      in data catalog meta data.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Attribute code (conv. 696)`
         - :term:`Attribute name (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`



   Attribute code (conv. 696)

      ~ is a code constructed from the characters of the
      effective attribute code vocabulary. ~s must be stable.

      .. seealso::

         - :term:`Attribute code vocabulary (conv. 696)`
         - :term:`Effective value (conv. 696)`
         - :term:`Stable attribute code (conv. 696)`



   Attribute code resolution (conv. 696)

      ~ is the procedure that determines the attribute name
      for a given attribute code. ~ follows data catalog meta
      data outward from the data catalog that contains the
      attribute through its containing data libraries. The
      first attribute catalog named in data catalog meta data
      that registers the attribute code provides the attribute
      name.

      .. admonition:: Reasoning

         Data catalog meta data make ~ explicit: it never
         depends on which attribute catalogs happen to be
         present. Resolving each attribute code separately lets
         an attribute catalog named closer to the data register
         only the attribute codes whose meaning differs, such
         as the name of a dealer versus the name of a car model.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Attribute catalog (conv. 696)`
         - :term:`Attribute code (conv. 696)`
         - :term:`Attribute name (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`
         - :term:`Data library (conv. 696)`



   Attribute code vocabulary (conv. 696)

      ~ is a collection of characters that may constitute an
      attribute code.

      .. admonition:: Reasoning

         Attribute codes become file names. The ~ must
         therefore contain only characters that are valid in
         file names on every file system and that do not depend
         on letter case.

      .. seealso::

         - :term:`Attribute code (conv. 696)`
         - :term:`Default attribute code vocabulary (conv. 696)`



   Attribute entry (conv. 696)

      ~ is a line in an attribute that consists of two
      attribute entry components: the record signature and the
      entry value, separated by the component separator. ~ must
      contain both attribute entry components.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Attribute entry component (conv. 696)`
         - :term:`Component separator (conv. 696)`
         - :term:`Entry value (conv. 696)`
         - :term:`Record signature (conv. 696)`



   Attribute entry component (conv. 696)

      ~ is one of the two parts of an attribute entry: the
      record signature or the entry value.

      .. seealso::

         - :term:`Attribute entry (conv. 696)`
         - :term:`Entry value (conv. 696)`
         - :term:`Record signature (conv. 696)`



   Attribute name (conv. 696)

      ~ is the readable name of an attribute, registered in an
      attribute catalog together with its attribute code.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Attribute catalog (conv. 696)`
         - :term:`Attribute code (conv. 696)`



   Component separator (conv. 696)

      ~ is one or more consecutive characters that separate
      the record signature from the entry value in an
      attribute entry. All attribute entries of a data catalog
      must use the effective ~.

      .. important::

         An attribute entry that uses a ~ other than the
         effective ~ is not valid.

      .. seealso::

         - :term:`Attribute entry (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Default component separator (conv. 696)`
         - :term:`Effective value (conv. 696)`
         - :term:`Entry value (conv. 696)`
         - :term:`Record signature (conv. 696)`



   Data catalog (conv. 696)

      ~ is a directory in the file system that contains
      attributes. Within a ~, a record signature identifies no
      more than one record. No naming conventions are defined
      for ~s. The configuration of a ~ is provided in its data
      catalog meta data.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`
         - :term:`Record signature (conv. 696)`



   Data catalog meta data (conv. 696)

      ~ is the set of settings of a data catalog or a data
      library: the component separator, the signature
      vocabulary, the signature length, the attribute code
      vocabulary, and the attribute catalog. A setting that is
      not provided takes its default value, except for the
      attribute catalog, which follows attribute code
      resolution.

      .. seealso::

         - :term:`Attribute catalog (conv. 696)`
         - :term:`Attribute code resolution (conv. 696)`
         - :term:`Attribute code vocabulary (conv. 696)`
         - :term:`Component separator (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Data library (conv. 696)`
         - :term:`Signature length (conv. 696)`
         - :term:`Signature vocabulary (conv. 696)`



   Data library (conv. 696)

      ~ is a directory that contains data catalogs. ~ may
      contain data catalog meta data. ~s may be nested.

      .. admonition:: Reasoning

         The data catalog meta data of a nested ~ may name an
         attribute catalog whose attribute names differ from
         those of the containing ~. Through attribute code
         resolution, that attribute catalog needs to register
         only the attribute codes that differ.

      .. seealso::

         - :term:`Attribute catalog (conv. 696)`
         - :term:`Attribute code resolution (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`



   Default attribute code vocabulary (conv. 696)

      ~ is the attribute code vocabulary that applies if the
      data catalog meta data do not provide one. Its contents
      are provided by the bound protocol.

      .. seealso::

         - :term:`Attribute code vocabulary (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`



   Default component separator (conv. 696)

      ~ is the component separator that applies if the data
      catalog meta data do not provide one. ~ is a single
      <space> character.

      .. admonition:: Reasoning

         The perspective states that a single space suffices as
         the separator: it is the simplest separator, visible
         in any text editor, and basic tools split a line on it
         without configuration.

      .. seealso::

         - :term:`Component separator (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`



   Default signature length (conv. 696)

      ~ is the signature length that applies if the data
      catalog meta data do not provide one. Its value is
      provided by the bound protocol and must satisfy the
      reasoning given for the signature length.

      .. seealso::

         - :term:`Data catalog meta data (conv. 696)`
         - :term:`Signature length (conv. 696)`



   Default signature vocabulary (conv. 696)

      ~ is the signature vocabulary that applies if the data
      catalog meta data do not provide one. Its contents are
      provided by the bound protocol.

      .. seealso::

         - :term:`Data catalog meta data (conv. 696)`
         - :term:`Signature vocabulary (conv. 696)`



   Effective value (conv. 696)

      ~ of a setting is the value that applies to a data
      catalog: the value provided in its data catalog meta data
      if present, otherwise the default value.

      .. seealso::

         - :term:`Data catalog (conv. 696)`
         - :term:`Data catalog meta data (conv. 696)`



   Entry value (conv. 696)

      ~ is the attribute entry component to the right of the
      component separator. ~ may include the characters that
      make up the component separator.

      .. important::

         ~ that consists of whitespace characters only is not
         valid.

      .. seealso::

         - :term:`Attribute entry (conv. 696)`
         - :term:`Attribute entry component (conv. 696)`
         - :term:`Component separator (conv. 696)`



   Full record (conv. 696)

      ~ is the mapping of attribute names to entry values for
      one record signature in a data catalog: each attribute
      that contains an attribute entry with the record
      signature contributes its attribute name and the entry
      value of that attribute entry.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Attribute entry (conv. 696)`
         - :term:`Attribute name (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Entry value (conv. 696)`
         - :term:`Record signature (conv. 696)`



   Null value (conv. 696)

      ~ is a special symbol or token to represent the absence
      of a value in an attribute entry. This model is based on
      the concept "nothing is nothing. Only nothing may
      represent nothing."

      In other words, ~s are not supported. A missing value is
      a missing attribute entry.

      .. seealso::

         - :term:`Attribute entry (conv. 696)`



   Record signature (conv. 696)

      ~ is the attribute entry component to the left of the
      component separator. ~ identifies a record within a data
      catalog. All characters in the ~ must belong to the
      effective signature vocabulary. The ~ must contain at
      least as many characters as the effective signature
      length.

      .. important::

         1. If the ~ contains characters outside of the
            effective signature vocabulary, the attribute entry
            is not valid.
         2. If the ~ is shorter than the effective signature
            length, the attribute entry is not valid.

      .. seealso::

         - :term:`Attribute entry (conv. 696)`
         - :term:`Attribute entry component (conv. 696)`
         - :term:`Component separator (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Effective value (conv. 696)`
         - :term:`Signature length (conv. 696)`
         - :term:`Signature vocabulary (conv. 696)`
         - :term:`Stable record signature (conv. 696)`



   Reference attribute (conv. 696)

      ~ is an attribute of a reference catalog whose entry
      values are record signatures from one connected data
      catalog.

      .. important::

         A protocol must make ~s distinguishable from the other
         attributes of a reference catalog.

      .. admonition:: Reasoning

         Reconstructing a connection requires knowing which
         entry values are record signatures and which data
         catalog they come from.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Entry value (conv. 696)`
         - :term:`Record signature (conv. 696)`
         - :term:`Reference catalog (conv. 696)`



   Reference catalog (conv. 696)

      ~ is a data catalog whose records are connections between
      records of other data catalogs. ~ contains one reference
      attribute per connected data catalog and may contain
      attributes of its own.

      .. admonition:: Reasoning

         The perspective keeps a connection apart from both
         sides: neither side has to be chosen in advance as its
         owner, and the connection can carry findings of its
         own, such as the price a dealer asks for a car model.

      .. seealso::

         - :term:`Attribute (conv. 696)`
         - :term:`Data catalog (conv. 696)`
         - :term:`Reference attribute (conv. 696)`



   Signature length (conv. 696)

      ~ is the minimum number of characters from the signature
      vocabulary that a record signature must contain. A
      protocol may require an exact length.

      .. admonition:: Reasoning

         A record signature is stable only if it is unique, and
         a record signature is chosen without looking at the
         existing data. The ~ must therefore make an accidental
         collision negligible for the expected number of
         records, given the size of the signature vocabulary.

      .. seealso::

         - :term:`Default signature length (conv. 696)`
         - :term:`Record signature (conv. 696)`
         - :term:`Signature vocabulary (conv. 696)`
         - :term:`Stable record signature (conv. 696)`



   Signature vocabulary (conv. 696)

      ~ is a set of unique non-whitespace characters that
      constitute a record signature.

      .. important::

         ~ must not include any character of the effective
         component separator.

      .. seealso::

         - :term:`Component separator (conv. 696)`
         - :term:`Default signature vocabulary (conv. 696)`
         - :term:`Effective value (conv. 696)`
         - :term:`Record signature (conv. 696)`



   Stable attribute code (conv. 696)

      ~ is a property of an attribute code: the attribute code
      **must not** be associated with any meaningful
      information, so that there is never a reason to update
      the attribute code to catch up with attribute updates.

      The only property permitted for a ~ is `uniqueness`:
      within an attribute catalog, no attribute code may be
      associated with more than one attribute name.

         .. include:: ./partials/ordered-not-stable.txt

      .. seealso::

         - :term:`Attribute catalog (conv. 696)`
         - :term:`Attribute code (conv. 696)`
         - :term:`Attribute name (conv. 696)`



   Stable record signature (conv. 696)

      ~ is a property of a record signature: the record
      signature **must not** be associated with any meaningful
      information, so that there is never a reason to update
      the record signature to catch up with data updates.

      The only property permitted for a ~ is `uniqueness`:
      within a data catalog, a record signature identifies no
      more than one record.

         .. include:: ./partials/ordered-not-stable.txt

      .. admonition:: Reasoning

         The perspective leaves uniqueness to whoever builds on
         the design. This convention requires it: a reference
         catalog pairs the attribute entries of its reference
         attributes by record signature, and pairing is only
         possible if a record signature identifies one record.
         Requiring `uniqueness` in every data catalog keeps
         reference catalogs structurally identical to all other
         data catalogs.

      .. seealso::

         - :term:`Data catalog (conv. 696)`
         - :term:`Record signature (conv. 696)`
         - :term:`Reference attribute (conv. 696)`
         - :term:`Reference catalog (conv. 696)`



|h.ref|
============================================================

.. include:: tables/ref.conv.696.txt


|h.page-info|
============================================================

.. include:: tables/page-info.conv.696.txt

.. |this| replace:: `Local Information Storage Model`

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt
