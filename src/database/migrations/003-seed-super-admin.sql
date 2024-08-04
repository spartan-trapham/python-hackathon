
INSERT INTO users (name, email, password)
VALUES ('Super Admin', 'superadmin@superadmin.com', '$2a$14$kqQG9Gn77My2yPWIlVasaONTaem2hlhd0nUrhzYzdMGBNb7ahqZ/S');

INSERT INTO roles (name, description)
VALUES ('Super Admin', 'Super Admin');

INSERT INTO role_permissions (role_id, permission_id)
VALUES (
    (SELECT id FROM roles WHERE name = 'Super Admin'),
    NULL
);

INSERT INTO user_roles (user_id, role_id)
VALUES (
    (SELECT id FROM users WHERE email = 'superadmin@superadmin.com'),
    (SELECT id FROM roles WHERE name = 'Super Admin')
);
