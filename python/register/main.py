from register import import_all_modules_for_register
from register import Registers

print("Registers.model._dict before: ", Registers.model._dict)
import_all_modules_for_register(['models'])
print("Registers.model._dict after: ", Registers.model._dict)