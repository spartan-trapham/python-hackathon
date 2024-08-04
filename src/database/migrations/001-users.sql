CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE public.users (
	id uuid DEFAULT uuid_generate_v4() NOT NULL,
	"name" varchar(128) NULL,
	email varchar(64) NOT NULL,
	"password" varchar NOT NULL,
	created_at timestamptz DEFAULT now() NOT NULL,
	updated_at timestamptz DEFAULT now() NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT pk_users_id PRIMARY KEY (id),
	CONSTRAINT uq_users_email UNIQUE (email)
);

CREATE TABLE public.roles (
	id uuid DEFAULT uuid_generate_v4() NOT NULL,
	"name" varchar(128) NOT NULL,
	description varchar NULL,
    created_at timestamptz DEFAULT now() NOT NULL,
	updated_at timestamptz DEFAULT now() NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT pk_roles_id PRIMARY KEY (id),
	CONSTRAINT uq_roles_name UNIQUE ("name")
);

CREATE TABLE public.permissions (
	id uuid DEFAULT uuid_generate_v4() NOT NULL,
	"name" varchar NOT NULL,
	metadata jsonb NULL,
    created_at timestamptz DEFAULT now() NOT NULL,
	updated_at timestamptz DEFAULT now() NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT pk_permissions_id PRIMARY KEY (id),
	CONSTRAINT uq_permissions_name UNIQUE ("name")
);
