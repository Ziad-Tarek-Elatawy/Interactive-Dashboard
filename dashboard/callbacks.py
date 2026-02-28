import pandas as pd
from dash import Input, Output, callback

# Load the processed dataset
df = pd.read_csv('data/processed/cleaned_fordgobike_data.csv')

# Extract start hour for the time slider
df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
df['start_hour'] = df['start_time'].dt.hour

# Define callbacks for KPIs and charts
@callback(
    [
        # KPI Outputs
        Output('total-trips-kpi', 'children'),
        Output('avg-duration-kpi', 'children'),
        Output('subscribers-kpi', 'children'),
        
        # Chart Outputs
        Output('time-analysis-chart', 'figure'),
        Output('user-behavior-chart', 'figure'),
        Output('station-analysis-chart', 'figure')
    ],
    [
        # Filter Inputs
        Input('user-type-filter', 'value'),
        Input('gender-filter', 'value'),
        Input('hour-slider', 'value')
    ]
)
def update_dashboard(selected_user, selected_gender, selected_hour_range):
    
    filtered_df = df.copy()

    # Apply User Type filter
    if selected_user != 'All':
        filtered_df = filtered_df[filtered_df['user_type'] == selected_user]

    # Apply Gender filter
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['member_gender'] == selected_gender]

    # Apply Hour filter
    if selected_hour_range:
        filtered_df = filtered_df[
            (filtered_df['start_hour'] >= selected_hour_range[0]) & 
            (filtered_df['start_hour'] <= selected_hour_range[1])
        ]

    # Calculate KPIs
    if not filtered_df.empty:
        total_trips = f"{len(filtered_df):,}"
        
        if 'duration_mins' in filtered_df.columns:
            avg_duration = f"{round(filtered_df['duration_mins'].mean(), 1)} Mins"
        else:
            avg_duration = "0 Mins"
            
        subs_count = len(filtered_df[filtered_df['user_type'] == 'Subscriber'])
        subs_percent = f"{(subs_count / len(filtered_df)) * 100:.1f}%"
    else:
        total_trips, avg_duration, subs_percent = "0", "0 Mins", "0%"

    # Chart Figures
    fig_time = {}
    fig_behavior = {}
    fig_station = {}

    return total_trips, avg_duration, subs_percent, fig_time, fig_behavior, fig_station