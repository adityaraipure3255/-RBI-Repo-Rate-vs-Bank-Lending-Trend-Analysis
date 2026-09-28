from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import cm
from pathlib import Path


# ============================================================
# OUTPUT FILE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "Research_Paper_2_Technology.pdf"


# ============================================================
# PDF SETTINGS
# ============================================================

doc = SimpleDocTemplate(
    str(OUTPUT_FILE),
    pagesize=A4,
    rightMargin=1.5 * cm,
    leftMargin=1.5 * cm,
    topMargin=1.4 * cm,
    bottomMargin=1.4 * cm
)


# ============================================================
# STYLES
# ============================================================

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=15,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=12,
    alignment=TA_CENTER,
    spaceAfter=8
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=13,
    spaceBefore=6,
    spaceAfter=4
)

subheading_style = ParagraphStyle(
    "SubHeadingStyle",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=9.5,
    leading=12,
    spaceBefore=4,
    spaceAfter=3
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.4,
    leading=11.2,
    alignment=TA_JUSTIFY,
    spaceAfter=4
)

bullet_style = ParagraphStyle(
    "BulletStyle",
    parent=body_style,
    leftIndent=12,
    firstLineIndent=-7,
    spaceAfter=2
)

small_style = ParagraphStyle(
    "SmallStyle",
    parent=body_style,
    fontSize=7.5,
    leading=9.5
)


def P(text, style=body_style):
    return Paragraph(text, style)


def bullet(text):
    return Paragraph("• " + text, bullet_style)


# ============================================================
# PAGE NUMBER
# ============================================================

def add_page_number(canvas, document):

    canvas.saveState()

    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.grey)

    canvas.drawString(
        1.5 * cm,
        0.8 * cm,
        "Technology Stack for RBI Repo Rate and Bank Lending Analysis"
    )

    canvas.drawRightString(
        A4[0] - 1.5 * cm,
        0.8 * cm,
        f"Page {document.page} of 3"
    )

    canvas.restoreState()


# ============================================================
# STORY
# ============================================================

story = []


# ============================================================
# PAGE 1
# ============================================================

story.append(
    P(
        "Technology Stack for RBI Repo Rate and Bank Lending Analysis",
        title_style
    )
)

story.append(
    P(
        "<b>Python, Pandas, NumPy, Matplotlib, Seaborn, MySQL and Power BI</b><br/>"
        "Research Paper 2 – Technology-Related Research",
        subtitle_style
    )
)

story.append(
    P(
        "<b>Project:</b> RBI Repo Rate vs Bank Lending Trend Analysis<br/>"
        "<b>Technology Domain:</b> Data Analysis, Database Management and Business Intelligence",
        subtitle_style
    )
)

story.append(P("Abstract", heading_style))

story.append(
    P(
        "Modern data-analysis projects require a combination of programming "
        "languages, data-processing libraries, database systems and "
        "visualisation platforms. This paper discusses the technologies "
        "used in the RBI Repo Rate vs Bank Lending Trend Analysis project."
    )
)

story.append(
    P(
        "Python is used as the main programming language. Pandas provides "
        "data structures and operations for tabular and time-series data, "
        "while NumPy supports numerical computation. Matplotlib and Seaborn "
        "are used to create analytical visualisations. MySQL provides "
        "structured storage and SQL-based analysis, while Power BI is used "
        "to build an interactive dashboard."
    )
)

story.append(
    P(
        "The technologies were selected because together they support the "
        "complete data-analysis workflow: data loading, cleaning, "
        "transformation, statistical analysis, database querying, "
        "visualisation and business reporting."
    )
)

story.append(
    P(
        "<b>Keywords:</b> Python, Pandas, NumPy, Matplotlib, Seaborn, "
        "MySQL, SQL, Power BI, Data Analysis, Business Intelligence."
    )
)

story.append(P("1. Introduction", heading_style))

story.append(
    P(
        "Data analysis involves converting raw information into useful "
        "insights. A typical workflow includes collecting data, checking "
        "data quality, cleaning records, transforming variables, performing "
        "analysis, creating visualisations and communicating results."
    )
)

