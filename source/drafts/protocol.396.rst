.. _writing-precisely.convention.396:

------------------------------------------------------------
Simple Data Storage Model: Symbolic Notation
------------------------------------------------------------

This document defines concepts only. Concrete characters belong to an
implementation (see Keel).

* Symbols used in this document
- N :: a name
- V :: a value
- T :: the secondary separator
- $ :: the primary separator

Every symbol written stands for something that must be present.
=[ ]= marks an optional part. Records are written one after another:
=NT$ TV$ T$= is three records.

* Separators
- primary separator ($) :: marks where one record ends and the next
  begins.
- secondary separator (T) :: marks where the name ends.
- separator rule :: the two must differ, and neither may contain the
  other.
- separator levels :: the model defines two levels, primary and
  secondary. A third level is left to implementations, within the
  extension boundary.

* Catalog
| construct     | context | layer 1     | layer 2     | meaning                    |
|---------------+---------+-------------+-------------+----------------------------|
| NTV$          | outside | defined     | defined     | pair                       |
| NTV$          | inside  | unsupported | defined     | association                |
| NT$           | outside | defined     | defined     | sequence start             |
| NT$           | inside  | unsupported | defined     | nested sequence start      |
| TV$           | outside | undefined   | undefined   |                            |
| TV$           | inside  | defined     | defined     | item                       |
| T$            | outside | undefined   | undefined   |                            |
| T$            | inside  | defined     | defined     | sequence end               |
| NTTV$         | any     | unsupported | defined     | sequence start, first item |
| $$ (run)      | any     | unsupported | defined     | close all                  |
| no T (X$)     | any     | undefined   | undefined   | name and value ambiguous   |
| NT$ T$, NTT$  | any     | excluded    | excluded    | empty sequence (null)      |
| other T runs  | any     | undefined   | undefined   | e.g. TTV$, TT$, NTTT…      |
