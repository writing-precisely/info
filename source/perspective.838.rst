.. _writing-precisely.perspective.documentation-as-code:
.. _perspective.838:

------------------------------------------------------------
Documentation as Code: Shifting Value
------------------------------------------------------------

In relation to software, *code* means several things. A
technically accurate definition of code is that it is a set
of instructions that a computer executes. A practical
definition views code as a collection of files that contain
the logic of what the program does.

   This definition is practical because this is the
   perspective where you *reason about code*.

The popular concept |dac| is actually based on a simplified
treatment of code: stored under a version control system,
updated through PRs, and pushed through the pipeline that
builds the application. |dac| borrows version control,
update model, and automation on the grounds that both kinds
of source code are plain files that a repository can hold.

However, *sharing a toolchain* is not the same as *treating*
|doc| as code.

   Besides, the tools were never specific to |a_code| in the
   first place.

.. _perspective.838.412:

I Will Show You the Source: What Do You See?
============================================================

|+a_src| and |d_src| are not the same kind of thing. An
|app| becomes a product only after a series of
transformations. Its source is inert: it must be built and
run before it delivers any practical value. Until then its
capabilities are unknown.

|+doc| is already a product in its source form, because
**reading it is enough**. Both the structure and content
always deliver valuable information.

This is why the readability of the source is among the most
essential requirements of every plain text |doc| format. In
fact, |doc| is even more beneficial in source code
form. Source files in *Asciidoc*, or *reStructuredText*, or
*Org-mode* carry information about crucial elements that the
rendered output discards.

   In |dac|, the value of |doc| as a product is not
   considered.

.. important::

   Why does it even matter? Acknowledging that |doc| is a
   product does not deny the fact that it is the rendered
   form that matters most. Thus, both pipelines are aligned
   perfectly: sources updated, sources reviewed, product
   built and deployed.

   It matters because it shifts the focus from a shallow
   procedure to a profound and important process while
   staying in the same context.



.. _perspective.838-115:

Use a Pipeline: They Are All the Same.
============================================================

The end products constructed by the build pipelines have
different fates in |d_src| and |a_src|.

For |doc|, the story ends there. The end product is made
available to readers. For |app|, the built program goes to
testing and it takes a number of iterations until
the result is good enough for a public release.

Thus, |dac| applies to the build pipeline only: from the
point when an updated |doc| source is pushed to the version
control system up to the point when the build process outputs a
|doc| site or a PDF document. The stages of this process are
quite similar to the build pipelines of |a_code|.

On stage 1, the *developer* updates the |a_src| and the
*author* updates the content and structure of |d_src|.

On stage 2, the *developer* submits the |a_src| for review
and the *author* requests a review from the |+sme|.

On stage 3, the changes are merged to trigger the build
process. (runs automatically; nothing interesting happens
after it has been set up.)



.. _perspective.838-645:

Stage 3: Building the Output
============================================================

Stage 3 is very important for those DevOps engineers who set
up the pipeline. Thanks to |dac|, they can apply the same
approach to both |d_src| and |a_src|.

For |doc|, nothing interesting happens on this
stage. Ever. Even in the case of a single source environment
that produces multiple variants of |doc| for different
groups of readers — internal+external |doc|, multiple
customers, multiple output formats, or a combination of
these — this stage hardly changes a lot.

This stage can be simplified to building output locally. In
this case calling the building a stage is too much.

.. important::

   If this stage is not boring, then the documentation is
   built on top of an inapt framework.



.. _perspective.838-629:

Stage 2: Reviewing the Changes
============================================================

This stage introduces an important distinction between
processing |a_src| and |d_src|. For both, this stage is the
review. In case of |a_src|, the review is done by an
experienced colleague familiar with the code base and rules
of updating it properly.

To review |d_src|, it may require attention of another
documentation author. But this stage only works if the
|+sme| is involved. And the |+sme| is not the same role as
the reviewer of |a_src|. The |+sme| is knowledgeable of the
subject being documented and is the owner of the resources
which were provided to be used as the basis of the
update. But the |+sme| need not know the complexity of
|d_src|.

One of the declared values of |dac| is that reviewers may
update |doc|, too. For a small project, it might
work. For complex projects, the |+sme| can make consistent
and correct changes to |d_src| only if this person
understands the structure, guidelines, layout principles,
and the authoring environment as well as assumes the
author's responsibility. In other words, the |+sme| must
become an author, too.

   This is where |dac| becomes uncomfortable as it places no
   such demands.



.. _perspective.838-735:

Stage 1: code|doc
============================================================

With the build pipeline being boring on stage 3 and the
review process not correctly shaped, you can observe a
paradox. |dac| is not directly related to code but the case
where code contributes to documentation is not related to
|dac|.

   |dac| declaring resemblance to code (as one might
   conclude from the very name) only takes a toolchain that
   happens to be used in software development. However, the
   toolchain is not directly related to code. On the other
   hand, the real contribution of code to documentation goes
   completely ignored.

In software, *code* is broader than *source code*. It covers
a program's behaviour, its algorithms, and its structure —
not the symbols in files processed by the toolchain. |+doc|
as a product is the content: the information and the means
of organizing it for readers. The logic and structure which
are used to reason about what software does — that's what
makes |a_code| a product, too.

It is reasonable to suggest that, as products, |doc| and
|a_code| are comparable. This comparison has exactly one
beneficiary: the author.



.. _perspective.838-168:

code|doc: Effective Immeditely
============================================================

A practice proven for |a_code| carries a value that |doc|
may be missing. It is not |a_code| being useful by
introducing C++ structures in prose. It is viewing parts of
|doc| **based on principles** that make those practices
valuable. Just a few examples:

Variables

   In |a_code|, a variable must be defined before it is
   used. In |doc|, terms are the variables. They must be
   declared properly.

Modules

   In |a_code|, modules group what belongs together and
   separates what does not. |+doc| is broken down into
   sections; what modularity adds is the criterion: a
   section must hold a selection of related ideas and
   nothing more.

Don't Repeat Yourself

   In |a_code|, a piece of logic is defined in one place and
   called wherever it is needed. In |doc|, the DRY principle
   requires the same. In practice, this criterion guards
   against saying the same thing in multiple places — just
   using a different wording.

None of these will arrive unchanged. A **variable** becomes
a defined term, a **module** becomes a bounded section,
**Don't Repeat Yourself** becomes one concept defined in
exactly one place along with related details. Best practices
change form because |doc| brings the same discipline into a
different context.

.. _perspective.838-396:

Reasoning from Another Context: Is What You Get
============================================================

Discipline that the two products share is the precision of
writing. |+a_code| reaches precision through incorporating
the reasoning into the context of operation. |+doc| reaches
it through incorporating the reasoning into its content and
form. A practice proven for one can be expected to have an
equivalent in the other. And the toolchain has nothing to do
with it.

------------------------------------------------------------

   :version: 1.0
   :revision: 2026-09-15
   :written.by:   |author|
   :assisted.by:  |agent|

.. include:: ./variables/common.txt
.. include:: ./variables/names.txt

