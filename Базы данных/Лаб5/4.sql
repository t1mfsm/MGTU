create or replace function orders_search (x date, y date default '2030-01-21', z bool default FALSE)
returns table(order_id INTEGER, order_date DATE, ship_date DATE) as $$
begin
  if y = '2030-01-21' then
    if not z then
      return query select orders.order_id, orders.order_date, orders.ship_date from orders where orders.order_date = x;
    else
      return query select orders.order_id, orders.order_date, orders.ship_date from orders where orders.ship_date = x;
    end if;
  else
    if not z then
      return query select orders.order_id, orders.order_date, orders.ship_date from orders where orders.order_date between x and y;
    else
      return query select orders.order_id, orders.order_date, orders.ship_date from orders where orders.ship_date between x and y;
    end if;
  end if;
end;
$$ language plpgsql;
