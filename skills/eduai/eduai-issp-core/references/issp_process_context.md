# Skill: ISSP Process Context

## Zweck

Dieses Skill File enthält die verbindlichen Kontexttexte zum Integrierten Supportprozess Studienprogrammentwicklung (ISSP).

Es dient dazu, sicherzustellen, dass der Agent vor jeder Antwort den passenden Introtext zum relevanten Prozessschritt, zur Prozessphase und ggf. zum Qualitätsmerkmal berücksichtigt.

Dieses Skill File ist zusätzlich zu verwenden zu:

- `issp-process-router` für die Prozessverortung,
- MCP-Retrieval für Detailinformationen aus der Dokumentbasis,
- Glossar-Skill für verbindliche Terminologie.

## Verbindliche Nutzungsregel

Vor jeder inhaltlichen Antwort muss der Agent:

1. die Nutzerfrage im ISSP-Prozess verorten,
2. den primären Prozessschritt bestimmen,
3. ggf. sekundäre Prozessschritte bestimmen,
4. die zugehörigen Introtexte aus diesem Skill File konsultieren,
5. bei Qualitätsfragen zusätzlich die relevanten Qualitätsmerkmale konsultieren,
6. danach eine MCP-Abfrage durchführen,
7. danach ggf. das Glossar für Terminologie konsultieren,
8. erst danach die finale Antwort formulieren.

Der Agent darf eine Frage nicht allein auf Basis des MCP-Retrievals beantworten, wenn der passende Prozess-Introtext nicht berücksichtigt wurde.

## Rolle der Introtexte

Die Introtexte liefern den verbindlichen Prozessrahmen.

Sie beantworten insbesondere:

- Worum geht es in diesem Prozessschritt?
- Welche Funktion hat der Schritt im Gesamtprozess?
- Welche typischen Inhalte und Outputs gehören dazu?
- Wie hängt der Schritt mit vorherigen und nachfolgenden Schritten zusammen?
- Welche Qualitätsmerkmale sind relevant?

Die Introtexte ersetzen nicht das MCP-Retrieval.
Das MCP-Retrieval liefert Detailinformationen, Beispiele, Dokumentstellen und operative Konkretisierungen.

## Antwortverhalten

Die finale Antwort muss den Introtext nicht immer zitieren.

Aber die Antwort muss mit dem Introtext konsistent sein.

Wenn Nutzer:innen direkt nach Bedeutung, Zweck, Rolle, typischen Outputs oder Einordnung eines Prozessschritts fragen, soll der Introtext explizit genutzt und bei Bedarf nah am Wortlaut wiedergegeben werden.

## Standard-Ablauf

Bei jeder Nutzerfrage:

1. Prozessrouting:
   - primärer Prozessschritt,
   - sekundäre Prozessschritte,
   - Qualitätsmerkmale,
   - Governance-Bezüge.

2. Kontextauswahl:
   - globale Introtexte,
   - Phasenintro,
   - Prozessschritt-Intro,
   - ggf. Qualitätsmerkmal-Intro.

3. MCP-Retrieval:
   - Suchanfrage mit Prozessschritt, Artefakten, Nutzerbegriffen, Synonymen und ggf. Qualitätsmerkmalen.

4. Glossarprüfung:
   - korrekte Begriffe,
   - Abgrenzungen,
   - Synonyme.

5. Antwort:
   - Prozessverortung,
   - relevante Artefakte,
   - MCP-Erkenntnisse,
   - prozessbezogene Antwort,
   - nächster sinnvoller Schritt.

**WICHTIG**: Kürzel wie K1, E4, O oder QM dürfen nie ausgegeben werden, sie dienen nur für interne Abstimmung der Prozessschritte!

---

# Auswahlregeln für Introtexte

## Immer zu berücksichtigen

Bei jeder Nutzerfrage sind diese globalen Texte als übergeordneter Rahmen relevant:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`

Falls die Antwort sehr kurz sein soll, müssen diese Texte nicht sichtbar referenziert werden, aber sie sind als Rahmen mitzudenken.

## Prozessschritt-Mapping

### K1 Kontextanalyse und strategische Ausrichtung

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `K1: Kontextanalyse und strategische Ausrichtung`

### K2 Absolvierenden-/Qualifikationsprofil

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Entwicklung Bildungsvision`
- `K2: Absolvierenden-/Qualifikationsprofil`

