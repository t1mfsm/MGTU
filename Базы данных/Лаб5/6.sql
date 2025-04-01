create function count_products_in_city(city text)
returns table(prod_id int, descriptipon text, quantity int)
language sql
as $$
	select products.product_id, description, sum(quantity) from orders
	join items on(items.order_id = orders.order_id)
	join products on(items.product_id = products.product_id)
	join customers on(orders.customer_id = customers.customer_id and customers.city = city)
	group by products.product_id, description
$$;