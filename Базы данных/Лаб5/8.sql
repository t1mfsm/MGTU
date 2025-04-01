CREATE OR REPLACE FUNCTION delete_related_items()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM items
    WHERE product_id = OLD.product_id;
    
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER delete_related_items_trigger
AFTER DELETE ON products
FOR EACH ROW
EXECUTE FUNCTION delete_related_items();