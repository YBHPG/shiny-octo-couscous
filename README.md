# shiny-octo-couscous

### The subject
That is a repository for a course project in **_"Infosystems Development"_** stydy. The subject of the project is to develop a web app that can contact a remote database server. It should be using _Flask_ Python module to manage the backend work.

### Content
The project should provide the following fuctionality in the web browser:
* User authorization;
* Work with SQL queries providing user data;
* Editing of tables (insert & delete functions);
* Product cart that provides client with a buying functionality.

### User authorization
User authorization works with a 'users' table from MySQL database. The module receives 'group_name' names from the table and checks if the login and password from session correlate with any string from an SQL server return.

> Snippet 1 (getting data from site)
```python
login = request.form.get('login')
password = request.form.get('password')
```

> Snippet 2 (checking the data from site for correlation with database)
```python
sql = provider.get('user.sql', login=login, password=password)
result = work_with_db(current_app.config['DB_CONFIG'], sql)

if len(result) > 0:
    session['group_name'] = result[0]['group_name']
    return render_template('success.html')
```

# To be continued -> ...
