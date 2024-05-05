# Notes application

Welcome to the Notes application web service! This is a Django-based web application designed to create notes.

![image](https://i.imgur.com/PjeRXiO.png)
![image](https://i.imgur.com/4KSK7cp.png)

> You can visit deployed version of the Notes application web service here:
> http://127.0.0.1:8000/


## Getting Started

### Prerequisites

Before you begin, it would be better if you have the following tools and technologies installed:

- Docker

[How to install Docker](https://docs.docker.com/engine/install/)

## Installing / Getting started

> A quick introduction of the setup you need to get run a project.

### Using Git

1. Clone the repo:

```shell
git clone https://github.com/Wonsky1/web-notes.git
```

2. You can open project in IDE and configure .env file using [.envsample](.envsample) file as an example.

<details>
<summary>Parameters for .env file:</summary>
- **SECRET_KEY**: `Your Django SECRET_KEY`
- **DATABASE_URL**: `Your DATABASE_URL`
</details>

3. Download the requirements:
```shell
pip install -r requirements.txt 
```

#### Using Docker:

4. Run Docker compose:
```shell
docker-compose up
```

5. Go to http://localhost:8001

#### Without Docker:


4. Make migrations and migrate:

```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```
5. Load the dumped data (optional):
```shell
python manage.py loaddata db_dump.json
```

6. Run the Django server:
```shell
python manage.py runserver
```

7. Go to http://localhost:8000


## Uncommon solutions / deviations from the task:
- Added favourite functional, which after enabling would make a note with orange "stick":
![image](https://i.imgur.com/M4W2YFz.png)
- Added pinned functional, which after enabling would make a note pined to the top.
- Default sorting: pinned notes -> favourite notes -> most recent notes
- Added description field for a note
- I have chosen not to show tag names inside the note, because it looked worse as for me:
![image](https://i.imgur.com/c520xYn.jpeg)
- I have not created filtering for archived/not archived notes, because as for me, it is worse for users to use it as a filter, so I have made it as another endpoint


## DB Structure

![image](https://i.imgur.com/td5bpr5.png)

## Contributing

Feel free to contribute to these enhancements, and let's make Web Notes Service even better!
