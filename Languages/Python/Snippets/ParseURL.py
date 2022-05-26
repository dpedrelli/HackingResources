from urllib.parse import urlparse

parsed = urlparse("www.microsoft.com")

"""
| Attribute | Index                              | Value                 | Value if not present   |
|-----------|------------------------------------|-----------------------|------------------------|
| scheme    | 0                                  | URL scheme specifier  | scheme parameter       |
| netloc    | 1                                  | Network location part | empty string           |
| path      | 2                                  | Hierarchical path     | empty string           |
| params    | 3                                  | No longer used        | always an empty string |
| query     | 4                                  | Query component       | empty string           |
| fragment  | 5                                  | Fragment identifier   | empty string           |
| username  | User name                          | None                  |
| password  | Password                           | None                  |
| hostname  | Host name (lower case)             | None                  |
| port      | Port number as integer,
if present | None                  |
"""