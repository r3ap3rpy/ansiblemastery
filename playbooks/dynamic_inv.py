import os                                                                                                   
import sys                                                                                                  
                                                                                                            
try:                                                                                                        
        import json                                                                                         
except Exception as e:                                                                                      
        print(f"Cannot import json because: {e}")                                                           
                                                                                                            
class DynamicInventory():                                                                                   
        def __init__(self):                                                                                 
                self.inventory = {}                                                                         
                self.read_cli_argy()                                                                        
                if self.args.list:                                                                          
                        self.inventory = self.our_inventory()                                               
                else:                                                                                       
                        self.inventory = self.empty_inventory()                                             
        def empty_inventory(self):                                                                          
                return {"meta":{"hostvars":{}}}                                                             
        def our_inventory(self):                                                                            
                return {"group":{"hosts":["ubuntu"],"vars":{"examplevariable":"thisrandomvalue"}}
                "_meta":{"hostvars":{"hostvars":"whatever"}}                                               
        def read_cli_args(self):                                                                            
                parser = argparse.ArgumentParser()                                                          
                parser.add_argument("--list",action="store_true")                                           
                                                                                                            
DynamicInventory()                                                                                          