This project uses Python, pandas, Plotly, and other libraries to analyze my LinkedIn connections and provide insights into my professional network.

What Does the Code Do?

Loads and cleans LinkedIn connection data from a CSV file.
Analyzes network growth over time (line chart).
Visualizes connections made per month (bar chart).
Identifies top companies and positions in my network (bar charts and treemaps).
Creates an interactive network graph visualizing connections between me and top companies.
Key Libraries:

pandas: Data manipulation and analysis.
Plotly.express: Interactive visualizations.
matplotlib.pyplot: Additional visualizations.
networkx: Graph creation.
pyvis: Interactive graph generation.
How to Run the Analysis

Prerequisites:
Python 3 (https://www.python.org/downloads/)
Required libraries: pip install pandas plotly matplotlib networkx pyvis
Download: Clone or download the repository.
Data: Place your LinkedIn connections CSV file (named "LinkedInConn.csv") in the project directory (see the code for expected column names, if you need to adapt the csv).
Run: Execute the Python code (e.g., in your terminal: python linkedin_analysis.py - assuming you named the file that way).
View Visualizations: Charts will be displayed, and the interactive graph will be saved as "Company_graph.html".
Project Purpose

This project can be used to:

Understand the composition of your professional network.
Identify trends in connections over time.
Discover potential networking or job opportunities.
Feel free to adapt, extend, and experiment with your own LinkedIn data!

Code Explanation

The code analyzes your LinkedIn connections with these key steps:

Import Libraries: Loads pandas (for data manipulation), plotly and matplotlib (for visualization), networkx (for graph creation), and pyvis (for interactive network visualization).

Load Data: Reads a CSV file named "LinkedInConn.csv" containing your LinkedIn connection data.

Clean Data:

Checks data structure, column names, data types.
Handles missing values within the 'company' column.
Analyze Connections Over Time:

Calculates connections made per date.
Creates a line chart showing growth of connections over time.
Analyze Connections by Month:

Groups connections by month of the year.
Creates a bar chart showing number of connections made each month.
Analyze Connections by Company:

Sorts connections by company affiliation.
Provides bar chart of top companies in your network.
Generates treemap visualizations for company analysis
Analyze Connections by Position:

Sorts connections by job position.
Generates a treemap visualization for position analysis
Interactive Network Graph:

Creates an interactive graph showing the connections between you and the top companies in your network, with positions listed within each company node.