story.append(
    P(
        "No single tool is required to perform every part of this process. "
        "Programming libraries are useful for flexible analysis, databases "
        "are suitable for structured storage and querying, and business "
        "intelligence tools are useful for interactive reporting."
    )
)

story.append(
    P(
        "The present project combines these technologies to analyse the "
        "relationship between the RBI repo rate and bank lending rates. "
        "The workflow demonstrates how different technologies can work "
        "together rather than replacing one another."
    )
)

story.append(P("2. Python", heading_style))

story.append(
    P(
        "Python is the primary programming language used in the project. "
        "Its simple syntax and large ecosystem make it suitable for data "
        "analysis, automation and scientific computing."
    )
)

story.append(
    P(
        "In this project, Python controls the complete analytical workflow. "
        "It imports libraries, loads RBI datasets, performs cleaning and "
        "transformation, calculates statistics and generates analytical "
        "outputs."
    )
)

story.append(
    P(
        "Python also provides integration with databases and visualisation "
        "libraries. This makes it suitable for building reproducible "
        "analysis scripts and Jupyter Notebook workflows."
    )
)

story.append(P("3. Pandas", heading_style))

story.append(
    P(
        "Pandas is a Python library designed for data manipulation and "
        "analysis. Its main structures are Series and DataFrame. A "
        "DataFrame represents tabular data using rows and columns."
    )
)

story.append(
    P(
        "The project uses Pandas to read Excel and CSV files, inspect "
        "datasets, convert dates, sort observations, detect missing values, "
        "merge datasets, resample time-series observations and export the "
        "cleaned dataset."
    )
)

story.append(
    P(
        "Pandas is especially useful for this project because both repo-rate "
        "and WALR datasets are structured as time-series tables. Its "
        "grouping, merging and time-series functionality simplifies the "
        "preparation of the final analytical dataset."
    )
)

story.append(P("4. NumPy", heading_style))

story.append(
    P(
        "NumPy is a numerical computing library for Python. It provides "
        "efficient arrays and mathematical operations and forms an important "
        "part of the Python scientific-computing ecosystem."
    )
)

story.append(
    P(
        "In this project, NumPy supports numerical calculations and "
        "statistical operations. It can be used together with Pandas when "
        "working with numerical columns and mathematical transformations."
    )
)


# ============================================================
# PAGE BREAK
# ============================================================

story.append(PageBreak())


# ============================================================
# PAGE 2
# ============================================================

story.append(P("5. Matplotlib", heading_style))

story.append(
    P(
        "Matplotlib is a Python visualisation library used to create charts "
        "and graphs. It provides control over axes, labels, legends, "
        "titles and other graphical elements."
    )
)

story.append(
    P(
        "The project uses Matplotlib to visualise the movement of repo "
        "rates and WALR over time. Line charts, scatter plots and other "
        "analytical charts help identify trends and relationships that may "
        "not be obvious from numerical tables."
    )
)

story.append(P("6. Seaborn", heading_style))

story.append(
    P(
        "Seaborn is a statistical visualisation library built on top of "
        "Matplotlib. It provides convenient functions for statistical "
        "graphics and attractive default visual presentation."
    )
)

story.append(
    P(
        "In this project, Seaborn is useful for relationship analysis and "
        "statistical visualisation, including correlation heatmaps and "
        "regression-style plots. These visuals help understand the "
        "association between monetary-policy rates and lending rates."
    )
)

story.append(P("7. MySQL and SQL", heading_style))

story.append(
    P(
        "MySQL is a relational database management system. It stores data "
        "in structured tables and supports SQL for retrieving, filtering, "
        "joining and aggregating information."
    )
)

story.append(
    P(
        "The project uses MySQL to store the repo-rate data and WALR data "
        "in separate tables. The <b>repo_rate</b> table contains policy "
        "rates, while <b>walr_data</b> contains bank-group-wise lending "
        "rates."
    )
)

