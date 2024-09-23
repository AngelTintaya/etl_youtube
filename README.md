# YouTube Comments Extractor

This project extracts comments from a YouTube video given its **Video ID** and stores the data in a CSV file as well as a SQLite database. It uses the YouTube Data API to fetch the comments and stores them in a table for further analysis or processing.

## Features

- Fetches comments from YouTube videos using the YouTube Data API.
- Saves extracted comments in a `youtube.csv` file under the `server_outputs` directory.
- Stores comments data into a SQLite database table for persistent storage.
- Accepts a YouTube video ID via command line arguments.
- Has a default YouTube video ID if none is provided via arguments.

## Requirements

The project relies on the following libraries:

- **pandas==2.2.3**: For handling the CSV file operations and data manipulation.
- **python-dotenv==1.0.1**: For loading environment variables such as the YouTube API key.
- **google-api-python-client==2.146.0**: To interact with the YouTube Data API.
- **SQLAlchemy==2.0.35**: For database interaction and handling SQLite operations.

Make sure you have the correct versions installed, as specified in the `requirements.txt` file.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/AngelTintaya/etl_youtube.git
cd etl_youtube
```

### Step 2: Create a Virtual Environment (Optional)

It's recommended to use a virtual environment to avoid dependency conflicts.

```bash
python -m venv env # Or virtualenv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### Step 3: Install Required Packages

Install the required dependencies listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```

### Step 4: Set up the .env file

You'll need to create a .env file to store your environment variables. The .env file should be in the root directory of the project.

```bash
touch .env
```

Add the following content to the .env file, replacing the placeholders with your actual values:

```makefile
DEVELOPER_KEY=your-developer-key
API_SERVICE_NAME=your-api-service-name
API_VERSION=your-api-version
DB_NAME=your-database-name
```

Make sure to define each variable accordingly:

- **DEVELOPER_KEY**: Your YouTube API developer key.
- **API_SERVICE_NAME**: The name of the API service (usually "youtube").
- **API_VERSION**: The version of the API you are using (usually "v3")
- **DB_NAME**: The name of the SQLite database (e.g., "youtube.db").

### Step 5: Create Required Folders

Create the following folders in the root directory of the project:

```bash
mkdir server_outputs
mkdir database
```

## Usage

To run the project, use the following command:

```bash
python main.py --videoid "3NOJW15_La0"
```

Alternatively, you can run the script without the --videoid argument. If no video ID is provided, the script will use a default YouTube video ID.

## File Structure

```bash
.
├── .env                 # Environment variables (YouTube API Key, DB name, etc.)
├── main.py              # Main script to run the extractor
├── requirements.txt     # Project dependencies
├── server_outputs/      # Folder to store the CSV file with extracted comments
│   └── youtube.csv
└── database/            # Folder to store the CSV file with extracted comments
   └── youtube.db        # SQLite database where comments are stored
```