In this project, I intend to link two amazing worlds: Databases and Python!

In the first part, I will use the module MySQLdb to connect to a MySQL database and execute my SQL queries.

In the second part, I will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, my biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. I won’t write any SQL queries only Python code. Last thing,my code won’t be “storage type” dependent. I will be able to change my storage easily without re-writing my entire project.
