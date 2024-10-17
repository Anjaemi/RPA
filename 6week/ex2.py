import pandas as pd
import matplotlib.pyplot as pit

hat=pd.read_csv('ch4-2.csv')
print(hat.describe(), end="\n\n")

pit.figure(figsize=(8,10))
pit.boxplot(hat.weight)
pit.title('B hatchery chick weight box', fontsize=17)
pit.ylabel('weight(g)')
pit.show()