import pandas as pd
import sys

# Die drei Excel-Dateien lesen
print("Debugging der Artikelnummer-Übereinstimmungen")

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

# 3. Überprüfe das Format der Artikelnummern in der OOL
print("\nFormat der Artikelnummern in der OOL überprüfen:")
ool_artikel_sample = ool_df['artikel no'].head(10).tolist()
print(f"Beispiele aus OOL: {ool_artikel_sample}")

# 4. Versuche, Übereinstimmungen zu finden
print("\nVersuche manuelle Übereinstimmungen zu finden:")
artikelnummern_set = set(all_artikelnummern)
matches_found = 0

for idx, row in ool_df.iterrows():
    artikel_no = str(row['artikel no'])
    if artikel_no in artikelnummern_set:
        matches_found += 1
        if matches_found <= 5:  # Zeige nur die ersten 5 Übereinstimmungen
            print(f"  Match gefunden: {artikel_no}")

print(f"\nGesamtanzahl der Übereinstimmungen: {matches_found}")

# 5. Überprüfe Datentypprobleme
print("\nPrüfe auf Datentypprobleme:")
ool_types = ool_df['artikel no'].apply(type).value_counts()
print(f"Datentypen in OOL['artikel no']: {ool_types}")

art_types = pd.Series(all_artikelnummern).apply(type).value_counts()
print(f"Datentypen in extrahierten Artikelnummern: {art_types}")

# 6. Typkonvertierung testen
print("\nTypkonvertierungstest:")
if all_artikelnummern and len(ool_df) > 0:
    # Nimm die erste Artikelnummer aus unserer Liste
    sample_art = all_artikelnummern[0] if all_artikelnummern else ""
    # Suche nach übereinstimmenden Werten in OOL mit und ohne Konvertierung
    direct_match = ool_df[ool_df['artikel no'] == sample_art]
    str_match = ool_df[ool_df['artikel no'].astype(str) == sample_art]
    
    print(f"Testartikelnummer: {sample_art}")
    print(f"Direkte Übereinstimmungen: {len(direct_match)}")
    print(f"String-konvertierte Übereinstimmungen: {len(str_match)}")

    # Probiere ein oder zwei Artikelnummern aus der OOL
    if len(ool_df) > 0:
        ool_sample = str(ool_df.iloc[0]['artikel no'])
        print(f"\nOOL-Artikelnummer: {ool_sample}")
        print(f"In unserer Artikelnummer-Liste: {ool_sample in artikelnummern_set}")
        # Teste doppelte Konvertierung
        double_converted = str(ool_sample) in set(str(a) for a in all_artikelnummern)
        print(f"Nach doppelter Stringkonvertierung: {double_converted}")

# 7. Probieren wir, führende Nullen zu entfernen oder hinzuzufügen
print("\nTest mit führenden Nullen:")
if all_artikelnummern and len(ool_df) > 0:
    # Versuche, Artikelnummern als Zahlen zu betrachten und führende Nullen zu entfernen
    numeric_artikelnummern = []
    for art in all_artikelnummern:
        try:
            # Entferne führende Nullen, indem wir zu int und zurück zu str konvertieren
            numeric_art = str(int(float(art)))
            numeric_artikelnummern.append(numeric_art)
        except (ValueError, TypeError):
            # Falls keine Zahl, behalte das Original
            numeric_artikelnummern.append(art)
    
    # Dasselbe für OOL
    numeric_ool = []
    for art in ool_df['artikel no']:
        try:
            numeric_art = str(int(float(art)))
            numeric_ool.append(numeric_art)
        except (ValueError, TypeError):
            numeric_ool.append(str(art))
    
    # Prüfe auf Übereinstimmungen
    numeric_matches = set(numeric_artikelnummern) & set(numeric_ool)
    print(f"Übereinstimmungen nach numerischer Konvertierung: {len(numeric_matches)}")
    if numeric_matches:
        print(f"Beispiele: {list(numeric_matches)[:5]}")

# Detaillierte Information für ein paar Artikelnummern
if all_artikelnummern and len(ool_df) > 0:
    print("\nDetailuntersuchung von Artikelnummern:")
    for i, art in enumerate(all_artikelnummern[:3]):
        print(f"\nArtikel {i+1}: '{art}'")
        print(f"  Länge: {len(art)}")
        print(f"  ASCII-Codes: {[ord(c) for c in art]}")
        
        # Suche nach Artikelnummern in OOL, die mit diesem Artikel beginnen oder enden
        starts_with = ool_df[ool_df['artikel no'].astype(str).str.startswith(art)]
        ends_with = ool_df[ool_df['artikel no'].astype(str).str.endswith(art)]
        print(f"  OOL-Einträge, die mit diesem Artikel beginnen: {len(starts_with)}")
        print(f"  OOL-Einträge, die mit diesem Artikel enden: {len(ends_with)}")
        
        # Für jeden Eintrag in OOL, vergleiche mit dem aktuellen Artikel
        all_similar = []
        for ool_art in ool_df['artikel no'].head(100):  # Begrenzt auf die ersten 100 zur Effizienz
            ool_art_str = str(ool_art)
            if art in ool_art_str or ool_art_str in art:
                all_similar.append(ool_art_str)
                
        print(f"  Ähnliche Artikelnummern in OOL: {len(all_similar)}")
        if all_similar:
            print(f"  Beispiele: {all_similar[:5]}") 