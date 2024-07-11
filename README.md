# Hello Patient Chatbot

This project consists of a FastAPI backend and a Next.js frontend for a chatbot application.

## Running the Application

### Required Software

1. Python
2. Node.js (version >= 18.17.0)
3. Docker and Docker Compose
4. [Poetry](https://python-poetry.org/docs/#installation)
5. Postgres libpq header files (e.g. `apt install libpq-dev` on Ubuntu, `brew install postgresql` on macOS)

### First-Time Setup

1. **Install Backend Dependencies**:
   `cd` into the `backend` directory and run `poetry install` to install the Python dependencies.

   ```sh
   cd backend
   poetry install
   ```

2. **Install Frontend Dependencies**:
   `cd` into the `frontend` directory and run `npm install` to install the Node.js dependencies.

```sh
   cd frontend
   npm install
```

### Running the Application

1. **Build and Start the Docker Containers**:
   From the root directory, run `docker-compose up --build` to build and start the Docker Containers for the banckend and frontend.

2. **Access the Application**:
   - The FastAPI backend will be available at `http://localhost:8000`
   - The Next.Js frontend will be available at `http://localhost:3000`
