
# todo_list-with-django-rest-framework


## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [Django](https://www.djangoproject.com/download/) (required version)
- [Git](https://git-scm.com/downloads)

## Installation

To install and set up the project, follow these steps:

1. Clone the repository:

   ```bash
       git clone https://github.com/Caliber24/todo_list_with_DRF.git
       cd todo_list_with_DRF

2. Create a virtual environment:

        
        python -m venv myenv
        source myenv/bin/activate  # For Linux or macOS
        myenv\Scripts\activate  # For Windows

3. Install dependencies:
    
        pip install -r requirements.txt

4.Set up the database:
        
        python manage.py makemigrations
        python manage.py migrate


5.Run the development server:
    
        python manage.py runserver

## Create superuser for login DjangoAdmin
Run the Command:

         python manage.py createsuperuser
