import json
import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def test_new():
    driver_path = os.path.abspath("/Users/kate/Downloads/chromedriver-mac-x64/chromedriver")

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://qahw.kandji.io")

    print(os.getcwd())

    # === Ключ localStorage, который использует твое приложение ===
    local_storage_key = "@@auth0spajs@@::83CtokwL7xEpJ7xz9VojvfpkZvGQcZMf::http://xxx.kandji.io/app/v1/::openid profile email offline_access"

    with open("session/local_storage.json", "r") as f:
        local_storage_value = json.load(f)
    value_str = json.dumps(local_storage_value)
    driver.execute_script(f"localStorage.setItem('{local_storage_key}', {value_str});")

    # with open("session/cookies.json", "r") as f:
    #     cookies = json.load(f)
    # for cookie in cookies:
    #     if "sameSite" in cookie and cookie["sameSite"] == "None":
    #         cookie["sameSite"] = "Strict"
    #     driver.add_cookie(cookie)

    driver.refresh()
    driver.get('https://qahw.kandji.io/devices')
    time.sleep(64)

# def test_new2():
#
#     access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhqZ2RlX2NMUUVqNk5tYmYtMGt1RyJ9.eyJodHRwOi8veHh4LmthbmRqaS5pby9hcHAvdjEvY2xhaW1zL2VtYWlsIjoiZWthdGVyaW4ubGlzaXRzeW5hQGdtYWlsLmNvbSIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdGVuYW50IjoicWFodyIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdXNlci9pZCI6Ijc1ZGQyZjMyLTgyZWQtNGFhMi05YTM4LTJkZWY5NGI2MzVjMSIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdXNlci9maXJzdF9uYW1lIjoiS2F0ZSIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdXNlci9sYXN0X25hbWUiOiJMIiwiaHR0cDovL3h4eC5rYW5kamkuaW8vYXBwL3YxL2NsYWltcy91c2VyL2Z1bGxfbmFtZSI6IkthdGUgTCIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdXNlci9pc19jb21wYW55X2FkbWluIjpmYWxzZSwiaHR0cDovL3h4eC5rYW5kamkuaW8vYXBwL3YxL2NsYWltcy91c2VyL3JvbGUiOiJzdGFuZGFyZCIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdXNlci90eXBlIjoiY29tcGFueSIsImh0dHA6Ly94eHgua2FuZGppLmlvL2FwcC92MS9jbGFpbXMvdXNlci9jcmVhdGVkX2F0IjoiMjAyNS0wNi0wNFQyMDozNTo0MS4yNzU5MzJaIiwiaHR0cDovL3h4eC5rYW5kamkuaW8vYXBwL3YxL2NsYWltcy91c2VyL2xvY2FsZSI6ImVuX1VTIiwiaHR0cDovL3h4eC5rYW5kamkuaW8vYXBwL3YxL2NsYWltcy90ZW5hbnQvaWQiOiI2N2NiMGRlMC02Y2QzLTQwYjMtYTA0OS03OTA4NmY2ZDVhZDIiLCJodHRwOi8veHh4LmthbmRqaS5pby9hcHAvdjEvY2xhaW1zL3RlbmFudC9ob3N0IjoiY2xpZW50LTkiLCJodHRwOi8veHh4LmthbmRqaS5pby9hcHAvdjEvY2xhaW1zL3RlbmFudC9wcmVmZXJyZWRfc3ViZG9tYWluIjoiNjdjYjBkZTAiLCJodHRwOi8veHh4LmthbmRqaS5pby9hcHAvdjEvY2xhaW1zL3RlbmFudC9kZXZpY2Vfc3ViZG9tYWluIjoiNjdjYjBkZTAiLCJodHRwOi8veHh4LmthbmRqaS5pby9hcHAvdjEvY2xhaW1zL3RlbmFudC9jb21wYW55X2lkIjoiNjdjYjBkZTAtNmNkMy00MGIzLWEwNDktNzkwODZmNmQ1YWQyIiwiaHR0cDovL3h4eC5rYW5kamkuaW8vYXBwL3YxL2NsYWltcy90ZW5hbnQvZW5hYmxlZF9jYXBhYmlsaXRpZXMiOiJlZHIga2FpIHNzbyBzY2ltIHZpc2liaWxpdHkga2FuZGppX2xvZ2luIGVudGVycHJpc2VfYXBpIHZ1bG5lcmFiaWxpdHlfbWFuYWdlbWVudCIsImlzcyI6Imh0dHBzOi8vYXV0aC5rYW5kamkuaW8vIiwic3ViIjoiYXV0aDB8dW5kZWZpbmVkfDc1ZGQyZjMyLTgyZWQtNGFhMi05YTM4LTJkZWY5NGI2MzVjMSIsImF1ZCI6WyJodHRwOi8veHh4LmthbmRqaS5pby9hcHAvdjEvIiwiaHR0cHM6Ly9rYW5kamktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzQ5MTQyMTc1LCJleHAiOjE3NDkxNDMwNzUsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJvcmdfaWQiOiJvcmdfbTdld3FUcDlqbmdzbnA1ZSIsImF6cCI6IjgzQ3Rva3dMN3hFcEo3eHo5Vm9qdmZwa1p2R1FjWk1mIn0.gFoshJ5kj41OesqvJXm-R5S7pKB_PKmJBNaMN7e820uxk5-z1RtGfCNNqTaQzWFpkhAuEzrPXvrjW-lO8Mxz2wup8bv7cHh-Agg-VcfOabggiOfDIscs276PIj6Li7iHg9vPuYQjIVfKsqEA9kisrGTYQcn4EnMzQTdI-fP4uKgTfzIvf945l0JpfSVLNstUYJ4DVn-PfZwXWKMBI1pAOcX0ZF4X04QrQeI_D8K1Ux--QH1S-4zOlRqWixMfkzeh1dOGKODuno4-xkHZJcwCXqIQXl5cmnELVamzS3BTgnGpNZbYLCyGdP_bvvXalBEPJrP1dyKW0TZwRKeA2oSfIQ"  # обрежь или подставь весь токен
#
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#
#     response = requests.get("https://qahw.kandji.io/devices", headers=headers)
#
#     # print(response.status_code)
#     print(response.json())
#     assert response.json()

