import streamlit as st

from mplutils import parse_from_rc_text
from plots import all_plots

# A textarea to enter the theme:
theme = st.sidebar.text_area("Enter your theme here:", height=600)

# To be updated as each plot completes:
plot_progress = st.sidebar.progress(0)

# output text:
output_div = st.sidebar.empty()


# Use `theme` to create a matplotlib rcParams dictionary:
rc_params, rc_errors = parse_from_rc_text(theme)

# print the error list as a bulleted list:
if rc_errors:
    for error in rc_errors:
        output_div.warning(error)


# Create five demo plots:
for i, plot in enumerate(all_plots):
    plot(rc_params)

    # Update the progress bar:
    plot_progress.progress((i + 1) / len(all_plots))


st.markdown(
    f"""
    <style>
        section[data-testid="stSidebar"] {{width: 30rem !important;}}
        section[data-testid="stSidebar"] {{width: 30rem !important;}}
    </style>
""",
    unsafe_allow_html=True,
)


st.button("Re-run")
