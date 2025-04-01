CREATE OR REPLACE FUNCTION rank_order()
RETURNS TABLE (
    order_id INT,
    order_date DATE,
    order_rank BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        orders.order_id, 
        orders.order_date, 
        RANK() OVER (ORDER BY orders.order_date) AS order_rank
    FROM 
        orders;
END;
$$ LANGUAGE plpgsql;
