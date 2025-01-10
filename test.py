import os
print(os.environ.get('DB_PASS'))
if column == "Job Title":
    for value in values:
        # If the value is less than 5 characters and looks like an abbreviation
        if len(value) < 5 and re.match(r'^[A-Za-z]+$', value):
            # Insert two queries for the abbreviation
            query1 = f"INSERT INTO delivery_schema.count_spec_template_updated_sample (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('% {value} %', '{column_name}', '{type_value}', '{order_name}', current_date(), NULL, NULL);"
            query2 = f"INSERT INTO delivery_schema.count_spec_template_updated_sample (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('{value}%', '{column_name}', '{type_value}', '{order_name}', current_date(), NULL, NULL);"
            query2 = f"INSERT INTO delivery_schema.count_spec_template_updated_sample (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('{value} %', '{column_name}', '{type_value}', '{order_name}', current_date(), NULL, NULL);"
            queries.append(query1)
            queries.append(query2)
        else:
            # Default behavior for other job titles
            query = f"INSERT INTO delivery_schema.count_spec_template_updated_sample (`values`, `attribute`, `type`, `order_name`, `load_date`, `status`, `completed_status`) VALUES ('%{value}%', '{column_name}', '{type_value}', '{order_name}', current_date(), NULL, NULL);"
            queries.append(query)
