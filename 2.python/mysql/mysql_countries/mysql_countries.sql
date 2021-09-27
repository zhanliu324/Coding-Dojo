select 
c.name,
l.language,
l.percentage
from languages l
join countries c on l.country_id = c.id
where l.language = 'Slovene'
order by l.percentage desc;


select
c.name,
count(ct.id) cities
from countries c
join cities ct on c.id = ct.country_id
group by c.name
order by cities desc;

select
ct.name,
ct.population,
ct.country_id
from cities ct
join countries c on ct.country_id = c.id
where c.name = 'Mexico'
and ct.population > 500000
order by ct.population desc;

select
c.name,
l.language,
l.percentage
from countries c
join languages l on c.id = l.country_id
where l.percentage > 89
order by l.percentage desc;

select
name, surface_area, population
from countries
where surface_area < 501
and population > 100000;

select
name, government_form,capital,life_expectancy
from countries
where government_form = 'Constitutional Monarchy'
and capital > 200
and life_expectancy > 75;

select 
c.name country_name,
ct.name city_name,
ct.district,
ct.population
from countries c
join cities ct on c.id = ct.country_id
where c.name = 'Argentina'
and ct.district = 'Buenos Aires'
and ct.population > 500000;

select 
region, count(id) countries
from countries
group by 1
order by countries desc;