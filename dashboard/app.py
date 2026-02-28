"""
Main Application Entry Point
Author: UI/UX Designer

This file initializes the Dash web application and assembles the main layout.
It imports the modularized UI components (Sidebar, KPI Cards, and Charts) 
and structures them using a responsive grid system.
"""

import dash
from dash import html

# Import modular UI components created by the UI/UX Designer
from components.filters import create_sidebar
from components.kpi_cards import create_kpi_cards
from components.charts import create_charts

# Initialize the Dash application
# 'suppress_callback_exceptions=True' allows the app to load even if callbacks 
# are assigned to components that are generated dynamically or exist in other files.
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Set the title that will appear on the browser's tab
app.title = "Ford GoBike Dashboard" 

# ==========================================================================
# Main Dashboard Layout Structure
# ==========================================================================
app.layout = html.Div(
    [
        # Part 1: The Sidebar (Contains all filter inputs like Dropdowns and Sliders)
        create_sidebar(),

        # Part 2: The Main Content Area (Contains the title, KPIs, and Charts)
        html.Div(
            [
                # Dashboard Main Header
                html.H1(
                    "Ford GoBike System Analysis", 
                    style={'color': '#2c3e50', 'marginBottom': '30px', 'fontWeight': 'bold'}
                ),
                
                # First Row: Key Performance Indicator (KPI) Cards Placeholder
                create_kpi_cards(),

                # Second & Third Rows: Visualizations and Charts Placeholders
                create_charts()
            ],
            # Applies the 'content' CSS class to ensure this section sits beside 
            # the fixed sidebar and does not overlap with it.
            className="content" 
        )
    ]
)

# ==========================================================================
# Server Execution
# ==========================================================================
if __name__ == '__main__':
    # Runs the application on a local development server.
    # Port 8055 is specified to avoid conflicts with previously running instances.
    app.run(host='127.0.0.1', port=8055, debug=True)