import pandas as pd

# Die drei Excel-Dateien lesen
print("TOP-50 DATEI:")
top50_df = pd.read_excel('top-50_03.03.2025.xlsx')
print(f"Anzahl Zeilen: {len(top50_df)}")
print(f"Spalten: {top50_df.columns.tolist()}")
print(top50_df.head(3).to_string())
print("\n" + "-"*80 + "\n")

print("ÜBERSETZUNGSDATEI (JNEB-EBITA-ARTIKEL):")
translator_df = pd.read_excel('JNEB-EBITA-ARTIKEL.xlsx')
print(f"Anzahl Zeilen: {len(translator_df)}")
print(f"Spalten: {translator_df.columns.tolist()}")
print(translator_df.head(3).to_string())
print("\n" + "-"*80 + "\n")

print("OPEN ORDER LIST (OOL):")
ool_df = pd.read_excel('OOL25.02.2025.xlsx')
print(f"Anzahl Zeilen: {len(ool_df)}")
print(f"Spalten: {ool_df.columns.tolist()}")
print(ool_df.head(3).to_string()) 