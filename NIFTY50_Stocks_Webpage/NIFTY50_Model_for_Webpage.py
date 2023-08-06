# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib.dates as mdates

import streamlit as st
from streamlit_option_menu import option_menu
from streamlit import components
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import datetime
from datetime import datetime

def load_data():

    # Load the data from the file
    all_data = pd.read_excel("D:/Data Analyst Course/Project_Nifty50/NIFTY50_Stocks_data.xlsx")
    return all_data

def preprocess_data(all_data, stock_name):
    # Filter the data for the given stock name
    filtered_data = all_data[all_data['Stock_Name'] == stock_name].copy()
    
    # Add date-related columns
    filtered_data['Year'] = filtered_data['Date'].dt.year
    filtered_data['Month'] = filtered_data['Date'].dt.month
    filtered_data['Day'] = filtered_data['Date'].dt.day

    return filtered_data

def train_model(X, y):
    X.fillna(0, inplace=True)
    # Create polynomial features

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create polynomial features
    poly = PolynomialFeatures(degree=2)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    # Create linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train_poly, y_train)

    return model

def predict_profit_loss(filtered_data, model, quantity, buying_date, selling_date):
    print(buying_date,selling_date)
    poly = PolynomialFeatures(degree=2)

    filtered_data['Date'] = filtered_data['Date'].astype(str)
    filtered_data['Date'] = filtered_data['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date())

# Convert the buying and selling dates to datetime.date objects
    buying_date = datetime.datetime.strptime(buying_date, '%Y-%m-%d').date()
    selling_date = datetime.datetime.strptime(selling_date, '%Y-%m-%d').date()

    # Get the current date
    today_date = datetime.date.today()

    # Check the cases and make predictions
    if buying_date > today_date and selling_date > today_date:
        # Case 1: Both buying date and selling date in the future
        buying_year = buying_date.year
        buying_month = buying_date.month
        buying_day = buying_date.day
        selling_year = selling_date.year
        selling_month = selling_date.month
        selling_day = selling_date.day

        last_100_data = filtered_data.iloc[-100:]
        volume_mean = np.mean(last_100_data['Volume'])
        chg_mean = np.mean(last_100_data['Chg%'])
        volume_std = np.std(last_100_data['Volume'])
        chg_std = np.std(last_100_data['Chg%'])

        X_buying = np.array([[volume_mean, chg_mean, buying_year, buying_month, buying_day]])
        X_buying_scaled = (X_buying - [volume_mean, chg_mean, 0, 0, 0]) / [volume_std, chg_std, 1, 1, 1]
        predicted_close_buying = model.predict(poly.fit_transform(X_buying_scaled))[-1]

        X_selling = np.array([[volume_mean, chg_mean, selling_year, selling_month, selling_day]])
        X_selling_scaled = (X_selling - [volume_mean, chg_mean, 0, 0, 0]) / [volume_std, chg_std, 1, 1, 1]
        predicted_close_selling = model.predict(poly.fit_transform(X_selling_scaled))[-1]

        pnl = (predicted_close_selling - predicted_close_buying) * quantity

        # st.write('Predicted Buying price:', predicted_close_buying)
        st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Predicted Buying price:</span>", unsafe_allow_html=True)
        st.write("<span style='color: yellow; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(predicted_close_buying), unsafe_allow_html=True)
        # st.write('Predicted Selling price:', predicted_close_selling)
        st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Predicted Selling price:</span>", unsafe_allow_html=True)
        st.write("<span style='color: yellow; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(predicted_close_selling), unsafe_allow_html=True)
        # st.write('profit/loss:',pnl )

    elif buying_date > today_date:
        # Case 2: Only buying date in the future
        if selling_date not in filtered_data['Date'].values:
            # st.write("Selling date can't be in past.")
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Selling Date: Can't be in past.</span>", unsafe_allow_html=True)
            pnl = None
        else:
            buying_year = buying_date.year
            buying_month = buying_date.month
            buying_day = buying_date.day

            last_100_data = filtered_data.iloc[-100:]
            volume_mean = np.mean(last_100_data['Volume'])
            chg_mean = np.mean(last_100_data['Chg%'])
            volume_std = np.std(last_100_data['Volume'])
            chg_std = np.std(last_100_data['Chg%'])

            X_buying = np.array([[volume_mean, chg_mean, buying_year, buying_month, buying_day]])
            X_buying_scaled = (X_buying - [volume_mean, chg_mean, 0, 0, 0]) / [volume_std, chg_std, 1, 1, 1]
            predicted_close_buying = model.predict(poly.fit_transform(X_buying_scaled))[-1]

            selling_price = filtered_data.loc[filtered_data['Date'] == selling_date, 'Close'].values[0]

            pnl = (selling_price - predicted_close_buying) * quantity

            # st.write('Predicted Buying price:', predicted_close_buying)
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Predicted Buying price:</span>", unsafe_allow_html=True)
            st.write("Predicted Buying price: ", "<span style='color: yellow; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(predicted_close_buying), unsafe_allow_html=True)
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Actual Selling price:</span>", unsafe_allow_html=True)
            st.write("<span style='color: blue; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(selling_price), unsafe_allow_html=True)
            # st.write('Actual Selling price:', selling_price)
            # st.write('profit/loss:',pnl )

    elif selling_date > today_date:
        # Case 3: Only selling date in the future
        if buying_date not in filtered_data['Date'].values:
            # st.write("Buying date not found in the dataset.")
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Buying date: There is Holiday in Stock Market .</span>", unsafe_allow_html=True)
            pnl = None
        else:
            buying_price = filtered_data.loc[filtered_data['Date'] == buying_date, 'Close'].values[0]

            selling_year = selling_date.year
            selling_month = selling_date.month
            selling_day = selling_date.day

            last_100_data = filtered_data.iloc[-100:]
            volume_mean = np.mean(last_100_data['Volume'])
            chg_mean = np.mean(last_100_data['Chg%'])
            volume_std = np.std(last_100_data['Volume'])
            chg_std = np.std(last_100_data['Chg%'])

            X_selling = np.array([[volume_mean, chg_mean, selling_year, selling_month, selling_day]])
            X_selling_scaled = (X_selling - [volume_mean, chg_mean, 0, 0, 0]) / [volume_std, chg_std, 1, 1, 1]
            predicted_close_selling = model.predict(poly.fit_transform(X_selling_scaled))[-1]

            pnl = (predicted_close_selling - buying_price) * quantity

            # st.write('Actual Buying price:', buying_price)
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Actual Buying price:</span>", unsafe_allow_html=True)
            st.write("<span style='color: blue; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(buying_price), unsafe_allow_html=True)
            # st.write('Predicted Selling price:', predicted_close_selling)
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px; '>Predicted Selling price:</span>", unsafe_allow_html=True)
            st.write("<span style='color: yellow; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(predicted_close_selling), unsafe_allow_html=True)
            # st.write('profit/loss:',pnl )

    else:
        # Case 4: None of the dates are in the future
        if buying_date not in filtered_data['Date'].values:
            # st.write("Buying date not found in the dataset.")
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Buying date: There is Holiday in Stock Market .</span>", unsafe_allow_html=True)
            pnl = None
        elif selling_date not in filtered_data['Date'].values:
            # st.write("Selling date not found in the dataset.")
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Selling date: There is Holiday in Stock Market .</span>", unsafe_allow_html=True)
            pnl = None
        else:
            buying_price = filtered_data.loc[filtered_data['Date'] == buying_date, 'Close'].values[0]
            selling_price = filtered_data.loc[filtered_data['Date'] == selling_date, 'Close'].values[0]

            pnl = (selling_price - buying_price) * quantity

            # st.write('Actual Buying price:', buying_price)
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Actual Buying price:</span>", unsafe_allow_html=True)
            st.write("<span style='font-size: 18px; font-weight: bold; color: blue;'>{:.2f}</span>".format(buying_price), unsafe_allow_html=True)
            # st.write("Actual Buying price: ", "<span style='color: blue; font-size: 20px; font-weight: bold;'>{:.2f}</span>".format(buying_price), unsafe_allow_html=True)
            # st.write('Actual Selling price:', selling_price)
            st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Actual Selling price:</span>", unsafe_allow_html=True)

            st.write("<span style='color: blue; font-size: 18px; font-weight: bold;'>{:.2f}</span>".format(selling_price), unsafe_allow_html=True)
            # st.write('profit/loss:',pnl )

    return pnl

def get_top_5_stocks(all_data):
    stock_closing_prices = all_data.groupby('Stock_Name')['Close'].mean()
    top_5_stocks = stock_closing_prices.sort_values(ascending=False).head(5)

    return top_5_stocks

def plot_predicted_vs_close(model, X_train, y_train, X_train_poly, X_test_poly):
    y_pred = model.predict(X_test_poly)
    y_predt = model.predict(X_train_poly)

    X_train['Close'] = y_train.values
    X_train['Predicted'] = pd.Series(y_predt,index=X_train.index)
    X_train['Date'] = pd.to_datetime(X_train[['Year', 'Month', 'Day']])
    y_predt=model.predict(X_train_poly)

    X_train_sorted = X_train.sort_values('Date')

    plt.figure(figsize=(30, 10))
    plt.plot(X_train_sorted['Date'], X_train_sorted['Predicted'], label='Predicted', color='green')
    plt.plot(X_train_sorted['Date'], X_train_sorted['Close'], label='Close',color='cyan')

    # Set the background color to black
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['figure.facecolor'] = 'black'

    # Customize the legend
    plt.legend(fontsize=25, facecolor='black', edgecolor='white', labelcolor='white')

    # Customize the axes labels
    plt.xlabel('Date', fontsize=40, color='white')
    plt.ylabel('Value', fontsize=40, color='white')

    # Set the tick format for the x-axis to display the full date
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # Adjust the spacing between the x-axis ticks to fit the labels
    plt.gcf().autofmt_xdate()

    # Customize the tick labels
    plt.xticks(fontsize=25, color='white')
    plt.yticks(fontsize=25, color='white')

    # Customize the title
    plt.title('Predicted Price vs Close Price', fontsize=50, color='white')

    # Set the color of the grid lines (lighter shade of white)
    grid_color = (0.8, 0.8, 0.8)  # RGB values for a lighter shade of white
    plt.grid(color=grid_color, linestyle='--')

    # Set the color of the frame
    ax = plt.gca()
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    # Save the plot to a BytesIO object
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight')
    plt.close()

    # Display the plot using st.image()
    img_buffer.seek(0)
    st.image(img_buffer, use_column_width=True)

def main():
    # Load the data
    all_data = load_data()

    selected = option_menu(
        menu_title=None,
        options=["Home", 'Prediction', "About Us"],
        icons=['house', "list-task", 'file-person'],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "crimson"},
        }
    )

    st.markdown(
    """
    <style>
    .title-text {
        color: yellow !important;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown('<h1 class="title-text">Welcome to Stock Market</h1>', unsafe_allow_html=True)
    
    html_temp = """
    <div style='background-color:Crimson; padding: 5px'>
    <h2 style="color: white; text-align: center;"><b>Stock Price and Profit/Loss Predictions </b></h2>
    </div>
    """ 

    css = """
    <style>
    .stApp {
        # background-image: url(https://miro.medium.com/v2/resize:fit:626/0*SaNg8uUaKCMQSS5g.jpg);
        background-size: 800px 800px;
        font-weight: bold;
        opacity: 1.5;
    }
    .form-title {
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }
    </style>
    """
    st.markdown(
        """
        <style>
        label {
            color: cyan !important;
            font-weight: bold !important;
            font-size: 20px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.pinimg.com/originals/90/af/3b/90af3bc70db361a92e61f3e424295157.jpg');
        background-size: cover;
        background-position: center;
        opacity: 0.5;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(html_temp + css, unsafe_allow_html=True)

    # Get the stock names
    stock_names = all_data['Stock_Name'].unique()

    # User input form
    if selected=="Prediction":
        with st.form("prediction_form"):
            st.markdown('<span class="form-title" style="color: white; font-weight: bold;">Please provide the following details:</span>', unsafe_allow_html=True)

            stock_name = st.selectbox("Stock Name:", stock_names, key="stock_name_input")
            quantity = st.number_input("Quantity:", value=1, min_value=1)
            buying_date = st.date_input("Buying Date:")
            selling_date = st.date_input("Selling Date:")
            predict_button = st.form_submit_button("Predict")

        if predict_button and stock_name and buying_date and selling_date:
            # Preprocess the data
            filtered_data = preprocess_data(all_data, stock_name)

            # Split the data into features (X) and target variable (y)
            X = filtered_data[['Volume', 'Chg%', 'Year', 'Month', 'Day']]
            y = filtered_data['Close']

            # Train the model
            model = train_model(X, y)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # # Create polynomial features
            poly = PolynomialFeatures(degree=2)
            X_train_poly = poly.fit_transform(X_train)
            X_test_poly = poly.transform(X_test)

            # Predict profit/loss
            pnl = predict_profit_loss(filtered_data, model, quantity, buying_date.strftime('%Y-%m-%d'), selling_date.strftime('%Y-%m-%d'))
            
            # Display the profit/loss
            if pnl is not None:
                # st.write("Profit/Loss:", pnl)
                color = "green" if pnl >= 0 else "red"
                st.markdown("<span style='font-weight: bold; color: white; font-size: 22px;'>Profit/Loss:</span>", unsafe_allow_html=True)
                st.write("<span style='font-size: 20px; font-weight: bold; color: {};'>{:.2f}</span>".format(color, pnl), unsafe_allow_html=True)

            # Plot predicted vs actual values
            plot_predicted_vs_close(model, X_train, y_train, X_train_poly, X_test_poly)

        # Add guidelines regarding stocks
        st.markdown("<h3 style='color: yellow;'>Guidelines Regarding Stocks:</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>- Do thorough research before investing in stocks.</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>- Diversify your investment portfolio.</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>- Set a realistic investment strategy and stick to it.</p>", unsafe_allow_html=True)
        
        st.markdown("<h2 style='color: red;'>Disclaimer:</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>Investment in stocks or other financial instruments is subject to market risks. There is no guarantee of returns, and you may lose money. It's important to do thorough research and consult with a financial advisor before making any investment decisions.</p>", unsafe_allow_html=True)
    if selected=="Home":
        st.markdown("<h2 style='color: yellow;'>About Nifty 50:</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>{selected}</p>", unsafe_allow_html=True)
        st.markdown("<h5 style='color: white;'> The NIFTY 50 is a benchmark Indian stock market index that represents the weighted average of 50 of the largest Indian companies listed on the National Stock Exchange. Nifty 50 is owned and managed by NSE Indices (previously known as India Index Services & Products Limited), which is a wholly owned subsidiary of the NSE Strategic Investment Corporation Limited. NSE Indices had a marketing and licensing agreement with Standard & Poor's for co-branding equity indices until 2013. The Nifty 50 index was launched on 22 April 1996, and is one of the many stock indices of Nifty. The NIFTY 50 index has shaped up to be the largest single financial product in India, with an ecosystem consisting of exchange-traded funds (onshore and offshore), and futures and options at NSE and SGX. NIFTY 50 is the world's most actively traded contract. WFE, IOM and FIA surveys endorse NSE's leadership position. Between 2008 & 2012, the NIFTY 50 index's share of NSE market fell from 65% to 29%[10] due to the rise of sectoral indices like NIFTY Bank, NIFTY IT, NIFTY Pharma, and NIFTY Next 50. The NIFTY 50 index covers 13 sectors of the Indian economy and offers investment managers exposure to the Indian market in one portfolio. As of January 2023, NIFTY 50 gives a weightage of 36.81% to financial services including banking, 14.70% to IT, 12.17% to oil and gas, 9.02% to consumer goods, and 5.84% to automobiles.[11][12].</p>", unsafe_allow_html=True)

    if selected=="About Us":
        st.markdown("<h2 style='color: yellow;'>Our Information:</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>{selected}</p>", unsafe_allow_html=True)

        photo1_path = "https://drive.google.com/uc?export=download&id=1omKXr89W2fQSCvFrLgsrLfTvnweXn3-1"
        photo2_path = "https://drive.google.com/uc?export=download&id=1m33L3E81hdhM1WuwTOLdyTfAO_YuDvT5"
        photo3_path = "https://drive.google.com/uc?export=download&id=1Pdl8rIxP_YuWXDCcfCMkkk_iOcoECpb0"
        photo4_path = "https://drive.google.com/uc?export=download&id=1RrlrhuMxGfqTKC9N-9TrCB0eShbZYGmG"

        # Create a grid layout with two columns
        col1, col2 = st.columns(2)

        # Display owner 1 photo and name
        with col1:
            st.image(photo1_path, width=200)
            st.markdown('<span style="color: white; font-weight: bold;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mayank Rai</span>', unsafe_allow_html=True)

            # st.write("Mayank Rai")

        # Display owner 2 photo and name
        with col2:
            st.image(photo2_path, width=200)
            # st.write("Sachin Kumar Rai")
            st.markdown('<span style="color: white; font-weight: bold;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sachin Kumar Rai</span>', unsafe_allow_html=True)

        # Display owner 3 photo and name
        with col1:
            st.image(photo3_path, width=200)
            # st.write("Dharmendra Kumar")
            st.markdown('<span style="color: white; font-weight: bold;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dharmedra Kumar</span>', unsafe_allow_html=True)

        # Display owner 4 photo and name
        with col2:
            st.image(photo4_path, width=200)
            # st.write("Kanika Kamra")
            st.markdown('<span style="color: white; font-weight: bold;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kanika Kamra</span>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()




