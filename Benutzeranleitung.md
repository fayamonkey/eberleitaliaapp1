# Benutzeranleitung: Eberle Artikelnummern-Matching-App

Diese Anleitung führt Sie durch die Verwendung der Eberle Artikelnummern-Matching-App, die entwickelt wurde, um den Abgleich von Artikelnummern zwischen Eberle Deutschland und Eberle Italien zu automatisieren.

## Inhaltsverzeichnis
1. [Installation](#installation)
2. [Starten der App](#starten-der-app)
3. [Dateien hochladen](#dateien-hochladen)
4. [Datenverarbeitung starten](#datenverarbeitung-starten)
5. [Ergebnisse herunterladen](#ergebnisse-herunterladen)
6. [Fehlerbehebung](#fehlerbehebung)

## Installation

### Voraussetzungen
- Python 3.10 oder höher
- Pip (Python-Paketmanager)

### Installationsschritte
1. Laden Sie alle Projektdateien herunter
2. Öffnen Sie eine Kommandozeile oder Terminal im Projektverzeichnis
3. Installieren Sie die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
```

## Starten der App

1. Öffnen Sie eine Kommandozeile oder Terminal im Projektverzeichnis
2. Führen Sie folgenden Befehl aus:

```bash
streamlit run app.py
```

3. Die App öffnet sich automatisch in Ihrem Standardbrowser

## Dateien hochladen

Die App benötigt drei Excel-Dateien zur Verarbeitung:

1. **Top-50 Liste (Eberle Italia)**:
   - Enthält die Codices (z.B. "RM4210090#1801") in Spalte A
   - Enthält Informationen über Lagerbestand, Kundenaufträge und monatlichen Verbrauch

2. **Übersetzungsdatei (JNEB-EBITA-ARTIKEL)**:
   - Enthält die Zuordnung zwischen Codices (ohne #-Teil) und Artikelnummern
   - Codices befinden sich in Spalte D, Artikelnummern in Spalte Q

3. **Open Order List (Eberle Deutschland)**:
   - Enthält die Artikelnummern in Spalte C
   - Diese Datei wird mit Markierungen für gefundene Übereinstimmungen ausgegeben

So laden Sie die Dateien hoch:
1. Klicken Sie auf "Browse files" (oder "Dateien durchsuchen") bei den entsprechenden Feldern
2. Wählen Sie die jeweilige Excel-Datei aus
3. Stellen Sie sicher, dass alle drei Dateien hochgeladen sind, bevor Sie fortfahren

## Datenverarbeitung starten

1. Nachdem alle drei Dateien hochgeladen wurden, klicken Sie auf den Button "Dateien verarbeiten"
2. Die App zeigt eine Fortschrittsanzeige und Status-Updates während der Verarbeitung an
3. Bei Fehlern (z.B. falsches Dateiformat) wird eine entsprechende Fehlermeldung angezeigt

## Ergebnisse herunterladen

Nach erfolgreicher Verarbeitung werden zwei Ausgabedateien zum Download angeboten:

1. **Markierte Open Order List**:
   - Enthält die Original-Open-Order-List mit rot markierten Zeilen für Übereinstimmungen
   - Klicken Sie auf "Markierte Open Order List herunterladen", um die Datei zu speichern

2. **Zusammenfassungsdatei**:
   - Enthält die Verbindungen zwischen Codices und Artikelnummern
   - Zeigt für jede Artikelnummer, ob sie in der Open Order List gefunden wurde
   - Enthält zusätzliche Informationen aus der Top-50-Liste (Lagerbestand, etc.)
   - Klicken Sie auf "Zusammenfassungsdatei herunterladen", um die Datei zu speichern

## Fehlerbehebung

### Problem: Die Dateien werden nicht akzeptiert

**Mögliche Ursachen und Lösungen:**
- **Falsches Dateiformat**: Stellen Sie sicher, dass alle Dateien im Excel-Format (.xlsx) vorliegen
- **Unerwartetes Dateiformat**: Prüfen Sie, ob die Struktur der Dateien dem erwarteten Format entspricht:
  - Top-50: Muss Spalte "Codice" und andere relevante Spalten enthalten
  - Übersetzungsdatei: Muss mindestens 17 Spalten haben
  - Open Order List: Muss Spalte "artikel no" enthalten

### Problem: Die App zeigt einen Fehler während der Verarbeitung

**Mögliche Ursachen und Lösungen:**
- **Inkonsistente Daten**: Prüfen Sie, ob die Daten in den Dateien konsistent sind
- **Unerwartetes Format in Zellen**: Stellen Sie sicher, dass die Zellen den erwarteten Datentyp enthalten

Bei anhaltenden Problemen wenden Sie sich bitte an den IT-Support.

---

## Kontakt

Bei Fragen oder Problemen wenden Sie sich bitte an:
support@eberle-it.de 