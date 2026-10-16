.. _writing-precisely.convention.325:

------------------------------------------------------------
Simple Data Storage Model
------------------------------------------------------------

.. highlights:: Purpose

   The simplest possible model for writing, storing and
   transmitting data. Expressiveness is sacrificed on
   purpose: the vocabulary is small enough that information
   gets its structure naturally. Data that does not fit is a
   sign the data (and probably the code) needs refactoring,
   not that the model needs to grow.

Observation: a simpler syntax requires a more sophisticated parser.
Simplicity does not remove complexity; it moves it into the parser.

* Statuses
- defined :: the construct has a meaning at this layer.
- unsupported :: the construct is defined at a higher layer, not at
  this one. In the model, it shows how features are distributed across
  layers; new versions of the model change this picture. In an
  implementation, it marks a construct the model defines but the
  implementation does not handle; the implementation must declare what
  it does on encountering it.
- undefined :: no layer of the model gives the construct a meaning.
  An implementation must resolve every undefined construct as one of:
  - a distinct role
  - an error
  - a skippable record
- excluded :: deliberately left out of the model, at every layer. Not an
  oversight: it does not belong because of how the model is defined.


* Inheritance
An implementation inherits from the model or from another
implementation (its parent), including the parent's catalog and
statuses.

- It may resolve what the parent leaves undefined.
- It may support what the parent leaves unsupported.
- It may declare a construct the parent defines as unsupported, with
  its handling.
- It must not change the meaning of a defined construct, or define an
  excluded one.

* Separators
- primary separator :: marks where one record ends and the next
  begins.
- secondary separator :: marks where the name ends.
- separator rule :: the two must differ, and neither may contain the
  other.
- separator levels :: the model defines two levels, primary and
  secondary. A third level is left to implementations, within the
  extension boundary.

* Parser boundary
The model accounts for parser complexity so that each layer is a
practical tool, not a theoretical possibility. A parser may ask only
these questions:

Within a record:
- Is there a name?
- Is there a value?
- Where are the separators, and how many are there in a row?

Across records, from state built by previous records:
- Are we inside a sequence? (layer 1)
- How deep is the nesting? (layer 2)

A record is classified from its own content and the state left by the
records before it, never by records that follow (no lookahead). Every
record can therefore be classified as soon as it arrives.

A layer or implementation that needs another question must name it and
justify it.

* Extension boundary (draft)
An implementation may:
- choose its concrete separators
- resolve undefined constructs
- use a third separator level as shorthand that expands into model
  records
- define modes and padding
- set conventions for names or values (e.g. metadata)

* Scope notes

- Depth :: the model sets no limit. Practical limits come from
  maintainability and the parser. An implementation may set a limit and
  must declare it.
- Metadata :: not a concept of the model. An implementation may offer
  it within the spec by its own conventions for names or values (e.g. a
  reserved name for a metadata sequence).
- Streaming :: a lost end mark leaves sequences open; only the receiver
  can detect it. Close all is a resynchronisation point. Where data loss
  is a real risk or tracking is crucial, limit or avoid sequences and let
  each record carry its own context (shown in Keel notation):
  #+begin_example
  seq name |
  seq id   | 123
  123      | item 1
  123      | item 2
  123      | item 3
  (end of sequence not received)
  | item 4
  | item 5
  #+end_example
  Records 4 and 5 carry no id, so the receiver can tell they do not
  belong to sequence 123.

* Deferred to layer 3
- Multiline values as a distinct structure. A sequence can carry lines
  of text, but it is not a multiline value.
- A record starting with a sequence separator (e.g. Keel's leading =/=).
- Anonymous sequences.
The last two conflict with nesting as defined at layer 2.


|h.ref|
============================================================

:ref:`writing-precisely.proposition.313`

|h.page-info|
============================================================

.. include:: tables/page-info.convention.325.txt
