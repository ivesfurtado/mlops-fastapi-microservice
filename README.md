# FastAPI MLOps Project

This repository showcases how to integrate **FastAPI**, **Docker**, and **Poetry** to build a production-ready Machine Learning Operations (MLOps) project. The project is designed to deploy machine learning models via a FastAPI microservice and automate the deployment process using GitHub Actions for a seamless CI/CD pipeline, deploying the containerized app to AWS EC2.

This project is based on the tutorial provided by [The Halftime Code](https://www.thehalftimecode.com/fastapi-for-mlops-integrate-docker-poetry-and-deploy-to-aws-ec2/), which walks through the entire process from project setup to deployment on AWS.

## Project Features

- **FastAPI**: A high-performance web framework for serving machine learning models.
- **Poetry**: Manages Python dependencies and virtual environments.
- **Docker**: Containerizes the application for flexible deployment.
- **AWS EC2**: Deployment platform using GitHub Actions for CI/CD.
- **GitHub Actions**: Automates testing, building, and deploying the model to AWS EC2.

## Project Structure

```plaintext
mlops/
├── .github/               # GitHub Actions workflows
│   └── workflows/
│       └── deploy.yml     # CI/CD pipeline
├── src/                   # Source code
│   ├── api/               # API routes
│   │   └── v1/
│   │       └── routes.py  # Prediction endpoint
│   ├── core/              # Core app setup
│   │   └── config.py      # Configuration management
│   └── app/               # Business logic
│       └── services/      # Model service logic
├── tests/                 # Unit tests
│   ├── test_api.py        # Test API endpoints
│   └── test_services.py   # Test business logic
├── models/                # Pre-trained machine learning model
│   └── model.pkl
├── Dockerfile             # Docker configuration
├── docker-compose.yaml    # Docker Compose setup
├── pyproject.toml         # Poetry configuration
└── README.md              # Documentation
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mlops-fastapi.git
cd mlops-fastapi
```

### 2. Install Dependencies

Ensure you have Poetry installed:

```bash
pip install poetry
```

Then, install the project dependencies:

```bash
poetry install
```

### 3. Train and Save the Model

Train a sample machine learning model (RandomForest on Iris dataset) and save it to the `models` directory:

```bash
poetry run python -m train_model
```

### 4. Run the FastAPI Application

Start the FastAPI server locally:

```bash
poetry run uvicorn src.core.server:app --reload
```

Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 5. Test the API

You can test the prediction endpoint using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/predict" \
-H "Content-Type: application/json" \
-d '{"features": {"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}}'
```

### 6. Run Tests

Run the unit tests with:

```bash
poetry run python -m pytest tests/
```

### 7. Dockerize the Application

To build and run the Docker container:

```bash
docker build -t mlops-fastapi .
docker run -p 8000:8000 mlops-fastapi
```

### 8. CI/CD Pipeline

The GitHub Actions CI/CD pipeline automates deployment to AWS EC2. Ensure you configure the necessary GitHub secrets for `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `EC2_SSH_KEY`, and `DOCKER_PASSWORD`.

## Deployment to AWS EC2

Follow the [tutorial](https://www.thehalftimecode.com/fastapi-for-mlops-integrate-docker-poetry-and-deploy-to-aws-ec2/) for detailed instructions on setting up AWS EC2 and automating deployment via GitHub Actions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## References

- Tutorial: [FastAPI for MLOps: Integrate Docker, Poetry, and Deploy to AWS EC2](https://www.thehalftimecode.com/fastapi-for-mlops-integrate-docker-poetry-and-deploy-to-aws-ec2/)
