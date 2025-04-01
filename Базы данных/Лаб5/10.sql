create or replace function delete_products_items() returns trigger
language plpgsql
as
$$
begin
	delete from items
	where items.product_id = old.product_id;
	return old;
end;
$$;

create or replace trigger delete_products_items_trigger
before delete on products
for each row
execute function delete_products_items();
