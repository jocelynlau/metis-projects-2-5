Flask App Bootstrap Template Tutorial
Jocelyn Lau
11/6/2019


1. [Original HTML flask app](https://github.com/jocelynlau/metis-projects-2-5/tree/master/project%203/flask_app)

2. [Startbootstrap.com](https://startbootstrap.com/)
- Choose and download a template file

3. Set up folder structure:
- initiator_app.py
- index.html
- templates
    - predictor.html
    - calculator.html
- static
    - all other bootstrap files

4. [Boostrapped flask app](
Update bootstrap files accordingly
- HTML files:
    - Use the templates and insert your basic HTML code in there
    - Update file paths
    - Change the bootstrap template file paths referenced in the HTML code to add 'static'
- predictor_app.py
    - Add template and/or static folders to flask initiation
    - Update file paths


Windows:
- Finder to template download
- Finder to original flask app
- Finder to bootstrapped flask app
- local browser path
- Bootstrap template
    - index.html
    - blank_page.html
- Original HTML and python files
- Updated HTML and python files

Command line:
- conda activate metis
- cd /Users/Jocelyn/Metis/metis-projects-2-5/project\ 3/flask_app 
- python3 predictor_app.py

- cd /Users/Jocelyn/Metis/metis-projects-2-5/project\ 3/flask_app_bootstrap 
- python3 predictor_app.py
