import pandas as pd
import sys

# Die drei Excel-Dateien lesen
print("Debugging der Artikelnummer-Übereinstimmungen mit verbessertem Matching")

# Dateien laden
top50_df = pd.read_excel('top-50_03.03.2025.xlsx')
translator_df = pd.read_excel('JNEB-EBITA-ARTIKEL.xlsx')
ool_df = pd.read_excel('OOL25.02.2025.xlsx')

# 1. Extrahiere ein paar Basis-Codices aus der Top-50-Liste
valid_rows = top50_df.dropna(subset=['Codice'])
sample_codices = []
count = 0
for _, row in valid_rows.iterrows():
    if count >= 5:  # Nur die ersten 5 zur Demonstration
        break
    full_codice = row['Codice']
    if '#' in str(full_codice):
        base_codice = full_codice.split('#')[0]
    else:
        base_codice = full_codice
    sample_codices.append((full_codice, base_codice))
    count += 1

print(f"Stichprobe von Codices aus Top-50 (gesamt {len(valid_rows)} Zeilen):")
for full, base in sample_codices:
    print(f"  Full: {full}, Base: {base}")

# 2. Für jeden Basis-Codice, finde die dazugehörigen Artikelnummern
print("\nSuche nach Artikelnummern in der Übersetzungsdatei:")
all_artikelnummern = []
for _, base_codice in sample_codices:
    # Alle Zeilen finden, in denen Spalte D dem Basis-Codice entspricht
    matching_rows = translator_df[translator_df.iloc[:, 3] == base_codice]
    
    artikelnummern = []
    for _, row in matching_rows.iterrows():
        if pd.notna(row.iloc[16]):  # Prüfen, ob die Zelle nicht NaN ist
            artikelnummern.append(str(row.iloc[16]))
    
    print(f"  Codice {base_codice}: {len(artikelnummern)} Artikelnummer(n) gefunden: {artikelnummern[:5]}")
    all_artikelnummern.extend(artikelnummern)

print(f"\nInsgesamt {len(all_artikelnummern)} Artikelnummern gefunden.")
if all_artikelnummern:
    print(f"Beispiele: {all_artikelnummern[:10]}")

# 3. Artikel-Varianten erstellen
print("\nErstellung von Artikel-Varianten:")
artikelnummern_varianten = set()
for art in all_artikelnummern[:10]:  # Nur die ersten 10 zur Demonstration
    # Das Original-Format hinzufügen
    artikelnummern_varianten.add(art)
    print(f"  Original: {art}")
    
    # Format für Integer-Vergleich hinzufügen
    try:
        numeric_art = str(int(float(art)))
        artikelnummern_varianten.add(numeric_art)
        print(f"  Numerisch: {numeric_art}")
    except (ValueError, TypeError):
        pass
    
    # Format mit führender '7' hinzufügen
    if not art.startswith('7') and art.isdigit():
        variante_mit_7 = '7' + art
        artikelnummern_varianten.add(variante_mit_7)
        print(f"  Mit führender 7: {variante_mit_7}")

# 4. Format der Artikelnummern in der OOL überprüfen
print("\nFormat der Artikelnummern in der OOL überprüfen:")
ool_artikel_sample = ool_df['artikel no'].head(10).tolist()
print(f"Beispiele aus OOL: {ool_artikel_sample}")

# 5. Suche nach Übereinstimmungen mit verbesserten Algorithmus
print("\nSuche nach Übereinstimmungen mit verbesserten Algorithmus:")
matches_found = 0
match_details = []

# Alle Artikelnummern-Varianten erstellen
artikelnummern_set = set()
for art in all_artikelnummern:
    # Original
    artikelnummern_set.add(art)
    
    # Numerisch
    try:
        numeric_art = str(int(float(art)))
        artikelnummern_set.add(numeric_art)
    except (ValueError, TypeError):
        pass
    
    # Mit führender 7
    if not art.startswith('7') and art.isdigit():
        artikelnummern_set.add('7' + art)

# Übereinstimmungen finden
for idx, row in ool_df.iterrows():
    ool_artikel = row['artikel no']
    ool_artikel_str = str(ool_artikel)
    
    # Auch Format ohne führende '7' in Betracht ziehen
    ool_ohne_7 = ool_artikel_str[1:] if ool_artikel_str.startswith('7') else ool_artikel_str
    
    # Überprüfe alle möglichen Formate
    if (ool_artikel_str in artikelnummern_set or 
        ool_ohne_7 in artikelnummern_set):
        matches_found += 1
        if matches_found <= 20:  # Zeige nur die ersten 20 Übereinstimmungen
            match_detail = {
                'ool_artikelnr': ool_artikel_str,
                'abmessung': row.get('Abmessung', ''),
                'format': 'Direkt' if ool_artikel_str in artikelnummern_set else 'Ohne führende 7'
            }
            match_details.append(match_detail)
            print(f"  Match {matches_found}: OOL-Nr: {ool_artikel_str}, Format: {match_detail['format']}")

print(f"\nGesamtanzahl der Übereinstimmungen: {matches_found}")

# 6. Untersuche Matching-Details für ein paar Beispiele
if match_details:
    print("\nDetails zu einigen gefundenen Übereinstimmungen:")
    for i, match in enumerate(match_details[:5]):
        print(f"\nMatch {i+1}:")
        print(f"  OOL-Artikelnummer: {match['ool_artikelnr']}")
        print(f"  Abmessung: {match['abmessung']}")
        print(f"  Gefunden durch: {match['format']}")
        
        # Finde die ursprüngliche Artikelnummer aus unserer Liste
        original_art = None
        if match['format'] == 'Direkt':
            if match['ool_artikelnr'] in all_artikelnummern:
                original_art = match['ool_artikelnr']
        else:  # Ohne führende 7
            for art in all_artikelnummern:
                if match['ool_artikelnr'][1:] == art:
                    original_art = art
                    break
        
        if original_art:
            print(f"  Ursprüngliche Artikelnummer aus Übersetzungsdatei: {original_art}")
            
            # Finde den zugehörigen Codice
            for _, base_codice in sample_codices:
                matching_rows = translator_df[translator_df.iloc[:, 3] == base_codice]
                for _, row in matching_rows.iterrows():
                    if pd.notna(row.iloc[16]) and str(row.iloc[16]) == original_art:
                        print(f"  Zugehöriger Codice: {base_codice}")
                        break 