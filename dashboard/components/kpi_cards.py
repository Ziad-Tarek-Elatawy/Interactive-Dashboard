from dash import html

def create_kpi_cards():
    """
    Creates a row containing three Key Performance Indicator (KPI) cards.
    
    The numerical values are initialized to '0' as placeholders. Each value 
    container is assigned a unique 'id' so that the Interactivity Expert 
    (Mohamed Yousef) can dynamically update them using Dash callbacks 
    based on the user's filter selections.
    
    Returns:
        html.Div: The HTML layout containing the flexbox row of KPI cards.
    """
    return html.Div(
        [
            # Card 1: Total Trips
            # ID: 'total-trips-kpi' -> Target this ID to update the total count of filtered trips.
            html.Div(
                [
                    html.Div("Total Trips", className="kpi-title"),
                    html.Div(id="total-trips-kpi", className="kpi-value", children="0")
                ],
                className="card-custom",
                style={"flex": "1", "marginRight": "15px"} # Ensures equal horizontal spacing
            ),
            
            # Card 2: Average Trip Duration (Minutes)
            # ID: 'avg-duration-kpi' -> Target this ID to update the calculated average duration.
            html.Div(
                [
                    html.Div("Avg Duration (Mins)", className="kpi-title"),
                    html.Div(id="avg-duration-kpi", className="kpi-value", children="0")
                ],
                className="card-custom",
                style={"flex": "1", "marginRight": "15px"}
            ),

            # Card 3: Annual Subscriber Percentage
            # ID: 'subscribers-kpi' -> Target this ID to update the percentage of subscriber users.
            html.Div(
                [
                    html.Div("Subscribers %", className="kpi-title"),
                    html.Div(id="subscribers-kpi", className="kpi-value", children="0%")
                ],
                className="card-custom",
                style={"flex": "1"} # The final card in the row does not need a right margin
            ),
        ],
        # Main container styling: Uses Flexbox to align the cards horizontally with even spacing
        style={"display": "flex", "justifyContent": "space-between", "marginBottom": "20px"}
    )