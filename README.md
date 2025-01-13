<h1> Telco Churn Analysis </h1>

## 1. Project Overview
This project analyzes business data to extract insights, improve decision-making, and identify key trends. The primary focus is to **Predicting Customer Churn**.

Key Objectives:
- Objective 1: Predicting whether a customer would churn or not
- Objective 2: Reducing loss caused by replacing churned customers

## 2. Data Sources
- [Dataset 1](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) - IBM Sample Data of Customer Churn of a Company in Telecommunication Industry (External Data)
- [Dataset 2](https://github.com/dhanylatief/Telco-Customer-Churn/blob/main/data/raw/data_telco_customer_churn.csv) - Main Data

## 3. Technologies Used
- Programming Language: Python (e.g., Pandas, NumPy)
- Visualization: Matplotlib, Seaborn, Plotly
- Version Control: Git
- Others: Jupyter Notebook

## 4. Project Structure

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── assets             <- Contains saved model and other assets that might be added
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│   └── slide          <- Contains analysis report
│
└── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                          generated with `pip freeze > requirements.txt`

```

## 5. Summary of Finding
### 5.1 Business Insight
1. Customers with short tenures are more likely to churn compared to those with longer tenures.
2. Customers who paid more per month tend to churn more compared to those who paid less
3. Both low values (0) in `Contract_Two Year` and `Contract_One Year` largely impact the model predictions, meaning that customers with **Month-to-Month** contract are the ones that are likely to churn.
4. With machine learning, we can reduce the total cost up to **73%**
  
    Total Cost **Before** ML: $231,845
  
    Total Cost **After** ML : $62,940
5. Our net revenue increased **53%** with machine learning
  
    Net Revenue **Before** ML: $1,072,098
  
    Net Revenue **After** ML : $1,644,455
### 5.2 Actionable Recommendation
Customer Service 

- Regular staff training to ensure optimal customer experience. 
- Conduct routine customer satisfaction survey through email or mobile app and evaluate the most common complaint.
- Optimize onboarding experience by offering accessible guides through website or app, video tutorials, etc. 

Marketing

- Create targeted marketing campaigns for ‘at-risk’ customers.
- Multichannel marketing to reach customers through their preferred channels.

Product

- Evaluate the quality of fiber optic service as it has the highest rate of churn.
- Develop personalized plans based on customer usage history.

Sales

- Offer additional deals such as monthly charges discounts & bundle deals to customers who have only used the services for 2 years or less
- Research prices of similar products or services to determine competitive pricing.
- Offer incentives for long-term contracts such as loyalty rewards to reduce churn associated with month-to-month contracts.

## 6. Contact
- Name: Muhammad Dhany Latief
- Email: m.dhany.latief@gmail.com
- Linkedin: https://www.linkedin.com/in/dhany-latief-22a674241/
