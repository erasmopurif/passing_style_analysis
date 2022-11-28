import streamlit as st
import pandas as pd
import json
from io import BytesIO

import utils

# Page config
st.set_page_config(
    page_icon="⚽️",
    layout="wide"
)

# Load data
@st.cache
def load_data():
    # Load the edited Soccerment allEvents dataset
    df_soccment = pd.read_csv("data/soccerment_serieA_2021-22_allEvents_EDIT.csv")
    # Load lineups.json, manually created from "Appendix 5 - Formations Explained"
    with open("data/lineups.json", "r") as f:
        lineups = json.load(f)
    # Load teams_lineups.json 
    with open("data/teams_lineups.json", "r") as f:
        teams_lineups = json.load(f)
    return df_soccment, lineups, teams_lineups

df_soccment, lineups, teams_lineups = load_data()


# Page title
st.title("Full Pitch & Field Tilt Networks")

# Matchdays selection
st.subheader("Select matchday(s)")

matchday_selection_1 = st.radio(
    "Matchday visualization",
    ("Single matchday", "Range of matchdays")
)
if matchday_selection_1 == "Single matchday":
    matchday = st.selectbox(
        "Matchday",
        (range(1,39))
    )
else:
    matchday_tuple = st.slider("Range of matchdays", 1, 38, (1, 38))
    min_match, max_match = matchday_tuple
    matchday_list = range(min_match, max_match+1)

# Team selection
st.subheader("Select team(s)")

team_selection = st.radio(
    "Team visualization",
    ("Single team", "Two teams", "All teams")
)
if team_selection == "Single team":
    team = st.selectbox(
        "Team",
        (sorted(teams_lineups.keys()))
    )
elif team_selection == "Two teams":
    team_list = st.multiselect(
        "Teams",
        sorted(teams_lineups.keys()),
        help="Select exactly two teams."
    )
    if len(team_list) > 2:
        st.warning("You have selected more than two teams!")
else:
    team_list = sorted(teams_lineups.keys())

# Additional parameters for the visualization
st.subheader("Select the area of the pitch for visualizing the passing network")
    
# Pitch zone for the passing network
pitch_zone_btn = st.radio(
    "Area of the pitch to visualize",
    ("Complete pitch (Full passing network)", "Final third (Field-tilt passing network)")
)
if pitch_zone_btn == "Complete pitch (Full passing network)":
    pitch_zone = "full"
else:
    pitch_zone = "field_tilt"

    
# Additional parameters for the visualization
st.subheader("Select the number of minimum passes")
    
# Insert number of minimum passes for the visualization
filter_passes_unit = st.number_input("Number of minimum passes", min_value=1, max_value=10, value=3, help="For multiple matchdays, this value is multiplied by the number of matchdays.")

# Put a little vertical space
st.text("")

# Run analysis
run_analysis = st.button("Run analysis", type="primary")
if run_analysis:
    if team_selection == "Single team":
        if matchday_selection_1 == "Single matchday":
            fig = utils.plot_single_matchday_single_team(df_soccment, team, matchday, teams_lineups, pitch_zone, filter_passes_unit)
        else:
            fig = utils.plot_multiple_matchdays_single_team(df_soccment, team, matchday_list, teams_lineups, pitch_zone, filter_passes_unit)
    elif team_selection == "Two teams":
        if matchday_selection_1 == "Single matchday":
            fig = utils.plot_single_matchday_two_teams(df_soccment, team_list, matchday, teams_lineups, pitch_zone, filter_passes_unit)
        else:
            fig = utils.plot_multiple_matchdays_two_teams(df_soccment, team_list, matchday_list, teams_lineups, pitch_zone, filter_passes_unit)
    else:
        if matchday_selection_1 == "Single matchday":
            fig = utils.plot_single_matchday_all_teams(df_soccment, team_list, matchday, teams_lineups, pitch_zone, filter_passes_unit)
        else:
            fig = utils.plot_multiple_matchdays_all_teams(df_soccment, team_list, matchday_list, teams_lineups, pitch_zone, filter_passes_unit)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.image(buf, use_column_width="auto")