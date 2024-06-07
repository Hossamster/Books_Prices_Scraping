# Books Scraping Project

This project involves scraping book data from the website [Books to Scrape](https://books.toscrape.com) using Scrapy, a popular web scraping framework. The data collected is stored in a CSV file named `dataset.csv`.

## Table of Contents
- [Books Scraping Project](#books-scraping-project)
	- [Table of Contents](#table-of-contents)
	- [Introduction](#introduction)
	- [Installation](#installation)
	- [](#)
	- [Commands Executed](#commands-executed)
	- [Files and Directories](#files-and-directories)
	- [](#-1)
	- [DATASET](#dataset)

## Introduction
The purpose of this project is to demonstrate how to scrape data from a website using Scrapy. The data includes book titles, prices, availability, and other relevant details.

## Installation
To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>	
2. Install Scrapy
   ```bash
   pip install scrapy
##
## Commands Executed
1. Start the Scrapy project:
   ```bash
   scrapy startproject books_scraping
2. Generate the spider:
   ```bash
   scrapy genspider -t crawl books_scraping https://books.toscrape.com
3. Run the scraper and save the data:
   ```bash
   scrapy crawl books_scraping -o dataset.csv
## Files and Directories
	•	books_scraping.py: The main Scrapy spider script.
	•	dataset.csv: The CSV file containing the scraped data.
	•	README.md: This README file.
##
## DATASET
![dataset](https://raw.githubusercontent.com/Hossamster/Books_Prices_Scraping/main/dataset_view.png)
