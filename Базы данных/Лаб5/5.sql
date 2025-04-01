create function products_in_orders(order1 int, order2 int)
returns table(prod_ord_id int, descriptipon text, quantity int, total money, ship_date date)
language sql
as $$
	select products.product_id, description, sum(quantity), sum(total), ship_date from orders
	join items on(items.order_id = orders.order_id)
	join products on(items.product_id = products.product_id)
	where orders.order_id in(order1, order2)
	group by products.product_id, description, ship_date
$$;