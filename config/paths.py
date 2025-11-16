import os

#PATH NAMES
BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GENERATED_CONTENT_PATH = os.path.join(BASE_DIRECTORY, "generated_content")
GENERATED_CONTENT_CLUB_PATH = os.path.join(GENERATED_CONTENT_PATH, "rso.json")
GENERATED_CONTENT_FORM_PATH = os.path.join(GENERATED_CONTENT_PATH, "responses.json")

SCRIPTS_PATH = os.path.join(BASE_DIRECTORY, "scripts")

                            