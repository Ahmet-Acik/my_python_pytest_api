# import requests
# import pytest

# def test_list_users():
#     url = "https://gorest.co.in/public/v2/users"
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": "Bearer ACCESS-TOKEN"
#     }
#     response = requests.get(url, headers=headers)
#     assert response.status_code == 200
#     json_response = response.json()
#     assert isinstance(json_response, list)
    


# def test_create_user():
#     url = "https://gorest.co.in/public/v2/users"
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": "Bearer ACCESS-TOKEN"
#     }
#     data = {
#         "name": "Tenali Ramakrishna",
#         "gender": "male",
#         "email": "tenali.ramakrishna@15ce.com",
#         "status": "active"
#     }
#     response = requests.post(url, headers=headers, json=data)
#     assert response.status_code == 201
#     json_response = response.json()
#     assert json_response["name"] == "Tenali Ramakrishna"
#     assert json_response["email"] == "tenali.ramakrishna@15ce.com"
    


# def test_update_user():
#     user_id = 6942464
#     url = f"https://gorest.co.in/public/v2/users/{user_id}"
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": "Bearer ACCESS-TOKEN"
#     }
#     data = {
#         "name": "Allasani Peddana",
#         "email": "allasani.peddana@15ce.com",
#         "status": "active"
#     }
#     response = requests.patch(url, headers=headers, json=data)
#     assert response.status_code == 200
#     json_response = response.json()
#     assert json_response["name"] == "Allasani Peddana"
#     assert json_response["email"] == "allasani.peddana@15ce.com"


# def test_delete_user():
#     user_id = 6942464
#     url = f"https://gorest.co.in/public/v2/users/{user_id}"
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": "Bearer ACCESS-TOKEN"
#     }
#     response = requests.delete(url, headers=headers)
#     assert response.status_code == 204import requests

# f1c902d4bdaca7158a6e1d549337cc80f2b7da262bf6347379af93b0ee06c4fe

import requests
import pytest
import uuid

@pytest.fixture
def base_url():
    return "https://gorest.co.in/public/v2"

@pytest.fixture
def headers():
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer f1c902d4bdaca7158a6e1d549337cc80f2b7da262bf6347379af93b0ee06c4fe"
    }

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -X GET "https://reqres.in/api/users?page=1&per_page=15"
"""
def test_list_users(base_url, headers):
    params = {"page": 1, "per_page": 20}
    url = f"{base_url}/users"
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, list)  

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -X POST "https://reqres.in/api/users" -d '{"name":"Tenali Ramakrishna", "job":"leader"}'
"""
def test_create_user(base_url, headers):
    url = f"{base_url}/users"
    unique_email = f"tenali.ramakrishna.{uuid.uuid4()}@15ce.com"
    data = {
        "name": "Tenali Ramakrishna",
        "gender": "male",
        "email": unique_email,
        "status": "active"
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.content)  # Debugging line to print the response content
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["name"] == "Tenali Ramakrishna"
    assert json_response["email"] == unique_email

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -X PUT "https://reqres.in/api/users/2" -d '{"name":"Allasani Peddana", "job":"zion resident"}'
"""
def test_update_user(base_url, headers):
    # First, create a user to update
    create_url = f"{base_url}/users"
    unique_email = f"allasani.peddana.{uuid.uuid4()}@15ce.com"
    create_data = {
        "name": "Allasani Peddana",
        "gender": "male",
        "email": unique_email,
        "status": "active"
    }
    create_response = requests.post(create_url, headers=headers, json=create_data)
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    # Now, update the created user
    update_url = f"{base_url}/users/{user_id}"
    update_data = {
        "name": "Allasani Peddana Updated",
        "email": unique_email,
        "status": "active"
    }
    update_response = requests.patch(update_url, headers=headers, json=update_data)
    print(update_response.content)  # Debugging line to print the response content
    assert update_response.status_code == 200
    json_response = update_response.json()
    assert json_response["name"] == "Allasani Peddana Updated"
    assert json_response["email"] == unique_email

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -H "Authorization: Bearer ACCESS-TOKEN" -X DELETE "https://reqres.in/api/users/2"
"""
def test_delete_user(base_url, headers):
    # First, create a user to delete
    create_url = f"{base_url}/users"
    unique_email = f"delete.user.{uuid.uuid4()}@15ce.com"
    create_data = {
        "name": "Delete User",
        "gender": "male",
        "email": unique_email,
        "status": "active"
    }
    create_response = requests.post(create_url, headers=headers, json=create_data)
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    # Now, delete the created user
    delete_url = f"{base_url}/users/{user_id}"
    delete_response = requests.delete(delete_url, headers=headers)
    assert delete_response.status_code == 204
    

# Unhappy path tests

def test_create_user_invalid_data(base_url, headers):
    url = f"{base_url}/users"
    invalid_data = [
        {"name": "", "gender": "male", "email": "qatest@test.com", "status": "active"},  # Missing name
        {"name": "Gino Paloma", "gender": "", "email": "qatest@test.com", "status": "active"},  # Missing gender
        {"name": "Gino Paloma", "gender": "male", "email": "", "status": "active"},  # Missing email
        {"name": "Gino Paloma", "gender": "male", "email": "qatest@test.com", "status": ""},  # Missing status
        {"name": "Gino Paloma", "gender": "male", "email": "invalid-email", "status": "active"}  # Invalid email
    ]
    expected_errors = [
        {"field": "name", "message": "can't be blank"},
        {"field": "gender", "message": "can't be blank, can be male of female"},
        {"field": "email", "message": "can't be blank"},
        {"field": "status", "message": "can't be blank"},
        {"field": "email", "message": "is invalid"}
    ]
    
    for data, expected_error in zip(invalid_data, expected_errors):
        response = requests.post(url, headers=headers, json=data)
        assert response.status_code == 422
        json_response = response.json()
        assert isinstance(json_response, list)
        assert any(error["field"] == expected_error["field"] and error["message"] == expected_error["message"] for error in json_response)

def test_create_user_duplicate_email(base_url, headers):
    url = f"{base_url}/users"
    unique_email = f"duplicate.user.{uuid.uuid4()}@15ce.com"
    data = {
        "name": "Duplicate User",
        "gender": "male",
        "email": unique_email,
        "status": "active"
    }
    # Create the user for the first time
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201

    # Try to create the user again with the same email
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 422
    json_response = response.json()
    assert isinstance(json_response, list)
    assert any(error["field"] == "email" and error["message"] == "has already been taken" for error in json_response)

def test_create_user_no_token(base_url):
    url = f"{base_url}/users"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "name": "No Token User",
        "gender": "male",
        "email": f"no.token.user.{uuid.uuid4()}@15ce.com",
        "status": "active"
    }
    response = requests.post(url, headers=headers, json=data, )
    assert response.status_code == 401
    json_response = response.json()
    assert "message" in json_response
    assert json_response["message"] == "Authentication failed"

def test_create_user_invalid_token(base_url):
    url = f"{base_url}/users"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer INVALID-TOKEN"
    }
    data = {
        "name": "Invalid Token User",
        "gender": "male",
        "email": f"invalid.token.user.{uuid.uuid4()}@15ce.com",
        "status": "active"
    }
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 401
    json_response = response.json()
    assert "message" in json_response
    assert json_response["message"] == "Invalid token"