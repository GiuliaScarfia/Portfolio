import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Giulia Scarfia | CV Portfolio", page_icon="📄", layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .stApp {
            background-color: #fbeff2;
        }
        .centered-image {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Profile Image ---
st.markdown('<div class="centered-image">', unsafe_allow_html=True)
image = Image.open("giulia_scarfia.jpg")
st.image(image, width=300)
st.markdown('</div>', unsafe_allow_html=True)

# --- Title ---
st.title("Giulia Scarfia")
st.subheader("AI & LANGUAGE SCIENCES SPECIALIST")
st.markdown("95041 Caltagirone, Italia | (+39) 393-5423818 | giuliascarfia@hotmail.it")
st.markdown("[GitHub](https://github.com/GiuliaScarfia) | [LinkedIn](https://www.linkedin.com/in/giulia-scarfia-050720219)")
st.divider()

# --- Su di me ---
st.header("🧠 Su di me")
st.markdown("""
Esperta in Scienze Linguistiche ed AI con un solido background accademico e una visione interdisciplinare che intreccia psicolinguistica, linguistica computazionale e scienze cognitive. 
Le mie esperienze di ricerca sono caratterizzate da approcci sperimentali, neuropsicologici e statistico-computazionali. 
Curiosa per natura, affronto ogni sfida con spirito critico e creativo, coltivando un profondo amore per l’arte, l’innovazione e il potere trasformativo della conoscenza.
""")

# --- Lingue ---
st.header("🌍 Lingue")
st.markdown("""
- Italiano (madrelingua)  
- Inglese (B2)
""")

# --- Formazione ---
st.header("🎓 Formazione")
st.markdown("""
**2022 – 2024 | Laurea Magistrale in Scienze Linguistiche** – Alma Mater Studiorum Università di Bologna  
- Tesi sperimentale in Psicolinguistica sull’interazione tra linguaggio, cognizione numerica e affordance, nel quadro dell’Embodied Cognition Account.  
- Studio degli effetti del numero grammaticale e della manipolabilità degli oggetti sull’attivazione motoria durante compiti di categorizzazione semantica.  
- Voto finale: 108/110  
[Link alla tesi](https://www.researchgate.net/publication/385955590_Linguaggio_cognizione_numerica_e_affordance_un%27indagine_sperimentale_nell%27ambito_dell%27embodied_cognition_account?channel=doi&linkId=673d9eacb903016a31cdc4d0&showFulltext=true)

**2018 – 2022 | Laurea Triennale in Lettere Moderne** – Università di Catania  
- Tesi multidisciplinare in Etica della Comunicazione sul rapporto tra pensiero, arte e scienza, ispirata al paradigma della complessità.  
- Approccio neuroestetico per esplorare le basi neurobiologiche dell’esperienza estetica.  
- Voto finale: 103/110

**2013 – 2018 | Diploma di Maturità Scientifica** – Istituto Superiore “Majorana Arcoleo” – Caltagirone  
- Voto finale: 97/100
""")

# --- Esperienza Lavorativa ---
st.header("💼 Esperienza Lavorativa")
st.markdown("""
**12/2025 – Attuale | Docente di Italiano L2 per Stranieri, Formasec S.r.l., Piazza Armerina (Italia)**
- Progettazione e svolgimento di corsi di lingua italiana L2 per studenti stranieri di diversi livelli (A1–C1).
- Preparazione di materiali didattici e attività comunicative orientate allo sviluppo delle competenze linguistiche e interculturali.
- Valutazione delle competenze linguistiche attraverso test di ingresso, verifiche in itinere e prove finali.

**07/2025 – Attuale | Addetta amministrativa, Asten – Agenzia per il Lavoro, Caltagirone**
- Front office, accoglienza utenti e supporto all’orientamento.
- Gestione documentale e utilizzo del gestionale Smartnet.
- Supporto ai processi di inserimento lavorativo e formazione.

**02/2024 - 11/2024 | Collaboratrice CLA - Centro Linguistico di Ateneo, Alma Mater Studiorum - Università di Bologna**  
- Gestione tecnica del laboratorio linguistico e supporto alla manutenzione informatica.  
- Coordinazione e assistenza durante l’erogazione di test di idoneità linguistica.  
- Attività di tutoraggio linguistico, con attenzione personalizzata a studenti con DSA.

**10/2020 – 2022 | Co-Art Director, Associazione Culturale Mediterraneum, Catania**  
- Collaborazione all’organizzazione del MEDPHOTOFEST, Festival Internazionale della Fotografia d’Autore.  
- Esperienza in catalogazione e archiviazione di opere artistiche e allestimento di mostre.  
- Attività di editing editoriale e promozione social per eventi culturali.
""")

# --- Tirocini e Ricerca ---
st.header("🔬 Tirocini e Ricerca")
st.markdown("""
**02/2024 – 10/2024 | Tirocinio presso il Gruppo di ricerca Cognitive Dynamics 4E – Università di Bologna**  
- Approfondimento dei principali paradigmi sperimentali delle Scienze Cognitive e della Psicolinguistica.  
- Partecipazione attiva a progetti di ricerca sperimentale, dall’ideazione alla raccolta e analisi dei dati (VR, eye tracking, esperimenti comportamentali).  
- Collaborazione a eventi di divulgazione scientifica e incontri periodici del gruppo di ricerca (lab meeting).
""")

# --- Competenze Tecniche ---
st.header("🛠️ Competenze Tecniche")
st.markdown("""
- Python  
- Jupyter Notebook  
- Streamlit  
- Machine/Deep Learning  
- Scikit-learn  
- TensorFlow  
- Data Science  
- Conoscenza di base di R
""")

# --- Competenze Trasversali ---
st.header("💡 Competenze Trasversali")
st.markdown("""
- Teamwork  
- Time management  
- Problem solving  
- Multitasking  
- Goal setting  
- Versatilità
""")

# --- Competenze Personali ---
st.header("🎯 Competenze Personali")
st.markdown("""
- Ascolto attivo  
- Sensibilità umanistica  
- Apertura alla sperimentazione  
- Pensiero creativo e dinamico  
- Empatia  
- Dialettica e cordialità  
- Prospettiva critica
""")

# --- Patente di Guida ---
st.header("🚗 Patente di guida")
st.markdown("Patente di categoria **B**")

# --- Hobby e Interessi ---
st.header("🎨 Hobby e Interessi")
st.markdown("""
**Cultura**:  
- Scrittura creativa  
- Competenze storico-artistiche  
- Inclinazione filosofica e poetica  
- Passione fotografica e cinematografica  
- Interessi psicologici, neurolinguistici e neuroestetici

**Sport**:  
- Allenamento in palestra  
- Fitness e nuoto in piscina  
- Surf e Yoga
""")

# --- Progetti con Streamlit ---
st.header("🚀 Progetti realizzati con Streamlit")
st.markdown("""
**🎬 Analisi sul cinema di Hollywood**  
[Visualizza app](https://bootcamp-ai-stream-giulias.streamlit.app/)  
- Andamento della produzione cinematografica nel tempo (bar chart).  
- Generi più popolari (grafico a torta).  
- Relazione tra budget e incassi (scatter plot).

**🎭 Analisi sugli eventi culturali in Italia**  
[Visualizza app](https://bootcamp-ai-stream-giulias2.streamlit.app/)  
- Confronto tra regioni, province e città per luoghi culturali (grafici a barra).  
- Mappa tematica-coropletica della distribuzione geografica.  
- Distribuzione percentuale per regione (grafico a torta).

**📄 CV Optimizer – Generatore di Curriculum Ottimizzati**  
[Visualizza app](https://cvoptimizer.streamlit.app/)  
- Web app interattiva per l’analisi e l’ottimizzazione del curriculum.
- Integra tecnologie NLP per confrontare CV e annunci di lavoro.
- Genera un CV ottimizzato e pronto per la candidatura.
""")

# --- Autorizzazione trattamento dati ---
st.header("🔐 Privacy")
st.markdown("""
Autorizzo il trattamento dei miei dati personali presenti nel CV ai sensi dell’art. 13 d. lgs. 30 giugno 2003 n. 196 - “Codice in materia di protezione dei dati personali” e dell’art. 13 GDPR 679/16 - “Regolamento europeo sulla protezione dei dati personali”.
""")

st.divider()
st.markdown("_Portfolio creato con ❤️ da Giulia Scarfia • Ultimo aggiornamento: Aprile 2025_")
