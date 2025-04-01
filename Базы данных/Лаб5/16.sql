CREATE OR REPLACE VIEW orders_view AS
SELECT * FROM orders;


CREATE OR REPLACE FUNCTION check_orders() RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    has_unconfirmed_order INT;
BEGIN
    SELECT COUNT(*) INTO has_unconfirmed_order
    FROM orders
    WHERE customer_id = NEW.customer_id
    AND status != 'P';
    
    IF has_unconfirmed_order > 0 THEN
        RAISE EXCEPTION 'This customer already has unpayed orders.';
    ELSE
        INSERT INTO orders (order_id, customer_id, order_date, ship_date, paid_date, status)
        VALUES (NEW.order_id, NEW.customer_id, NEW.order_date, NEW.ship_date, NEW.paid_date, NEW.status);
    END IF;
    
    RETURN NEW;
END;
$$;

CREATE OR REPLACE TRIGGER check_orders_trigger
INSTEAD OF INSERT ON orders_view
FOR EACH ROW
EXECUTE FUNCTION check_orders();

