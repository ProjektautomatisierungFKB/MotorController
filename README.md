# MotorController

## Übersicht

Das Projekt implementiert einen Drive Controller, der die Steuerung eines Roboterantriebs ermöglicht. Es umfasst folgende Hauptkomponenten:

1. **DriveController**: Hauptmodul für Fahrfunktionen.
2. **MotorMQTTClient**: Schnittstelle zur MQTT-Kommunikation.
3. **ServoController**: Steuert einzelne Servomotoren.
4. **Main-Skript**: Startet und verwaltet die Anwendung.

---

## Funktionen

### DriveController

Die Klasse steuert die Bewegungen des Roboters durch die Servos der Räder:

- **Idle**: Stoppt alle Räder.
- **Vorwärts/Rückwärts**: Setzt die Servos für die Bewegung des Roboters vorwärts oder rückwärts.
- **Links/Rechts fahren**: Ermöglicht seitliche Bewegungen.
- **Links/Rechts drehen**: Dreht den Roboter an Ort und Stelle.

### MotorMQTTClient

Verarbeitet eingehende MQTT-Befehle zur Steuerung des Roboters:

- **Topics**:

  - **Subscribe Topics**:
    - `robotX/logic/control/input/manual`: Empfängt manuelle Steuerbefehle wie `UP`, `DOWN`, `LEFT`, `RIGHT`, `nil` (Idle).
  - **Publish Topics**:
    - Keine Publish-Themen definiert.

- **Nachrichtenverarbeitung**:

  - MQTT-Nachrichten werden basierend auf dem Payload-Content an den `DriveController` delegiert.

### ServoController

Die Klasse steuert individuelle Servomotoren über GPIO-Pins:

- **Funktionen**:
  - **Idle**: Stoppt den Servo.
  - **Drehen**:
    - Im Uhrzeigersinn (clockwise).
    - Gegen den Uhrzeigersinn (counter-clockwise).

### Main-Skript

Das Hauptskript:

- Initialisiert den `MotorMQTTClient` mit den GPIO-Pins der Räder.
- Verbindet sich mit dem MQTT-Broker.
- Startet die Hauptschleife, um kontinuierlich Nachrichten zu empfangen und zu verarbeiten.

---

## Externe Schnittstellen

### Data Transfer Objects (DTOs)

- **MQTT-Payloads**:
  - `nil`: Stoppt den Roboter.
  - `UP`, `DOWN`: Bewegt den Roboter vorwärts oder rückwärts.
  - `LEFT`, `RIGHT`: Steuert seitliche Bewegungen.

### APIs

- **MQTT**:

  - Verbindung zu MQTT-Broker Mosquito auf definiertem Host und Port.

- **GPIO**:

  - Steuerung der Servos erfolgt über die Bibliothek `gpiozero`.

---

## Interne Architektur

### Komponenten

1. **DriveController**:

   - Kernmodul für die Bewegungslogik.

2. **MotorMQTTClient**:

   - Bindeglied zwischen MQTT-Befehlen und dem DriveController.

3. **ServoController**:

   - Low-Level-Kontrolle einzelner Servomotoren.

### Abhängigkeiten

- **Logger**: Zum Debuggen und Verfolgen der Bewegungslogik.
- **gpiozero**: Für die Hardwaresteuerung der Servos.

### Datenfluss

1. MQTT-Nachrichten werden im `MotorMQTTClient` empfangen.
2. Nachrichten werden an den `DriveController` weitergeleitet.
3. Der `DriveController` sendet Steuerbefehle an die `ServoController` der einzelnen Räder.

---

## Entwicklerdokumentation

### Nutzung interner Bibliotheken

- **gpiozero**:

  - Wird zur Steuerung der GPIO-Pins für die Servomotoren verwendet.
  - Dokumentation: [GPIO Zero](https://gpiozero.readthedocs.io/)

- **Logger**:

  - Zum Protokollieren von Bewegungsbefehlen und Statusmeldungen.

### Designentscheidungen

1. **Trennung von Bewegungs- und Kommunikationslogik**:

   - Der `DriveController` fokussiert sich auf die Steuerung, während der `MotorMQTTClient` ausschließlich für die Kommunikation verantwortlich ist.

2. **Modularität**:

   - Jeder Servo wird unabhängig über den `ServoController` gesteuert.

3. **Erweiterbarkeit**:

   - Zusätzliche Bewegungsmuster können leicht durch neue Methoden im `DriveController` implementiert werden.

### Hinweise für Entwickler

- Passen Sie die GPIO-Pins entsprechend der Hardwarekonfiguration an.
- Testen Sie die Bewegungslogik zunächst in einer simulierten Umgebung oder mit Debugging-Ausgaben.
- Beachten Sie die Stromanforderungen der Servos, insbesondere bei gleichzeitiger Bewegung mehrerer Motoren.

