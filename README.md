# gsuite

[![Build Status](https://travis-ci.org/marcosvidolin/gsuitefy.svg?branch=master)](https://travis-ci.org/marcosvidolin/gsuitefy) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ff1fcd33e0c0461f8aac31250b64b9ac)](https://www.codacy.com/manual/marcosvidolin/gsuitefy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marcosvidolin/gsuitefy&amp;utm_campaign=Badge_Grade)

Gsuite Admin client to manage users and groups

## How to use

Install:

```shell
pip install gsuitefy
```

Import:

```python
from gsuitefy.gsuite import GSuiteAdmin
```

Sample:
```python
# User with gsuite manager rights
MANAGER_USER_MAIL = 'group-manager@bar.com'
# The scopes
SCOPES = ['https://www.googleapis.com/auth/admin.directory.group'
        , 'https://www.googleapis.com/auth/admin.directory.group.member']
# Email of the Service Account
SERVICE_ACCOUNT_EMAIL = 'sa@bar.iam.gserviceaccount.com'
# Path to the service account JSON file
SERVICE_ACCOUNT_FILE_PATH = os.path.join(os.path.dirname(__file__), 'service-account.json')

gsuite = GSuiteAdmin(group_management_email=MANAGER_USER_MAIL,
    service_account=SERVICE_ACCOUNT_FILE_PATH,
    service_account_email=SERVICE_ACCOUNT_EMAIL,
    scopes=SCOPES)

gsuite.add_member_to_group(member='foo@bar.com', groupKey='foo-group@bar.com')
```

## Development

Install all the project's dependencies

```shell
pip install -r requirements.txt
```

## Contributors

[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/0)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/0)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/1)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/1)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/2)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/2)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/3)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/3)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/4)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/4)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/5)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/5)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/6)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/6)[![](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/images/7)](https://sourcerer.io/fame/marcosvidolin/marcosvidolin/gsuitefy/links/7)
