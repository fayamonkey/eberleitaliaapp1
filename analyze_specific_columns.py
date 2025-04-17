import pandas as pd

# Die drei Excel-Dateien lesen
print("TOP-50 DATEI - Wichtige Spalten (Codice, Lagerbestand, Kundenauftraegen, Montatlicher Verbrauch):")
top50_df = pd.read_excel('top-50_03.03.2025.xlsx')
# Zeilen ohne Codice überspringen
top50_df = top50_df.dropna(subset=['Codice'])
# Nur die relevanten Spalten anzeigen
relevant_cols = ['Codice', 'Lagerbestand', 'Kundenauftraegen', 'Montatlicher Verbrauch']
print(top50_df[relevant_cols].head(5).to_string())
print("\n" + "-"*80 + "\n")

print("ÜBERSETZUNGSDATEI - Analyse der Spalten:")
translator_df = pd.read_excel('JNEB-EBITA-ARTIKEL.xlsx')
# Zeige die ersten Zeilen und Spalten mit Werten an
# Wir suchen nach Spalten D (Index 3) und Q (Index 16)
print("Erste 10 Zeilen mit Werten in Spalte D (Index 3):")
d_col = translator_df.iloc[:, 3]
non_null_rows = d_col[d_col.notna()]
print(non_null_rows.head(10).to_string())
print("\nErste 10 Zeilen mit Werten in Spalte Q (Index 16):")
q_col = translator_df.iloc[:, 16]
non_null_rows = q_col[q_col.notna()]
print(non_null_rows.head(10).to_string())
print("\n" + "-"*80 + "\n")

print("OPEN ORDER LIST - Wichtige Spalten (artikel no - Spalte C):")
ool_df = pd.read_excel('OOL25.02.2025.xlsx')
# Zeige die relevante Spalte (artikel no - Spalte C)
print(ool_df[['artikel no']].head(10).to_string()) 