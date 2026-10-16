.. _writing-precisely.perspective.394:

------------------------------------------------------------
[Foundation] Closing and Layering a Term System
------------------------------------------------------------

.. highlights::

   .. include:: partials/featured.perspective.672.txt

Reliability of :ref:`a closed term system
<writing-precisely.perspective.672>` depends on the structure
of the closure and the consistency of the levels of detail.


.. _writing-precisely.perspective.394-87:

Structure of the Closure
============================================================

Ideally, every term in the system is defined within the
system through its relations to other terms. The chain of
definitions cannot go on indefinitely: at some point, there
are terms the system cannot define. These are foundation
terms. The system owns them, but it does not own their
definitions, which rest on what the reader already
knows. Instead of defining foundation terms, the system
introduces them in a dedicated, formalized space, using
:term:`expected terms <Expected term (conv. 274)>` carefully
chosen for this particular system. In this way, a closed
term system gives them a stable base. Without it, foundation
terms invite different readings, and since every other term
is built on them, a misread foundation term distorts the
understanding of the whole system.

A problem statement is an example of such a space. It is
written before any solution exists, and it names what the
solution will be about in words the reader already
understands. Everything the solution later defines is built
on the terms the problem statement introduced.


.. _writing-precisely.perspective.394-06:

Levels of Detail
============================================================

The consistency of the levels of detail deals with another
problem: without it, the structure of the system becomes
obscure. What does an online store consist of? A product
catalog, a shopping cart, a checkout, and a message queue.
Each of these terms can be well defined, and the list looks
complete. Yet the message queue is how the checkout passes
orders on for processing: it is not a part of the store next
to the checkout but a part of how the checkout is
implemented. The answer flattens two levels of detail into
one.

To avoid this, each term must be placed on exactly one
level. Although glossaries are the designated place for term
definitions, it is more common for definitions to be included
in structured documents that present information in the form
of a narrative.

The level of detail can apply to any structural unit,
ranging from a sentence up to the whole document, in the
sense that all terms in the unit belong to the same level. If
the level of detail is associated with a small unit, such as
a sentence, switching from one level to another happens
frequently. The switch not only requires more effort to
understand the meaning but also creates an additional risk of
incorrect interpretation.

A natural approach is to keep the chosen level of detail
within a section and declare it in the heading. This works
for each section individually. When the context grows to
include more than one section, the switch becomes much harder
to notice: the declaration stays with its section, while the
reader's context does not. A good example of this problem is
cross-references, where the reader is recommended to continue
reading elsewhere for more detail and arrives at a different
level in the middle of a thought.

The most stable control of the level of detail is through
whole documents whose kind implies the level of detail or
which state it explicitly. Documents whose structure is
predefined are particularly reliable in this respect, as each
section must follow a set of requirements. Links to other
documents make switching the level of detail a predictable
transition or continuation: unlike a cross-reference into
another section, a link leads to a document whose level the
reader knows before starting to read.


Tiers: Term Catalogs in Document Types
============================================================

When a closed term system is implemented in a set of
documents, the level of detail becomes its organizing
principle. Suppose the level of detail is applied
consistently per document, and each document is treated as
an instance of a document type: a set of predefined sections
whose content is created and modified according to specific
requirements. Then the whole system can be reasoned about as
a network of relations among those document types.

When terms are extracted from an instance, the associated
document type provides simple criteria for determining which
terms belong together. The terms defined in an instance of a
specific document type form a closed term system, too: terms
defined in instances of more general document types are known
to its reader and work within it as expected terms. Provided
the level of detail covers the whole document, the terms in
the catalog can be evaluated as expected or provided terms,
which reveals problems such as missing term relations or
:ref:`excessive details <writing-precisely.perspective.452-91>`.

The catalog of terms defined in one instance constitutes a
separate tier within the closed term system being designed.
If each term is defined in only one instance, it belongs to
exactly one tier, and the document type of that instance
gives it its level of detail.


Orders: Arrangements of Tiers
============================================================

With an effective arrangement of tiers, a closed term system
becomes repeatable: the same arrangement can be used to build
new systems. An order is a template for such an arrangement.
It is a lightweight construct. It mandates document types,
which contain no content of their own, associates each of
them with a level of detail, and prescribes which more
general document types supply terms to which more specific
ones.

When an order is instantiated, the instances of its document
types form a closed term system as the product, and their
term catalogs become its tiers.


|h.ref|
============================================================

.. seealso::

   - :ref:`writing-precisely.perspective.528`
   - :ref:`writing-precisely.perspective.672`

|h.page-info|
============================================================

.. include:: tables/page-info.perspective.394.txt

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt
