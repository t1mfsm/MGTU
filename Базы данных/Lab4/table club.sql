create table club(
	club_id int primary key,
	club_title varchar(50) unique,
	budget money check (budget > money(0))
)