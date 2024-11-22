# Orphanage Management System

An efficient and user-friendly **Orphanage Management System** designed to streamline donation and adoption processes for orphanages. The system allows users to donate items or money, and provides an easy way to request child adoption, complete with appointment scheduling.

## Features
### Donations
- Accept monetary and non-monetary donations.
- Donation types include:
  - Money
  - Clothes
  - Toys
  - School Supplies
  - Food Items
  - Blankets
- Secure payment options for monetary donations.
- Display orphanage address for non-monetary item deliveries.

### Adoption
- List of children available for adoption with their details (name, age, gender, date of birth).
- Allows users to request adoption by clicking on a child's name.
- Schedule an appointment for adoption inquiries.

### Admin Features
- Manage details of orphans (e.g., age, date of admission, guardian contact).
- View donation and adoption records.

## Tech Stack
- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python (Django Framework)
- **Database:** MySQL (default Django database)
- **Version Control:** Git, GitHub

## Installation
Follow these steps to set up the project locally:

### Prerequisites
- Python 3.9+
- Git
- Virtual Environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AdityaKumar00007/Orphanage-Management-System.git
   cd Orphanage-Management-System

   
2.Set up a virtual environment:
 python -m venv env
 source env/bin/activate  # For Linux/MacOS
 env\Scripts\activate     # For Windows

3.Install dependencies:
 pip install -r requirements.txt


4.Apply migrations:
 python manage.py migrate


5.Start the development server:
 python manage.py runserver
 Open your browser and visit:

6.Open your browser and visit:
 http://127.0.0.1:8000/

 
Usage
Home Page:
 1.Displays an overview of the orphanage.
 2.Links to Donation and Adoption pages.
Donation Page:
 1.Fill out the donation form for monetary donations.
 2.View orphanage address for delivering non-monetary donations.
Adoption Page:
 1.Browse through the list of children available for adoption.
 2.Request adoption and get an appointment schedule.

   
