# Projektplan: Eberle Artikelnummern-Matching-App (MVP)

## Projektziel
Entwicklung einer Streamlit-App zur Automatisierung des Prozesses zum Abgleich von Artikelnummern zwischen Eberle Deutschland und Eberle Italien. Das MVP soll die drei Excel-Dateien verarbeiten und die entsprechenden Ergebnisse liefern, ohne unnötige Extras.

## Architektur
- **Frontend**: Streamlit (minimalistisches, professionelles UI)
- **Backend**: Python mit Pandas für die Datenverarbeitung
- **Datenspeicherung**: Temporäre Dateien im Arbeitsspeicher, keine Datenbank nötig

## Komponenten/Module
1. **Datei-Upload-Modul**: Ermöglicht dem Benutzer, die drei Excel-Dateien hochzuladen
2. **Datenverarbeitungsmodul**: Enthält die Logik zum Abgleich der Artikelnummern
3. **Ergebnis-Export-Modul**: Erzeugt die Ausgabedateien zum Download

## Technische Details
- **Programmiersprache**: Python 3.10+
- **Hauptbibliotheken**: 
  - Streamlit (UI)
  - Pandas (Datenverarbeitung)
  - Openpyxl (Excel-Manipulation)
  - XlsxWriter (Excel-Ausgabe mit Formatierung)

## Funktionsablauf
1. Benutzer lädt die drei Excel-Dateien hoch:
   - Top-50 Liste (Eberle Italien)
   - Übersetzungsdatei
   - Open Order List (Eberle Deutschland)
2. Die App verarbeitet die Dateien:
   - Extrahiert die Codices aus der Top-50 Liste
   - Findet über die Übersetzungsdatei die entsprechenden Artikelnummern
   - Sucht diese Artikelnummern in der Open Order List
   - Markiert die gefundenen Zeilen in der Open Order List
3. Die App erzeugt zwei Ausgabedateien:
   - Die modifizierte Open Order List mit rot markierten Zeilen
   - Eine Zusammenfassungsdatei mit den Verbindungen zwischen Codices und Artikelnummern

## Zeitplan
1. **Setup & Infrastruktur**: 1 Tag
   - Einrichtung der Entwicklungsumgebung
   - Installation der Abhängigkeiten
   - Erstellen der Projektstruktur
2. **Datei-Upload-Komponente**: 1 Tag
   - Erstellen der Streamlit-Oberfläche
   - Implementieren der Datei-Upload-Funktionalität
3. **Datenverarbeitungsmodul**: 2-3 Tage
   - Implementieren der Datenextraktionslogik
   - Implementieren der Matching-Logik
   - Implementieren der Markierungslogik
4. **Ergebnis-Export-Komponente**: 1-2 Tage
   - Implementieren der Excel-Export-Funktionalität mit Formatierung
   - Implementieren der Download-Funktionalität
5. **Tests & Bugfixing**: 1-2 Tage
   - Testen mit realen Daten
   - Beheben von Fehlern
6. **Dokumentation & Bereitstellung**: 1 Tag
   - Erstellen einer Benutzeranleitung
   - Vorbereiten der Bereitstellung

## Qualitätskontrolle
- Tests mit realen Datensätzen nach jeder Implementierungsphase
- Überprüfung der Genauigkeit der Matching-Ergebnisse
- Sicherstellung der Benutzerfreundlichkeit der Oberfläche

## Risiken & Abhilfemaßnahmen
- **Risiko**: Inkonsistenzen in den Excel-Dateien
  - **Abhilfe**: Robuste Fehlerbehandlung und Datenvalidierung
- **Risiko**: Performance-Probleme bei großen Dateien
  - **Abhilfe**: Optimierung der Datenverarbeitungslogik
- **Risiko**: Benutzerfreundlichkeit
  - **Abhilfe**: Klare Anleitungen und intuitive Benutzeroberfläche

## Ressourcen
- 1 Entwickler (Python, Pandas, Streamlit)
- Teststelle für Qualitätssicherung
- Excel-Testdateien aus der realen Umgebung

## Liefergegenstände
1. Streamlit-App als ausführbares Python-Programm
2. Benutzeranleitung
3. Quellcode mit Dokumentation 