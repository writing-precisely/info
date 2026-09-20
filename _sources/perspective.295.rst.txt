.. _writing-precisely.experimentation.storing:
.. _perspective.295:

------------------------------------------------------------
Storing for Experimentation
------------------------------------------------------------

With so many solutions for storing data ranging from
versatile, fast, and feature-rich database management
systems down to spreadsheets, plain text is a reasonable
choice when it comes to storing ad hoc data or supporting
experimentation.

Plain text is especially attractive to help break out of the
limitations that ready-made solutions may have: missing
features, proprietary formats, and simply bad memory of how
to do this or that thing with SQL or a formula.

Experimentation data has one reliable feature: its structure is
not reliable.

With data like this, sophisticated solutions don't work. A
database can't simply be set up so you can get on with your
work. Tables, data types, and constraints ought to be
decided before the first value goes in. Skip the planning,
and you quickly reach a state where the structure no longer
fits the data and has to be rebuilt. Planning pays off when
you need what databases are built for: large volumes of
data, many users, fast queries. Experimentation needs none
of them.

JSON and YAML look like an escape. They are plain text, so
the data stays open. There are lots of tools that process
these formats. However, when your understanding changes and
you need to redesign, the structure may have to change with
it, which more often than not entails a considerable effort.

Think about this: what would the simplest shape of data in
plain text look like, such that you can easily update it,
manage it with a text editor and basic CLI tools, and still
be able to store complex information?

   In formal language the requirements are: design a simple
   local storage model for reasonably complex data based on
   file system objects so that the user can edit it manually
   or implement a management system for it in a single
   evening.

That's what I would require for collecting bits from the
internet, designing an original task management system (who
hasn't tried this?), or recording findings of my research
where I don't even know how to group those findings
upfront.

.. _perspective.295.directory.file.line:

A Directory of Files; A File of Lines
============================================================

The conceptual model is traditional: the system stores
information as records. Records have attributes.

   If you consider a car model to buy, then each model is a
   record whose attributes are *name*, *price*, and *year*.

   Mapped onto directories and files, the system works as
   follows:

   1. For the records, create a directory: `cars`.
   2. For each attribute, create a file in that directory:
      `name.txt`, `price.txt`, `year.txt`.
   3. In each file, use the following line format:
      `[record identifier] + [separator] + [value]`.

   A `record identifier` has exactly one requirement: it
   must not contain the `separator`. A single space will
   suffice as the `separator`. The `value` is anything.

.. _perspective.295.directory.file.line.relation.many-to-many:

Only Many-to-Many Relations Are Supported
------------------------------------------------------------

A connection between records is itself a record, kept in a
directory of its own. That directory follows the same rules
as any other: its files are attributes, and its lines are
`record identifiers` followed by `values`. Only its values
are special: they are `record identifiers` from the
directories that you are linking.

The files that participate in the relation must differ from
attribute files. For example, they may use their own naming
conventions.



.. _perspective.295.directory.file.line.record-indentifier.feature:

Record Identifiers Have Only Two Features
------------------------------------------------------------

A `record indentifier` has only two properties: it may not
contain the `separator` and it must be unique in an
attribute file. *Uniqueness* is required to enable
:ref:`relations
<perspective.295.directory.file.line.relation.many-to-many>`.

No other property is allowed. Even sequence numbers cannot
be used as `record identifiers`.



.. _perspective.295.directory.file.line.value.anything:

Value Is Anything but Not Nothing
============================================================

The `value` may contain anything. No characters have to be
escaped even if a `value` contains the
`separator`. Semantically, a line is a pair: the `record
identifier` ends at the `separator`, and what follows is the
value. No special checks.

Data types: By attribute name

   A value is of the type named by its file: a value in
   `price.txt` is a price.

Null values: Not Supported

   Nothing is the only equivalent of nothing. A value is
   missing if the `record identifier` is not found for the
   attribute.


------------------------------------------------------------

   :version: 0.1
   :revision: 2026-09-20
   :written.by:   |author|
   :assisted.by: Anthropic Claude, Opus 5

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt
