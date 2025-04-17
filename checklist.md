# Checkliste: Eberle Artikelnummern-Matching-App

## Setup & Struktur
- [x] Projektplan erstellen
- [x] Gedankendokumentation (thoughts.md) einrichten
- [x] Entwicklungs-Journal (journal.md) einrichten
- [x] Diese Checkliste erstellen
- [x] Projektstruktur erstellen
- [ ] Virtuelle Umgebung einrichten
- [x] Abhängigkeiten definieren (requirements.txt erstellt)

## Komponenten
### Datei-Upload-Modul
- [x] Streamlit-App-Struktur erstellen
- [x] Datei-Upload-Komponente für die drei Excel-Dateien implementieren
- [x] Validierung der hochgeladenen Dateien
- [x] Fehlerbehandlung für falsche Dateiformate

### Datenverarbeitungsmodul
- [x] Funktion zur Extraktion der Codices aus der Top-50-Liste
- [x] Funktion zum Abrufen der Artikelnummern aus der Übersetzungsdatei
- [x] Funktion zum Abgleich der Artikelnummern mit der Open Order List
- [x] Funktion zur Erstellung der Zusammenfassungsdatei

### Ergebnis-Export-Modul
- [x] Funktion zur Erstellung der markierten Open Order List
- [x] Funktion zur Erstellung der Zusammenfassungsdatei
- [x] Download-Funktionalität für beide Ergebnisdateien
- [x] Formatierung der Ausgabedateien (rote Markierung, etc.)

## Tests & Qualitätssicherung
- [ ] Unit-Tests für die Datenverarbeitungsfunktionen
- [ ] Integrationstests für den gesamten Prozessablauf
- [ ] Testen mit realen Datensätzen
- [ ] Performance-Tests mit größeren Datensätzen

## Dokumentation
- [x] README.md erstellen
- [x] Kommentieren des Codes
- [x] Benutzeranleitung erstellen

## Bereitstellung
- [ ] Lokales Ausführen der Anwendung testen
- [ ] Bereitstellung vorbereiten
- [ ] Finale Tests vor der Übergabe 