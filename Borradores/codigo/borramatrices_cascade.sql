-- Name: borramatrices(text, text); Type: FUNCTION; Schema: public; Owner: asopomcas
--

CREATE or REPLACE FUNCTION borramatrices_cascade(_schema text, _parttionbase text) RETURNS void
    LANGUAGE plpgsql
    AS $$
DECLARE
    row     record;
BEGIN
    FOR row IN
        SELECT
            table_schema,
            table_name
        FROM
            information_schema.tables
        WHERE
            table_type = 'BASE TABLE'
        AND
            table_schema = _schema
        AND
            table_name ILIKE (_parttionbase || '%')
    LOOP
        EXECUTE 'DROP TABLE ' || quote_ident(row.table_schema) || '.' || quote_ident(row.table_name) || ' CASCADE' ;
        RAISE INFO 'Dropped table: %', quote_ident(row.table_schema) || '.' || quote_ident(row.table_name);
    END LOOP;
END;
$$;
