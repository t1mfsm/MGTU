CREATE OR REPLACE FUNCTION get_order_rank(order_date_input DATE) RETURNS INT AS $$
DECLARE 
    rank_val INT;
BEGIN
    SELECT DENSE_RANK() OVER (ORDER BY order_date) INTO rank_val
    FROM orders
    WHERE order_date = order_date_input;
    
    RETURN rank_val;
END;
$$ LANGUAGE plpgsql;
