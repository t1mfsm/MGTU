create or replace function alter_or_drop_table() RETURNS event_trigger
language plpgsql
as $$
begin
	raise exception 'Cannot alter or drop table';
end;
$$;

create event trigger alter_table_block
	on table_rewrite
	execute procedure alter_or_drop_table();
create event trigger drop_table_block
	on sql_drop
	execute procedure alter_or_drop_table();
