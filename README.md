# REST API Using Flask

##Steps to create API: 
1. mkdir flask-first-project
2. Create your own virtual env `python -m venv flaskVEnv`
4. pip install Flask

##Steps to run API:
1. Run API
   >(flaskVEnv) flask-first-project>set FLASK_APP=first_api.py
   
   >(flaskVEnv) flask-first-project>flask run
   
    Running on http://127.0.0.1:5000/ Use url to open in browser
   
   To run API in debug mode `set FLASK_DEBUG=1`

2. Add below code in module and run it
    ```
      if __name__ == '__main__':
        app.run()
    ```
   
    ```
    flask-first-project>python -m api_with_run
    ```
 
To run API in debug mode `app.run(debug=True)`   
 