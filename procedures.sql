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
				   '|| Cost ||' smallint);');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| table3 ||'
				  ('|| PatientID ||' SERIAL PRIMARY KEY, 
				   '|| PatientName ||' varchar(40), 
				   '|| Phone ||' varchar(12));');
    EXECUTE format('CREATE TABLE IF NOT EXISTS '|| table4 ||'
				  ('|| Number ||' SERIAL PRIMARY KEY, 
				   '|| Date ||' date, 
				   '|| Patient ||' integer,
				   '|| Service ||' integer,
				   '|| Doctor ||' integer);');
    RAISE NOTICE '(%, %, %, %) created', table1, table2, table3, table4;
END;
$$;


--CALL CreateTables();

