**Github API test**

This is a sample README.md file for a project. It contains instructions to set up the development environment, documentation on how to run the application, test, migrations, and scripts, as well as information on the implementation and architecture decision process, and deployment instructions.

**Development Environment**

To set up the development environment from scratch, follow these steps:

Clone the repository to your local machine
bash

`git clone https://github.com/pascal007/github_api.git`

**Create virtual environment and Install dependencies**

`python -m venv venv`

Proceed to activate the virtual environment and install dependencies in the main folder

`cd main`
`pip install -r requirements.txt`

**To run Application**

`python manage.py run`

This will start the app on port 5000

**To run Application**

`python manage.py run`

Application will start on port 5000

**To run Test**

`python manage.py test`

**To run Migrations**

After making changes to your model, you can proceed to run migrations using

`python manage.py db migrate`

**To run Scripts**

This is used to populate the database with data needed in the app.

You can specify the size of data by entering the --total argument on your terminal

`python ./scripts/seed.py --total [data size]`

in the argument above, `[data size]` should be an integer value denoting the size of data to be populated

**Implementation and Architecture**

This project was built using Python, Flask, and Sqlite database. 
The choice of these technologies was based on their ease of use and scalability,
and it is also a technology used in Umba where I intend to work.
The application was built using a bit of modular architecture, with each module being responsible
for a specific functionality.


**Deployment**

To deploy the application, follow these steps:

Create a compute service on any of the cloud providers

