import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/cleaned_fordgobike_data.csv")

#Univariate Plotting Functions
def duration_distribution(ax, df):
    sns.histplot(df["duration_mins"], bins=40, kde=True, ax=ax)
    ax.set_title("Distribution of Trip Duration (Minutes)", fontsize = 10)
    ax.set_xlabel("Duration (Minutes)")
    ax.set_ylabel("Count")

def age_distribution(ax, df):
    sns.histplot(df["age"], bins=30, kde=True, ax=ax)
    ax.set_title("Distribution of Age", fontsize = 10)
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")

def gender_distribution(ax, df):
    sns.countplot(x="member_gender", data=df, ax=ax)
    ax.set_title("Gender Distribution", fontsize = 10)

def age_group_count(ax, df):
    sns.countplot(x="age_group", data=df, ax=ax)
    ax.set_title("Number of Riders per Age Group", fontsize = 10)

#Bivariate Plot Functions

def age_vs_duration(ax, df):
    sns.scatterplot(x="age", y="duration_mins", data=df, alpha=0.3, ax=ax)
    ax.set_title("Age vs Trip Duration", fontsize = 10)

def avg_duration_by_age_group(ax, df):
    avg_duration = df.groupby("age_group")["duration_mins"].mean()
    avg_duration.plot(kind="bar", ax=ax)
    ax.set_title("Average Trip Duration by Age Group", fontsize = 10)
    ax.set_ylabel("Average Duration (Minutes)", fontsize = 10)

def duration_by_gender(ax, df):
    sns.barplot(x="member_gender", y="duration_mins", data=df, ax=ax)
    ax.set_title("Trip Duration by Gender", fontsize = 10)

def run_all_plots(df):
    fig, axes = plt.subplots(3, 3, figsize=(18, 15))
    fig.suptitle("EDA", fontsize=10)

    duration_distribution(axes[0, 0], df)
    age_distribution(axes[0, 1], df)
    gender_distribution(axes[0, 2], df)
    age_group_count(axes[1, 0], df)
    age_vs_duration(axes[1, 1], df)
    avg_duration_by_age_group(axes[1, 2], df)
    duration_by_gender(axes[2, 0], df)

    axes[2, 1].set_visible(False)
    axes[2, 2].set_visible(False)

    plt.tight_layout(pad=4.0, h_pad=5.0, w_pad=4.0)  # more padding between subplots
    plt.show()

run_all_plots(df)