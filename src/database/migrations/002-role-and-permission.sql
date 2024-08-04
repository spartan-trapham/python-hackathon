CREATE TABLE public.user_roles (
	id uuid DEFAULT uuid_generate_v4() NOT NULL,
	user_id uuid NOT NULL,
	role_id uuid NULL,
    created_at timestamptz DEFAULT now() NOT NULL,
	updated_at timestamptz DEFAULT now() NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT pk_user_roles_id PRIMARY KEY (id),
	CONSTRAINT uq_user_roles_user_id_role_id UNIQUE (user_id,role_id),
	CONSTRAINT fk_user_roles_users_user_id FOREIGN KEY (user_id) REFERENCES public.users(id),
	CONSTRAINT fi_user_roles_roles_role_id FOREIGN KEY (role_id) REFERENCES public.roles(id)
);

CREATE TABLE public.role_permissions (
	id uuid DEFAULT uuid_generate_v4() NOT NULL,
	role_id uuid NOT NULL,
	permission_id uuid NULL,
    created_at timestamptz DEFAULT now() NOT NULL,
	updated_at timestamptz DEFAULT now() NULL,
	deleted_at timestamptz NULL,
	CONSTRAINT pk_role_permissions_id PRIMARY KEY (id),
	CONSTRAINT uq_role_permissions_role_id_permission_id UNIQUE (role_id,permission_id),
	CONSTRAINT fk_role_permissions_roles_role_id FOREIGN KEY (role_id) REFERENCES public.roles(id),
	CONSTRAINT fk_role_permissions_permissions_permission_id FOREIGN KEY (permission_id) REFERENCES public.permissions(id)
);
