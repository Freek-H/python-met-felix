https://dev.mysql.com/doc/world-setup/en/world-setup-installation.html
https://downloads.mysql.com/docs/world-db.zip
mysql -u root
SOURCE het_pad/world.sql

SELECT * FROM city;

SELECT
	id
	,Name
	,CountryCode
	,District
	,Population
  FROM city;
  
SELECT
	CountryCode
	,id
	,Name
	,District
	,Population
  FROM city;
  
SELECT
	*
  FROM city
WHERE CountryCode = 'NLD'

SELECT
	*
  FROM country
  
SELECT
	*
  FROM country
WHERE CountryCode = 'NLD'

SELECT
	Name
  FROM country
WHERE Name LIKE 'A%'

SELECT
	land.Name AS Land
    ,stad.Name AS Hoofdstad
  FROM country AS land
  JOIN city AS stad
  	ON land.Capital = stad.ID;