import streamlit as st
from datetime import datetime
import re
import os

def main():
    st.title("Streamlit Checkbox Application")

    # Sidebar checkboxes
    st.sidebar.title("Select Columns")
    order_name = st.sidebar.text_input("Enter Order Name", key="order_name")  # New input for order_name
    sample = st.sidebar.checkbox("Sample")
    order = st.sidebar.checkbox("Order")
    sub_industry = st.sidebar.checkbox("Sub Industry")
    industry = st.sidebar.checkbox("Industry")
    sector = st.sidebar.checkbox("Sector")
    county = st.sidebar.checkbox("County")
    post_town = st.sidebar.checkbox("Post Town")
    post_code = st.sidebar.checkbox("Post Code")
    region = st.sidebar.checkbox("Region")
    location_type = st.sidebar.checkbox("Location Type")
    company_status = st.sidebar.checkbox("Company Status")
    website = st.sidebar.checkbox("Website")
    employee_range = st.sidebar.checkbox("Employee Range")
    turnover_range = st.sidebar.checkbox("Turnover Range")
    employees = st.sidebar.checkbox("Employees")
    turnover = st.sidebar.checkbox("Turnover")
    company_age = st.sidebar.checkbox("Company Age")
    job_title = st.sidebar.checkbox("Job Title")
    job_title_level = st.sidebar.checkbox("Job Title Level")
    

    # Employee range values (predefined)
    employee_ranges = [
        "1 to 5", "6 to 10", "11 to 19", "20 to 49", "50 to 99", "100 to 199", 
        "200 to 499", "500 to 999", "1000 to 5000", "5000+", "Uncategorised", "NULL"
    ]
    
    # Turnover range values (predefined)
    turnover_ranges = [
        "100K to 250K", "100M to 500M", "10M to 25M", "1B+", "1M to 2.5M", 
        "2.5M to 5M", "250K to 500K", "25M to 50M", "500K to 1M", "500M to 1B", 
        "50M to 100M", "5M to 10M", "Upto 100K", "Uncategorised", "NULL"
    ]

    # Job title levels
    job_title_levels = [
        "Manager", "Senior", "C level", "Company Secretary", "Director", "VP level", 
        "General", "Government", "Intern", "Junior", "Administration", "Student", "Uncategorised"
    ]

    # Input fields for selected columns
    st.subheader("Inputs for Selected Columns")
    column_inputs = {}

    def get_inputs(column_name):
        st.write(f"### {column_name}")
        # Get INC values
        inc_inputs = st.text_area(f"Enter INC values for {column_name} (comma-separated or newline-separated):", key=f"{column_name}_inc")
        # Get EXC values
        exc_inputs = st.text_area(f"Enter EXC values for {column_name} (comma-separated or newline-separated):", key=f"{column_name}_exc")

        # Function to split values and handle escaping of quotes
        def split_and_escape(input_string):
            # Split by commas, but handle quoted sections
            pattern = r'(?:"([^"]*)"|\'([^\']*)\'|([^,]+))'
            values = re.findall(pattern, input_string)
            processed_values = []
            for value in values:
                # Take the first matched group that isn't empty
                matched_value = value[0] or value[1] or value[2]
                if matched_value:
                    # Escape single quotes
                    processed_values.append(matched_value.strip().replace("'", "\\'"))
            return processed_values

        # Process INC and EXC values
        inc_values = split_and_escape(inc_inputs)
        exc_values = split_and_escape(exc_inputs)

        return {"inc": inc_values, "exc": exc_values}

    def get_range_inputs(column_name, range_values):
        st.write(f"### {column_name} - Range")
        # Select predefined ranges for INC and EXC
        inc_selected = st.multiselect(f"Select INC values for {column_name}:", range_values, key=f"{column_name}_inc")
        exc_selected = st.multiselect(f"Select EXC values for {column_name}:", range_values, key=f"{column_name}_exc")
        return {"inc": inc_selected, "exc": exc_selected}

    def get_min_max_range_inputs(column_name):
        st.write(f"### {column_name} - MIN and MAX Values")
        min_inc = st.number_input(f"Enter MIN INC for {column_name}:", key=f"{column_name}_min_inc", min_value=0)
        max_inc = st.number_input(f"Enter MAX INC for {column_name}:", key=f"{column_name}_max_inc", min_value=0)
        min_exc = st.number_input(f"Enter MIN EXC for {column_name}:", key=f"{column_name}_min_exc", min_value=0)
        max_exc = st.number_input(f"Enter MAX EXC for {column_name}:", key=f"{column_name}_max_exc", min_value=0)
        return {"inc": {"min": min_inc, "max": max_inc}, "exc": {"min": min_exc, "max": max_exc}}

    def get_sample_or_order_inputs(column_name):
        st.write(f"### {column_name}")
        inc_input = st.selectbox(f"Select INC for {column_name} (Y/N):", options=["Y", "N"], key=f"{column_name}_inc")
        return {"inc": inc_input}

    # Multi-select dropdown for Job Title Level
    def get_job_title_level_inputs():
        st.write("### Job Title Level")
        inc_values = st.multiselect("Select INC values for Job Title Level:", job_title_levels, key="job_title_level_inc")
        exc_values = st.multiselect("Select EXC values for Job Title Level:", job_title_levels, key="job_title_level_exc")
        return {"inc": inc_values, "exc": exc_values}

    if sample:
        column_inputs["Sample"] = get_sample_or_order_inputs("Sample")
    if sub_industry:
        column_inputs["Sub Industry"] = get_inputs("Sub Industry")
    if industry:
        column_inputs["Industry"] = get_inputs("Industry")
    if sector:
        column_inputs["Sector"] = get_inputs("Sector")
    if county:
        column_inputs["County"] = get_inputs("County")
    if post_town:
        column_inputs["Post Town"] = get_inputs("Post Town")
    if post_code:
        column_inputs["Post Code"] = get_inputs("Post Code")
    if region:
        column_inputs["Region"] = get_inputs("Region")
    if location_type:
        column_inputs["Location Type"] = get_inputs("Location Type")
    if company_status:
        column_inputs["Company Status"] = get_inputs("Company Status")
    if website:
        column_inputs["Website"] = get_inputs("Website")
    if employee_range:
        column_inputs["Employee Range"] = get_range_inputs("Employee Range", employee_ranges)
    if turnover_range:
        column_inputs["Turnover Range"] = get_range_inputs("Turnover Range", turnover_ranges)  # For other range values
    if employees:
        column_inputs["Employees"] = get_min_max_range_inputs("Employees")
    if turnover:
        column_inputs["Turnover"] = get_min_max_range_inputs("Turnover")
    if company_age:
        column_inputs["Company Age"] = get_min_max_range_inputs("Company Age")
    if job_title:
        column_inputs["Job Title"] = get_inputs("Job Title")
    if job_title_level:
        column_inputs["Job Title Level"] = get_job_title_level_inputs()  # Use the multi-select for job title level
    if order:
        column_inputs["Order"] = get_sample_or_order_inputs("Order")

    # Button to generate queries
    if st.button("Generate Insert Queries"):
        # Get current date for use in SQL
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Validate order_name is provided
        if not order_name:
            st.error("Please enter an Order Name")
            return

        # Generate queries for each selected column and its inputs
        queries = []
        for column, inputs in column_inputs.items():
            # Convert column name to lowercase and replace spaces with underscores
            column_name = column.lower().replace(" ", "_")

            if isinstance(inputs, dict):
                if 'min' in inputs['inc']:  # Range inputs (Employees, Turnover, Company Age)
                    # Only handle range columns like Employees, Turnover, Company Age
                    if column in ["Employees", "Turnover", "Company Age"]:
                        # Add comment for the group
                        queries.append(f"-- Insert queries for {column_name} (Range)")
                        for range_type in ['inc', 'exc']:
                            range_values = inputs[range_type]
                            if isinstance(range_values, dict):  # This is for min/max range inputs
                                min_value = range_values.get('min', None)
                                max_value = range_values.get('max', None)
                                if min_value is not None and min_value != 0:
                                    # Generate a separate query for the MIN value
                                    query = f"INSERT INTO delivery_schema.count_spec_template_updated (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('{min_value}', '{column_name}', '{range_type.upper()}', '{order_name}', current_date(), NULL, NULL);"
                                    queries.append(query)
                                if max_value is not None and max_value != 0:
                                    # Generate a separate query for the MAX value
                                    query = f"INSERT INTO delivery_schema.count_spec_template_updated (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('{max_value}', '{column_name}', '{range_type.upper()}', '{order_name}', current_date(), NULL, NULL);"
                                    queries.append(query)
                else:  # Regular inputs (Sub Industry, etc.)
                    # Add comment for the group
                    queries.append(f"-- Insert queries for {column_name}")
                    for range_type, values in inputs.items():
                        if values:
                            for value in values:
                                # Skip if value is '0', 'NULL', or 'Uncategorised'
                                if value == "0" or value == "NULL" or value == "Uncategorised":
                                    continue
                                # Determine whether the value is in "INC" or "EXC" section
                                if range_type == 'inc':
                                    type_value = 'INC'
                                elif range_type == 'exc':
                                    type_value = 'EXC'
                                else:
                                    continue
                                query = f"INSERT INTO delivery_schema.count_spec_template_updated (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('{value}', '{column_name}', '{type_value}', '{order_name}', current_date(), NULL, NULL);"
                                queries.append(query)

        # Display queries
        if queries:
            st.subheader("Generated Insert Queries:")
            st.code("\n".join(queries))

if __name__ == "__main__":
    main()
    