story.append(
    P(
        "SQL is used to inspect records, calculate averages, identify "
        "maximum and minimum values, perform yearly analysis, join the "
        "two datasets and calculate quarter-to-quarter changes."
    )
)

story.append(P("8. SQL Techniques Used", heading_style))

for item in [
    "<b>CREATE TABLE:</b> Creates structured database tables.",
    "<b>SELECT:</b> Retrieves required columns and records.",
    "<b>WHERE:</b> Filters data based on conditions.",
    "<b>JOIN:</b> Combines repo-rate and WALR datasets.",
    "<b>GROUP BY:</b> Supports yearly and bank-group analysis.",
    "<b>AVG, MAX and MIN:</b> Calculate descriptive statistics.",
    "<b>LAG:</b> Compares a quarter with the previous quarter.",
    "<b>Aggregate calculations:</b> Support correlation and trend analysis."
]:
    story.append(bullet(item))

story.append(P("9. Power BI", heading_style))

story.append(
    P(
        "Microsoft Power BI is a business intelligence and data "
        "visualisation platform. It allows users to connect data sources, "
        "create data models, build interactive visuals and present results "
        "through dashboards."
    )
)

story.append(
    P(
        "In this project, the cleaned CSV dataset is imported into Power BI. "
        "Measures are created for average rates and correlation, while "
        "visuals are used to present trends, changes, comparisons and "
        "relationships."
    )
)

story.append(P("10. Power BI Dashboard Components", heading_style))

for item in [
    "KPI cards for average repo rate and average WALR.",
    "Correlation KPI for the repo-rate and WALR relationship.",
    "Line chart for repo rate versus All SCBs WALR.",
    "Clustered column chart for WALR by bank group.",
    "Line chart for quarterly changes.",
    "Scatter chart for repo rate versus WALR relationship.",
    "Year-wise average repo-rate visualisation."
]:
    story.append(bullet(item))

story.append(P("11. Technology Comparison", heading_style))

tech_data = [
    ["Technology", "Main Role"],
    ["Python", "Programming and workflow control"],
    ["Pandas", "Data cleaning and manipulation"],
    ["NumPy", "Numerical computation"],
    ["Matplotlib", "Data visualisation"],
    ["Seaborn", "Statistical visualisation"],
    ["MySQL", "Structured data storage"],
    ["SQL", "Database querying and analysis"],
    ["Power BI", "Interactive dashboard and reporting"]
]

table = Table(
    [[P(x, small_style), P(y, small_style)] for x, y in tech_data],
    colWidths=[4.5 * cm, 11.5 * cm],
    repeatRows=1
)

table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3)
    ])
)

story.append(table)


# ============================================================
# PAGE BREAK
# ============================================================

story.append(PageBreak())


# ============================================================
# PAGE 3
# ============================================================

story.append(P("12. End-to-End Technology Workflow", heading_style))

story.append(
    P(
        "The technologies work together in a sequential data-analysis "
        "workflow. RBI datasets are first collected and loaded into Python. "
        "Pandas is then used to inspect, clean and transform the datasets. "
        "The two datasets are aligned by quarter and merged into a common "
        "analytical dataset."
    )
)

workflow_data = [
    ["Stage", "Technology", "Purpose"],
    ["Data Collection", "RBI Data + Python", "Obtain official datasets"],
    ["Data Cleaning", "Pandas + NumPy", "Clean and transform data"],
    ["EDA", "Pandas + NumPy", "Statistics and exploration"],
    ["Visualisation", "Matplotlib + Seaborn", "Charts and relationships"],
    ["Database", "MySQL + SQL", "Store and query structured data"],
    ["Dashboard", "Power BI", "Interactive reporting"]
]

workflow_table = Table(
    [
        [
            P(a, small_style),
            P(b, small_style),
            P(c, small_style)
        ]
        for a, b, c in workflow_data
    ],
    colWidths=[3.7 * cm, 5.0 * cm, 7.3 * cm],
    repeatRows=1
)

workflow_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3)
    ])
)

story.append(workflow_table)

story.append(P("13. Data Cleaning and Quality", heading_style))

