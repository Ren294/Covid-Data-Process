# BIG DATA PROJECT: Covid-Data-Process
# Project Objective
The Covid Data Process project aims to design and implement a comprehensive, real-time data processing pipeline specifically tailored to manage the continuous influx of `COVID-19` data. This project seeks to build a scalable and efficient system capable of ingesting, processing, storing, and visualizing `COVID-19` data in real-time, enabling stakeholders to make informed decisions based on the most current information available.

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

The system is divided into several components, each responsible for specific tasks within the data process:

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

## Data Process:

- **Job Scheduling**: `Airflow` orchestrates and schedules the system’s workflows, ensuring smooth execution of data ingestion, processing, and storage tasks.

- **Batch processing**: `Apache Spark` processing on data stored in HDFS, facilitating complex data analysis tasks.

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
- `Apache Spark`: For both real-time and batch data processing.
- `Hadoop HDFS`: Provides distributed storage for large volumes of processed data.
- `Apache Hive`: Allows SQL-like querying and analysis of data stored in HDFS.
- `Apache Airflow`: rchestrates and schedules the workflow of the entire system.
  
### **Visualization**

- `Amazon QuickSight`: Provides business intelligence and data visualization capabilities for insightful reporting and analysis.

# Installation and Deployment

## Set up environment

### 1. Create an AWS EC2 Instance

**1.1. Log in to AWS Management Console:**

- Visit the [AWS Management Console](https://aws.amazon.com/console/) and log in with your credentials.

**1.2. Launch a New EC2 Instance:**

- Navigate to the **EC2 Dashboard**.
  
- Click on **Launch Instance**.

- Choose an **Amazon Machine Image (AMI)**:
  - `Amazon Linux 2 AMI` (HVM) - Kernel 5.10, SSD Volume Type

    <center>
        <img src="image/imageEC2.jpeg" width="600" />
    </center>

- Choose an **Architecture**
  - This project only run on architecture `ARM64`
  
    <center>
        <img src="image/architectureEC2.jpeg" width="600" />
    </center>

- Choose an **Instance Type**:
  - For this project, `t4g.2xlarge` is recommended for its balance between performance and cost.
    
    <center>
        <img src="image/typeEC2.jpeg" width="600" />
    </center>

- Configure **Instance Details**:
  - Ensure that **Auto-assign Public IP** is set to "Enable".

- Configure **Storage**:
  - You should increase to **60GB** for this project.

    <center>
        <img src="image/storageEC2.jpeg" width="600" />
    </center>
  
- Configure **Security Group**:
  - Add the following rules:
    - SSH: Port 22, Source: Replace **0.0.0.0** with `your IP`.
    - Custom TCP Rule: Port **(0-10000)**, Source: Replace **0.0.0.0** with `your IP`.
      
    <center>
        <img src="image/securityEC2.jpeg" width="600" />
    </center>
  
- **Review and Launch the instance**.

- Download the key pair **(`.pem` file)** and keep it safe; it’s needed for **SSH** access.

**1.3. Access the EC2 Instance**
- Open your terminal.
  
- Navigate to the directory where the `.pem` file is stored.
  
- Run the following command to connect to your instance:
  
    ```bash
    ssh -i "your-key-file.pem" ec2-user@your-ec2-public-ip
    ```
### 2. Install `Docker` on the `EC2 Instance`

**2.1: Update the Package Repository**
- Run the following commands to ensure your package repository is up to date:

    ```bash
    sudo yum update -y
    ```
  
**2.2. Install Docker**
- Install `Docker` by running the following commands:

    ```bash
    sudo yum install -y docker
    ```
  
- Start `Docker` and enable it to start at boot:

    ```bash
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

- Verify `Docker` installation:

    ```bash
    docker --version
    ```

### 3. Install Docker Compose
**3.1. Install Docker Compose**
- `Docker Compose` is not available in the default `Amazon Linux 2` repositories, so you will need to download it manually:

    ```bash
      sudo curl -L "https://github.com/docker/compose/releases/download/v2.19.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

**3.2. Apply Executable Permissions**
- Apply executable permissions to the binary:

    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```
    
**3.3. Verify Docker Compose Installation**
- Verify the installation by checking the version:

    ```bash
    docker-compose --version
    ```
    
## 4. Clone the Project Repository

**4.1. Install Git (if not already installed)**
- Install Git to clone the repository:

    ```bash
    sudo yum install -y git
    ```
    
**4.2. Clone the Repository**
- Run the following command to clone the project repository:

    ```bash
    git clone https://github.com/your-username/covid-data-process.git
    ```
- Navigate to the project directory:

  ```bash
  cd covid-data-process
  ```

## 5.Running the Project

**5.1. Port forwarding to the `AWS EC2 Instance`**
- Use the SSH command provided:
    ```bash
    ssh -i "your-key-file.pem" \
       -L 8080:localhost:6060 \
       -L 8088:localhost:8088 \
       -L 9094:localhost:9094 \
       -L 5432:localhost:5432 \
       -L 9090:localhost:9090 \
       ec2-user@eec2-user@your-ec2-public-ip
    ```
  - This command establishes a secure SSH connection to your EC2 instance and sets up port forwarding, allowing you to access various services running on your instance from your local machine.

**5.2. Grant Execution Permissions for Shell Scripts**
- Once connected, ensure all shell scripts have the correct execution permissions:

    ```bash
    chmod +x ./*
    ```
    
  - This command grants execute permissions to all .sh files in the project directory, allowing them to be run without any issues.
 
**5.3. Initialize the Project Environment**
- Run the `init-pro.sh` script to initialize the environment:

    ```bash
    ./init-pro.sh
    ```
    
- This script performs the following tasks:
  - Sets the `AIRFLOW_UID` environment variable to match the current user's ID.
  - Creates necessary directories for `Spark` and `NiFi`.
  - Prepares the environment for running `Airflow` by initializing it with `Docker`.

**5.4. Start the Docker Containers**
- Next, bring up all the services defined in the `docker-compose` file:

    ```bash
    docker-compose --profile all up
    ```
    
   - This command starts all the necessary containers for the project, including those for NiFi, Kafka, Spark, Hadoop, Hive, and Airflow.

**5.5. Post-Deployment Configuration**
- After the `Docker containers` are running, execute the `after-compose.sh` script to perform additional setup:

    ```bash
    ./after-compose.sh
    ```
    
- This script:
  - Sets up `HDFS directories` and assigns the appropriate permissions.
  - Creates `Kafka topics` (covidin and covidout).
  - Submits a `Spark job` to process streaming data.

**5.6. Configure and Run Apache NiFi**
- Now, you need to configure and start your data workflows in `Apache NiFi`:
  - Open the `NiFi Web UI` by navigating to `http://localhost:8080/nifi` in your browser.
  - Add the [template](template/Ren294TemplateFinal.xml) for the `NiFi` workflow:

    <center>
        <img src="image/nifi.jpeg" width="900" />
    </center>
    
  - Start the `NiFi` workflow to begin ingesting and processing `COVID-19` data.

