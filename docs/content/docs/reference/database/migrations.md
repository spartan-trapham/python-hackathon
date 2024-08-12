+++
weight = 3202
date = "2023-05-03T22:37:22+01:00"
draft = true
author = "Pham Xuan Tra"
title = "Migrations"
icon = "rocket_launch"
toc = true
description = "Update database structure for business logic changes"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["intermediate"]
+++

Migration is a process of maintaining the states of database. This process can be detached from the source code. The directory of migration usually contains only `sql` supporting updating database states. The process of running those `sql` belongs to an application named [flyway](https://www.red-gate.com/products/flyway/community/)

```
migrations
├── 001-users.sql
├── 002-role-and-permission.sql
└── 003-seed-super-admin.sql
```
