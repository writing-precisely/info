.. _writing-precisely.case.768-1:

------------------------------------------------------------
Local Storage for Employee Details
------------------------------------------------------------

Lab69 is a persistent storage system for incomplete information. It is based
on simple principles that allow a great degree of flexibility and
extensibility. Due to its simplicity, Lab69 is easy to implement and
reason about.

.. rubric:: Purpose

Lab69 is designed to support research, investigation and other
activities where it is difficult to predict the optimal structure of
data upfront. In Lab69, data can be rearranged, extended, and
redefined throughout its lifetime without causing significant updates.

.. rubric:: Implementation

Lab69 is based on file system objects: directories and
files. There are very few mandatory naming conventions in
Lab69. However, it is strictly required that effective conventions
be applied consistently.

Lab69 does not have the concept of null. If an object does not have a certain
value then it is not recorded at all.

.. rubric:: Problem statement

When storing information about an entity, such as an employee, in a spreadsheet
or database, you create a table with columns for each attribute of the
entity. In the case of employee records, the attributes might be the employee name,
email, position, and date of employment. For each employee, you create a
separate record placing each piece of information in the designated column.

=================  ===============================  =================  ==================
Name               Email                            Position           Employment date
=================  ===============================  =================  ==================
Alice Green        alice.green@imagicorp.com        Marketing Manager  February 15, 2020
Brian Carter       brian.carter@imagicorp.com       Software Engineer  August 10, 2021   
Chloe Hernandez    chloe.hernandez@imagicorp.com    HR Specialist      May 1, 2023 
=================  ===============================  =================  ==================

The actual format of storing this information varies depending on the system you
are using: YAML, JSON, XML, a persistent binary structure or any other. Storing,
analysing, and presenting a simple structure, such as the employee records
example are simple. When the data need to become more complex, the data storage
format and the agent need to become more complex, too.


Employee records in a YAML document

.. code-block:: yaml

   employees:
     - name: Alice Green
       email: alice.green@imagicorp.com
       position: Marketing Manager
       date_of_employment: 2020-02-15
     - name: Brian Carter
       email: brian.carter@imagicorp.com
       position: Software Engineer
       date_of_employment: 2021-08-10
     - name: Chloe Hernandez
       email: chloe.hernandez@imagicorp.com
       position: HR Specialist
       date_of_employment: 2023-05-01
   
In case of employee records, you introduce more complexity when you decide to
improve the design and store positions in another document. Then, your original
*employees* document needs to be redesigned to store references to positions
from the *positions* document. The references must be unique position
identiers. As such, numeric identifiers, unique abbreviations or
a sequence of characters of certain pattern may be used.

Positions:

.. code-block:: yaml

   positions:
     MM: Marketing Manager
     SE: Software Engineer
     HR: HR Specialist
   
The employee records can now reference just the unique position identifier. The
obvious improvement is that you may make further changes to the *positions*
document without affecting the structure of the *employees* document.

.. code-block:: yaml

   employees:
     - name: Alice Green
       email: alice.green@imagicorp.com
       position: MM
       date_of_employment: 2020-02-15
     - name: Brian Carter
       email: brian.carter@imagicorp.com
       position: SE
       date_of_employment: 2021-08-10
     - name: Chloe Hernandez
       email: chloe.hernandez@imagicorp.com
       position: HR
       date_of_employment: 2023-05-01
   
The reference to positions in *employees* is symantically coupled with the name
of the position. If you decide to change the job description of *Software
Engineer* to *Developer*, you will probably not bother changing the *SE*
reference to *D* until it is confusing. The agent for this data structure needs
to be made more complex to be able to process references to other documents.

Over time, when the complexity of information grows, the data structures for
persistent storage will become more and more complex. Some structures will have
to be adjusted based on the usage. The agent that processes these data
structures must also grow in complexity.

Lab69 defines the persistent storage in a way that the complexity of data
will not grow. The agent that complies with the rules of Lab69 need not be
altered to process relations and which were not known or were not included in
the initial version of your structure. 

Overview
============================================================


The *employee* catalogue in Lab69 is represented by a directory. Each column
is stored in a separate file. All values of the name attribute are stored in the
*name.69* file, all values of the email attribute are stored in the *email.69*
file and so on.

The .69 files are very simple in structure. Each value in this file is recorded
on a separate line. Each line may only contain a unique identifier and the value
itself. In other words, each record in a .69 file always consists of exactly two
components.

The contents of the *name.69* file

483729 Alice Green
915384 Brian Carter
627418 Chloe Hernandez

Contents of the *email.69* file

483729 alice.green@imagicorp.com
915384 brian.carter@imagicorp.com
627418 chloe.hernandez@imagicorp.com 

