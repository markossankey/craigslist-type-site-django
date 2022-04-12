# **Before starting, make sure you have the most recent version of python and postgres installed**

## Setting up the virutal environment
1. Fork to your github and clone down with `$ git clone "url"`
2. Create a virtual environment with `$ python3 -m venv .venv`
  (can replace .venv with whatever you want the name to be, but replace it in the next step aswell)
3. `$ source .venv/bin/activate`
4. `$ pip install -r requirements.txt`
5. if psycopg2 doesn't install, just run `pip install psycopg2`

## Setting up postgres database
1. Start postgres in new terminal with `postgres`
2. In another new window, run `createdb markos_list`

## Connecting Django Project and Postgres database
1. Back in the first terminal, verify you are in the the 'assessment-4' folder and still running your virtual environment
  (it should say the virtual environment name before the command line in your terminal (.venv if you followed exact steps))
2. Run `$ python3 manage.py makemigrations`
  (should say something like 'no changes')
3. To load fixture data into db -- `$ python3 manage.py migrate`
  (should print in the terminal 'Applying ......' about 20 times, followed by 'OK' on each line)
4. To load records -- `$ python3 manage.py loaddata data.json`
5. Finally, run `$ python3 manage.py runserver` and verify that there are no errors, to quickly pull up webpage, control click 'http://...'

## When you are done
1. On the terminal running postgres, do the same and you can close that terminal window
2. On the terminal running the django server, hit cmd+C to quit it
3. `$ deactivate` to exit virtual environment
4. `cd ..``
5. `rm -rf assessment-4`

### Considerations
- In addition to categories and posts, I added subcategories. Due to this, my urls will contain 'subcategory/(number)' between 'category/(number)' and 'post'
- Used a script and excel to generate posts, so they're are pretty generic. I added the category and subcategory along with id for verification that everything was working correctly
- To create a subcategory, go to category page and there will be an input that says "Add subcategory".  There is currently no functionality to delete subcategories, as it was a lower priority since subcategories weren't required

