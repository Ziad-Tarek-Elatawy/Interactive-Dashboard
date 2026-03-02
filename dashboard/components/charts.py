from dash import html, dcc


def create_charts():
    """
    New layout:
    - Row 1: Time Analysis (full width)
    - Row 2: User Analysis (donut + gender) | Station Analysis (side by side)
    """
    def chart_card(title, chart_id, class_extra=""):
        cls = "card-custom"
        if class_extra:
            cls += " " + class_extra
        return html.Div([
            html.H4(title),
            html.Hr(),
            dcc.Graph(
                id=chart_id,
                style={'height': '100%'},
                config={'displayModeBar': False}
            )
        ], className=cls,
           style={"display": "flex", "flexDirection": "column", "flex": "1"})

    return [
        # ── Row 1: Time Analysis (full width) ─────────────────────────────
        html.Div([
            chart_card("📅 Time Analysis – Trips by Weekday & Hour", "time-analysis-chart"),
        ], className="chart-top-row"),

        # ── Row 2: User Analysis + Station Analysis ───────────────────────
        html.Div([
            chart_card("👥 User Analysis – Subscriber vs Customer & Gender", "user-behavior-chart"),
            chart_card("📍 Station Analysis – Top Start Stations", "station-analysis-chart"),
        ], className="chart-bottom-row"),
    ]