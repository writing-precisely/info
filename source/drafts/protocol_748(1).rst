.. _protocol.748:

------------------------------------------------------------
Numeric Code Storage Protocol
------------------------------------------------------------

.. rubric:: Purpose

This protocol defines |this|. It realizes the |conv| on a file
system: it maps the terms of the convention onto directories
and files named by numeric codes and provides the values that
the convention leaves to its protocols.

Each term below declares its relation to the convention:

- *Realizes*: gives a concrete form to a convention term
  without changing its mechanism.
- *Specializes*: narrows a convention term or provides its
  value.
- *New*: introduces a mechanism the convention does not have,
  with reasoning.

.. rubric:: Foundation

- :ref:`convention.696`, version 0.3


.. glossary::
   :sorted:

   Data library (Class, 748)

      *Realizes* :term:`Data library (conv. 696)`.

      ~ is a directory that contains data catalogs. ~ may
      contain data catalog meta data and nested ~ies.

      .. (open) naming of nested data libraries.

      .. seealso::

         - :term:`Data catalog (Class, 748)`
         - :term:`Data catalog meta data (Class, 748)`
         - :term:`Data library (conv. 696)`



   Data catalog (Class, 748)

      *Realizes* :term:`Data catalog (conv. 696)`.

      ~ is a directory named by its catalog code.

      .. seealso::

         - :term:`Catalog code (Class, 748)`
         - :term:`Data catalog (conv. 696)`



   Catalog code (Class, 748)

      *New.*

      ~ is the name of a data catalog: exactly three digits.
      Within a data library, a ~ identifies no more than one
      data catalog.

      .. admonition:: Reasoning

         The convention requires reference attributes to be
         distinguishable from the other attributes of a
         reference catalog. A reference attribute is named by
         a ~ and any other attribute by an attribute code.
         Because a ~ is shorter than the minimum attribute code
         length, the name of a file alone tells which kind it
         is. Three digits provide 1000 data catalogs per data
         library, which is sufficient for experimentation.

      .. seealso::

         - :term:`Attribute (Class, 748)`
         - :term:`Data catalog (Class, 748)`
         - :term:`Data library (Class, 748)`
         - :term:`Minimum attribute code length (Parameter, 748)`
         - :term:`Reference catalog (Class, 748)`
         - :term:`Attribute code (conv. 696)`
         - :term:`Reference attribute (conv. 696)`



   Attribute (Class, 748)

      *Realizes* :term:`Attribute (conv. 696)`.

      ~ is a file in a data catalog named by an attribute code
      followed by ``.txt``. Each line of an ~ is an attribute
      entry.

      .. admonition:: Reasoning

         The ``.txt`` extension makes every operating system
         open the file in a text editor.

      .. seealso::

         - :term:`Data catalog (Class, 748)`
         - :term:`Attribute (conv. 696)`
         - :term:`Attribute code (conv. 696)`
         - :term:`Attribute entry (conv. 696)`



   Reference catalog (Class, 748)

      *Realizes* :term:`Reference catalog (conv. 696)`.

      ~ is a data catalog in which each reference attribute
      is a file named by the catalog code of the connected
      data catalog followed by ``.txt``.

      .. seealso::

         - :term:`Attribute (Class, 748)`
         - :term:`Catalog code (Class, 748)`
         - :term:`Data catalog (Class, 748)`
         - :term:`Reference attribute (conv. 696)`
         - :term:`Reference catalog (conv. 696)`



   Data catalog meta data (Class, 748)

      *Realizes* :term:`Data catalog meta data (conv. 696)`.

      ~ is the file |f.conf| in a data catalog or a data
      library. Its lines always use the default field
      separator.

      .. admonition:: Reasoning

         ~ may itself define a custom component separator, so
         reading it must not depend on its own contents.

      .. (open) the format of settings and their names,
         including how the attribute catalog is named.

      .. seealso::

         - :term:`Data catalog (Class, 748)`
         - :term:`Data library (Class, 748)`
         - :term:`Data catalog meta data (conv. 696)`
         - :term:`Default component separator (conv. 696)`
         - :term:`Component separator (conv. 696)`



   Default signature vocabulary (Parameter, 748)

      *Specializes* :term:`Default signature vocabulary (conv. 696)`.

      ~ consists of the lowercase Latin letters ``a``-``z`` and
      the digits ``0``-``9``: 36 characters.

      .. admonition:: Reasoning

         Every character is readable, typeable on any keyboard,
         and free of letter-case ambiguity.

      .. seealso::

         - :term:`Default signature vocabulary (conv. 696)`



   Default signature length (Parameter, 748)

      *Specializes* :term:`Default signature length (conv. 696)`.

      ~ is 12.

      .. admonition:: Reasoning

         With the 36 characters of the
         :term:`default signature vocabulary <Default signature vocabulary (Parameter, 748)>`,
         12 positions give about 4.7 × 10\ :sup:`18`
         combinations. For one million records, the probability
         of an accidental collision is about one in ten
         million.

      .. seealso::

         - :term:`Default signature vocabulary (Parameter, 748)`
         - :term:`Default signature length (conv. 696)`



   Signature length (Parameter, 748)

      *Specializes* :term:`Signature length (conv. 696)`.

      ~ is exact: a record signature must contain exactly as
      many characters as the effective signature length.

      .. admonition:: Reasoning

         A record signature of the wrong length is recognizable
         at a glance as truncated or mistyped.

      .. seealso::

         - :term:`Signature length (conv. 696)`



   Default attribute code vocabulary (Parameter, 748)

      *Specializes* :term:`Default attribute code vocabulary (conv. 696)`.

      ~ consists of the digits ``0``-``9``.

      .. admonition:: Reasoning

         Digits are valid in file names on every file system
         and have no letter case.

      .. seealso::

         - :term:`Default attribute code vocabulary (conv. 696)`



   Attribute code length (Parameter, 748)

      *New.*

      ~ is the exact number of characters in an attribute
      code. If the data catalog meta data provide no custom ~,
      the default attribute code length applies. A custom ~
      must not be less than the minimum attribute code length.

      .. seealso::

         - :term:`Data catalog meta data (Class, 748)`
         - :term:`Default attribute code length (Parameter, 748)`
         - :term:`Minimum attribute code length (Parameter, 748)`
         - :term:`Attribute code (conv. 696)`



   Minimum attribute code length (Parameter, 748)

      *New.*

      ~ is 4.

      .. admonition:: Reasoning

         An attribute code must be longer than a catalog code,
         so that attributes and reference files never share a
         name.

      .. seealso::

         - :term:`Attribute code length (Parameter, 748)`
         - :term:`Catalog code (Class, 748)`
         - :term:`Reference catalog (Class, 748)`
         - :term:`Attribute code (conv. 696)`



   Default attribute code length (Parameter, 748)

      *New.*

      ~ matches the minimum attribute code length.

      .. admonition:: Reasoning

         Four digits provide 10000 attribute codes shared
         across all data catalogs of a data library. Needing
         more distinct attributes indicates a design problem,
         not a capacity problem.

      .. seealso::

         - :term:`Attribute code length (Parameter, 748)`
         - :term:`Minimum attribute code length (Parameter, 748)`



------------------------------------------------------------

   :version: 0.1
   :revision: 2026-09-20
   :written.by:   |author|
   :assisted.by: Anthropic Claude, Opus 5

.. |this| replace:: `Numeric Code Storage Protocol`
.. |conv| replace:: `Local Information Storage Model`

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt
