import pandas as pd
import sys

# Die drei Excel-Dateien lesen
print("Debugging der erweiterten Artikelnummer-Übereinstimmungen")

# Dateien laden
top50_df = pd.read_excel('top-50_03.03.2025.xlsx')
translator_df = pd.read_excel('JNEB-EBITA-ARTIKEL.xlsx')
ool_df = pd.read_excel('OOL25.02.2025.xlsx')

# Extrahiere Codices aus der Top-50-Liste
print("Extrahiere Codices aus der Top-50-Liste...")
valid_rows = top50_df.dropna(subset=['Codice'])
codices_data = []
for _, row in valid_rows.iterrows():
    full_codice = row['Codice']
    # Codice in den Teil vor und nach # aufteilen
    if '#' in str(full_codice):
        base_codice = full_codice.split('#')[0]
    else:
        base_codice = full_codice
        
    # Informationen sammeln
    entry = {
        'full_codice': full_codice,
        'base_codice': base_codice,
        'lagerbestand': row.get('Lagerbestand', None),
        'kundenauftraege': row.get('Kundenauftraegen', None),
        'monatlicher_verbrauch': row.get('Montatlicher Verbrauch', None)
    }
    codices_data.append(entry)

print(f"Gefundene Codices: {len(codices_data)}")
for i, entry in enumerate(codices_data[:3]):  # Zeige die ersten 3 Einträge
    print(f"\nCodeice {i+1}: {entry['full_codice']}")
    print(f"  Base Codice: {entry['base_codice']}")
    print(f"  Lagerbestand: {entry['lagerbestand']}")
    print(f"  Kundenaufträge: {entry['kundenauftraege']}")
    print(f"  Monatlicher Verbrauch: {entry['monatlicher_verbrauch']}")

# Erstelle erweiterte OOL-Datei
print("\nErstelle erweiterte OOL-Datei...")
ool_df_extended = ool_df.copy()
ool_df_extended['Lagerbestand'] = None
ool_df_extended['Kundenauftraege'] = None
ool_df_extended['Monatlicher Verbrauch'] = None
ool_df_extended['Codice'] = None

# Sammle alle Match-Indizes
all_match_indices = []

# Für jeden Codice die Artikelnummern finden und verarbeiten
for codice_entry in codices_data[:5]:  # Begrenze auf die ersten 5 zur Demonstration
    print(f"\nVerarbeite Codice {codice_entry['full_codice']}...")
    base_codice = codice_entry['base_codice']
    
    # Artikelnummern für den Basis-Codice finden
    matching_rows = translator_df[translator_df.iloc[:, 3] == base_codice]
    
    artikelnummern = []
    for _, row in matching_rows.iterrows():
        if pd.notna(row.iloc[16]):  # Prüfen, ob die Zelle nicht NaN ist
            artikelnummern.append(str(row.iloc[16]))
    
    # Artikelnummern vorbereiten - verschiedene Formate berücksichtigen
    artikelnummern_set = set()
    for art in artikelnummern:
        # Das Original-Format hinzufügen
        artikelnummern_set.add(art)
        
        # Format für Integer-Vergleich hinzufügen (ohne führende Nullen)
        try:
            numeric_art = str(int(float(art)))
            artikelnummern_set.add(numeric_art)
        except (ValueError, TypeError):
            pass
        
        # Format mit führender '7' hinzufügen für potenziellen Vergleich mit OOL
        if not art.startswith('7') and art.isdigit():
            artikelnummern_set.add('7' + art)
    
    # Jede Zeile in der Open Order List überprüfen
    match_indices = []
    for idx, row in ool_df.iterrows():
        # Konvertiere die OOL-Artikelnummer in verschiedene Formate für den Vergleich
        ool_artikel = row['artikel no']
        ool_artikel_str = str(ool_artikel)
        
        # Auch Format ohne führende '7' in Betracht ziehen
        ool_ohne_7 = ool_artikel_str[1:] if ool_artikel_str.startswith('7') else ool_artikel_str
        
        # Überprüfe alle möglichen Formate
        if (ool_artikel_str in artikelnummern_set or 
            ool_ohne_7 in artikelnummern_set):
            match_indices.append(idx)
    
    # Zusätzliche Daten in die erweiterte OOL-Datei eintragen
    for idx in match_indices:
        ool_df_extended.at[idx, 'Lagerbestand'] = codice_entry.get('lagerbestand')
        ool_df_extended.at[idx, 'Kundenauftraege'] = codice_entry.get('kundenauftraege')
        ool_df_extended.at[idx, 'Monatlicher Verbrauch'] = codice_entry.get('monatlicher_verbrauch')
        ool_df_extended.at[idx, 'Codice'] = codice_entry.get('full_codice')
    
    all_match_indices.extend(match_indices)
    print(f"  Gefunden: {len(match_indices)} Übereinstimmungen")

# Ergebnisse anzeigen
print(f"\nGesamtzahl der Übereinstimmungen: {len(all_match_indices)}")

# Beispiele für erweiterte Zeilen anzeigen
if all_match_indices:
    print("\nBeispiele für erweiterte Zeilen:")
    sample_indices = all_match_indices[:5] if len(all_match_indices) >= 5 else all_match_indices
    
    for i, idx in enumerate(sample_indices):
        row = ool_df_extended.iloc[idx]
        print(f"\nZeile {i+1}:")
        print(f"  Artikel-Nr: {row['artikel no']}")
        print(f"  Abmessung: {row['Abmessung']}")
        print(f"  Lagerbestand: {row['Lagerbestand']}")
        print(f"  Kundenaufträge: {row['Kundenauftraege']}")
        print(f"  Monatlicher Verbrauch: {row['Monatlicher Verbrauch']}")
        print(f"  Codice: {row['Codice']}")
else:
    print("Keine Übereinstimmungen gefunden.") 