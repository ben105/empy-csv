import botocore
import boto3

from datetime import datetime
from jose import jwt
from typing import Dict
from pycognito import Cognito


CLIENT_ID = '4qte47jbstod8apnfic0bunmrq'
USER_POOL = 'us-east-2_ghlOXVLi1'


class Auth:
    """Authenticate with Emporia's AWS Cognito Service."""
    def __init__(self, username: str, password: str):
        self.client = boto3.client(
            'cognito-idp', 
            region_name='us-east-2', 
            config=botocore.client.Config(signature_version=botocore.UNSIGNED)
        )

        self.cognito = Cognito(USER_POOL, CLIENT_ID,
            user_pool_region='us-east-2', username=username)
        self.cognito.authenticate(password=password)

        self.tokens = self.refresh_tokens()

    def refresh_tokens(self) -> Dict[str, str]:
        """Refresh and return new tokens."""
        self.cognito.renew_access_token()
        return self._extract_tokens_from_cognito()

    def get_id_token(self):
        """Retrieve the ID token used for Emporia authentication."""
        now = datetime.now()
        dec_access_token = jwt.get_unverified_claims(self.tokens['access_token'])
        if now > datetime.fromtimestamp(dec_access_token["exp"]):
            self.tokens = self.refresh_tokens()
        return self.tokens['id_token']

    def _extract_tokens_from_cognito(self) -> Dict[str, str]:
        return {
            'access_token': self.cognito.access_token,
            
            # Emporia uses this token for authentication
            'id_token': self.cognito.id_token,
            
            'refresh_token': self.cognito.refresh_token,
            'token_type': self.cognito.token_type
        }
