from decouple import config
import requests
import uuid


class WiseService:
    def __init__(self):
        self.token = config("WISE_KEY")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        self.main_url = config("WISE_URL")
        self.profile_id = self._get_profile_id()[0]
        self.business_id = self._get_profile_id()[1]

    def _get_profile_id(self):
        url = f"{self.main_url}/v1/profiles"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        profile_id = [p["id"] for p in data if p["type"] == "personal"][0]
        business_id = [p["id"] for p in data if p["type"] == "business"][0]
        return profile_id, business_id

    def create_quotes(self, source_currency, target_currency, target_amount):
        url = f"{self.main_url}/v2/quotes"
        data = {
            "sourceCurrency": source_currency,
            "targetCurrency": target_currency,
            "targetAmount": target_amount,
            "profile": self.profile_id,
        }

        response = requests.post(url, json=data, headers=self.headers)
        quotes_id = response.json()["id"]
        return quotes_id

    def create_recipient(self, full_name, iban):
        url = f"{self.main_url}/v1/accounts"
        data = {
            "currency": "EUR",
            "type": "iban",
            "profile": self.profile_id,
            "accountHolderName": full_name,
            "details": {
                "legalType": "PRIVATE",
                "iban": iban,
            },
        }
        response = requests.post(url, json=data, headers=self.headers)
        recipient_id = response.json()["id"]
        return recipient_id

    def create_transfer(self, recipient_account_id, quote_id, customer_transaction_id):
        url = f"{self.main_url}/v1/transfers"
        data = {
            "targetAccount": recipient_account_id,
            "quoteUuid": quote_id,
            "customerTransactionId": customer_transaction_id,
        }
        response = requests.post(url, json=data, headers=self.headers)
        transfer_id = response.json()["id"]
        return transfer_id

    def fund_transfer(self, transfer_id):
        url = f"{self.main_url}/v3/profiles/{self.profile_id}/transfers/{transfer_id}/payments"
        data = {"type": "BALANCE"}
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def cancelation(self, transfer_id):
        url = f"{self.main_url}/v1/transfers/{transfer_id}/cancel"
        resp = requests.put(url, headers=self.headers)
        return resp.json()


if __name__ == "__main__":
    wise = WiseService()
    quote_id = wise.create_quotes("EUR", "EUR", 35)
    recipient_id = wise.create_recipient("pasdf Pavlov", "DE89370400440532013000")
    customer_transaction_id = str(uuid.uuid4())
    transfer_id = wise.create_transfer(recipient_id, quote_id, customer_transaction_id)
    print(wise.fund_transfer(transfer_id))
