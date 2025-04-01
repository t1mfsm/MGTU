CREATE OR REPLACE PROCEDURE GetMatchesByClub(IN clubName VARCHAR(255))
LANGUAGE plpgsql
AS $$
DECLARE
    matchId_var INT;
    matchDate_var DATE;
    opponent_var VARCHAR(255);
    result_var VARCHAR(10);
    done BOOLEAN := FALSE;
    cur CURSOR FOR
        SELECT m.match_id, m.match_date, m.opponent, m.result
        FROM matches m
        INNER JOIN club c ON m.club_id = c.club_id
        WHERE c.title = clubName;
BEGIN
    OPEN cur;

    RAISE NOTICE '% % % %', 'ID', 'Match Date', 'Opponent', 'Result';

    LOOP
        FETCH cur INTO matchId_var, matchDate_var, opponent_var, result_var;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE '% % % %', matchId_var, matchDate_var, opponent_var, result_var;
    END LOOP;

    CLOSE cur;
END;
$$;

