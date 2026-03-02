from dash import html, dcc


def create_sidebar():
    """
    Vertical Sidebar with brand logo, navigation feel, and stacked filters.
    Vibrant gradient design with smooth spacing.
    """

    # Inline style for dropdown control — guarantees dark text on white bg
    dd_style = {
        'backgroundColor': '#ffffff',
        'borderRadius': '10px',
        'border': 'none',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.12)',
        'color': '#1e293b',
        'fontSize': '0.88rem',
        'fontWeight': '500',
    }

    return html.Div(
        [
            # ── Brand Section ──────────────────────────────────────────────
            html.Div([
                html.Div("🚲", className="sidebar-logo-icon"),
                html.Div([
                    html.Div("Ford GoBike", className="sidebar-brand-name"),
                    html.Div("Analytics Dashboard", className="sidebar-brand-sub"),
                ]),
            ], className="sidebar-brand"),

            html.Div(className="sidebar-divider"),

            # ── Filters Section ────────────────────────────────────────────
            html.Div("FILTERS", className="sidebar-section-label"),

            # Filter 1: User Type
            html.Div([
                html.Label("User Type", className="sidebar-filter-label"),
                dcc.Dropdown(
                    id='user-type-filter',
                    options=[
                        {'label': 'All',        'value': 'All'},
                        {'label': 'Subscriber', 'value': 'Subscriber'},
                        {'label': 'Customer',   'value': 'Customer'},
                    ],
                    value='All', clearable=False,
                    style=dd_style,
                ),
            ], className="sidebar-filter-group"),

            # Filter 2: Gender
            html.Div([
                html.Label("Gender", className="sidebar-filter-label"),
                dcc.Dropdown(
                    id='gender-filter',
                    options=[
                        {'label': 'All',    'value': 'All'},
                        {'label': 'Male',   'value': 'Male'},
                        {'label': 'Female', 'value': 'Female'},
                        {'label': 'Other',  'value': 'Other'},
                    ],
                    value='All', clearable=False,
                    style=dd_style,
                ),
            ], className="sidebar-filter-group"),

            # Filter 3: Age Group
            html.Div([
                html.Label("Age Group", className="sidebar-filter-label"),
                dcc.Dropdown(
                    id='age-group-filter',
                    options=[
                        {'label': 'All',   'value': 'All'},
                        {'label': '25-34', 'value': '25-34'},
                        {'label': '35-44', 'value': '35-44'},
                        {'label': '45-54', 'value': '45-54'},
                        {'label': '55-64', 'value': '55-64'},
                        {'label': '65-80', 'value': '65-80'},
                    ],
                    value='All', clearable=False,
                    style=dd_style,
                ),
            ], className="sidebar-filter-group"),

            # Filter 4: Hour of Day
            html.Div([
                html.Label("Hour of Day", className="sidebar-filter-label"),
                dcc.RangeSlider(
                    id='hour-slider',
                    min=0, max=23, step=1,
                    marks={0: '0h', 6: '6h', 12: '12h', 18: '18h', 23: '23h'},
                    value=[0, 23],
                ),
            ], className="sidebar-filter-group sidebar-slider-group"),

            # ── Spacer ─────────────────────────────────────────────────────
            html.Div(style={"flex": "1"}),

            # ── Footer ─────────────────────────────────────────────────────
            html.Div([
                html.Div("📊 Real-time Analytics", className="sidebar-footer-text"),
            ], className="sidebar-footer"),
        ],
        className="sidebar"
    )