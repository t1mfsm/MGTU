create function customers_from_company (x text)
returns table(last_name TEXT, first_name TEXT, address TEXT, city TEXT phone TEXT)
as $$
 	select last_name, first_name, address, city, phone from customers where company_name = x
	$$ language sql;
