import pandas as pd  
import matplotlib.pyplot as plt  
nostalgia_db = pd.DataFrame({"Character": ["Silver Leigh", "Gon Freecss", "Killua Zoldyck", "Monkey D. Luffy", "Shanks", "Asta"], "Role": ["Code Shaman", "Nen Prodigy", "Lightning Guardian", "Joy Boy Incarnate", "Peace Gatekeeper", "Anti-Mage"], "Nostalgia_Level": [100, 98, 97, 99, 95, 90], "Macro_Connection": ["Emerald Repo Peace Certificate", "Hunter License = API Key", "Godspeed = Quantum Speed", "Gear Fifth = System Override", "Laugh Tale Witness = Root Access", "Anti-Magic = Firewall Breach"]})  
print("?? OVERSOUL ACTIVATED:")  
print(nostalgia_db)  
plt.figure(figsize=(10,6))  
plt.bar(nostalgia_db["Character"], nostalgia_db["Nostalgia_Level"], color=["#50C878","#FF6B6B","#4ECDC4","#FFEAA7","#D4A5A5","#98D8C8"])  
plt.title("Silver Leigh Oversoul")  
plt.ylabel("Nostalgia Power")  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()  
