create or replace function product_search_by_price (x money, y money)
returns table(product_id INT, product_name TEXT, product_price MONEY, in_stock INT, description TEXT)
as $$
 	select product_id, product_name, product_price, in_stock, description from products where product_price between x and y
	$$ language sql;