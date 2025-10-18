import streamlit as st
from io import BytesIO
from datetime import datetime

# Try to import reportlab, handle gracefully if not available
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, ListFlowable, ListItem
    from reportlab.lib.enums import TA_LEFT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    st.warning("⚠️ PDF generation is not available. Please ensure reportlab is installed.")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Antony Best | Data Engineer", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for enhanced styling with dark/light mode support
st.markdown("""
<style>
    .main-header {
        background: var(--background-color);
        padding: 2rem;
        border-radius: 10px;
        color: var(--text-color);
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border: 2px solid var(--border-color);
        border-top: 4px solid #10b981;
    }
    .main-header h1 {
        color: var(--text-color) !important;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    .main-header h2 {
        color: var(--secondary-text-color) !important;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 400;
    }
    .contact-info {
        color: var(--secondary-text-color) !important;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    /* Section headers that adapt to theme */
    .section-header {
        padding: 0.5rem 1rem;
        border-left: 4px solid #10b981;
        border-radius: 5px;
        margin: 1rem 0;
        background-color: var(--background-color);
        border: 1px solid var(--border-color);
    }
    
    /* Light mode section headers */
    [data-theme="light"] .section-header {
        background: linear-gradient(90deg, #f8fafc 0%, #e2e8f0 100%);
        color: #1a202c;
    }
    
    /* Dark mode section headers */
    [data-theme="dark"] .section-header {
        background: linear-gradient(90deg, #2d3748 0%, #4a5568 100%);
        color: #e2e8f0;
    }
    
    .skill-badge {
        background: linear-gradient(45deg, #10b981, #059669);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .experience-card {
        background: var(--background-color);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #10b981;
        margin: 0.5rem 0;
        border: 1px solid var(--border-color);
    }
    
    /* Ensure text is visible in both themes */
    .section-header h3 {
        color: inherit !important;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# --- ENHANCED HEADER ---
st.markdown("""
<div class="main-header">
    <h1>👨🏾‍💻 Antony Best</h1>
    <h2>Data Engineer</h2>
    <div class="contact-info">📧 antony.best@googlemail.com | 📱 07891 664159</div>
</div>
""", unsafe_allow_html=True)

# --- PROFESSIONAL SUMMARY ---
st.markdown('<div class="section-header"><h3>📋 Professional Summary</h3></div>', unsafe_allow_html=True)
summary_text = """
I specialise in architecting and building robust data systems and pipelines that transform raw data into actionable business intelligence, 
working extensively with **Snowflake**, **Azure Data Factory**, and **dbt** to create scalable data architectures. 

My technical expertise includes designing sophisticated data models using star and snowflake schemas, implementing ETL/ELT processes, 
and integrating AI/ML platforms including **Snowflake AI Cortex** and **Azure OpenAI** for advanced analytics and automation.

I implement advanced SQL techniques and Python programming for data engineering, with strong experience in cloud data warehouses (AWS, Azure, GCP), 
and hold certifications in **Snowflake SnowPro** and **Azure AZ-900**. I'm proficient in MLOps practices, agile methodologies, and CI/CD processes.

Additionally, I develop comprehensive data models that support real-time analytics dashboards and API endpoints, 
enabling stakeholders to access critical insights for data-driven decision-making across diverse business environments.
"""
st.write(summary_text)
st.markdown("---")

# --- WORK EXPERIENCE ---
st.markdown('<div class="section-header"><h3>💼 Work Experience</h3></div>', unsafe_allow_html=True)

experience = [
    {
        "role": "Lead Business Intelligence Learner Analytics Developer | University of Birmingham UK (04/2024 – Present)",
        "details": [
            "Designed, built, and optimised end-to-end data platforms using Snowflake, Azure Data Factory, and dbt.",
            "Delivered scalable ELT solutions integrating multiple data systems into a unified warehouse.",
            "Built Azure Functions integrating with APIM APIs for cloud-native automation and AI integration.",
            "Implemented Snowflake AI Cortex for advanced analytics, built AI agents, and integrated Snowflake AI API into Azure Functions.",
            "Proficient in Python, SQL, Terraform, CI/CD, and version control with agile methodologies.",
            "Collaborated with architects, analysts, and stakeholders to deliver data strategies aligned with business goals.",
            "Used Jira for project management and daily scrum calls in agile development environment.",
        ]
    },
    {
        "role": "Data Engineer | Capgemini UK (05/2023 – 04/2024)",
        "details": [
            "Processed XML data in AWS Glue, loading structured data into AWS and metadata into Snowflake.",
            "Developed Python scripts for file validation, batch IDs, and Snowflake integration.",
            "Used Apache Airflow for ETL orchestration and workflow management.",
        ]
    },
    {
        "role": "Data Specialist | Capgemini UK (05/2023 – 08/2023)",
        "details": [
            "Used SQL (SSM) for DataLake extractions and report generation.",
            "Created SSRS and Power BI reports for reconciliation and analysis.",
        ]
    },
    {
        "role": "DataOps | Capgemini UK (02/2023 – 04/2023)",
        "details": [
            "Connected to ClickHouse via Docker OCS.",
            "Modelled data from unstructured sources and visualised API calls using Insomnia and DBeaver.",
        ]
    },
    {
        "role": "Data Engineering / Developer / Tester | Capgemini UK (02/2022 – 01/2023)",
        "details": [
            "Migrated SAS solutions to PySpark and BigQuery.",
            "Used Databricks, Airflow, and GCP for ETL orchestration.",
            "Implemented AI (GPT3) for code testing and reconciliation.",
        ]
    },
    {
        "role": "Data Analyst | Self Employed (09/2020 – 01/2022)",
        "details": [
            "Analysed CSV data using Python, Pandas, Seaborn, and Matplotlib to visualise insights.",
        ]
    },
]

for job in experience:
    with st.expander(f"💼 {job['role']}"):
        for line in job["details"]:
            st.markdown(f"- {line}")

st.markdown("---")

# --- SKILLS ---
skills = [
    "Snowflake", "dbt", "Azure Data Factory", "Python", "SQL",
    "Terraform", "Azure Functions", "APIM", "AWS Glue", "Power BI",
    "Airflow", "Databricks", "GCP", "BigQuery", "Git / CI-CD",
    "Snowflake AI Cortex", "Jira", "Agile"
]

st.markdown('<div class="section-header"><h3>🛠️ Technical Skills</h3></div>', unsafe_allow_html=True)

# Create skill badges
skill_html = ""
for skill in skills:
    skill_html += f'<span class="skill-badge">{skill}</span>'

st.markdown(skill_html, unsafe_allow_html=True)
st.markdown("---")

# --- EDUCATION & CERTIFICATIONS ---
st.markdown('<div class="section-header"><h3>🎓 Education & Certifications</h3></div>', unsafe_allow_html=True)

education_text = """
🎓 **BSc (Hons) in Audio Systems Design**, University of Derby  

📜 **Certifications:**  
- Snowflake SnowPro Core Certified  
- Microsoft Certified Azure Fundamentals (AZ-900)  
- Python PCAP Certified  
- BigQuery Basics (Coursera)  
- SAS & PySpark Certificates (Coursera)
"""
st.write(education_text)
st.markdown("---")

hobbies_text = """
🎶 Music  
🎾 Tennis  
🧠 Learning new skills and AI technologies  
💡 Exploring new data tools and innovations
"""
st.write(hobbies_text)
st.markdown("---")

# --- PDF GENERATION (TWO-COLUMN LAYOUT) ---
if REPORTLAB_AVAILABLE:
    pdf_buffer = BytesIO()

    doc = BaseDocTemplate(pdf_buffer, pagesize=A4, leftMargin=30, rightMargin=30, topMargin=30, bottomMargin=30)
    styles = getSampleStyleSheet()
    
    # Enhanced professional styling with modern colors and better typography
    styles.add(ParagraphStyle(name='CVTitle', fontSize=22, leading=26, spaceAfter=6, fontName='Helvetica-Bold', textColor='#1a365d', alignment=1))
    styles.add(ParagraphStyle(name='CVSubtitle', fontSize=15, leading=17, spaceAfter=10, fontName='Helvetica', textColor='#2d3748', alignment=1))
    styles.add(ParagraphStyle(name='CVSectionHeader', fontSize=12, leading=14, spaceAfter=4, spaceBefore=10, fontName='Helvetica-Bold', textColor='#2b6cb0', borderWidth=1, borderColor='#2b6cb0', borderPadding=3, backColor='#f7fafc'))
    styles.add(ParagraphStyle(name='CVBody', fontSize=9, leading=11, spaceAfter=3, fontName='Helvetica', textColor='#2d3748'))
    styles.add(ParagraphStyle(name='CVListItem', fontSize=8, leading=10, leftIndent=15, fontName='Helvetica', textColor='#4a5568'))
    styles.add(ParagraphStyle(name='CVContact', fontSize=9, leading=11, spaceAfter=8, fontName='Helvetica', textColor='#718096', alignment=1))
    styles.add(ParagraphStyle(name='CVJobTitle', fontSize=10, leading=12, spaceAfter=1, fontName='Helvetica-Bold', textColor='#1a365d'))
    styles.add(ParagraphStyle(name='CVCompany', fontSize=8, leading=10, spaceAfter=3, fontName='Helvetica', textColor='#718096', fontStyle='italic'))
    styles.add(ParagraphStyle(name='CVSummary', fontSize=8, leading=10, spaceAfter=5, fontName='Helvetica', textColor='#2d3748'))
    styles.add(ParagraphStyle(name='CVSkills', fontSize=8, leading=10, spaceAfter=3, fontName='Helvetica', textColor='#4a5568'))
    styles.add(ParagraphStyle(name='CVCert', fontSize=8, leading=10, spaceAfter=1, fontName='Helvetica', textColor='#2d3748'))
    styles.add(ParagraphStyle(name='CVSkillsHeader', fontSize=9, leading=11, spaceAfter=2, fontName='Helvetica-Bold', textColor='#1a365d'))

    # Define two-column layout with more space
    frame_left = Frame(doc.leftMargin, doc.bottomMargin, (A4[0] - 60) / 2, A4[1] - 60, id='left')
    frame_right = Frame(doc.leftMargin + (A4[0] - 60) / 2 + 10, doc.bottomMargin, (A4[0] - 60) / 2, A4[1] - 60, id='right')
    doc.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame_left, frame_right])])

    story = []

    # LEFT COLUMN: Summary + Experience + Education
    story.append(Paragraph("ANTONY BEST", styles['CVTitle']))
    story.append(Paragraph("Data Engineer", styles['CVSubtitle']))
    story.append(Paragraph("📧 antony.best@googlemail.com  |  📱 07891 664159", styles['CVContact']))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Professional Summary", styles['CVSectionHeader']))
    story.append(Paragraph(summary_text, styles['CVSummary']))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Work Experience", styles['CVSectionHeader']))
    
    # Filter out roles that go in right column
    left_column_experience = []
    for job in experience:
        if "Data Engineering / Developer / Tester" not in job['role'] and "Data Analyst" not in job['role']:
            left_column_experience.append(job)
    
    for job in left_column_experience:
        # Split role and company/date
        role_parts = job['role'].split(' | ')
        if len(role_parts) == 2:
            role_title = role_parts[0]
            company_date = role_parts[1]
        else:
            role_title = job['role']
            company_date = ""
            
        story.append(Paragraph(role_title, styles['CVJobTitle']))
        if company_date:
            story.append(Paragraph(company_date, styles['CVCompany']))
        else:
            # Add spacing for roles without company/date to maintain consistency
            story.append(Spacer(1, 2))
        
        story.append(ListFlowable(
            [ListItem(Paragraph(item, styles['CVListItem'])) for item in job["details"]],
            bulletType='bullet'
        ))
        story.append(Spacer(1, 8))

    # Add Data Analyst role to right column first
    story.append(Paragraph("Data Analyst", styles['CVJobTitle']))
    story.append(Paragraph("Self Employed (09/2020 – 01/2022)", styles['CVCompany']))
    story.append(Spacer(1, 2))
    data_analyst_details = [
        "Analysed CSV data using Python, Pandas, Seaborn, and Matplotlib to visualise insights.",
    ]
    story.append(ListFlowable(
        [ListItem(Paragraph(item, styles['CVListItem'])) for item in data_analyst_details],
        bulletType='bullet'
    ))
    story.append(Spacer(1, 8))
    
    # Add Data Engineering role to right column
    story.append(Paragraph("Data Engineering / Developer / Tester", styles['CVJobTitle']))
    story.append(Paragraph("Capgemini UK (02/2022 – 01/2023)", styles['CVCompany']))
    story.append(Spacer(1, 2))
    data_engineering_details = [
        "Migrated SAS solutions to PySpark and BigQuery.",
        "Used Databricks, Airflow, and GCP for ETL orchestration.",
        "Implemented AI (GPT3) for code testing and reconciliation.",
    ]
    story.append(ListFlowable(
        [ListItem(Paragraph(item, styles['CVListItem'])) for item in data_engineering_details],
        bulletType='bullet'
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Education & Certifications", styles['CVSectionHeader']))
    
    # Education section with enhanced formatting
    story.append(Paragraph("BSc (Hons) in Audio Systems Design", styles['CVJobTitle']))
    story.append(Paragraph("University of Derby", styles['CVCompany']))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Professional Certifications:", styles['CVSkillsHeader']))
    certifications = [
        "Snowflake SnowPro Core Certified",
        "Microsoft Certified Azure Fundamentals (AZ-900)",
        "Python PCAP Certified",
        "BigQuery Basics (Coursera)",
        "SAS & PySpark Certificates (Coursera)"
    ]
    story.append(ListFlowable(
        [ListItem(Paragraph(cert, styles['CVCert'])) for cert in certifications],
        bulletType='bullet'
    ))
    story.append(Spacer(1, 6))

    # RIGHT COLUMN: Skills + Additional Experience + Hobbies
    
    story.append(Paragraph("Technical Skills", styles['CVSectionHeader']))
    # Format skills in categories for better readability with enhanced styling
    core_skills = "Snowflake • dbt • Azure Data Factory • Python • SQL"
    cloud_skills = "Terraform • Azure Functions • APIM • AWS Glue • Power BI"
    tools_skills = "Airflow • Databricks • GCP • BigQuery • Git / CI-CD"
    ai_skills = "Snowflake AI Cortex • Jira • Agile"
    
    story.append(Paragraph("Core Technologies:", styles['CVSkillsHeader']))
    story.append(Paragraph(core_skills, styles['CVSkills']))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Cloud & Tools:", styles['CVSkillsHeader']))
    story.append(Paragraph(cloud_skills, styles['CVSkills']))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Data Platforms:", styles['CVSkillsHeader']))
    story.append(Paragraph(tools_skills, styles['CVSkills']))
    story.append(Spacer(1, 3))
    story.append(Paragraph("AI & Methodologies:", styles['CVSkillsHeader']))
    story.append(Paragraph(ai_skills, styles['CVSkills']))
    story.append(Spacer(1, 6))


    story.append(Paragraph("Interests", styles['CVSectionHeader']))
    # Clean up hobbies text for better formatting
    hobbies_clean = hobbies_text.replace("🎶 ", "").replace("🎾 ", "").replace("🧠 ", "").replace("💡 ", "")
    story.append(Paragraph(hobbies_clean, styles['CVSkills']))

    doc.build(story)
    pdf_buffer.seek(0)

    # --- DOWNLOAD BUTTON ---
    st.download_button(
        label="📥 Download Antony Best's CV (PDF)",
        data=pdf_buffer,
        file_name=f"Antony_Best_Data_Engineer_CV_{datetime.now().strftime('%Y%m%d')}.pdf",
        mime="application/pdf",
    )
else:
    st.info("💡 PDF download will be available once the app is deployed with the requirements.txt file.")