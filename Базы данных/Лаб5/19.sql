DO $$
DECLARE 
    club_id INT;
    budget MONEY;
BEGIN
    FOR club_id, budget IN 
        SELECT club.club_id, club.budget
        FROM club
        WHERE club.budget < 100000000::money
    LOOP
        UPDATE club
        SET budget = club.budget * 1.1
        WHERE club.club_id = club.club_id;
    END LOOP;
END $$;
