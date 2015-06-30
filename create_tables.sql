-- the users
create table users (
    id  serial primary key,
    name text not null
);

-- the possible tasks
create table tasks (
    id serial primary key,
    title text not null,
    description text not null
);

-- a task associated with a user in time

create table user_tasks (
    id serial primary key,
    task_id int references tasks(id),
    user_id int references users(id),
    duration tsrange not null,
    completed boolean not null
);
