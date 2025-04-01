CREATE FUNCTION GetTotalProductCount(order_id_param INT) RETURNS INT
AS $$
DECLARE total_count INT;
BEGIN
    SELECT SUM(quantity) INTO total_count
    FROM items 
    WHERE order_id = order_id_param;
    RETURN total_count;
END;
$$ LANGUAGE plpgsql;
