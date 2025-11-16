# FALL25_CS152_Project


## Abstract
Universities offer a wide range of recognized clubs and organizations for students
to join, yet many students struggle to connect with them. Research has shown
that student involvement is strongly tied to academic performance, leadership
development, well-being, and long-term career readiness, making it an essen-
tial component of the college experience. At San Jos´e State University, where
there are more than 300 student organizations, this gap is exacerbated by lim-
ited club visibility, the commuter nature of the campus, and the demanding
schedules of students. To address this gap, we propose a web application that
automatically matches students with campus organizations based on their pro-
files. The system will operate through the following workflow: data collection,
database management, backend development, and front-end interface design.
Information about student organizations will be collected from the University’s
webpage and stored in a relational database. Our application will accept student
questionnaire responses and run a keyword-based matching algorithm, providing
students with a personalized interface to discover recommended organizations.
At the conclusion of the project, the primary deliverable will be a fully func-
tional web application capable of matching students to campus organizations
based on their interests, skills, and availability.

## How to run this application
### Prerequisites
1. Install Python

### How to run this application: Terminal Commands
Create a local copy of the repository:
<br>**git clone https://github.com/lexinejazly-asuncion/FALL25_CS152_Project.git**

Make sure you are in the correct folder: 'FALL25_CS152_Project', if not run:
<br>**cd FALL25_CS152_Project**

This application runs on a virtual environment. 
Create a virtual environment:
**python3 -m venv venv**

*Note: This only needs to be done the first time the project is set up.*

Activate the virtual environment:
**. venv/bin/activate**

Install application dependencies and libraries:
**pip install -r requirements.txt**

After installing these dependencies run:
<br>**python3**
<br>**import nltk**
<br>**nltk.download('punkt')**
<br>**nltk.download('averaged_perceptron_tagger_eng’)**
<br>**nltk.download('wordnet')**
<br>**exit()**

For now, this application can only scape the university website for basic information about RSOs:
**python3 main.py**

Deactivate virtual environment: 
**deactivate**





