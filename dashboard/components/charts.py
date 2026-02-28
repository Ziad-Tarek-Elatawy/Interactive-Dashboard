from dash import html, dcc

def create_charts():
    """
    Generates the layout structure for the dashboard's visualization section.
    
    This function creates empty dcc.Graph placeholders wrapped in styled cards. 
    Each graph is assigned a unique 'id' so that the Viz Expert (Ziad Tarek) 
    can render the Plotly figures inside them, and the Interactivity Expert 
    (Mahmoud Youssef) can connect them to the filter callbacks.
    
    Returns:
        html.Div: The HTML layout containing the chart placeholders.
    """
    return html.Div(
        [
            # First Row: Contains two charts side-by-side (Time Analysis & User Behavior)
            html.Div(
                [
                    # Chart 1: Time Analysis Placeholder
                    html.Div(
                        [
                            html.H4("Time Analysis", style={'textAlign': 'center', 'color': '#2c3e50'}),
                            html.Hr(),
                            dcc.Graph(id='time-analysis-chart', style={'height': '350px'})
                        ],
                        className="card-custom",
                        style={"flex": "1", "marginRight": "15px"}
                    ),

                    # Chart 2: User Behavior Placeholder
                    html.Div(
                        [
                            html.H4("User Behavior", style={'textAlign': 'center', 'color': '#2c3e50'}),
                            html.Hr(),
                            dcc.Graph(id='user-behavior-chart', style={'height': '350px'})
                        ],
                        className="card-custom",
                        style={"flex": "1"}
                    ),
                ],
                style={"display": "flex", "justifyContent": "space-between", "marginBottom": "20px"}
            ),

            # Second Row: Station Analysis Placeholder (Takes up the full width)
            html.Div(
                [
                    html.H4("Station Analysis", style={'textAlign': 'center', 'color': '#2c3e50'}),
                    html.Hr(),
                    dcc.Graph(id='station-analysis-chart', style={'height': '400px'})
                ],
                className="card-custom",
                style={"width": "100%"}
            )
        ]
    )