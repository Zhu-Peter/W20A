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
    PRIMARY KEY (id),
    FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE
);

-- INSERT at least 3 clients and 5 posts

insert into client (username, joined_on, password) values 
    ('john', '2019-01-01', '1234password'),
    ('jane', '2019-02-02', '2345password'),
    ('jill', '2019-03-03', '9876password');

insert into post (client_id, content, title) values 
    (1, 'This is a post', 'This is a title'),
    (2, 'This is another post', 'This is another title'),
    (3, 'This is a third post', 'This is a third title'),
    (2, 'This is a 4th post', 'This is a fourth title'),
    (3, 'This is fifth post', 'This is 5th title');

-- Create the following DB procedures:

-- Given a username and password as input, SELECT the id and username  for the user that matches that given input

create procedure get_user(user varchar(20), passvarchar(20))
    select id, username from client where username = user and password = pass;

-- Given a user id, blog content and title as input, INSERT a new row into the post table

create procedure create_post(client_id int, content varchar(200), title varchar(20))
    insert into post (client_id, content, title) values (client_id, content, title);

-- Given no input, return the id, content and title of each post
create procedure get_posts()
    select id, content, title from post;

