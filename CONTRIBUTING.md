# Guidelines

## Issues
Use project-board to handle issues status.
We also will create issues for discussions on things that will affect our app, like DB models, what linter we will use or is we should upload our app to AWS or other cloud.


## PRs and branches
- On the PR's description, start with mentioned the issue. Use '#' and just choose the right issue or fill the issue's id.
- The name of the new branch might start with #issueid#desciprtion_of_branch, so we will have one branch per issue. 
For example: 153_creating_login_page



## Testing
In order to use automatic tests, we will store all our tests on `/tests` folder. 

We should call our test files with "test" before the description, like `test_whatYouWantToTest.py`. 
Also the functions inside the test files should be called with "test" before the description, like `test_testFunctionName()`. That way `pytest` would know what files and function is our tests.

To test out our tests, we should connect into the Box, `vagrant ssh`, go to the vagrant folder, `cd /vagrant` and then call `python3 -m pytest` to run the tests.


## General Guidelines
### linter and coding style
We will follow a set of coding style rules and use linter to keep the order.
We will use both flake8 and pylint.


### routes and controllers
We need to keep routes short, in intent to follow rest-api rules.
To keep the backend synchronized with the frontend, we need to talk one language.
GET routes will always return templates(using render_template function) and POST routes always return a JSON.
That way GET routes its for representing a view to the user, and POST routes its for getting data from the backend.


### MVC design
**Models** - we will add new models into 'tutor/models folder, one file for a model. We must do `vagrant halt` and then `vagrant up --provision` to keep the migrations synchronized.

**Views** - we will add new views into 'tutor/templates' folder, one file for a view. We will use a layout, `templates/base.html` as a base for all our templates. 

**Controllers** - we will add controllers into 'tutor/controllers' folder, one file for a controller. When helper controllers are needed, write them on the specific controller. Keep controllers short and doing one thing, use helper functions to achieve that.

**Routing** - we will add new routes into 'tutor/routes' folder, one file for a route. After that, we need to import the route on `run.py` file, using `from tutor.routes mport %YOUR_ROUTE_FILE_NAME%`.

**Migrations** - we use migration when we want to change something on DB. Try to avoid changing it directly, and always use migration for such things. 

To use migrations, we first need to create one by connecting to the Box, using `vagrant ssh`. Then we need to be on the app folder, using `cd /vagrant` to apply the commands easier.

Now we can use `flask-migrate` commands to create a new migration. Use `python3 run.py db revision --message %SHORT_DESCRIPTION_OF_WHAT_YOU_WANT_TO_DO%`. The description should be short, so use one migration for one purpose. Also the separators should be `-` or `_` (on both cases the command will make it `_` on the filename).

Then you need edit your new migration, that would be on `/migrations/versions` folder. Once you save your changes and complete to configure your migration, you should call `flask run.py db migrate` and `flask run.py db upgrade` on the Box to apply the migration changes. You can also use `vagrant up --provision` again (after `vagrant halt` of course).

### Adding new dependencies
We are using `pipenv` to handle packages.
To add a new package:
1. Start up the machine
2. SSH into the machine using `vagrant ssh`
3. Change into the project's directory - `cd /vagrant/`
4. Start up the virtual environment - `pipenv shell`
5. Install the new library - `pipenv install %LIBRARY%`
The Pipfile and Pipfile.lock are updated automatically.
