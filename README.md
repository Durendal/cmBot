# cmBot
A class for interacting with the coinmine API

cmBot was written for Python 2.7 and has not been tested with 3.x
Donations are appreciated :)

	BTC: 1GicRCkw8EigtNdFwfTR6cFxM7uA8nNwbd
	LTC: LMzNLYqu1AKyvdwbdHjNZgkjAALKFJvpMB

=============
Dependencies:
=============
requests - http://docs.python-requests.org/en/latest/

======
About:
======
cmBot is just a set of wrapper functions built around the coinmine.pw API, for convenience they are placed inside of a class.

===========
Other Info:
===========
http://coinmine.pw/api-information.php - official API Documentation

=================
Member Functions:
=================

	_getBaseURL()
		returns the base url used in queries: 'coinmine.pw/api.php'
	
	_getInfoAPIKey()
		returns the value of _infoAPIKey

	_getPayAPIKey()
		returns the value of _payAPIKey

	_getAccount()
		returns the value of _account

	_publicAPICall(method)
		takes method as an argument and returns a call to the public API using the user defined method uses GET method

	_authInfoAPIKey(params)
		takes a set of parameters to be used to make an authenticated call to the API with the Info API Key uses GET method

	_authPayAPIKey(data)
		takes a set of data parameters to be used to make an authenticated call to the API with the Pay API Key uses POST method

	coinProfit()
		returns current information about mined coins in json format

	poolInfo()
		returns current information about coinmine pools in json format

	workers()
		returns information about all of your workers in json format

	switch(ticker)
		switches your worker to any mined coin by your program, returns status code in json format

	payInfo()
		returns information about your balances in json format

	setPayInfo(address, payout, note, manual)
		takes 4 optional parameters, only those specified will be sent.
		Change your payout settings, returns status code in json format

	transHist()
		returns last 100 payout transactions history in json format

=================
Member Variables:
=================

	_account - user account to use for requests
	_infoAPIKey - Info API Key to use for requests
	_payAPIKey - Pay API Key to use for requests
	_baseURL - base form of the url to use for requests