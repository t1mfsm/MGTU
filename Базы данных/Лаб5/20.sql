WITH PlayerRank AS (
    SELECT 
        c.title AS Клуб,
        p.fio AS Игрок,
        p.salary AS Зарплата,
        ROW_NUMBER() OVER (PARTITION BY c.club_id ORDER BY p.player_id) AS player_rank
    FROM 
        club c
    JOIN 
        player p ON c.club_id = p.club_id
    WHERE 
        c.title = 'FC Barcelona'
)
SELECT 
    Клуб,
    Игрок,
    Зарплата,
    CASE WHEN player_rank % 2 = 0 THEN CAST(Зарплата AS numeric) * 0.1 ELSE 0 END AS Бонус
FROM 
    PlayerRank;
