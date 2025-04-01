CREATE OR REPLACE PROCEDURE insert_order(
	IN order_id INT,
    IN customer_id INT,
    IN order_date DATE,
    IN ship_date DATE,
    IN paid_date DATE,
    IN status VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    BEGIN
        INSERT INTO orders (order_id, customer_id, order_date, ship_date, paid_date, status)
        VALUES (order_id, customer_id, order_date, ship_date, paid_date, status);
        COMMIT;
    EXCEPTION WHEN others THEN
        ROLLBACK;
        RAISE EXCEPTION 'Ошибка при выполнении операции: %', SQLERRM;
    END;
END;
$$;
