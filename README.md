# Eberle Artikelnummern-Matching-App

Eine Streamlit-Anwendung zur Automatisierung des Abgleichs von Artikelnummern zwischen Eberle Deutschland und Eberle Italien.

## Funktionen

- Automatischer Abgleich von Artikelnummern zwischen verschiedenen ERP-Systemen
- Verarbeitung von drei Excel-Dateien: Top-50, Übersetzungsdatei und Open Order List
- Erzeugung einer markierten Open Order List mit hervorgehobenen passenden Artikelnummern
- Erzeugung einer Zusammenfassungsdatei mit den Verbindungen zwischen Codices und Artikelnummern

## Installation

```bash
# Repository klonen oder Dateien herunterladen

# Abhängigkeiten installieren
pip install -r requirements.txt
```

## Verwendung

```bash
# Streamlit-App starten
streamlit run app.py
```

1. Laden Sie die drei Excel-Dateien hoch:
   - Top-50 Liste (Eberle Italia)
   - Übersetzungsdatei
   - Open Order List (Eberle Deutschland)
2. Klicken Sie auf "Verarbeiten", um den Abgleich zu starten
3. Laden Sie die erzeugten Dateien herunter:
   - Markierte Open Order List
   - Zusammenfassungsdatei

## Projektstruktur

```
├── app.py                   # Hauptanwendungsdatei (Streamlit-App)
├── utils/                   # Hilfsfunktionen
│   ├── __init__.py
│   ├── data_processing.py   # Datenverarbeitungsfunktionen
│   └── file_utils.py        # Dateioperationen
├── requirements.txt         # Abhängigkeiten
└── README.md                # Diese Datei
```

## Anforderungen

- Python 3.10+
- Streamlit
- Pandas
- Openpyxl
- XlsxWriter 