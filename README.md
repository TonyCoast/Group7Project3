# Group7Project3

# INFLATION IN THE US

### Contributors
* Tony Coast
* Tanner Amman
* Anisa Braun
* Nels Jacobson
* Devang Patel

### Background
This project was completed for the Data Visualization Bootcamp Project 3. Gather and store data to create a dashboard page with user driven interactions

### The Code 
Database was created in order to house all of the data used for the analysis. This was done using Postgres and database was saved as a .sql file
create table cpi_atl(
series_id varchar(50),
value varchar(50),
period varchar(50),
label varchar(50),
dairy varchar (50),
alcohol varchar(50),
meats varchar(50)
)


create table cpi_chicago(
series_id varchar(50),
value varchar(50),
period varchar(50),
label varchar(50),
dairy varchar (50),
alcohol varchar(50),
meats varchar(50)
)

create table cpi_denver(
series_id varchar(50),
value varchar(50),
period varchar(50),
label varchar(50),
dairy varchar (50),
alcohol varchar(50),
meats varchar(50)
)

### Datasets
1. We are analyzing 2013-2022 data from the Bureau of Labor Statitics (bls.gov)
2. We are honing in on three categories:
  a) Alcohol
  b) Dairy & related
  c) Meat, poultry, fish and eggs
3. We are comparing the Consumer Price Index (CPI) as well as the Producer Price Index (PPI)
4. We are looking specifically at 3 cities: Chicago, Atlanta & Denver

### Future Opportunities 
* Analyzing stock price data and its relation to CPI & PPI data
* Reviewing data from all major US cities
