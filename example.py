import cmBot

def main():
	
	infoAPIKey = "YOUR_INFO_API_KEY"
	payAPIKey = "YOUR_PAY_API_KEY"
	account = "YOUR_ACCOUNT_NAME"

	miner = cmBot.cmBot(account, infoAPIKey, payAPIKey)

	# Uncomment the following lines to test it out
	#print miner.coinProfit()
	#print miner.poolInfo()
	#print miner.workers()
	#print miner.transHist()
if __name__ == '__main__':
	main()