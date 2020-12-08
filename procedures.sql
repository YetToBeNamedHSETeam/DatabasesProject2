CREATE EXTENSION dblink;
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
	RETURN 1;
END IF;

END
$func$ LANGUAGE plpgsql;


-- CALL CreateTables();
CREATE OR REPLACE PROCEDURE CreateTables()
LANGUAGE plpgsql
AS $$
    DECLARE table1 VARCHAR     := 'Doctor';
    DECLARE table2 VARCHAR     := 'Service';
    DECLARE table3 VARCHAR     := 'Patient';
    DECLARE table4 VARCHAR     := 'Logbook';

    DECLARE DoctorID VARCHAR       := 'DoctorID';
    DECLARE DoctorName VARCHAR     := 'DoctorName';
    DECLARE ServiceID VARCHAR      := 'ServiceID';
    DECLARE Title VARCHAR          := 'Title';
    DECLARE Cost VARCHAR       	   := 'Cost';
    DECLARE PatientID VARCHAR      := 'PatientID';
    DECLARE PatientName VARCHAR    := 'PatientName';
    DECLARE Phone VARCHAR          := 'Phone';
    DECLARE Number VARCHAR    	   := 'Number';
    DECLARE Date   VARCHAR         := 'Date';
    DECLARE Patient   VARCHAR      := 'Patient';
    DECLARE Service   VARCHAR      := 'Service';
	DECLARE Doctor   VARCHAR       := 'Doctor';

BEGIN
	EXECUTE format('CREATE TABLE IF NOT EXISTS '|| table1 ||' 
				  ('|| DoctorID ||' SERIAL PRIMARY KEY, 
				   '|| DoctorName ||' varchar(40));');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| table2 ||'
				  ('|| ServiceID ||' SERIAL PRIMARY KEY, 
				   '|| Title ||' varchar(40), 
				   '|| Cost ||' int);');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| table3 ||'
				  ('|| PatientID ||' SERIAL PRIMARY KEY, 
				   '|| PatientName ||' varchar(40), 
				   '|| Phone ||' varchar(12));');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| table4 ||'
				  ('|| Number ||' SERIAL PRIMARY KEY, 
				   '|| Date ||' date, 
				   '|| Patient ||' integer,
				   FOREIGN KEY ('|| Patient ||') REFERENCES '|| table3 ||'( '||PatientID||' )
                        	ON DELETE CASCADE
                        	ON UPDATE CASCADE,
				   '|| Service ||' integer,
				   FOREIGN KEY ('|| Service ||') REFERENCES '|| table2 ||'( '||ServiceID||' )
                        	ON DELETE CASCADE
                        	ON UPDATE CASCADE,
				   '|| Doctor ||' integer,
				   FOREIGN KEY ('|| Doctor ||')REFERENCES '|| table1 ||'( '||DoctorID||' )
                        	ON DELETE CASCADE
                        	ON UPDATE CASCADE);');
    RAISE NOTICE '(%, %, %, %) created', table1, table2, table3, table4;
END;
$$;


-- filling the table by name --
CREATE OR REPLACE PROCEDURE FillTable(IN table_n name)
LANGUAGE plpgsql
AS $$
	DECLARE table1 VARCHAR     := 'Doctor';
    DECLARE table2 VARCHAR     := 'Service';
    DECLARE table3 VARCHAR     := 'Patient';
    DECLARE table4 VARCHAR     := 'Logbook';
BEGIN
    IF table_n = table1 THEN
	
        INSERT INTO Doctor (DoctorID, DoctorName) VALUES (1, 'Vasiliy Pupkin');
        INSERT INTO Doctor (DoctorID, DoctorName) VALUES (2, 'Sanya Kekov');
		INSERT INTO Doctor (DoctorID, DoctorName) VALUES (3, 'Kista Nonameova');
		INSERT INTO Doctor (DoctorID, DoctorName) VALUES (4, 'Andjelika Djolinova');
		INSERT INTO Doctor (DoctorID, DoctorName) VALUES (5, 'Elena Malysheva');
		INSERT INTO Doctor (DoctorID, DoctorName) VALUES (6, 'Mortal Combat');
		INSERT INTO Doctor (DoctorID, DoctorName) VALUES (7, 'Frog Memov');
		INSERT INTO Doctor (DoctorID, DoctorName) VALUES (8, 'Michail Dirty');
        RAISE NOTICE 'Table (%) filled', table1;
    END IF;

    IF table_n = table2 THEN
	
        INSERT INTO Service (ServiceID, title, cost) VALUES (1,  'Kidnay removal', 20000);
        INSERT INTO Service (ServiceID, title, cost) VALUES (2,  'Treatment with braces', 150000);
        INSERT INTO Service (ServiceID, title, cost) VALUES (3,  'Breast augmentation', 500000);
        INSERT INTO Service (ServiceID, title, cost) VALUES (4,  'Rhinoplasty', 200000);
		INSERT INTO Service (ServiceID, title, cost) VALUES (5,  'Lip injection', 5000);
		INSERT INTO Service (ServiceID, title, cost) VALUES (6,  'liposuction', 400000);
		INSERT INTO Service (ServiceID, title, cost) VALUES (7,  'Total face change', 1000000);
		INSERT INTO Service (ServiceID, title, cost) VALUES (8,  'Total body change', 2000000);

        RAISE NOTICE 'Table (%) filled', table2;
    END IF;

    IF table_n = table3 THEN
        INSERT INTO Patient (PatientID, PatientName, Phone) VALUES (1, 'Donatella Versache', '4567321');
        INSERT INTO Patient (PatientID, PatientName, Phone) VALUES (2, 'Sergey Zverev', '1112223');
        INSERT INTO Patient (PatientID, PatientName, Phone) VALUES (3, 'Kim Kardashian', '2244466');
		INSERT INTO Patient (PatientID, PatientName, Phone) VALUES (4, 'Bred Pit', '1234098');
		INSERT INTO Patient (PatientID, PatientName, Phone) VALUES (5, 'Kylie Jenner', '7592345');
		INSERT INTO Patient (PatientID, PatientName, Phone) VALUES (6, 'Aleksey Scherbakov', '5678321');

        RAISE NOTICE 'Table (%) filled', table3;
    END IF;

    IF table_n = table4 THEN
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/1/2020', 1, 7, 6);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/2/2020', 1, 6, 3);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/2/2020', 2, 2, 1);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/3/2020', 3, 8, 7);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/5/2020', 3, 4, 2);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/5/2020', 4, 3, 4);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/6/2020', 5, 5, 5);
        INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/10/2020', 5, 5, 5);
		INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/14/2020', 6, 1, 8);
		INSERT INTO Logbook (Date, Patient, Service, Doctor) VALUES ('12/16/2020', 6, 4, 1);


        RAISE NOTICE 'Table (%) filled', table4;
    END IF;
