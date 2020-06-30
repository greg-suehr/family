# Tables

Tables provide a way to interact with your applicaiton's data model.

The module is broken out into domains:
  - Table : represents application data and provides and interface to interact with it.
  - Search : defines rules and workflows to query the data.
  - Analyze : provides tools to visualize and optimize.


## Table

A Table flexibly represents a set of related entities.

Interfaces are provided to interact with these entites:
  - Select: reference a variety of Search rules to select data.
  - Insert: workflows to add new data, including populating necessary relationships.
  - Update: select and modify existing data, subject to app data intergrity rules.

In aim of interpretability, Tables should be defined using plain text files such as YAML.


### Table.Select

Interacts with Search.

TODO:


### Table.Insert

Follow model defined relationships (e.g. foreign keys) to build a workflow for inserting data.

Tables should specify an insert_mode:
  - type_list: small tables which can reasonably be display on screen and scrolled to nav.
  - entities: large tables that users will frequently add to or manipulate.

For a budget application: a base 'entity' table, Transactions, and a 'type_list', Transaction_type.

TODO:
 - implement insert(), break out SQL from control tables.


### Table.Update:

Define a workflow to modify or delete data

Tables can define accessibility rules that are universal, group based, or user based.
 - can_update:
 - can_delete:

TODO:
 - implement update(): break out SQL from control tables.

