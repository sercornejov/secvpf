# secvpf
App to create portfolios (Simple)

This project is a simple app to generate portfolios of different people and careers.
The database has referential integrity keys defined.

When a user registers, it creates a record in the Django-admin database and assigns it a specific permission group. In addition, it creates a record in the other tables with null data, but with the user_id so that the relationship between each table is unambiguous and thus filtering each table by user is very simple
