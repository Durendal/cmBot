import requests

class cmBot:

	def __init__(self, account = "", infoapikey = None, payapikey = None, baseurl = 'coinmine.pw/api.php'):
		self._account = account
		self._infoAPIKey = infoapikey
		self._payAPIKey = payapikey
		self._baseURL = baseurl

	def _getBaseURL(self):
		return self._baseURL

	def _getInfoAPIKey(self):
		return self._infoAPIKey

	def _getPayAPIKey(self):
		return self._payAPIKey

	def _getAccount(self):
		return self._account

	def _publicAPICall(self, method):
		params = { 'method' : method }
		result = requests.get("http://www." + self._getBaseURL(), params = params, verify = False)
		return result.json()

	def _authInfoAPIKey(self, params):
		result = requests.get("https://ssl." + self._getBaseURL(), params = params, verify = False)
		return result.json()

	def _authPayAPIKey(self, data):
		result = requests.post("https://ssl." + self._getBaseURL(), data = data, verify = False)
		return result.json()

	def _setParams(self):
		params = {
					'apikey' : self._getInfoAPIKey(),
					'account' : self._getAccount(),
				}
		return params

	def _setData(self):
		data = {
					'apikey' : self._getPayAPIKey(),
					'account' : self._getAccount(),
				}
		return data

	def coinProfit(self):
		return self._publicAPICall("coinprofit")

	def poolInfo(self):
		return self._publicAPICall("poolinfo")

	def workers(self):
		params = self._setParams()
		params['method'] = 'workers'
					
		return self._authInfoAPIKey(params)

	def switch(self, ticker):
		params = self._setParams()
		params['method'] = 'switch'
		params['ticker'] = ticker

		return self._authInfoAPIKey(params)

	def payInfo(self):
		data = self._setData()
		data['method'] = 'payinfo'
		return self._authPayAPIKey(data)

	def setPayInfo(self, address = None, payout = None, note = None, manual = None):
		data = self._setData()
		data['method'] = 'setpayinfo'
					
		if address:
			data['address'] = address
		if payout:
			data['payout'] = payout
		if note:
			data['note'] = note
		if manual:
			data['manual'] = manual
		return self._authPayAPIKey(data)

	def transHist(self):
		data = self._setData()
		data['method'] = 'transhist'
		return self._authPayAPIKey(data)