Although the identifiers in this example are made of digits, the values are not 
expected to be in any particular order. However, if the same identifier is found
in several columns, then all values bound to this identifier are linked as
fields in a record.

For example, *Alice Green* from *name.69* is bound to the *483729*
identifier. The value *alice.green@imagicorp.com* is also bound to this
identifier in the *email.69* file. Thus, there exists a record with the
identifier *483729*. Its *name* attribute is set to **Alice Green** and its
*email* attribute is set to *alice.green@imagicorp.com*.

At this point, Lab69 reveals its key features:

1. Identifiers do not have any semantic association
2. Values in a column are in an arbitrary order.
3. Columns are not defined in any particular order.

Lab69 references
============================================================


References in Lab69 are stored as ordinary columns. To implement a reference
to another catalogue, create the catalogue and then create a reference columns.

Example:

The contents of *name.69* column from the *position* catalogue

836521 Marketing Manager
294867 Software Engineer
751304 HR Specialist

Now, we can place a reference to the related positions in the *employees*
catalogue. To make it clear that *position* is not an ordinary column but a
reference, this example uses the *@* prefix.

Example:

The contents of the *@position.69* column in the *employee* catalogue

483729 836521
915384 294867
627418 751304

Besides being unique, identifiers must always follow three rules:

1. They should not be associated with any data and must always be a sequence of
   random non-whitespace characters.
2. The identifier in a column may consist only characters from the chosen
   vocabulary. This implies that identifiers cannot be a sequence of digits for
   one value and a sequence of alphabetic characters - for another.
3. Once assigned the identifier is never changed 

Benefits
============================================================

In Lab69, there are now primary keys. The way how a record is unique among
other records in the catalogue depends on the needs of the application that uses
the catalogue. If needed, the combination of unique attributes that identify a
record may be easily changed.

The record identifier is very stable as it does not depend on the state of any
of its attributes: there is no practical reason to change the record identifier
to another. The stability of the record identifier makes it an ideal candidate for
constructing references in data sets.

The columns in a catalogue are not defined in any order. 

In Lab69, there is no concept of null. If a certain value does not exist, it
is merely not included a column. If the value becomes known it is added without
having to redefine the schema or any other metadata.

Columns are formally strict. The structure of columns is simple and is easy to manage. For each line there
are always two components: the unique identifier, or the signature, and the
value. If one of these is missing the whole line is invalid and is ignored.

Columns are semantically strict. The values must be consistent. If the column is declared to store email
addresses, then no other values are allowed.

Columns are resilient. Non conforming lines, such as those with missing
signatures or values or blank lines, must be skipped by the agent.

The smallest unit that Lab69 recognizes is a value and a signature. Values
the actual units of information that Lab69 stores and they can be anything
you need: a number, a name of a person, or a date. A signature is a sequence of
non-white space characters that can be associated with a value.

Implementing Lab69 is easy. Due to the simplicity of the format, the same conforming
agent can process complex structures that describe totally different phenomena.

Implementing relations
============================================================


One to many

In the catalogue that references another, such as *employee*, create a column
(*@position.69*) that matches the identifier of the referenced catalogue
(*position*). In this column, create values for all relevant record signatures
where the data matches a record signature from the *position* catalogue. Note
that the *@* prefix is not mandatory. It is a convenience for the sake of this
demonstration.

Many to many

In the case of employee records, the many to many relation may be introduced
when you need to track which projects employees are envolved: one employee may
be assigned to multiple projects, and one project is assigned to multiple
employees. Assuming there already exists a catalogue for projects (named
*project*) and for employees (named *employee*), create a new catalogue
(named *project-employees*). Each value of the *@project.69* column has a record
signature and the data that refers to a valid signature from the *project*
catalogue. Each value of the *@employee.69* column has a record signature and
the data that refers to a valid signature form the *employee* catalogue.

Note that the naming convensions in this section differ from the recommended
practicies in the *Lab69* specification where catalogue names are created in
the same way as record signatures.

Self references
------------------------------------------------------------

In the case of employee records, self references are introduced in the new
*manager.69* column. This column refers to another record in the *employee*
catalogue informing that the referenced employee is the manager for the current
record.

In the *manager.69* column, the values include the record signature of the
current employee and the data refers to a valid record signature in the
*employee* catalogue.

Example:

The contents of the *name.69* column

483729 Alice Green
627418 Chloe Hernandez

A record from the *manager.69* column where *Alice Green* is the manager of
*Cloe Hernandez*.

627418 483729

.. important::

   catalogue (dir) -> attribute (file) -> value (line) -> signature: content

   application:

   1. search in sparse data sets
   2. data types: defined based on the purpose of the catalogue
      the boundaries of the catalogue are easy to detect based on signatures

