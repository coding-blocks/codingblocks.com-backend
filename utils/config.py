from decouple import config

class Config:

  PUBLIC_URL=config('PUBLIC_URL', default='http://localhost:3000')

  ONEAUTH_URL=config('ONEAUTH_URL', default='https://account.codingblocks.com')
  ONEAUTH_CLIENT_ID=config('ONEAUTH_CLIENT_ID', default='2387689957')
  ONEAUTH_CLIENT_SECRET=config('ONEAUTH_CLIENT_SECRET', default='S3xu7DdHj3R4IESHLER0mWULDGc1vCaSnfATZrRDTSzeMR8zeMBsIq7E9CyljzX3')
  ONEAUTH_REDIRECT_URI=config('ONEAUTH_REDIRECT_URI', default='https://test.codingblocks.com/events/callback')
