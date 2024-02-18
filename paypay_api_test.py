import paypayopa
import time

API_KEY = ""
API_SECRET = ""
client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
# 加盟店IDを入れる
client.set_assume_merchant("")

# Creating the payload to create a QR Code, additional parameters can be added basis the API Documentation
request = {
  "merchantPaymentId": round(time.time()),
  "codeType": "ORDER_QR",
  # 支払い完了後に開くページ/アプリのURL
  "redirectUrl": "",
  "redirectType":"WEB_LINK",
  # 支払いの説明
  "orderDescription":"絶対払えよ！！",
  "orderItems": [{
      "name": "TabiKan",
      "category": "pasteries",
      "quantity": 1,
      "productId": "67678",
      "unitPrice": {
          "amount": 1,
          "currency": "JPY"
      }
  }],
  "amount": {
      "amount": 100,
      "currency": "JPY"
  },
}
# Calling the method to create a qr code
response = client.Code.create_qr_code(request)
# Printing if the method call was SUCCESS
print(response['resultInfo']['code'])
# 以下によりQRコードが発行してくれるURLを嘉永してくれる
print(response['data']['url'])