.. _writing-precisely.proposition.313:

------------------------------------------------------------
Simple Data Storage Model
------------------------------------------------------------

.. highlights:: Opportunity

   

* Principles
- Concepts first :: define concepts and capabilities first, then apply
  syntax.
- Structure emerges :: the model must not force structural decisions
  before the writer is ready to make them.
- No tooling required :: data is readable and writable in any plain
  text editor.
- Tools add capabilities, not rules :: a parser extends what the data
  means; it never adds obligations for the writer (quoting, escaping,
  closing braces).
- Layers :: each layer only adds; it never changes the meaning of what a
  lower layer defines. Data valid at layer N is valid, with the same
  meaning, at every higher layer. Lower layers keep the parser trivial;
  a system uses the lowest layer it needs.
- Catalog :: the model and every implementation carry the full catalog
  of possible record constructs, each with its status. The catalog is
  the overview of capabilities.
- Lossless modes :: an implementation may present data in several modes
  (e.g. reading, writing, storage). Converting between modes must never
  lose data. Losslessness is about data, not spelling: two spellings of
  the same records are the same data. Not negotiable.
Excluded:
- null :: there is no syntax for "nothing", and special values would
  open the door to chaos. Constructs that would carry only nothing
  (an empty sequence) are excluded.
- datatypes :: no primitive types (numbers, strings, booleans and so
  on). Everything in a file is characters; reading a number from them is
  a best guess. Format-level types also promise less than they seem: a
  field like =age= holds a number, but -3, 0 and 300 are all numbers and
  not all are valid ages. The application must process and validate the
  value anyway, so typing belongs to the contract between producer and
  consumer, not to the model.
- escaping :: not needed; see the dividing separator.

An implementation must not change defined meanings or define excluded
constructs.

* Layer 1: pairs and simple sequences
Goal: the simplest useful data and a trivial parser (two states:
outside a sequence and inside one).

- data :: an ordered sequence of records. Order is significant.
- record :: the content between two primary separators.
- name :: a non-empty sequence of characters containing neither
  separator. Names may repeat; data is a sequence, not a map.
- value :: a non-empty sequence of characters not containing the
  primary separator. It may contain T.
- dividing separator :: the first T in a record. Every later T is an
  ordinary character of the value, so no escaping is needed.
- pair :: =NTV$= outside a sequence.
- sequence :: a named, ordered group of items: =NT$=, then items
  =TV$=, then the end =T$=.
- open sequence :: a sequence whose end has not been encountered. Its
  items received so far are valid; the sequence is not finished.

* Layer 2: associations and nesting
Goal: structured data. The parser needs a stack, nothing more.

- association :: =NTV$= inside a sequence.
- member :: an association, an item or a nested sequence.
- nesting :: =NT$= inside an open sequence opens a child sequence.
  =T$= closes the innermost open sequence.
- start with first item :: =NTTV$= is =NT$ TV$= in one record.
- close all :: a run of primary separators closes every open sequence.
  With no open sequence it has no effect.

Capability: a sequence may mix associations, items and nested
sequences. Lists and associations need no separate structures.



|h.ref|
============================================================

:ref:`writing-precisely.perspective.580`

|h.page-info|
============================================================

.. include:: tables/page-info.proposition.313.txt

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt

