# NIFTY50_Stock_Price_Prediction  
![Nifty50_logo](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/afa298be-224d-4348-9b38-1ccea2efe44e)

This project focuses on stock price prediction for NIFTY-50 stocks using a robust model trained on four years of historical data. 
Users can input their stock preferences, quantities, buying and selling dates, allowing for portfolio analysis. 
Whether predicting future prices or using historical data, the model calculates the portfolio's returns, streamlining the process through integration with Google Sheets. 
This project provides a powerful tool for investors to make informed decisions and analyze their investments effectively.

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Project Plan](#project-plan)
- [Preprocessing](#preprocessing)
- [Model Building](#model-building)
- [Google Sheet Integration](#google-sheet-integration)
- [Web Page](#web-page)
- [Model Application](#model-application)
- [Future Plan](#future-plan)
- [Model Limitation](#model-limitation)
- [Challenges](#challenges)
- [Conclusion](#conclusion)
- [Learning](#learning)

## Introduction  
- As an investment advisor the aim of this project was to predict future prices of Nifty50 stocks using advanced machine learning algorithms
- Here the Investors can use our model to make well-informed decisions based on data-driven insights.
- The platform allows users to enter stock details and receive approximate profit/loss estimations
- Our model will empowers investors to optimize their portfolios and enhance trading strategies with reliable forecasts.

## Objectives

**Objectives:**  
* Understand the Importance of Nifty50
* Describe Data Sources
* To Showcase Model Accuracy
* To Demonstrate Webpage Interface
* To predict profit/loss based on user’s:
	Stock name 
	Quantity 
	Buying date 
	Selling date
* Emphasize Real-world Applications
* Future Plans

## Importance of Nifty50
![Nifty50_stocks_img](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/fd8c7727-00ca-4608-a98d-f11c334ecc8b)
- Nifty50 is India's benchmark stock market index, representing the performance of the top 50 companies in the country
- It serves as a crucial indicator of the overall health and direction of the Indian economy.
- Nifty50 significantly influences investor sentiment, guiding investment decisions and portfolio strategies.
- The index reflects market trends, helping investors gauge the overall performance and direction of the stock market.


## Project Plan
![Project_flow](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/6d74fff4-43b5-45ee-8b61-853ad6cca3aa)

## Preprocessing
**Web Scraping:**  
Meticulously extracted a rich historical dataset spanning four years of NIFTY50 stock information, sourcing data exclusively from official and reputable websites, 
notably "https://in.investing.com/" and "https://www.nseindia.com/". 
This rigorous data collection process ensures the utmost reliability and credibility of the dataset.

**Null and Noise Handling:** 
Conducted a thorough assessment to identify and address null values in the dataset. Also, implemented noise reduction techniques to ensure data accuracy.

**Unwavering Data Type Uniformity:**   
Enforced a meticulous standardization of data types across the entire dataset, eliminating any discrepancies or irregularities. 
This meticulous data type consistency not only facilitates seamless data processing but also lays the groundwork for precise and error-free analytical insights.

**Data Size and Structure Assessment:**  
Conducted a thorough evaluation of the size and shape of each data table, providing an insightful understanding of the dataset's intricate structure. 
This meticulous examination serves as a critical foundation for deciphering the composition and nuances of the data, empowering comprehensive analysis.

**Strategic Data Compilation and Filtering:**   
Aggregated and organized the extensive NIFTY-50 stock data by their respective stock names, enabling effortless data filtration and retrieval. 
This strategic data compilation approach allows for precise selection and extraction of data pertinent to users' preferences for predicting 
expected profit or loss based on specific buying and selling dates.

* By executing these preprocessing steps, the dataset was refined, cleaned, and made ready for further analysis, establishing a solid foundation for accurate prediction.

## Model Building
![Predicted_vs_Close_price](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/08d2f533-7df1-4771-8def-99e8da4dd39d)
- Our machine learning model utilizes polynomial regression to predict profit/loss in Nifty50 stocks.
- Accurate predictions assist investors in making informed decisions.
- The model is trained on historical stock data to ensure reliability.
- It offers a user-friendly interface for inputting stock details and obtaining predictions.
- This project showcases the application of AI in real-world financial analysis.


## Google Sheet Integration
![Google_sheet](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/8a9510cc-a764-4ef4-a42f-3add49d1e7a8)

## Web Page
![Web_page](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/ec8227c6-db89-4556-8dbc-172498beea97)
- The web page allows users to input stock details, quantity, buying, and selling dates for personalized predictions.
- User-friendly interface for inputting stock details, quantity, buying, and selling dates.
- Accurate predictions aid investors in making informed decisions.
- Validation through training on historical stock data ensures reliability.
- Practical application of AI in financial analysis, optimizing investments.

## Model Application
![Stock_input](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/527cec33-aa08-430e-a7f2-e0acf90fa701)

- Informed Investment Decisions  
- Risk Management  
- Portfolio Optimization  
- Financial Planning  
- Enhancing Market Understanding  
- Empowering Individual Investors  
- Confidence in Decision-making  
- Validating Existing Strategies  
- Future Applications
  
![Prediction_Graph](https://github.com/Kumar-Dharm/Image_Gallery/assets/132021299/f7febc3d-8e69-4f68-9f74-dde868db5b7e)
- Our model will leverages the power of data and machine learning to empower investors and traders with valuable insights, fostering data-driven decision-making and enhancing overall performance in the financial sector.

## Future Plan

* Fetching the live data and automate the model on the server.
* If it works fine then deploying over the server so that users can use it.

## Model Limitation
**Limited data:**
Utilizing only 4 years of historical data might not capture long-term trends and patterns that could significantly influence stock prices.  
**Overfitting risk:**
Polynomial regression may lead to overfitting due to its sensitivity and small fluctuations in the data.  
**Limited input features:**
Relying solely on close price, volume, and date might not encompass all relevant factors impacting stock performance.  
**Market complexity:**
The stock market is influenced by multifaceted factors, including geopolitical events and macroeconomic trends, which may not be accounted for in the model.

## Challenges
- Integrating the machine learning model with Google Cloud and Google Sheets posed initial challenges.
- Deploying the model on the web page required optimizing performance and ensuring functioning of the web page.
- Coordinating frontend and backend development for seamless user experience was a complex task.
- Overcoming hurdles in data handling and processing to deliver accurate predictions to users.


## Conclusion  
* Our team successfully developed a Google sheet and also web-based machine learning model utilizing polynomial regression to predict profit/loss in Nifty50 stocks. 
* Users can input stock details, quantity, buying, and selling dates to get predictions for his/her portfolio either he/she will be in profit/loss. 
* This project demonstrates our collaborative efforts in applying AI for real-world financial analysis and decision-making.

## Learning
**Web Scraping Mastery:**  
Attained a high level of competence in web scraping techniques, enabling efficient and reliable data acquisition from online sources, notably exemplified by NIFTY50 stock price data extraction.

**Data Preprocessing Expertise:**  
Cultivated strong skills in data cleaning and preprocessing, ensuring the data's integrity, consistency, and suitability for analysis and prediction. 

**Machine Learning Integration:**  
Successfully integrated machine learning models with Google Sheets, showcasing the ability to bridge the gap between data analysis and real-world applications, particularly in the context of stock price prediction.

**Insightful Data Analysis:**  
Acquired the capability to employ various analytical tools and methodologies to derive valuable insights from complex datasets, facilitating informed decision-making processes.

**Problem-Solving Aptitude:**  
Applied data-driven insights and machine learning models to formulate pragmatic solutions to real-world challenges, exemplified by predicting NIFTY50 stock prices for future investment decisions.

**Interactive Webpage Creation:**  
Developed proficiency in creating user-friendly web interfaces and interactive web pages, enhancing user engagement and facilitating data presentation in a user-friendly manner.

**Client Communication Skills:**  
Strengthened the ability to effectively communicate with clients, addressing their queries, and tailoring data-driven solutions to meet their specific needs, thereby fostering strong client relationships.

**Project Management Competency:**  
Demonstrated project management skills by effectively coordinating various tasks, from data acquisition and preprocessing to model integration and web development, ensuring project success and timeliness.

**Continuous Learning Mindset:**  
Embraced a growth-oriented mindset, actively seeking out new techniques, tools, and technologies to stay at the forefront of data science and web development, thereby ensuring the project's ongoing relevance and effectiveness.

These learnings not only highlight our project's accomplishments but also underscore our growth and development as a data scientist and web developer, showcasing our ability to tackle complex challenges and deliver practical solutions.


|---------------------------------------------------------------------------------------------------------------------------|
