from dash import html, dcc

def create_sidebar():
    """
    Constructs the layout for the dashboard's side navigation bar containing data filters.
    
    This layout provides the user interface for filtering data across the dashboard. 
    It includes dropdowns for categorical data and a range slider for continuous data.
    Each filter component is assigned a specific 'id', which must be utilized by the 
    Interactivity Expert (Mahmoud Youssef) within the Dash Callbacks to dynamically 
    update the charts and KPI cards based on user selection.
    
    Returns:
        html.Div: The HTML layout of the sidebar containing the filter components.
    """
    return html.Div(
        [
            # Sidebar Header
            html.H2("Filters", className="display-6"),
            html.Hr(),
            html.P("Customize your data:", className="lead mb-4"),
            
            # Filter 1: User Type Dropdown (Subscriber vs. Customer)
            # ID: 'user-type-filter' -> Used to trigger callbacks for user category updates.
            html.Div(
                [
                    html.Label("User Type:"),
                    dcc.Dropdown(
                        id='user-type-filter',
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'Subscriber', 'value': 'Subscriber'},
                            {'label': 'Customer', 'value': 'Customer'}
                        ],
                        value='All', # Sets the default state to show all users
                        clearable=False, # Prevents the user from leaving the field entirely empty
                        className="text-dark" # Ensures text is readable against the dark sidebar background
                    ),
                ],
                className="mb-4"
            ),

            # Filter 2: Gender Dropdown
            # ID: 'gender-filter' -> Used to trigger callbacks for demographic updates.
            html.Div(
                [
                    html.Label("Gender:"),
                    dcc.Dropdown(
                        id='gender-filter',
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'Male', 'value': 'Male'},
                            {'label': 'Female', 'value': 'Female'},
                            {'label': 'Other', 'value': 'Other'}
                        ],
                        value='All', # Sets the default state to show all genders
                        clearable=False,
                        className="text-dark"
                    ),
                ],
                className="mb-4"
            ),

            # Filter 3: Hour of the Day Range Slider
            # ID: 'hour-slider' -> Used to filter the dataset by the time of day trips occurred.
            html.Div(
                [
                    html.Label("Hour of Day:"),
                    dcc.RangeSlider(
                        id='hour-slider',
                        min=0,
                        max=23,
                        step=1,
                        # Generates visual markers on the slider every 4 hours for better UX
                        marks={i: f'{i}h' for i in range(0, 24, 4)}, 
                        value=[0, 23], # Default range encompasses the entire 24-hour period
                        className="mt-2"
                    ),
                ],
                className="mb-4"
            ),
        ],
        # Applies the CSS class defined in style.css to fix the sidebar to the left
        className="sidebar" 
    )