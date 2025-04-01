CREATE OR REPLACE FUNCTION update_item_total()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE items
    SET total = items.quantity * NEW.product_price
    WHERE items.product_id = NEW.product_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER item_price_update_trigger
AFTER UPDATE ON products
FOR EACH ROW
EXECUTE FUNCTION update_item_total();

