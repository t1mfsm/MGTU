create table player(
	player_id int primary key,
	club_id int,
	first_name varchar(20),
	last_name varchar(30),
	birthdate date,
	salary money check (salary > money(0))
)