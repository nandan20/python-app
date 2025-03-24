**CI/CD Pipeline with GitHub Actions, ArgoCD, and Blue-Green Deployment on Minikube**

**Overview**
This project demonstrates a CI/CD pipeline using GitHub Actions for a Flask-based microservice. The pipeline automates the build, test, lint, and deployment process. The application is deployed on Minikube using ArgoCD with a blue-green deployment strategy.

**Project Features**
GitHub Actions Workflow:
Build Job: Builds and pushes a Docker image to Docker Hub.
Lint Job: Lints Python code using flake8.
Test Job: Runs unit tests with pytest.
SonarCloud Integration: Analyzes code quality.
Deployment Job: Deploys the application to Minikube via ArgoCD.
ArgoCD for Continuous Deployment.
Blue-Green Deployment Strategy for rolling updates without downtime.
Minikube Dashboard for managing Kubernetes resources.
NGROK for external access to the application.

**Project Directory Structure**
├── .github/workflows/ci-cd-pipeline.yml   # GitHub Actions pipeline
├── app/
│   ├── requirements.txt                    # Python dependencies
│   ├── server.py                            # Flask application
│   ├── test_app.py                          # Unit tests
├── k8s/
│   ├── deployment.yaml                      # Kubernetes Deployment (Blue-Green)
│   ├── service.yaml                         # Kubernetes Service
├── Dockerfile                               # Docker container setup
└── README.md                                # Documentation

1. Prerequisites
Ensure the following are installed:
Docker
Minikube
kubectl
ArgoCD
GitHub Secrets
NGROK

GitHub Secrets Required
Secret Name	                Description
DOCKER_USERNAME	        Docker Hub username
DOCKER_PASSWORD     	Docker Hub password
SONAR_ORG	            SonarCloud organization key
SONAR_PROJECT	        SonarCloud project key
SONAR_TOKEN	            SonarCloud authentication token
ARGOCD_USERNAME	        ArgoCD login username
ARGOCD_PASSWORD	        ArgoCD login password

2. Setting Up Minikube
Start Minikube:
`minikube start`

Enable the Kubernetes dashboard:
`minikube dashboard`

3. Running ArgoCD on Minikube
Install ArgoCD
`kubectl create namespace argocd`
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

Expose ArgoCD
`kubectl port-forward svc/argocd-server -n argocd 8443:443`

Access ArgoCD UI at:
👉 https://localhost:8443

Login to ArgoCD
`argocd login localhost:8443 --username=admin --password=<ARGOCD_PASSWORD> --insecure`

4. CI/CD Pipeline Workflow
The GitHub Actions workflow is defined in .github/workflows/ci-cd-pipeline.yml. It consists of the following stages:
1️⃣ Build and Push Docker Image
Uses Docker Buildx for multi-platform builds.

Pushes the Docker image to Docker Hub.

2️⃣ Lint Python Code
Uses flake8 to enforce coding standards.

3️⃣ Run Unit Tests
Uses pytest to execute test cases.

4️⃣ Code Quality Analysis
Scans the repository using SonarCloud.

5️⃣ Deployment to Kubernetes
Updates the k8s/deployment.yaml file with the new Docker image tag.

Pushes changes to GitHub, triggering ArgoCD to sync the deployment.

5. Blue-Green Deployment
The k8s/deployment.yaml defines two separate deployments:
my-app-blue
my-app-green
By modifying k8s/service.yaml, we can switch traffic between versions:
`selector:
  app: my-app
  version: green  # Switch to 'blue' when needed`

To apply changes:
`kubectl apply -f k8s/deployment.yaml`
`kubectl apply -f k8s/service.yaml`

`kubectl get pods`

6. Accessing the Application
To expose the Flask application externally:
    Forward service using Minikube
    `kubectl port-forward svc/my-app-service 8080:80`

    Using NGROK
    ngrok http 8080
    Copy the NGROK URL and access the application in a browser.

7. Monitoring in Minikube Dashboard
    `minikube dashboard`

8. Testing the Pipeline
Trigger a CI/CD Workflow
Push any change to the main branch:
`git add .`
`git commit -m "Trigger CI/CD Pipeline"`
`git push origin main`

Verify the GitHub Actions pipeline at GitHub → Actions tab.
Monitor deployment updates in ArgoCD UI.

Conclusion
This project successfully demonstrates a CI/CD pipeline with GitHub Actions, ArgoCD, and Blue-Green Deployment on Minikube. The pipeline automates testing, linting, code analysis, and deployment, ensuring a smooth DevOps workflow.


