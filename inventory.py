#This manages the inventory and presentation of the inventory
import numpy as np

class Inventory:
    def __init__(self):
        self.bag = []


    
    def add_item(self,item):
        self.bag.append(item)
        print("{item} added to bag!")

    def drop_item(self,item):
        self.bag.pop(item)
        print("{item} dropped")

    def list_inventory(self):
        if self.bag is not None:
            print(self.bag)
        else:
            print("[EMPTY]")