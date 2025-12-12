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

### First Time Set Up  
Create a local copy of the repository:  
```
git clone https://github.com/lexinejazly-asuncion/FALL25_CS152_Project.git
```

Make sure you are in the correct folder: 'FALL25_CS152_Project', if not run:
```
cd FALL25_CS152_Project
```

This application runs on a virtual environment.   
Create a virtual environment:  
```
python3 -m venv venv
```
*Note: Creating a virtual environment only needs to be done the first time the project is set up.*  

Activate the virtual environment:  
```
. venv/bin/activate
```
Install application dependencies and libraries:  
```
pip install -r requirements.txt
```

After installing these dependencies, run:  
```
python3  
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet') 
exit()
```

### How to run this application  
### Step 0a: Check the virtual environment is activated  
If your virtual environment is activated, it should say (venv) in your command line (Go to Step 0b)  
If it's not, activate the virtual environment:  
```
. venv/bin/activate
```

#### Step 0b: Check if Models and Data are initialized
If they are initialized, you will see a the ./Model/generated_content directory with 3 files: trained_models, club_indices.pkl, rso.json  (Go to Step 1)  
If any of these 3 files are missing, delete the generated_content folder (if it exists) 

**IMPORTANT**: This step must be completed before starting the web application!   

Run the main.py script:  
```
python3 main.py
```

This process will:  
- Scrape club information  
- Pre-process the club descriptions  
- Train the Lexical (TF-IDF) and Semantic (Sentence Transformer) models   
- Save all models and matrices to the ./models directory  

#### Step 1: Run the web application  

Run the app.py script:
```
python3 app.py
```

Deactivate virtual environment: 
```
deactivate
```


