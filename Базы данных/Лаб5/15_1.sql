CREATE OR REPLACE FUNCTION ordered_item()
RETURNS TABLE (
    item_id INT,
    order_id INT,
    product_id INT,
    quantity INT,
    total MONEY,
    row_num BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        items.item_id,
        items.order_id,
        items.product_id,
        items.quantity,
        items.total,
        ROW_NUMBER() OVER (ORDER BY items.order_id) AS row_num
    FROM
        items;
END;
$$ LANGUAGE plpgsql;
