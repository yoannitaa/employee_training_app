# Python CRUD Application for Employee Training Inventory

A comprehensive Python application for managing employee training inventory data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the banking or financial industry, specifically addressing the need to manage employee training data efficiently. Employee training inventory plays a crucial role in ensuring that employees have skills and competencies that align with the job competencies required by the organization.

**Benefits:**
* Improved data accuracy and consistency of employee training records
* Streamlined employee training data management processes
* Easier monitoring training requirement within department
* Better tracking of employee competency compliance within the organization
* Real time access to employee training history and status
* Reduced risk of error of manual training record
* Better coordination between Employee, HR Staff and Employee Manager

**Target Users:**

This application is designed for Employee, HR Department, Employee Manager within the organization to facilitate their employee skill and competencies related to training requirement.

## Features

* **Create:**
    * Add new training data entries with essential details like employee name, job title, department name, training name, training category, training date, training validity, training status.
    * Implement validation rules to ensure data integrity (e.g uniqe employee ID).
* **Read:**
    * Search and retrieve specific employee training records by applying filters based unique employee ID.
    * Display comprehensive information for each employee training data in a user-friendly format.
    * Integrate pagination and sorting capabilities for large datasets (if applicable).
* **Update:**
    * Modify existing employee training data to reflect changes in job title, department name, training name, training category, training date, training validity, training status.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted employee training records with appropriate authorization checks (if applicable).
    * Implement soft delete functionality to prevent permanent data loss (optional, depending on business needs).
    * Consider offering data archiving capabilities (optional).
* **Security:**
    * Implement user authentication and authorization mechanisms (if sensitive data is involved) to control access to different CRUD operations.
* **Reporting:**
    * Generate reports or summaries based on employee training data to support training monitoring (optional).
    * Export data in various formats (e.g., CSV, Excel) for further analysis (optional).

## Installation

1. **Prerequisites:**
    * Python version 3.7 or later
    * Additional dependencies (list any required packages)

2. **Installation:**
    ```bash
    git clone https://github.com/yoannitaa/employee_training_app.git
    cd <your-repo-name>
   ```

3. **Database Setup (if applicable):**
    Follow specific instructions for configuring your database connection, aligning with the business's chosen database management system.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new employee training record, for example, a new training record, providing details like employee name, job title, department name, training name, training category, training date, training validity, training status.
    * **Read:** Search and retrieve customer information by employee ID.
    * **Update:** Modify customer details, such as updating their training name, job title, department name, training validity.
    * **Delete:** Remove a customer record from the system (with appropriate authorization, if applicable).

## Data Model
This project utilizes a collection type database in Python to represent employee training data. The following fields are typically stored:
   * emp_id: (String) - unique identifier for each employee.
   * emp_name: (String) - employee name
   * job_title: (String) - employee job title
   * dept_name: (String) - employee department
   * training_name: (String) - training name
   * training_cat: (String) - training category (Sertifikasi or Non-Sertifikasi)
   * training_date: (String) - date which employee took training
   * training_valid: (Int) - training validity
   * training_status: (String) - training status (Aktif or Expired)

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to my email or submit an issue if you encounter any problems or have suggestions for improvements.

