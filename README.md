# <h3> Description: </h3>
<p> 
  The project has multiple routes, each serving distinct purposes.
  <li> <b> <i> '/': </i> </b> Home page where you can enter the products that you want to track. </li>
  <li> <b> <i> '/results': </i> </b> Scrapes the first 5 products that is relevant to the search that the user typed and stores the product details in the database. </li> 
  <li> <b> <i> '/details/id:name' </b> </i> Provides all the details of a particular product </li>
  <br/><br/>
  The data is collected and inserted to the database whenever the search is performed.
</p>
<img src="https://github.com/Chandrahas-B/Amazon-price-tracker/assets/84665480/bbbef318-894d-451b-bb79-dc721622acc5" width= 800px height= 300px  style='float:right;' />
<img src="https://github.com/Chandrahas-B/Amazon-price-tracker/assets/84665480/b95a481d-59aa-426c-8de1-42cfaf054459" width= 800px height= 300px  style='float:left;'/>


# <h2> To run the application: </h2>

-- Using Docker compose:
```
docker compose up
```

-- Using pip:
```
pip install -r requirements.txt
```
Note:
<li> For this approach, make sure postgres is installed on the system locally. </li>
<li> Create a .env file in the folder and add the following lines: <br/></li>

```
DBNAME = <DBNAME_TO_USE>
DB_HOSTNAME = <HOST_NAME>
DB_USERNAME = <USERNAME>
DB_PASSWORD = <PASSWORD>
DB_PORT = <PORT>
```
Example:
```
DBNAME = 'postgres'
DB_HOSTNAME = 'localhost'
DB_USERNAME = 'postgres'
DB_PASSWORD = 'password'
DB_PORT = 5432
```
Once 'postgres' and '.env' is installed and created:
```
python main.py
```
