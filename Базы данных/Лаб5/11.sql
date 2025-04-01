CREATE OR REPLACE FUNCTION log_new_item() RETURNS TRIGGER AS $$
BEGIN
    RAISE NOTICE 'Добавлен новый товар в заказ. Product ID: %, Quantity: %, Order ID: %', NEW.product_id, NEW.quantity, NEW.order_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_new_item_trigger
AFTER INSERT ON items
FOR EACH ROW
EXECUTE FUNCTION log_new_item();

select * from items

INSERT INTO items (item_id, order_id, product_id, quantity, total)
VALUES (12, 2, 1, 6, 93);
