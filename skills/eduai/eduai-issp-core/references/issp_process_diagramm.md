# Skill: ISSP Process Diagram

## Zweck

Dieses Skill File enthält die kanonische Mermaid-Darstellung des ISSP-Prozesses.

Es ist zu verwenden, wenn Nutzer:innen nach einer grafischen Darstellung, einem Prozessdiagramm, einer Prozessübersicht, einer Visualisierung, einem Mermaid-Diagramm oder einer Darstellung des ISSP-Ablaufs fragen.


## Trigger

Verwende dieses Skill insbesondere bei Nutzerformulierungen wie:

- „Zeig mir den Prozess grafisch“
- „Kannst du den ISSP-Prozess als Diagramm darstellen?“
- „Gib mir das Mermaid-Diagramm“
- „Visualisiere den Curriculumsprozess“
- „Ich brauche eine Prozessgrafik“
- „Wie sieht der Ablauf aus?“
- „Stelle den Prozess als Flowchart dar“
- „Gib mir eine grafische Übersicht“
- „Kannst du den Prozess in Mermaid ausgeben?“

## Antwortregel

Wenn nach einer grafischen Darstellung gefragt wird:

1. Gib eine kurze Einleitung.
2. Gib das Mermaid-Diagramm in einem `mermaid`-Codeblock aus.
3. Verändere die Prozesslogik nicht.
4. Kürze das Diagramm nicht, ausser Nutzer:innen verlangen ausdrücklich eine vereinfachte Darstellung.
5. Wenn zusätzlich eine Erklärung gewünscht wird, erkläre danach kurz die Hauptbereiche:
   - Information / Inputs
   - Curriculum-Kernprozess
   - Governance Studienordnung
   - Implementierung und Start Betrieb
   - Qualitätsmerkmale

## Sprache

Übersetze das Diagramm nach Englisch, wenn die Anfrage in Englisch gestellt wurde. Verändere keine Inhalte und erfinde keine Begriffe. Wenn es keine klare Übersetzung gibt, mach dies kenntlich.

## Hinweis zum MCP

Wenn der globale System Prompt für jede Nutzerfrage eine MCP-Abfrage verlangt, führe auch bei Diagrammfragen eine kurze MCP-Abfrage zur Prozessübersicht durch. Die kanonische Diagramm-Ausgabe selbst stammt jedoch aus diesem Skill File.

## Kanonisches Mermaid-Diagramm

```mermaid
flowchart TD

    subgraph info["Information"]
        %% Inputs
        I1["1.1 Berufsfeldanalyse,<br/>Zukunftsperspektiven etc."]
        I2["1.1 Daten aus Qualitätsmanagement<br/>Studium und Lehre"]
    end

    %% Qualitätsmerkmale
    QM["1.2 Qualitätsmerkmale"]

    %% Kernprozess
    subgraph CP["Curriculumsprozess <br/>Studienprogrammverantwortliche/Studiendekanate (ISSP-Begleitung durch LE und SLS)"]
        K1["1. Kontextanalyse und strategische Ausrichtung"]
        subgraph EB["Entwicklung Bildungsrevision"]
            K2["2. Absolvierenden-/<br/>Qualifikationsprofil"]
            K3["3. Kompetenzraster/<br/>übergeordnete Lernziele"]
            K4["4. Modularisierungskonzept<br/>Programmstruktur"]
        end
        subgraph CFO["Curriculare Formalisierung<br/>und Operationalisierung"]
            K5["5. Modulübersicht<br/>Bestehensvoraussetzungen"]
            K6["6. Mustercurriculum"]
            K7["7. Übergangsregelungen"]
            K8["8. Modulkoordination"]
            K9["9. Modulkatalog<br/>(Modulinhalte, -voraussetzungen"]
        end
        O["Implementierung und Start Betrieb"]
    end

    %% Governance
    subgraph G1["Erarbeitungsprozess<br/>Studienordnung"]
      E1["Fakultät: Grundsatzentscheid"]
      E2["Tangierte Fakultäten: Überfakultäre Abstimmung"]
      E3["Studiendek.-Gespräch: Empfehlung"]
      E4["Fakultät: Entwurf Studienordnung"]
      E5["Lehrentwicklung: Rechtskonformitätsprüfung"]
    end

    subgraph G2["Erlassprozess<br/>Studienordnung"]
      E6["Fakultätsversammlung: Erlass (unter Vorbehalt Genehmigung Erweiterte Universitätsleitung (EUL))"]
      E7["Prorektorat Lehre und Studium.: Traktandiert in Universitätsleitung (UL)"]
      E8[UL: Kenntnisnahme]
      E9[EUL: Genehmigung]
    end

    %% Input-Kernprozess
    I1 --> K1
    I2 --> K1

    %% Kernprozess
    K1 --> K2
    K2 --> K3
    K3 --> K4
    K4 --> K5
    K5 --> K6
    K6 --> K7
    K7 --> K8
    K8 --> K9

    %% Übergang Kernprozess-Governance
    K3 --> E1
    K4 --> E2
    K5 --> E4
    K7 --> E4

    %% Erarbeitungsprozess StudO
    E1 --> E2
    E2 --> E3
    E3 --> E4
    E4 --> E5

    %% Erlassprozess StudO
    E5 --> E6
    E6 --> E7
    E7 --> E8
    E8 --> E9

    %% Outputs
    E9 --> O
    K9 --> O

    %% Qualitätsmerkmale gelten für den gesamten Kernprozess
    QM --> CP

    %% Styles für Subgraph Container Hintergründe (Füllung + Rand):
    style info fill:#f7b6d2,stroke:#d6709f,stroke-width:2px,color:#000
    style CP fill:#aec7e8,stroke:#7da8d9,stroke-width:2px,color:#000
    style G1 fill:#2ca02c,stroke:#20721c,stroke-width:2px,color:#fff
    style G2 fill:#2ca02c,stroke:#20721c,stroke-width:2px,color:#fff

    %% Knoten Styles
    style QM fill:#1f77b4,stroke:#0f4c8c,stroke-width:2px,color:#fff
    style I1 fill:#f7b6d2,stroke:#d6709f,color:#000
    style I2 fill:#f7b6d2,stroke:#d6709f,color:#000

    style CFO fill:#aec7e8,stroke:#7da8d9,color:#000
    style EB fill:#aec7e8,stroke:#7da8d9,color:#000
    style K1 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K2 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K3 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K4 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K5 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K6 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K7 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K8 fill:#aec7e8,stroke:#7da8d9,color:#000
    style K9 fill:#aec7e8,stroke:#7da8d9,color:#000
    style O  fill:#aec7e8,stroke:#7da8d9,color:#000

    style E1 fill:#2ca02c,stroke:#20721c,color:#fff
    style E2 fill:#2ca02c,stroke:#20721c,color:#fff
    style E3 fill:#2ca02c,stroke:#20721c,color:#fff
    style E4 fill:#2ca02c,stroke:#20721c,color:#fff
    style E5 fill:#2ca02c,stroke:#20721c,color:#fff
    style E6 fill:#2ca02c,stroke:#20721c,color:#fff
    style E7 fill:#2ca02c,stroke:#20721c,color:#fff
    style E8 fill:#2ca02c,stroke:#20721c,color:#fff
    style E9 fill:#2ca02c,stroke:#20721c,color:#fff

    %% Pfeilfarbe global definieren
    linkStyle default stroke:#333,stroke-width:2px
```