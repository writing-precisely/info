.. _writing-precisely.perspective.580:

------------------------------------------------------------
Simplest Data Model in Plain Text
------------------------------------------------------------

What would it take to design the *simplest data model* that
would serve the purpose of accumulating information and
building up structure with the smallest possible vocabulary?


- **Investigating an incident.** Something fails without
  warning. Each finding is recorded as it turns up. One is
  a cause, another a consequence, a third unrelated. Which
  is which becomes clear only at the end, when part of the
  evidence is already gone.
- **Cataloguing a collection.** A set of items arrives with
  no inventory. Each one is described as it is examined.
  One has a date, another an owner, a third only a guess.
  What the collection holds becomes clear when most of it
  has been seen.
- **Exploring an unfamiliar system.** A system is taken
  over with no description. Each part is noted as it is
  met, with what it seems to depend on. Some early notes
  prove wrong and are corrected where they stand. How the
  parts fit together becomes clear as the notes grow.


.. _writing-precisely.perspective.580-78:

Layer 1: Pairs
============================================================

If information is arranged as a simple sequence of
statements or sentences there is nothing but intrinsic
grammatical structure that holds them together. In the
context of a data model, all statements constitute one
atomic unit. In this form, it serves badly even for
capturing ideas during brainstorming or for task capturing
let alone complex data structures. Even a shopping list is
out of scope.

Names and values, heading and prose, list items
are examples when information is organized around
pairs. One element of a pair is associated with capturing
the purpose, label, or name of data and the other element
holds the associated value.

In the simplest data model, a pair forms an entry composed
of the following components:

- the left element (name)
- the right element (value)
- a separator between the elements (secondary separator)
- a separator between pairs (primary separator)

Restrictions
------------------------------------------------------------

Without having to introduce additional syntax to escape
special characters, the simplest data model must abide by the
following restrictions:

- The name may contain neither primary nor secondary separator.
- The secondary separator may not use the token already
  claimed by the primary separator.
- The value may not contain the primary separator.
- After the secondary separator is consumed, the secondary
  separator token becomes part of the value until the
  primary separator.

The simplest model does not have the root or the mark of the
end of the sequence. When all pairs are properly
constructed, there is no way to formally complete the
sequence.

The model cannot restrict the sequence from repeating one
and the same name multiple times.

There is no way to require the order of pairs.

Layer 1 recognizes only correctly formed pairs and ignores
everything else. As such, it is very easy to implement.

Additional capabilities must be encoded in special names or
values.


.. _writing-precisely.perspective.580-91:

Layer 2: Associations and Nesting
============================================================

Layer 1 works but is not very capable. Strangely, more
advanced capabilities arrive when a pair is broken to
introduce additional distinct types of entry:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Entry type
     - What is present
     - What it does
   * - Name Entry
     - The name and the secondary separator. The value is
       missing.
     - Introduces a named sequence. In an open sequence,
       starts a nested sequence.
   * - Value Entry
     - The secondary separator and the value. The name is
       missing.
     - Adds an item to the current sequence.
   * - Close Entry
     - The secondary separator only. Both the name and the
       value are missing.
     - Ends the current sequence.
   * - Reset Entry
     - The primary separator only. There is no name,
       secondary separator, or value.
     - Ends all open sequences.

These deficient entries enable sequences as values as well
as nested structures. In an open sequence, `Value Entries`
and `Pairs`, in any order, are the sequence items.

Capabilities
------------------------------------------------------------

Without extending the syntax, the simplest data format
introduces new capabilities by exhausting possible
combinations of its elements.

Combinations of entries introduce capabilities that were
not designed separately. An example is a sequence that mixes
list items and associated values. It follows from the
definitions above; nothing was added to support it. Using
the basic elements to their full extent keeps the design
consistent.

Layer 2 is not built on top of Layer 1. It fully consumes
Layer 1 and adds more, without additional syntax: the
additional capabilities are introduced by simplifying the
basic construct defined on Layer 1.

A document is read entirely at one layer or entirely at the
other. Which layer applies is part of the contract between
producer and consumer, not a property of the content.

Refusing to add syntax has a price: the complexity moves to
the parser. On Layer 2, data parsing requires taking into
account not only the current entry but also the sequences
that are still open.


Conclusion
============================================================

Two separators are enough to build pairs, sequences, and
nested structures. No capability required a new token. Each
one came from removing a part of the pair and giving the
remainder a role.

The price is paid elsewhere. The writer gets less syntax.
The parser gets more work. The producer and the consumer
must agree on everything the content does not declare: the
layer, the data types, the meaning of a missing value.

The following is left to an implementation:

- what a line without the secondary separator means on
  Layer 2
- how an empty value differs from an unknown one
- how a multi-line value is assembled from value entries
- which tokens serve as the separators

The idea reaches beyond this model: before adding syntax,
exhaust the combinations of what is already there.



|h.page-info|
============================================================

.. include:: tables/page-info.perspective.580.txt

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt

