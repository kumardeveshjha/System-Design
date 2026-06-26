

from saving_acc import SavingsAccount
from fd_acc import FixedDeposite 

fixed_depo = FixedDeposite(1000)
saving = SavingsAccount(1000)
saving.deposit(1000)
saving.withdraw(500)
fixed_depo.deposit(2000)
fixed_depo.withdraw(1000)