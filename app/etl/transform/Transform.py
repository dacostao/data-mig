class Transform():

    def transform_hired_employees(data):
        transformed_data = []
        for row in data:
            transformed_row = {
                'id': int(row[0]),
                'name': row[1],
                'datetime': row[2],
                'department_id': int(row[3]),
                'job_id': int(row[4])
            }
            transformed_data.append(transformed_row)
        return transformed_data

    def transform_departments(data):
        transformed_data = []
        for row in data:
            transformed_row = {
                'id': int(row[0]),
                'department': row[1]
            }
            transformed_data.append(transformed_row)
        return transformed_data

    def transform_jobs(data):
        transformed_data = []
        for row in data:
            transformed_row = {
                'id': int(row[0]),
                'job': row[1]
            }
            transformed_data.append(transformed_row)
        return transformed_data