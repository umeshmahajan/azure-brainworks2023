import requests

class VaultClient:
    def __init__(self, vault_url, role_id, secret_id, secret_path):
        self.vault_url = vault_url
        self.role_id = role_id
        self.secret_id = secret_id
        self.secret_path = secret_path

    def authenticate_with_approle(self):
        """AI is creating summary for authenticate_with_approle

        Returns:
            [type]: [description]
        """
        auth_url = f"{self.vault_url}/v1/auth/approle/login"
        auth_data = {
            "role_id": self.role_id,
            "secret_id": self.secret_id
        }

        try:
            auth_response = requests.post(auth_url, json=auth_data)
            auth_response.raise_for_status()

            token = auth_response.json()["auth"]["client_token"]
            print("token=======", token)
            return token

        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")
            return None

    def get_secret(self, token):
        """AI is creating summary for get_secret

        Args:
            token ([type]): [description]

        Returns:
            [type]: [description]
        """
        headers = {
            "X-Vault-Token": token,
        }

        url = f"{self.vault_url}/v1/{self.secret_path}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            secret_data = response.json()["data"]
            return secret_data

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving secret: {e}")
            return None

if __name__ == "__main__":
    VAULT_URL = "http://localhost:8200"
    ROLE_ID = "a6b0caef-2292-6623-83b4-9c0463410f34"
    SECRET_ID = "f473dfaf-e92c-b255-4f15-ba607f06926d"
    SECRET_PATH = "secret/data/snowflake"

    vault_client = VaultClient(VAULT_URL, ROLE_ID, SECRET_ID, SECRET_PATH)

    token = vault_client.authenticate_with_approle()

    if token:
        secret_data = vault_client.get_secret(token)

        if secret_data:
            print("Secret data:", secret_data)
        else:
            print("Failed to retrieve secret.")
    else:
        print("Failed to authenticate with AppRole.")
