CREATE TABLE IF NOT EXISTS produtos(
    code int(4) NOT NULL,
    name CHAR(50),
    stock BIGINT NOT NULL,
    value FLOAT,
    id_category TINYINT NOT NULL,
    PRIMARY KEY(code)
);

CREATE TABLE IF NOT EXISTS categorias(
    id TINYINT not NULL,
    name CHAR(40) NOT NULL,
    description VARCHAR(200),
    PRIMARY KEY(id)
);

ALTER TABLE produtos ADD FOREIGN KEY (id_category)REFERENCES categories(id);



