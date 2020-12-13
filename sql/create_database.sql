CREATE EXTENSION IF NOT EXISTS dblink;
-- Creating a database by name --
--- SELECT CreateDB('app');
CREATE OR REPLACE FUNCTION CreateDB(dbname text)
RETURNS integer AS
$func$
BEGIN

IF EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
	RAISE NOTICE 'Database already exists';
	RETURN 1;
ELSE
	PERFORM dblink_exec('dbname=' || current_database() || ' user=postgres password=mypass'
, 'CREATE DATABASE ' || quote_ident(dbname));
	IF EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
	    RAISE NOTICE 'Database created successfully';
    END IF;
	RETURN 1;
END IF;

END
$func$ LANGUAGE plpgsql;
				    
				    
CREATE OR REPLACE FUNCTION DeleteDB(dbname text)
-- Deleting a database by name --
--- SELECT DeleteDB('app');
RETURNS integer AS
$func$
BEGIN

IF EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
	PERFORM dblink_exec('dbname=' || current_database() || ' user=postgres password=mypass'
, 'DROP DATABASE ' || quote_ident(dbname));
	IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = dbname) THEN
	    RAISE NOTICE 'Database deleted successfully';
    END IF;
	RETURN 1;
ELSE
	RAISE NOTICE 'Database does not exist';
	RETURN 1;
END IF;

END
$func$ LANGUAGE plpgsql; 
