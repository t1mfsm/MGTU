DO $$
DECLARE 
    start_date DATE := '2024-04-03';
    end_date DATE := '2024-04-10';
    current_date DATE := start_date;
    match_row RECORD;
BEGIN
    CREATE TEMP TABLE MatchesTable (
        MatchID INT,
        Home VARCHAR,
        Away VARCHAR
    );

    FOR match_row IN 
        SELECT
            m.match_id,
            CASE WHEN m.club_id = c1.club_id THEN m.opponent ELSE c2.title END AS Home,
            CASE WHEN m.club_id = c1.club_id THEN c2.title ELSE m.opponent END AS Away
        FROM
            matches m
        INNER JOIN
            club c1 ON m.club_id = c1.club_id
        INNER JOIN
            club c2 ON m.club_id = c2.club_id
        WHERE
            m.match_date BETWEEN start_date AND end_date
    LOOP
        INSERT INTO MatchesTable (MatchID, Home, Away)
        VALUES (match_row.match_id, match_row.Home, match_row.Away);
    END LOOP;

    FOR match_row IN 
        SELECT * FROM MatchesTable
    LOOP
        RAISE NOTICE 'Match ID: %, Home: %, Away: %', match_row.MatchID, match_row.Home, match_row.Away;
    END LOOP;

    DROP TABLE MatchesTable;
END $$;