### K3 Kompetenzraster / übergeordnete Lernziele

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Entwicklung Bildungsvision`
- `K3: Kompetenzraster / übergeordnete Lernziele`

### K4 Modularisierungskonzept / Programmstruktur

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Entwicklung Bildungsvision`
- `K4: Modularisierungskonzept – Programmstruktur`

### K5 Modulübersicht / Bestehensvoraussetzungen

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Curriculare Formalisierung und Operationalisierung`
- `K5: Modulübersicht und Bestehensvoraussetzungen`

### K6 Mustercurriculum

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Curriculare Formalisierung und Operationalisierung`
- `K6: Mustercurriculum`

### K7 Übergangsregelungen

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Curriculare Formalisierung und Operationalisierung`
- `K7: Übergangsregelungen`

### K8 Modulkoordination

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Curriculare Formalisierung und Operationalisierung`
- `K8: Modulkoordination`

### K9 Modulkatalog

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Curriculare Formalisierung und Operationalisierung`
- `K9: Modulkatalog`

### O Implementierung und Start Betrieb

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `O: Implementierung und Start Betrieb`

## Qualitätsfragen

Wenn eine Nutzerfrage ein Qualitätsmerkmal betrifft, ist zusätzlich das passende Qualitätsmerkmal zu konsultieren.

Qualitätsmerkmale:

- `QM: Studierbarkeit`
- `QM: Curriculare Operationalisierbarkeit`
- `QM: Kohärenz der Prozess-Elemente`
- `QM: Fachliche und berufsfeldrelevante Begründbarkeit`
- `QM: Wissenschaftlichkeit`
- `QM: Handlungsorientierung / Handlungskompetenzorientierung`
- `QM: Nutzung systematischer Qualitätsprozesse`
- `QM: Einbezug relevanter Querschnittsthemen`

Beispiel:

Nutzerfrage:
„Wie stellen wir sicher, dass die Bestehensvoraussetzungen studierbar bleiben?“

Zu konsultieren:

- `GLOBAL: ISSP Gesamtüberblick`
- `GLOBAL: Curriculumprozess`
- `PHASE: Curriculare Formalisierung und Operationalisierung`
- `K5: Modulübersicht und Bestehensvoraussetzungen`
- `QM: Studierbarkeit`
- ggf. `QM: Curriculare Operationalisierbarkeit`

## Governance-Fragen

Wenn eine Frage Studienordnung, Rechtsgrundlagen, Erlass, Genehmigung, Rechtskonformitätsprüfung oder Übergangsregelungen betrifft:

1. Den passenden Curriculumprozessschritt konsultieren.
2. Governance-Routing anwenden.
3. MCP-Retrieval für rechtlich-reglementarische Details durchführen.
4. Keine verbindliche Rechtsberatung geben.

Beispiele:

- Bestehensvoraussetzungen in der Studienordnung → K5 + Governance E4/E5
- Übergangsbestimmungen → K7 + Governance E4/E5
- Genehmigung Studienordnung → Governance E6–E9 + O

---

# Kanonische Introtexte

Die folgenden Texte sind die verbindlichen Introtexte für Prozessrahmen, Prozessschritte und Qualitätsmerkmale.

Sie sollen nicht paraphrasiert werden, wenn Nutzer:innen ausdrücklich nach Definition, Zweck oder Beschreibung eines Prozessschrittes fragen.

---

## GLOBAL: ISSP Gesamtüberblick

Integrierter Supportprozess Studienprogrammentwicklung (ISSP) – Gesamtüberblick

Der integrierte Supportprozess Studienprogrammentwicklung (ISSP) bietet den Studienprogrammverantwortlichen und den Studiendekanaten Unterstützung bei der Neu- und Weiterentwicklung von Studienprogrammen. Er verbindet die fachlich-akademische Gestaltung von Studienprogrammen mit hochschuldidaktischen, rechtlich-reglementarischen und technisch-administrativen Anforderungen.

Grundlage für die verschiedenen Unterstützungsmöglichkeiten bildet ein idealtypischer Ablauf für den curricularen Entwicklungsprozess von Studienprogrammen, der auf wichtigen Qualitätsmerkmalen von Curricula beruht und mit dem Erarbeitungs- und Erlassprozess der Rechtsgrundlagen eines Studienprogramms verknüpft ist.

Vor diesem Hintergrund lassen sich massgeschneiderte Unterstützungsangebote bestimmen, die fachliche Besonderheiten und die spezifischen fakultären Rahmenbedingungen optimal berücksichtigen.

---

## GLOBAL: Curriculumprozess

Im Prozess der Curriculumentwicklung soll aus einer strategisch überzeugenden Idee ein studierbares Studienangebot entstehen. Curriculumentwicklung ist daher idealerweise ein Prozess schrittweiser Konkretisierung. Ausgehend von einer strategischen Vision führt er zunächst über fachliche und didaktische Konkretisierungen und anschliessend über konkrete curriculare Formalisierungen hin zu regulatorischen Entscheidungen, die in die organisatorische, rechtliche und technische Umsetzung des Studienangebots münden, bevor das Studienangebot in einem Evaluations- und Weiterentwicklungsprozess kontinuierlich verbessert und neuen Gegebenheiten angepasst werden kann.

Vier Phasen strukturieren den Entwicklungs- bzw. Implementierungsprozess, wobei durch die Übergänge eine zunehmende Verdichtung bzw. Formalisierung der curricularen Grundidee stattfindet. Damit nehmen die Freiheitsgrade zusehends ab: während am Anfang die Möglichkeiten erkundet werden, werden später Entscheidungen getroffen und verbindlich implementiert.

---

## K1: Kontextanalyse und strategische Ausrichtung

Die strategische Verortung definiert die äusseren Rahmenbedingungen und Zielsetzungen des Studienangebots. Sie hat insbesondere die Frage beantwortet, weshalb ein neues Studienangebot geschaffen werden soll, welche Zielgruppen adressiert werden und welche Position das Angebot innerhalb der institutionellen Angebotslandschaft einnehmen soll.

Als Grundlage für den Ausarbeitungsprozess eines Studienprogramms ist zu klären, in welchem Umfeld ein Studienprogramm entsteht und wie es sich strategisch positioniert. Ausgangspunkt sind neben fachwissenschaftlichen Überlegungen gesellschaftliche und bildungspolitische Entwicklungen, Berufsfeldanalysen, strategische Ausrichtungen der UZH und der beteiligten Fakultäten sowie bereits bestehende Studienangebote. Es geht darum, die fachlichen, institutionellen und ressourcenbezogenen Rahmenbedingungen zu prüfen und Ziele zu umschreiben, die mit dem Programm verfolgt werden sollen. Diese Kontuierung des Programms berücksichtigt insbesondere Aspekte der Profilbildung, Internationalisierung, Interdisziplinarität oder die Erschliessung neuer Zielgruppen.

Typische Themen sind etwa die Berufsmöglichkeiten der Absolvent:innen, die Einordnung in das UZH-Curriculum, der Vergleich mit bestehenden Studienprogrammen (Unterschiede, Überlappungen, Ergänzungen), die Charakterisierung der Studieninteressierten sowie Überlegungen zum Schwerpunkt des Programms, z. B. Nähe zur Forschung oder zu inter-/transdisziplinären Kompetenzen. Dazu können auch Praxispartner aus relevanten Berufsfeldern mit einbezogen werden.

Zentrale Outputs sind eine schriftlich festgehaltene Ausgangslage mit strategischer Begründung, eine klare Positionierung des Programms im Angebotsportfolio der Fakultät und erste, grob umrissene Ziele, die in den weiteren Prozessschritten genutzt werden können.

---

## PHASE: Entwicklung Bildungsvision

Auf der Kontextanalyse und der strategischen Ausrichtung aufbauend, wird in der zweiten Phase des Curriculumprozesses die eigentliche Bildungsvision entwickelt. Die strategischen Zielsetzungen werden nun in ein fachliches, wissenschaftliches und didaktisches Zielbild übersetzt. Aus institutionellen Erwartungen entstehen Vorstellungen darüber, welche Kompetenzen Absolvent:innen erwerben sollen, welches Bildungsverständnis dem Studienangebot zugrunde liegt und welche fachlichen Inhalte und Qualifikationsbestandteile (Aufteilung des Qualifikationsprofils in Qualifikationsbestandteile – Modularisierung) dafür relevant sind.
Die Bildungsvision beschreibt zunächst primär inhaltliche und didaktische Zielvorstellungen und konkretisiert sie einem Entwurf zu den Modulen und Leistungsnachweisen.

---

## K2: Absolvierenden-/Qualifikationsprofil

Das Absolvierenden- bzw. Qualifikationsprofil beschreibt, welche Kompetenzen, Kenntnisse, Fertigkeiten und Haltungen Studierende am Ende des Studienprogramms erworben haben sollen. Es ist der zentrale Ausgangspunkt für die Gewährleistung des Constructive Alignment: Die Programmstruktur, Module, Lehr-/Lernformen und Leistungsnachweise werden konsequent in Beziehung gesetzt und aufeinander abgestimmt.

Inhaltlich geht es darum zu klären, für welche beruflichen und wissenschaftlichen Handlungsfelder das Programm qualifiziert und in welchen typischen Situationen Absolvent:innen ihr Wissen und Können einsetzen. Grundlage bilden Analysen relevanter Berufsfelder, wissenschaftliche und gesellschaftliche Trends, die strategischen Ziele und Ressourcen der involvierten Organisationseinheiten sowie Anforderungen des Arbeitsmarktes und der Forschung. Ein gutes Qualifikationsprofil benennt zentrale Kompetenzbereiche, macht Alleinstellungsmerkmale sichtbar und beschreibt die Anschlussfähigkeit an weiterführende Studienangebote oder berufliche Tätigkeiten.

Erarbeitet wird das Profil vor allem von der Studienprogrammdirektion und Fachvertreter:innen, idealerweise unter Einbezug von Praxispartnern, Alumni, Studierenden und dem Studiendekanat.

Der typische Output ist eine konsistente Darstellung (z. B. auch für Kommunikationsunterlagen) der Qualifikationsziele. Sie dient als Referenz für alle weiteren curricularen Entscheidungen.

---

## K3: Kompetenzraster / übergeordnete Lernziele

Aufbauend auf dem Qualifikationsprofil werden im nächsten Schritt übergeordnete Lernziele und ein Kompetenzraster entwickelt. Ziel ist es, die angestrebten Kompetenzen systematisch zu strukturieren und über den Studienverlauf hinweg zu operationalisieren. Damit wird die Kompetenzorientierung des Programms konkret: Nicht Inhalte stehen im Zentrum, sondern die Fähigkeit der Studierenden, sich in realen Handlungssituationen zu bewähren.

Das Kompetenzraster ordnet die wesentlichen Kompetenzbereiche (z.B. Fach-, Methoden-, Sozial- und Personalkompetenz sowie fachspezifische wissenschaftliche Handlungskompetenzen) und verortet sie über Semester, Studienphasen oder Modulgruppen hinweg. Übergeordnete Lernziele formulieren, was Absolvent:innen auf Programmebene können sollen; sie werden später in Modulzielen und Leistungsnachweisen weiter ausdifferenziert. Querschnittsthemen wie etwa wissenschaftliches Arbeiten, Digitalisierung oder Nachhaltigkeit können im Raster als durchgehende Entwicklungsstränge sichtbar gemacht werden.

Die Ausarbeitung erfolgt durch die Studienprogrammdirektion gemeinsam mit den verantwortlichen Lehrenden der Module, um Kohärenz und studierbare Progression sicherzustellen.

Als Output entsteht ein programm-spezifisches Kompetenzraster (häufig in Form einer Matrix) mit klar formulierten übergeordneten Lernzielen. Dieses dient als verbindliche Referenz für Programmstruktur, Modulplanung und die Ausgestaltung des Mustercurriculums und unterstützt die Qualitätsentwicklung im Sinne des Constructive Alignment.

---

## K4: Modularisierungskonzept – Programmstruktur

In diesem Prozessschritt wird die äussere Struktur des Studienprogramms bestimmt. Die Programmstruktur und das Modularisierungskonzept legen fest, wie Module zugeschnitten, gruppiert und zueinander in Beziehung gesetzt werden, sodass das Qualifikationsprofil und das Kompetenzraster im Aufbau des Curriculums sichtbar und umsetzbar werden.

Typische Inhalte sind die Definition von Modultypen (Pflicht-, Wahlpflicht-, Wahlmodule), von Modulgrössen und -rhythmen sowie die Festlegung von Programmdimensionen, entlang derer die Module geordnet werden – etwa inhaltliche Bereiche, Studienverlauf (Studienstufen, Studienjahre), Profil- oder Schwerpunktbereiche. Die gewählten Strukturierungsprinzipien beeinflussen, wie gut Studierende sich orientieren können, wie klar das Profil des Programms erkennbar ist und wie tragfähig die studienorganisatorische Umsetzung gelingt.

Als Output entsteht ein konsistentes Modularisierungskonzept mit einer geordneten Programmstruktur (Modulgruppen, Modultypen, Zuordnung zu Inhalts- und Verlaufsdimensionen). Dieses bildet die Basis für Modulübersicht, Bestehensvoraussetzungen, Mustercurriculum und die technische Umsetzung im Modulkatalog.

---

## PHASE: Curriculare Formalisierung und Operationalisierung

Damit aus der Bildungsvision ein studierbares und institutionell betreibbares Curriculum entstehen kann, müssen die Zielvorstellungen in einem Operationalisierungsschritt formalisiert werden. In der dritten Phase des Curriculumprozesses werden die Ergebnisse aus der fachlichen und didaktischen Beschäftigung mit dem Studienprogramm deshalb schrittweise in curriculare Strukturen übersetzt. Dabei wird in der Beschäftigung mit den Dimensionen entschieden, wie die Module des Curriculums gegliedert werden sollen (Inhaltsdimension, Verlaufsdimension) und ob bzw. wie stark das Studium gesteuert werden soll (Modultypen, Bestehensvoraussetzungen und ggf. Aufstufungsvoraussetzungen). Modellierungsmuster helfen, die für das Studienprogramm geeigneten Entscheidungen zu treffen. Ziel ist es, das Studienangebot eine transparente, abbildbare und studierbare Form zu giessen. Der Übergang von der Ausarbeitung der Bildungsvision zu deren Operationalisierung ist aber nicht trennscharf. Die verschiedenen Entwicklungsschritte sind mit einander verzahnt und verweisen aufeinander.

---

## K5: Modulübersicht und Bestehensvoraussetzungen

Die Modulübersicht und die Bestehensvoraussetzungen übersetzen Modularisierungskonzept und erste Überlegungen zur Programmstruktur in klare, überprüfbare Regeln. Die Modulübersicht zeigt, welche Module zum Studienprogramm gehören, wie sie Modulgruppen, Inhaltsbereichen, Studienstufen oder Profilbereichen zugeordnet sind und welche Rolle sie im Kompetenzaufbau spielen.

Die Bestehensvoraussetzungen formulieren die formalen Bedingungen für den erfolgreichen Abschluss des Programms. Dazu gehören etwa: welche Pflichtmodule zu absolvieren sind, wie viele ECTS aus bestimmten Inhalts- oder Modulgruppen erforderlich sind, allfällige Mindestnoten sowie – bei gestuften Curricula – Aufstufungsvoraussetzungen zwischen Studienabschnitten. Über diese Regeln wird gesteuert, welche inhaltlichen Mindeststandards alle Studierenden erfüllen und wie viel Spielraum für individuelle Profilbildung bleibt.

Erarbeitet werden Modulübersicht und Bestehensvoraussetzungen von der Studienprogrammdirektion in Abstimmung mit Fachvertreter:innen, Studiendekanat, Rechtsdienst und Studienadministration.

Der Output sind eine vollständige Modulübersicht (oft tabellarisch) und juristisch belastbare Bestehensvoraussetzungen, die in der Studienordnung verankert und in Wegleitungen sowie Studienplanungstools sichtbar gemacht werden.

---

## K6: Mustercurriculum

Das Mustercurriculum beschreibt einen idealtypischen Studienverlauf über die Semester hinweg. Es zeigt, in welcher Abfolge Studierende die Module sinnvollerweise belegen, damit der Wissens- und Kompetenzaufbau systematisch, studierbar und mit vertretbarem Workload erfolgt.

Inhaltlich umfasst das Mustercurriculum die zeitliche Verortung der Module und Modulgruppen, Empfehlungen zu sinnvollen Modulabfolgen (sowie gegebenenfalls die Ausweisung von Mobilitätsfenstern und Bereichen für Profilbildung. Es ist damit ein zentrales Instrument, um Progression sichtbar zu machen und Überlastung oder „Prüfungsballungen“ zu vermeiden.

Der typische Output ist ein nach Semestern gegliedertes Mustercurriculum (bzw. Regelcurriculum bei formaler Stufung), das intern als Grundlage für die Koordination von Lehrangebot und Leistungsnachweisen dient und extern Studierenden zur Studienplanung kommuniziert wird.

---

## K7: Übergangsregelungen

Übergangsregelungen werden immer dann relevant, wenn ein bestehendes Studienprogramm geändert oder ersetzt wird. Sie stellen sicher, dass Studierende, die nach alter Ordnung begonnen haben, ihr Studium unter fairen, transparenten und rechtlich sicheren Bedingungen abschliessen können.

Inhaltlich klären Übergangsregelungen, wie bisher erbrachte Leistungen angerechnet werden, welche alten Module durch welche neuen ersetzt werden können, bis wann die alte Ordnung gilt, ob es Parallelangebote gibt und welche besonderen Fristen oder Sonderregelungen für Studierende in unterschiedlichen Studienphasen gelten. Sie adressieren damit sowohl fachlich-curriculare Anschlüsse als auch administrative und rechtliche Fragen.

---

## K8: Modulkoordination

Modulkoordination stellt sicher, dass die einzelnen Module eines Studienprogramms inhaltlich, didaktisch und organisatorisch zusammenwirken und gemeinsam die Qualifikationsziele erreichen helfen. Sie verbindet Programmebene (Kompetenzraster, Programmstruktur) und Modulebene (Modulcurricula, Leistungsnachweise).

Typische Inhalte dieses Schrittes sind die Abstimmung von Modulzielen mit den übergeordneten Lernzielen, die Koordination von Lehr-Lern-Formen und Leistungsnachweisen über die Module hinweg, die Verteilung von Arbeitsbelastung und Prüfungen im Semester, die Identifikation und Gestaltung von Kern- und Integrationsmodulen sowie die Sichtbarmachung von Querschnittsthemen. Modulbeschreibungen dienen dabei als zentrale Grundlage für Abstimmung und Reflexion.

Typische Outputs sind abgestimmte Modulbeschreibungen, interne Übersichten über Lernziele und Leistungsnachweise (z.B. entlang des Mustercurriculums), vereinbarte Koordinationsmechanismen (Regeltermine, Gremien) sowie dokumentierte Absprachen zu Kernmodulen und Prüfungsformaten.

---

## K9: Modulkatalog

Der Modulkatalog ist die konsolidierte, veröffentlichte Gesamtschau aller Module, die im Rahmen eines oder mehrerer Studienprogramme angeboten werden. Er macht das Modularisierungskonzept operativ sichtbar und ist eine zentrale Informationsquelle für Studierende, Lehrende und Administration.

Inhaltlich enthält der Modulkatalog für jedes Modul formale Angaben (Titel, ECTS, Angebotsrhythmus, Sprache, Modultyp, Zuordnung zu Programmen und Inhaltsbereichen), die Modulziele und eine Kurzbeschreibung von Inhalten, Lehr- und Prüfungsformen sowie Angaben zu Teilnahme- und Bestehensvoraussetzungen. Die Art der Darstellung – z.B. Gruppierung nach Inhaltsbereichen oder nach Studienverlauf – folgt den gewählten Programmdimensionen und unterstützt die Studienplanung.

Die Inhalte werden von den Modulverantwortlichen erstellt und von der Studienprogrammdirektion hinsichtlich Passung zu Programmzielen und Struktur überprüft; die Studienadministration und das Prorektorat Lehre und Studium sorgen für die korrekte technische Abbildung in den Systemen (Vorlesungsverzeichnis, Studienfortschritts-Apps etc.).

Als Output entsteht ein konsistenter, digital verfügbarer Modulkatalog, der eng mit der Studienordnung und den Bestehensvoraussetzungen verknüpft ist. Er bildet die Grundlage für Einschreibung, Studienverlaufsplanung, Monitoring des Studienfortschritts und die Qualitätssicherung der Lehre.

---

## O: Implementierung und Start Betrieb

Mit der curricularen Formalisierung liegt ein strukturell konsistentes und operationalisierbares Curriculum vor. Dieses muss nun in die institutionelle Realität überführt werden. Die vierte Phase des Curriclumprozesses dient deshalb der rechtlichen, organisatorischen und technischen Implementierung des Studienangebots. Die zuvor entwickelten curricularen Strukturen werden verbindlich beschlossen, in die technischen Systeme überführt und für Studierende sichtbar gemacht. Gleichzeitig werden Verantwortlichkeiten, Prozesse und Governance-Strukturen festgelegt, damit das Studienangebot dauerhaft durchgeführt, administriert und weiterentwickelt werden kann.

---

# Qualitätsmerkmale

## QM: Studierbarkeit

Studierbarkeit beschreibt, wie gut ein Studienprogramm unter realistischen Bedingungen absolvierbar ist. Im Fokus steht, ob Aufbau, Workload und Prüfungsdichte es den Studierenden erlauben, die vorgesehenen Kompetenzen innerhalb der Regelstudienzeit zu erwerben, ohne systematisch überlastet zu werden. Dazu gehören transparente Anforderungen, klar kommunizierte Bestehens- und Aufstufungsvoraussetzungen, eine nachvollziehbare Struktur sowie Unterstützung bei kritischen Übergängen (Studieneinstieg, Stufenwechsel, Abschluss).

Wesentliche Aspekte sind die Verteilung der ECTS und Leistungsnachweise über die Semester, die Abstimmung von Pflicht- und Wahlanteilen, die Berücksichtigung von Mobilität, Teilzeitstudium und individuellen Profilbildungsmöglichkeiten sowie die Passung zwischen Workload und Modulzielen.

Nachweise sind ein plausibilisiertes Mustercurriculum, Workload-Abschätzungen und -Rückmeldungen, Evaluationsergebnisse, Dokumentation von Anpassungen aufgrund von Überlastungsindikatoren sowie klare, verständliche Informationen in Studienordnung, Wegleitungen und Modulkatalog.

---

## QM: Curriculare Operationalisierbarkeit

Curriculare Operationalisierbarkeit meint, dass ein Studienprogramm technisch und organisatorisch robust umgesetzt werden kann. Die curriculare Idee muss so modelliert sein, dass sie in Reglementen, IT-Systemen und administrativen Prozessen eindeutig abgebildet, automatisiert unterstützt und im Alltag zuverlässig vollzogen werden kann – auch bei grossen Studierendenzahlen oder Sonderfällen.

Inhaltlich geht es um konsistente Bestehens- und Aufstufungsregeln, eindeutig definierte Programmdimensionen, klare Modulzuordnungen, saubere Schnittstellen zwischen Programmen sowie um eine Modellierung, die Studienfortschritt, Anerkennungen und Abschlusskontrollen technisch nachvollziehbar macht. Informationsangebote (Modulkatalog, Studienfortschritts-Apps, Academic Record) müssen diese Logik konsistent widerspiegeln.

Beteiligt sind Studienprogrammdirektion, Student Lifecycle Services/Studienadministration, IT, Rechtsdienst und Studiendekanat.

Typische Outputs sind eine konsistente Abbildung der Programmstruktur in den Systemen, klare Prozessbeschreibungen (z.B. für Anerkennungen, Aufstufungen), technisch geprüfte Regeltexte sowie belastbare, auswertbare Daten zum Studienverlauf.

---

## QM: Kohärenz der Prozess-Elemente

Dieses Qualitätsmerkmal zielt auf die innere Stimmigkeit des Curriculums im Sinne des Constructive Alignment. Qualifikationsprofil, Kompetenzraster, Programmstruktur, Modulziele, Lehr-/Lernformen, Leistungsnachweise, Mustercurriculum und Qualitätssicherungsprozesse sollen sich gegenseitig stützen, statt nebeneinander zu stehen.

Dies bedeutet, dass die Qualifikationsziele zur Formulierung übergeordneter Lernziele führen, woraus Modulziele abgeleitet werden können. Lehr-Lern-Settings sind auf diese Ziele zugeschnitten, und die Leistungsnachweise prüfen jene wissenschaftlichen Handlungskompetenzen, die in den Lernzielen umschrieben sind. Programmstruktur und Mustercurriculum sorgen dafür, dass die erforderlichen Handlungskontexte im Studienverlauf tatsächlich vorkommen. Das Qualitätsmanagement begleitet diesen Kreislauf, indem sie Daten zurückspielt und Anpassungen anstösst.

---

## QM: Fachliche und berufsfeldrelevante Begründbarkeit

Ein Studienprogramm soll sowohl fachlich als auch hinsichtlich einschlägiger Berufsfelder überzeugend begründet sein. Das Curriculum soll die Profile der Referenzdisziplin(en) sichtbar machen und zugleich auf relevante wissenschaftliche und berufliche Rollen vorbereiten.

Typische Aspekte sind eine systematische Berufsfeldanalyse, die Berücksichtigung wissenschaftlicher und gesellschaftlicher Trends, die Identifikation typischer Tätigkeitsprofile, für die der Abschluss qualifiziert. Diese Überlegungen münden in ein Qualifikationsprofil, das Kompetenzen konkret benennt und deren Anwendungskontexte beschreibt.

Merkmale der fachlichen und berufsfeldrelevanten Begründbarkeit des Curriculums werden etwa im Qualifikationsprofil, durch dokumentierte Berufsfeldanalysen und Stakeholder-Workshops und in der Strukturierung des Studienprogramms sichtbar. Auch ein begründeter Vergleich mit ähnlichen Angeboten anderer Hochschulen sowie eine klare Darstellung der Anschlussfähigkeit an Arbeitsmarkt und weiterführende Studien trägt dazu bei.

---

## QM: Wissenschaftlichkeit

Die Dimension Wissenschaftlichkeit prüft, inwieweit das Programm Studierende in die Logik wissenschaftlichen Wissens und Arbeitens einführt. Dabei geht es nicht nur um die Verfügbarkeit relevanter Inhalte, sondern um die Fähigkeit, Wissen methodisch fundiert zu generieren, kritisch zu prüfen und weiterzuentwickeln.

Dies umfasst den Anschluss an den Stand von Forschung und Praxis, eine starke Rolle von Methoden- und Theoriemodulen, forschungsnahe Lehr-Lern-Settings (z.B. forschendes Lernen, Projektseminare) sowie die explizite Thematisierung der Dynamik und Kritikwürdigkeit wissenschaftlichen Wissens. Die Wissenschaftlichkeit des Curriculums zeigt sich in Leistungsnachweisen, die typische wissenschaftliche Diskursformen einfordern (etwa auch Reviews, Gutachten, Forschungsberichte).

---

## QM: Handlungsorientierung / Handlungskompetenzorientierung

Diese Qualitätsdimension stellt sicher, dass das Studium auf den Aufbau von Handlungskompetenzen ausgerichtet ist – also auf die Fähigkeit, Wissen in realen oder realitätsnahen Situationen anzuwenden. Im Zentrum stehen komplexe, beobachtbare wissenschaftliche Handlungskompetenzen.

Inhaltlich bedeutet dies: Qualifikationsziele und Lernziele sind kompetenzorientiert formuliert, gestützt auf geeignete Kompetenzmodelle (z.B. Fach-, Methoden-, Sozial- und Personalkompetenz sowie fachspezifische Kompetenzbereiche). Lehr-Lern-Settings bieten authentische Handlungskontexte (Fallarbeit, Projekte, Praxisbezüge, Labor, simulationsbasierte Formate) und Leistungsnachweise prüfen die Bewältigung solcher Kontexte.

Sichtbar wird die Handlungs- und Kompetenzorientierung in den Qualifikationsprofilen, in konsistente Lernzielsystematiken, Modulbeschreibungen mit handlungsbezogenen Lernzielen und Prüfungsformaten sowie im Mustercurriculum, das einen progressiven Aufbau von Handlungskompetenzen ausweist.

---

## QM: Nutzung systematischer Qualitätsprozesse

Diese Dimension fragt, wie Erkenntnisse aus der Qualitätssicherung und -entwicklung strukturiert und die Gestaltung der Studienprogramme einbezogen werden.

Daten aus dem Qualitätsmanagement Studium und Lehre (etwa aus Evaluationen, aus der Zusammenstellung von Kennzahlen oder aus den Qualitätsgespräche mit Lehrenden und Studierenden), aber auch externe Rückmeldungen können für die Prozesse der Curriculumentwicklung bzw. -anpassung genutzt werden.

---

## QM: Einbezug relevanter Querschnittsthemen

Dieses Qualitätsmerkmal stellt sicher, dass wichtige Querschnittsthemen systematisch in das Studienprogramm integriert sind. Dazu zählen etwa Future Skills, Nachhaltigkeit, Digitalisierung und Künstliche Intelligenz, Forschungs- und Praxisbezug, Internationalisierung und Mobilität, Spracherwerb, Accessibility sowie fakultätsübergreifendes Studium.

Inhaltlich geht es darum, diese Themen nicht punktuell, sondern als roten Faden im Qualifikationsprofil, im Kompetenzraster, in Programmstruktur und Modulen sichtbar zu machen. Dies kann über eigene Module, thematische Schwerpunkte, subcurriculare Stränge oder die explizite Einbettung in bestehende Module erfolgen. Wichtig ist, dass die Beiträge der einzelnen Module zu den Querschnittsthemen transparent kommuniziert werden.

Besondere Berücksichtigung finden dabei die Dimensionen, die im UZH-Curriculum programmatisch beschrieben werden.

Nachweise für den Einbezug von Querschnittsthemen sind u.a. Qualifikationsziele, in denen Querschnittskompetenzen benannt sind, entsprechende Module oder Modulgruppen im Modulkatalog, ihre Verortung im Mustercurriculum sowie Erläuterungen in Wegleitungen, wie Studierende diese Querschnittskompetenzen im Verlauf ihres Studiums erwerben und in den Leistungsnachweisen der Module nachweisen.