from dash import html, dcc

def create_charts():
    """
    4 sections as per project requirements:
    - Row 1: Time Analysis + User Analysis (side by side)
    - Row 2: Station Analysis (full width)
    """
    def chart_card(title, chart_id):
        return html.Div([
            html.H4(title),
            html.Hr(),
            dcc.Graph(
                id=chart_id,
                style={'height': '100%'},
                config={'displayModeBar': False}
            )
        ], className="card-custom",
           style={"display": "flex", "flexDirection": "column", "flex": "1"})

    return [
        # ── Row 1: Time Analysis + User Analysis ───────────────────────────
        html.Div([
            chart_card("📅 Time Analysis – Trips by Weekday & Hour", "time-analysis-chart"),
            chart_card("👥 User Analysis – Subscriber vs Customer & Gender", "user-behavior-chart"),
        ], className="chart-top-row"),

        # ── Row 2: Station Analysis (wide) ─────────────────────────────────
        html.Div([
            chart_card("📍 Station Analysis – Top Start Stations", "station-analysis-chart"),
        ], className="chart-bottom-row"),
    ]