-- Create the following tables: 
-- client:
-- id (PK)
-- username (unique)
-- joined_on
-- password

-- post:
-- id(PK)
-- client_id (FK)
-- content
-- title

Create Table client (
    id int(11) NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    joined_on datetime NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

create table post (
    id int(11) NOT NULL AUTO_INCREMENT,
    client_id int(11) NOT NULL,
    content varchar(255) NOT NULL,
    title varchar(255) NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE
);