story.append(
    P(
        "Data quality is an important part of the analytical workflow. "
        "The project checks column types, missing values, duplicate "
        "records and date consistency. Numeric columns are converted to "
        "appropriate numeric formats and dates are standardised before "
        "analysis."
    )
)

story.append(
    P(
        "Pandas is used to identify and handle missing observations, while "
        "sorting and merging operations ensure that repo-rate and WALR "
        "records are correctly aligned. Validation is performed after "
        "processing to confirm the final dataset structure."
    )
)

story.append(P("14. Reproducibility", heading_style))

story.append(
    P(
        "Using Python scripts and notebooks makes the analysis reproducible. "
        "The same cleaning and transformation steps can be executed again "
        "when updated RBI data becomes available. SQL queries provide a "
        "structured way to repeat database analysis, while Power BI stores "
        "the dashboard model and visual configuration."
    )
)

story.append(
    P(
        "The project therefore separates data preparation, database "
        "analysis and reporting while maintaining a common analytical "
        "dataset."
    )
)

story.append(P("15. Why These Technologies Were Chosen", heading_style))

for item in [
    "Python provides a flexible and widely used programming environment.",
    "Pandas simplifies tabular and time-series data manipulation.",
    "NumPy supports efficient numerical calculations.",
    "Matplotlib provides detailed control over analytical charts.",
    "Seaborn simplifies statistical visualisation.",
    "MySQL provides structured relational data storage.",
    "SQL allows efficient querying and aggregation.",
    "Power BI converts analysis into an interactive business dashboard."
]:
    story.append(bullet(item))

story.append(P("16. Advantages", heading_style))

story.append(
    P(
        "The combined technology stack provides flexibility, reproducibility "
        "and clear communication of results. Python supports detailed "
        "analysis, SQL provides database-level operations and Power BI "
        "provides an accessible interface for users who want to explore "
        "the results visually."
    )
)

story.append(P("17. Limitations", heading_style))

for item in [
    "Different tools require separate environments and configurations.",
    "Large datasets may require optimisation and efficient memory usage.",
    "Power BI dashboards depend on correctly prepared source data.",
    "Python and SQL analysis require programming knowledge.",
    "Visualisations can be misleading if scales, aggregation or filters are used incorrectly."
]:
    story.append(bullet(item))

story.append(P("18. Future Scope", heading_style))

story.append(
    P(
        "The technology stack can be extended by adding automated data "
        "pipelines, scheduled data refreshes, cloud databases, advanced "
        "statistical models and machine-learning techniques. Power BI "
        "dashboards can also be connected to regularly updated sources "
        "for more frequent monitoring."
    )
)

story.append(P("19. Conclusion", heading_style))

story.append(
    P(
        "The RBI Repo Rate vs Bank Lending Trend Analysis project "
        "demonstrates how multiple technologies can be integrated into a "
        "complete data-analysis workflow. Python and its libraries handle "
        "data preparation and analysis, MySQL and SQL provide structured "
        "database operations, and Power BI provides interactive reporting."
    )
)

story.append(
    P(
        "The selection of these technologies is based on their complementary "
        "roles. Together they provide a practical workflow for converting "
        "raw financial data into cleaned datasets, statistical findings, "
        "visual insights and an interactive dashboard."
    )
)

story.append(P("20. References", heading_style))

references = [
    "Python Software Foundation, Python Documentation.",
    "Pandas Documentation, Package Overview and User Guide.",
    "NumPy Documentation, NumPy User Guide.",
    "Matplotlib Documentation, User Guide.",
    "Seaborn Documentation, Statistical Data Visualization.",
    "MySQL Documentation, MySQL Connector/Python Developer Guide.",
    "Microsoft Learn, Power BI Documentation and Python Integration."
]

for ref in references:
    story.append(bullet(ref))


# ============================================================
# BUILD PDF
# ============================================================

doc.build(
    story,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number
)

print("=" * 60)
print("PAPER 2 CREATED")
print("=" * 60)
print(f"Output: {OUTPUT_FILE}")
print("Pages: 3")
print("=" * 60)