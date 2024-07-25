import requests

def test_frontend_backend_integration():
    frontend_url = "<http://127.0.0.1:65284//>" 
    response = requests.get('http://127.0.0.1:65284/')
    print(response) #frontend connected with backend

    assert response.status_code == 200
    assert "Hello from the Backend!" in response.text  #Checked the response too which is coming from Back End

if __name__ == "__main__":
    test_frontend_backend_integration()
    print("Test passed!")