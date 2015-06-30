-- add a user to users
create function add_user(name text) returns void as $$
    begin
        insert into users(name) values(name);
    end
$$ LANGUAGE plpgsql;

-- add a task
create function add_task(title text, description text) returns void as $$
    begin
        insert into tasks(title, description) values(title, description);
    end
$$ LANGUAGE plpgsql;
