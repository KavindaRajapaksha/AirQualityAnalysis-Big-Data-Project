# Air Quality Analysis: Detecting the Most Polluted Locations and Times

This project demonstrates the use of **Hadoop MapReduce** to analyze a large-scale air quality dataset from India, focusing on identifying pollution hotspots and understanding temporal air quality trends.

## Project Objective

To design and implement custom MapReduce jobs on the **Air Quality Data in India (2015–2020)** dataset to:

* Analyze AQI category distribution over time
* Identify the most polluted monitoring stations based on PM2.5 averages

## Dataset Overview

* **Source**: [Kaggle - Air Quality Data in India](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
* **Original Records**: \~2.5 million
* **Cleaned Records**: \~1.8 million
* **Format**: CSV
* **Monitored Cities**: Delhi, Mumbai, Bengaluru, Chennai, Kolkata, and 20+ others
* **Fields Used**: `StationId`, `Datetime`, `PM2.5`, `AQI_Bucket`

Data was preprocessed using **Python (pandas)** to remove null values and retain essential columns. Final dataset: `air_quality_cleaned.csv`.

## Environment Setup

* **Preprocessing**: Python (Jupyter Notebook)
* **Big Data Processing**: Apache Hadoop on Ubuntu Linux (VirtualBox)
* **Java JDK 8**: Required for Hadoop
* **HDFS**: Used to store and process the dataset
* **Python Scripts**: Used as custom mapper and reducer logic via Hadoop Streaming

## MapReduce Tasks

### 1. AQI Bucket Distribution by Date

* **Mapper**: Extracts date and AQI category
* **Reducer**: Aggregates counts per AQI bucket per date

### 2. Average PM2.5 by Station

* **Mapper**: Extracts station ID and PM2.5 value
* **Reducer**: Computes average PM2.5 per station

## Repository Contents

| File                      | Description                                |
| ------------------------- | ------------------------------------------ |
| `mapper_aqi_bucket.py`    | Mapper script for AQI category analysis    |
| `reducer_aqi_bucket.py`   | Reducer script for counting AQI categories |
| `mapper_avg_pm25.py`      | Mapper script for PM2.5 values per station |
| `reducer_avg_pm25.py`     | Reducer script to compute average PM2.5    |
| `air_quality_cleaned.csv` | Cleaned dataset used for MapReduce jobs    |



## Results

* Identified pollution trends across dates and cities
* Located the most polluted stations by PM2.5 levels
* Demonstrated scalable data processing using Hadoop MapReduce
