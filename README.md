# Setup Instructions
1. Clone the repository.
2. In your terminal, cd into the repository folder.
3. Create the virtual environment with `python -m venv env`
4. Activate the env with:
    - Windows (PowerShell/CMD): `env\Scripts\activate`
    - Windows (Git Bash): `source env/Scripts/activate`
    - macOS/Linux: `source env/bin/activate`
5. Install Django with `pip install -r requirements.txt`. This requires Python 3.12 or newer.
6. Get to the Django project folder with `cd product_info`
7. Run the server with `python manage.py runserver`
8. Open `localhost:8000/catalog/` on your browser.

# Design Decisions
- The search bar searches within product descriptions, not titles.
- The categories filter is an OR filter. A product passes if its category matches any of the selected options.
- The tags filter is an AND filter. A product passes only if it contains all the selected tags.
- The username for `admin/` is `jacob`. The password can be found in the notes for this submission.
- The product, category, and tag data is stored in `db.sqlite3`
- Unit tests are in `catalog/tests.py`. They can be run with `python manage.py test` from `product_info/`.

# AI Usage
- AI was used to write the product names and descriptions, to help me brainstorm before any code was written, and to review the final result, but no code was taken directly from AI.
- I wrote and reviewed every piece of code.