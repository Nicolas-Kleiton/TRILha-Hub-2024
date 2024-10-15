CREATE EXTENSION pgcrypto;

CREATE TABLE IF NOT EXIST users (
    id_users            VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid(),
    password_users      VARCHAR(255) NOT NULL,
    name_users          VARCHAR(255) NOT NULL,
    email_users         VARCHAR(255) NOT NULL,
    created_at_users    TIMESTAMP DEFAULT NOW()
);
