create procedure NewCustomers ()
language sql
as $$
	insert into customers (company_name, customer_id, last_name, first_name, address, city, phone)
	values 
	('Google', 15, 'Shakirov', 'Timur', '124 Ouwn St', 'Moscow', '234-4231'),
	('Yandex', 16, 'Ivanov', 'Ivan', '421 Fow St', 'Spb', '842-6541'),
	('Sber', 17, 'Sidorov', 'Petr', '12434 Pot St', 'Madrid', '564-5894');
$$;