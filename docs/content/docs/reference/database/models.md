+++
weight = 3201
date = "2023-05-03T22:37:22+01:00"
draft = true
author = "Pham Xuan Tra"
title = "Models"
icon = "rocket_launch"
toc = true
description = "Presentation of database in the code base"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["intermediate"]
+++

A model describes exactly a database table (columns, constrains, indexes). Following [Alchemy Unify pattern](https://docs.sqlalchemy.org/en/20/tutorial/), the model is designed to work with both ORM and Core of SQLAlchemy

```python
class User(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'users'

    name = Column(VARCHAR(128), nullable=True)
    email = Column(VARCHAR(64), nullable=False)
    password = Column(VARCHAR, nullable=False)
```
_In the model sample, User inherit ID (UUID) and some audit columns (`created_at`, `created_by`, `updated_at`, `updated_by`)
