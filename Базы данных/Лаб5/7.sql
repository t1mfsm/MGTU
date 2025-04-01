CREATE OR REPLACE FUNCTION update_product_stock() RETURNS TRIGGER AS $$
DECLARE
    current_stock INT;
BEGIN
    SELECT in_stock INTO current_stock
    FROM products
    WHERE product_id = NEW.product_id;

    UPDATE products
    SET in_stock = current_stock - NEW.quantity
    WHERE product_id = NEW.product_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_product_stock_trigger
AFTER INSERT ON items
FOR EACH ROW
EXECUTE FUNCTION update_product_stock();
