# API with Registration System using Flask and SQL Database

This repository contains a Flask-based API that fetches data from a JSON file. In order to access the API and obtain the necessary API key, users are required to register on a Flask website. The registration details are stored in an SQL database, allowing users to log in again in the future.

## Getting Started

To run this API and registration website locally, follow these steps:

1. Clone the repository to your local machine.

```bash
git clone https://github.com/masanbasa3k/Python_Flask_API.git
cd your-repo
```

2. Install the required dependencies using `pip`.

```bash
pip install -r requirements.txt
```

3. Configure the SQL Database

   - Make sure you have an SQL database server installed and running.
   - Update the database connection details in `config.py` to match your database settings.

4. Set Up the JSON File

   - Place your JSON data in `data.json` that you want to expose via the API.

5. Run the Application

```bash
python main.py
```

6. Access the Registration Website

   - Open your web browser and go to `http://127.0.0.1:5000`.
   - Register an account to obtain your API key.

7. Access the API

   - Now that you have an API key, you can use it to make requests to the API.
   - Include the API key as a header in your requests: `Authorization: API_KEY`.

## API Endpoints

The following endpoints are available:

- `GET /api/data`: Fetches data from the JSON file.
- `POST /api/data`: Adds new data to the JSON file. *(Requires valid API key)*
- `PUT /api/data/{id}`: Updates existing data in the JSON file. *(Requires valid API key)*
- `DELETE /api/data/{id}`: Deletes data from the JSON file. *(Requires valid API key)*

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes and push them to your fork.

```bash
git commit -m "Your commit message"
git push origin feature/your-feature-name
```

4. Create a pull request from your fork's branch to the main repository's `main` branch.

5. Wait for review and approval from the maintainers.


Feel free to customize this README according to your repository's specifics. Make sure to provide clear instructions, necessary setup details, and any additional information that users might find helpful. Good luck with your project!
