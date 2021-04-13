import requests
from urllib.parse import urljoin

class OneauthService:
  _url: str
  _client_id: str
  _client_secret: str
  _redirect_uri: str

  def __init__(self, url: str, client_id: str, client_secret: str, redirect_uri: str):
    self._url = url
    self._client_id = client_id
    self._client_secret = client_secret
    self._redirect_uri = redirect_uri

  def exchange_grant_with_user(self, grant_code: str):
    payload = {
      "client_id" : self._client_id,
      "redirect_uri" : self._redirect_uri,
      "client_secret" : self._client_secret,
      "grant_type" : "authorization_code",
      "code"  : grant_code
    }
    response = requests.post(urljoin(self._url, 'oauth/token'), data=payload).json()
    access_token = response['access_token']
    headers = {
      "Authorization": f"Bearer {access_token}"
    }
    user = requests.get(urljoin(self._url, 'api/users/me'), headers=headers)

    return user

def get_oneauth_service() -> OneauthService:
  return OneauthService(
    url="https://account.codingblocks.com",
    client_id=2387689957,
    client_secret="S3xu7DdHj3R4IESHLER0mWULDGc1vCaSnfATZrRDTSzeMR8zeMBsIq7E9CyljzX3",
    redirect_uri="https://test.codingblocks.com/events/callback"
  )
