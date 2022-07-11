# Flask-SQLRESTful_API
This is a Simple Flask API that connects to a sqlite3 Database and is used to perform 4 operations: GET, POST, DELETE and PUT <br>
The <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/test.py">test.py</a> file is used to create dummy tables to check if the sqlite3 commands are working or not.
<br>

In the <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/tree/main/code"><b>code</b></a> folder:
- <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/code/create_tables.py">create_tables.py</a> file is used to create the <i>users</i> and the <i>items</i> table.
- <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/code/data.db">data.db</a> is the Database file that contains the two tables mentioned.
- <b>class Item</b> has been moved to the new <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/code/item.py">item.py</a> <i>(Previously in <b>app.py</b>)</i>
- <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/code/app.py">app.py</a>, <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/code/security.py">security.py</a> & <a href="https://github.com/n-rohit/Flask-SQLRESTful_API/blob/main/code/user.py">user.py</a> are the files where most of the code remains the same as the <b>AdvancedRESTful_API</b> code.

<i>This is an improved version of the <a href="https://github.com/n-rohit/Flask-AdvancedRESTful_API">Flask-AdvancedRESTful_API</a> Code.</i>
