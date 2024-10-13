# registration/tests/test_registration.py
import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_registration_view(client):
    url = reverse('register')
    # AAA Approach { arrange - action - assert }
    
    # Simulate a POST request with valid data
    response = client.post(url, {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    })

    # Check that the response redirects after successful registration
    assert response.status_code == 302
    
    # Ensure the user was created in the database
    user = User.objects.get(username='testuser')
    assert user is not None
    
    # Assert the password is correctly set
    assert user.check_password('password1234')

# @pytest.mark.django_db
# def test_registration_password_mismatch(client):
#     url = reverse('register')

#     # Simulate a POST request with mismatched passwords
#     response = client.post(url, {
#         'username': 'testuser',
#         'email': 'testuser@example.com',
#         'password': 'password123',
#         'confirm_password': 'password124'  # Different passwords
#     })

#     # Check that the form is invalid and re-rendered
#     assert response.status_code == 200
#     assert "Passwords do not match." in response.content.decode()
