# Streamlit web application for REEdI CP3: Careers Progression Pathway Planning. 
Repository Structure
REEdI.py: This is the main Python script that defines the Streamlit web application. It contains the application's layout, functionality, and interactions.
Procfile: This is a configuration file used for deploying the Streamlit app on platforms like Heroku. It specifies the command to run when the app is deployed.
setup.sh: This shell script is used to configure Streamlit's settings, including theme colours and server configuration.

# REEdI.py Documentation
1. Imports: The script starts by importing necessary libraries, including Streamlit, Streamlit components, and Pillow (PIL) for image handling.
2. Streamlit Configuration: st.set_page_config is used to set page configuration, including the page title, icon, and layout.
3. CSS Styling: overall_streamlit_style contains custom CSS styling for the Streamlit app. It's applied to change the app's appearance, including fonts, colours, and sidebar styling.
4. Sidebar Information: The sidebar_info function defines the content displayed in the sidebar. It provides an overview of the project's goals and elements.
5. Main Function: The main function handles the main content of the web application based on the user's choice between two pages: "REEdI Modules' Skillification Platform" and "Skills-In-Demand Analysis."
6. Image Display: It displays an image on the selected page, along with a title.
7. Tableau Integration: The HTML templates (html_temp) embed Tableau visualizations into the Streamlit app. It uses the Tableau JavaScript API to embed interactive visualizations into the app.
8. Footer: The footer function displays a powered by Abodoo message at the bottom of the app.
9. Controller: The load_page function orchestrates the loading of the sidebar, main content, and footer.
Main Execution: The script is executed when the file is run directly, and it calls the load_page function to start the Streamlit app.

# Procfile Documentation
The Procfile is used for deploying the Streamlit app on a platform like Heroku. It specifies the command to run the app. In this case, it runs setup.sh && streamlit run REEdI.py, which first runs the setup.sh script to configure Streamlit's settings and then run the REEdI.py script.

# setup.sh Documentation
The setup.sh script is used to configure Streamlit's settings. It does the following:
1. Create the ~/.streamlit directory if it doesn't exist.
2. Creates or overwrites a config.toml file within the ~/.streamlit directory.
3. Sets various Streamlit configuration options, including theme colours, headless mode, the listening port, and CORS settings.
This script ensures that the Streamlit app is configured with the specified theme colours and server settings when it is deployed.

# To run this Streamlit app, you can follow these steps:

1. Set up a Streamlit environment.
2. Create the necessary directory structure and files as shown in your repository.
3. Deploy the app, for example, on Heroku, using the Procfile. Use the credentials to login to Heroku
