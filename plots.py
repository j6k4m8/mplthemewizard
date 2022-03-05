import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import datetime


def histogram(rc_params):

    ## data:
    random_gaussian = np.random.normal(0, 1, 100)

    ## plot:
    with plt.rc_context(rc_params):
        fig, ax = plt.subplots()
        ax.set_title("Difference between a duck")
        ax.set_xlabel("Difference (room temperature, vacuum)")
        ax.set_ylabel("Frequency")
        ax.hist(random_gaussian, bins=20)
        st.pyplot(fig)


def scatter_lines(rc_params):

    ## data:
    random_x1 = sorted(np.random.uniform(0, 1, 100))
    random_y1 = sorted(np.random.uniform(0, 1, 100))

    random_x2 = sorted(np.random.uniform(0, 1, 100))
    random_y2 = sorted(np.random.uniform(0, 1, 100))

    random_x3 = sorted(np.random.uniform(0, 1, 100))
    random_y3 = sorted(np.random.uniform(0, 1, 100))

    ## plot:
    with plt.rc_context(rc_params):
        fig, ax = plt.subplots()
        ax.scatter(random_x1, random_y1, label="SWaLLOWBot 9000")
        ax.scatter(random_x2, random_y2, label="African swallow")
        ax.scatter(random_x3, random_y3, label="European swallow")
        ax.set_xlabel("Load (grams)")
        ax.set_ylabel("Velocity ($\mu m / ms$)")
        ax.legend()
        st.pyplot(fig)


def timeseries_with_sem(rc_params):

    ## data:
    # Timeseries over a year:
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2020, 12, 31)
    time_delta = end - start
    time_delta_in_days = time_delta.days

    # Random values over time:
    random_values = np.random.normal(0, 1, time_delta_in_days)
    # running mean:
    running_mean = np.convolve(random_values, np.ones(80) / 80, mode="valid")

    ## plot:
    with plt.rc_context(rc_params):
        fig, ax = plt.subplots()
        ax.set_title("Stock price over a year")
        ax.set_xlabel("Date")
        ax.set_ylabel("Stock price ($)")
        ax.plot(
            [start + datetime.timedelta(days=i) for i in range(time_delta_in_days)][
                : len(running_mean)
            ],
            running_mean,
            label="Running average (80 days)",
            # dashed:
            linestyle="--",
        )
        # Plot standard error of the mean:
        ax.fill_between(
            [start + datetime.timedelta(days=i) for i in range(time_delta_in_days)][
                : len(running_mean)
            ],
            running_mean + np.std(running_mean),
            running_mean - np.std(running_mean),
            alpha=0.2,
            label="Standard error of the mean",
        )
        ax.legend()
        st.pyplot(fig)


all_plots = [
    histogram,
    scatter_lines,
    timeseries_with_sem,
]
