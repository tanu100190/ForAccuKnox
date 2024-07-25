# Kubernetes Deployment and Automated Testing

## Prerequisites
- Docker
- Minikube
- kubectl
- Python
- requests library (`pip install requests`)

## Setup

1. Start Minikube:
    
    minikube start
   

2. Deploy the backend and frontend services:
    
    kubectl apply -f backend-deployment.yaml
    kubectl apply -f frontend-deployment.yaml
  

3. Get the URL for the frontend service:
    
    minikube service frontend-service

4. Open the url : http://127.0.0.1:65284/
   Hello from the Backend! is printed on the body of the page.

## Automated Testing

1. Install the `requests` library:
    
    pip install requests
   

2. Run the test script:
   
    python test_integration.py
    

## Repository Structure files used:
1. backend-deployment.yaml
2. frontend-deployment.yaml
3. test_integration.py
4. README.md
5. 