END;
$$;


-- CALL FillAllTables();
CREATE OR REPLACE PROCEDURE FillAllTables()
LANGUAGE plpgsql
AS $$
BEGIN
    CALL FillTable('Doctor');
    CALL FillTable('Service');
    CALL FillTable('Patient');
    CALL FillTable('Logbook');

END;
$$;


-- creating an index on the phone number field --
-- CALL CreateIndex();
CREATE OR REPLACE PROCEDURE CreateIndex()
LANGUAGE plpgsql
AS $$
BEGIN
	CREATE INDEX phone_index  ON Patient (Phone);  
END;
$$;


-- full and partial table cleanup --
-- select ClearTables('{Doctor}');
CREATE OR REPLACE FUNCTION ClearTables(tbnames text[]) RETURNS int AS
$func$
DECLARE
    tbname text;
BEGIN
    FOREACH tbname IN ARRAY tbnames LOOP
        EXECUTE FORMAT('DELETE FROM %s', tbname);
        EXECUTE FORMAT('ALTER SEQUENCE %s_doctorid_seq restart with 1', tbname);
    END LOOP;
    RETURN 1;
END
$func$ LANGUAGE plpgsql;


-- dropping one or more tables -- 
-- SELECT DropTables('{Doctor, Service}');
CREATE OR REPLACE FUNCTION DropTables(tbnames text[]) RETURNS int AS
$func$
DECLARE
    tbname text;
BEGIN
    FOREACH tbname IN ARRAY tbnames LOOP
        EXECUTE FORMAT('DROP TABLE %s', tbname);
    END LOOP;
    RETURN 1;
END
$func$ LANGUAGE plpgsql;


-- deleting all tables --
-- CALL DropAllTables();
CREATE OR REPLACE PROCEDURE DropAllTables()
LANGUAGE plpgsql
AS $$
BEGIN
    PERFORM DropTables('{Doctor, Sercvice, Patient, Logbook}');
END;
$$;

