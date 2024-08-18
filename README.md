# BIG DATA PROJECT: Covid-Data-Process
# Project Objective
The Covid Data Process project aims to design and implement a comprehensive, real-time data processing pipeline specifically tailored to manage the continuous influx of `COVID-19` data. As the pandemic unfolds, timely and accurate data processing has become crucial for understanding and mitigating its impact. This project seeks to build a scalable and efficient system capable of ingesting, processing, storing, and visualizing `COVID-19` data in real-time, enabling stakeholders to make informed decisions based on the most current information available.

# Datasets Selection
The dataset, sourced from the [COVID-19 API](https://covid-api.com/api), offers comprehensive and regularly updated reports on the global spread and impact of `COVID-19`. It encompasses a wide range of data points that track the pandemic's progression across various regions, including countries, states, and provinces. This dataset captures essential metrics such as the number of confirmed cases, deaths, recoveries, and active cases, providing a granular view of the pandemic's evolution over time.

Data from API format example:
  ```
    {
        "data":
            [
                0:{
                "date":"2023-03-09"
                "confirmed":209451
                "deaths":7896
                "recovered":0
                "confirmed_diff":0
                "deaths_diff":0
                "recovered_diff":0
                "last_update":"2023-03-10 04:21:03"
                "active":201555
                "active_diff":0
                "fatality_rate":0.0377
                "region":{
                    "iso":"AFG"
                    "name":"Afghanistan"
                    "province":""
                    "lat":"33.9391"
                    "long":"67.7100"
                    "cities":[]
                }
                ...
              ]
    }
  ```
# System Architecture
The system architecture for this `COVID-19` data processing pipeline is designed to ensure efficient data ingestion, processing, storage, and visualization. It leverages a combination of open-source technologies and cloud services to provide a scalable, robust, and flexible framework for managing and analyzing large volumes of real-time data.

- The system is divided into several components, each responsible for specific tasks within the data process:

<center>
    <img src="image/arch.jpeg" width="900" />
</center>

## Data Ingestion:

- **Data Source**: `COVID-19` data is retrieved from the API `https://covid-api.com/api/` using HTTP requests. `NiFi` handles data ingestion, performing initial cleaning and transformation to prepare the data for further processing.

- **Producer/Consumer**: `NiFi` acts as both producer and consumer, forwarding processed data to `Apache Kafka` for streaming.

## Real-Time Data Streaming:

- **Message Brokering**: `Kafka` serves as the message broker, streaming data between system components in real-time.

- **Monitoring**: `Redpanda` monitors `Kafka`’s performance, ensuring system stability.

- **Streaming Analytics**: `Spark Streaming` processes the data in real-time, performing computations like aggregations and filtering as data flows through `Kafka`.

## Data Storage:

- **Distributed Storage**: Data is stored in `Hadoop HDFS`, providing scalable, reliable storage.

- **Data Warehousing**: `Apache Hive` on `HDFS` enables efficient querying of large datasets.

- **Job Scheduling**: `Airflow` orchestrates and schedules the system’s workflows, ensuring smooth execution of data ingestion, processing, and storage tasks.

## Containerization:

- **Consistency & Deployment**: `Docker` containers ensure consistent environments across development, testing, and production, and are deployed on `AWS EC2` for scalability.

## Data Visualization:

- **Interactive Dashboards**: `Amazon QuickSight` visualizes the processed data, allowing for the creation of interactive dashboards and reports.

# Technologies Used

### **Environment**

- `Amazon EC2`: Hosts the system in a scalable and flexible cloud environment.
- `Docker`: Containerizes the system components, ensuring consistency and easy deployment.
  
### **Frameworks and Tools**

- `Apache NiFi`: Handles data ingestion and initial processing from the COVID-19 API.
- `Apache Kafka`: Enables real-time data streaming between system components.
- `Redpanda`: Monitors Kafka to ensure stable data flow and system performance.
- `Apache Spark Streaming`: Processes data in real-time, performing computations like aggregations and filtering.
- `Hadoop HDFS`: Provides distributed storage for large volumes of processed data.
- `Apache Hive`: Allows SQL-like querying and analysis of data stored in HDFS.
- `Apache Airflow`: Orchestrates and schedules the workflow of the entire system.
### **Visualization**
- `Amazon QuickSight`: Provides business intelligence and data visualization capabilities for insightful reporting and analysis.
