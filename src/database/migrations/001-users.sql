CREATE TABLE users
(
    id         uuid                     DEFAULT uuid_generate_v4() NOT NULL PRIMARY KEY,
    name       text                                                NOT NULL UNIQUE,
    email      text                                                NOT NULL UNIQUE,
    password   text                                                NOT NULL,
    created_at timestamp WITH TIME ZONE DEFAULT NOW()              NOT NULL,
    updated_at timestamp WITH TIME ZONE,
    deleted_at timestamp WITH TIME ZONE,
);

INSERT INTO users (name, email, password)
VALUES ('example', 'example@example.com', '$2a$14$kqQG9Gn77My2yPWIlVasaONTaem2hlhd0nUrhzYzdMGBNb7ahqZ/S');