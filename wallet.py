# using custom modules

from crypto_utils import wallet

my_wallet = wallet("chris") 
my_wallet.deposit("ETH", 0.7)
print(my_wallet.get_balance())