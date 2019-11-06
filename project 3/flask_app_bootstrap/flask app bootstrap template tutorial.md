Flask App Bootstrap Template Tutorial
Jocelyn Lau
11/6/2019


1. [Original HTML flask app](https://github.com/jocelynlau/metis-projects-2-5/tree/master/project%203/flask_app)

2. [Startbootstrap.com](https://startbootstrap.com/)
- Choose and download a template file

3. [Boostrapped flask app](https://github.com/jocelynlau/metis-projects-2-5/tree/master/project%203/flask_app_bootstrap)

- Set up folder structure (VERY IMPORTANT):
    - initiator_app.py
    - index.html
    - templates (html templates)
        - predictor.html
        - calculator.html
    - static
        - all other bootstrap files

- Update bootstrap files accordingly
    - HTML files:
        - Make copies of the html templates and insert your basic HTML code in there
        - Update file paths
        - Change the bootstrap template file paths referenced in the HTML code to add 'static'
    - predictor_app.py
        - Add template and/or static folders to flask initiation
        - Update file paths