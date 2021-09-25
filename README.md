# Data warehouse tech stack

## Table of Contents
  - [Introduction](#Introduction)
  - [Technologies Used](#Technologies)
  - [Folders](#Folders)
  - [Architecture](# DesignArchitecture)
# Introdcution 

## Business  overview
An AI startup that deploys sensors to businesses, collects data from all activities in a business - from people’s interaction to the smart appliances installed in the company to reading environmental and other relevant information.
## Objective  
 The contract with the client is to reduce the cost of running the client facility as well as to increase the livability and productivity of workers with the responsibility to install all the required sensors, receive a stream of data from all sensors, and analyze the data to provide key insights to the business.
 
 # Folder 


# Design architecture
![design](https://user-images.githubusercontent.com/47286297/134458760-f7ebd17e-8c1f-4cb5-b815-9acee4997e37.png)

- Loading the raw dataset to our Database then initialize different Airflow dag scripts task schedules to be used as a source to DBT.

- Transformation on data using DBT using the data as a source and saving the data as table/view and stored the processed and transformed data on the data warehouse. 
- Finalize with visualization of the data warehouse using Redshift by consuming the data from the warehouse to make perspicacious visualization

## Technologies
-   [Data warehouse](https://g.co/kgs/UCz1nE): To  used for reporting and data analysis and is considered a core component of business intelligence. 
  -   [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation.html): To create,ocherstrate and monitor data workflows 
  - [PostgreSQL](https://g.co/kgs/mvNNFY):For Database management system emphasizing extensibility and SQL compliance
  - [Redash:](https://redash.io/):To Build a version control script system by hitting the API, download the queries and built an automated git storage process 
 