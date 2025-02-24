from __future__ import print_function
import time
import brevo_python
from brevo_python.rest import ApiException
from pprint import pprint
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from starlette.config import Config

config = Config(".env")

configuration = brevo_python.Configuration()
configuration.api_key['api-key'] = config("BREVO_API_KEY")

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

