import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load cleaned data
sum_order_items_df = pd.read_csv("sum_order_items.csv")
mean_review_score_df = pd.read_csv("mean_review_score.csv")
monthly_orders_df = pd.read_csv("monthly_orders.csv")
highest_orders_city_df = pd.read_csv("highest_orders_city.csv")
customer_segment_df = pd.read_csv("customer_segment.csv")


st.header('E-Commerce Public Dataset Dashboard :sparkles:')
st.subheader('Product Categories Performance Based on Number of Orders')

col1, col2 = st.columns(2)

with col1:
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x="order_count", 
                y="product_category", 
                data=sum_order_items_df.head(5), 
                palette=colors,
                ax=ax)
    ax.set_title("Best Performing Product Categories", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

with col2:
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x="order_count", 
                y="product_category", 
                data=sum_order_items_df.sort_values(by="order_count", ascending=True).head(5), 
                palette=colors,
                ax=ax)
    ax.set_title("Best Performing Product Categories", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

st.subheader("Product Categories Performance Based on Customer's Review Score")

col1, col2 = st.columns(2)

with col1:
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x="mean_review_score", 
                y="product_category", 
                data=mean_review_score_df.head(5), 
                palette=colors,
                ax=ax)
    ax.set_title("Best Performing Product Categories", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

with col2:
    colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x="mean_review_score", 
                y="product_category", 
                data=mean_review_score_df.sort_values(by="mean_review_score", ascending=True).head(5), 
                palette=colors,
                ax=ax)
    ax.set_title("Best Performing Product Categories", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=30)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

st.subheader("Number of Orders per Month")

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(
    monthly_orders_df["order_purchase_timestamp"],
    monthly_orders_df["order_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", labelsize=20, rotation=30)
ax.tick_params(axis="y", labelsize=20)
st.pyplot(fig)

st.subheader("Total Revenue per Month")

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(
    monthly_orders_df["order_purchase_timestamp"],
    monthly_orders_df["revenue"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", labelsize=20, rotation=30)
ax.tick_params(axis="y", labelsize=20)
st.pyplot(fig)


st.subheader("Customer Segmentation Based on RFM Score")

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="customer_count", 
    y="customer_segment",
    data=customer_segment_df.sort_values(by="customer_segment", ascending=False),
    color="#90CAF9",
    ax=ax
)
# ax.set_title("Number of Customer for Each Segment", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel("Number of Customer", fontsize=30)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=25)
st.pyplot(fig)