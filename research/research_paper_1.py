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
OUTPUT_FILE = BASE_DIR / "Research_Paper_1_Topic.pdf"


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
        "RBI Repo Rate and Bank Lending Trends in India"
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
        "RBI Repo Rate and Bank Lending Trends in India",
        title_style
    )
)

story.append(
    P(
        "<b>A Data-Driven Study of Monetary Policy Transmission</b><br/>"
        "Research Paper 1 – Topic-Related Research",
        subtitle_style
    )
)

story.append(
    P(
        "<b>Project:</b> RBI Repo Rate vs Bank Lending Trend Analysis<br/>"
        "<b>Domain:</b> Banking, Monetary Policy and Financial Data Analysis<br/>"
        "<b>Data Source:</b> Reserve Bank of India (RBI)",
        subtitle_style
    )
)

story.append(P("Abstract", heading_style))

story.append(
    P(
        "The Reserve Bank of India (RBI) uses monetary policy to influence "
        "financial conditions and support macroeconomic stability. The "
        "policy repo rate is an important monetary-policy instrument and "
        "its movement can influence interest rates across the financial "
        "system. Bank lending rates are particularly important because "
        "they affect the cost of borrowing for households and businesses."
    )
)

story.append(
    P(
        "This paper studies the relationship between the RBI repo rate and "
        "bank lending rates in India using Weighted Average Lending Rate "
        "(WALR) data for Scheduled Commercial Banks. The study considers "
        "Public Sector Banks, Private Sector Banks, Foreign Banks and "
        "the aggregate All SCBs series. The project uses RBI data and a "
        "quarterly analytical framework covering June 2012 to June 2026."
    )
)

story.append(
    P(
        "Python, Pandas, NumPy, Matplotlib and Seaborn are used for data "
        "preparation and exploratory analysis, while SQL and Power BI "
        "support database analysis and reporting. The project examines "
        "rate levels, quarterly changes and a one-quarter lag."
    )
)

story.append(
    P(
        "<b>Keywords:</b> RBI, Repo Rate, Monetary Policy, WALR, Bank "
        "Lending Rates, Monetary Transmission, Banking Sector."
    )
)

story.append(P("1. Introduction", heading_style))

story.append(
    P(
        "Interest rates influence borrowing, investment, consumption and "
        "saving decisions in an economy. In India, monetary policy affects "
        "financial conditions through several channels, with the interest-"
        "rate channel being particularly relevant to bank lending."
    )
)

story.append(
    P(
        "The repo rate acts as an important policy signal. A reduction in "
        "the policy rate generally represents monetary easing, while an "
        "increase represents tightening. Changes in the policy rate can "
        "affect market rates, bank funding conditions and lending rates."
    )
)

story.append(
    P(
        "The transmission is not necessarily immediate or one-to-one. "
        "Banks consider deposit costs, liquidity, competition, credit risk, "
        "operating costs and loan repricing conditions while determining "
        "lending rates. Existing loans can also respond more slowly than "
        "new loans."
    )
)

story.append(P("2. Background of Monetary Policy", heading_style))

story.append(
    P(
        "The RBI is India's central bank and is responsible for implementing "
        "monetary policy within the established policy framework. Monetary "
        "policy affects the financial system through interest rates, credit "
        "conditions and other channels."
    )
)

story.append(
    P(
        "The interest-rate channel explains how changes in policy rates can "
        "eventually influence borrowing costs. When policy conditions become "
        "easier, lending rates may decline depending on the transmission "
        "mechanism. During tightening periods, lending rates may increase."
    )
)

story.append(P("3. Repo Rate", heading_style))

story.append(
    P(
        "The repo rate is an important policy rate used by the RBI. It "
        "provides a signal about the monetary-policy stance and influences "
        "financial-market conditions. In this project, historical RBI "
        "policy-rate observations are converted into a quarterly series."
    )
)

story.append(
    P(
        "For quarters containing multiple policy observations, the last "
        "available repo-rate observation is used. This creates a consistent "
        "quarterly series that can be compared with the quarterly WALR data."
    )
)

story.append(P("4. Bank Lending Rates and WALR", heading_style))

story.append(
    P(
        "Bank lending rates represent the interest charged by banks on "
        "loans. WALR, or Weighted Average Lending Rate, provides a broad "
        "measure of lending conditions by considering the weighted average "
        "of lending rates."
    )
)

story.append(
    P(
        "The RBI provides bank-group-wise WALR data for outstanding rupee "
        "loans. The project uses Public Sector Banks, Private Sector Banks, "
        "Foreign Banks and All SCBs. All SCBs is used as the main aggregate "
        "series for comparison with the repo rate."
    )
)

story.append(
    P(
        "Outstanding-loan WALR represents the stock of existing loans. "
        "Therefore, it can adjust more slowly because loans may have "
        "different repricing schedules."
    )
)


# ============================================================
# PAGE BREAK
# ============================================================

story.append(PageBreak())


# ============================================================
# PAGE 2
# ============================================================

story.append(P("5. Existing Studies and RBI Evidence", heading_style))

story.append(
    P(
        "The RBI has published several analyses of monetary-policy "
        "transmission and bank lending rates. These studies show that "
        "changes in policy rates are transmitted to lending rates, but "
        "the magnitude and speed of transmission can differ."
    )
)

story.append(
    P(
        "RBI analysis of the monetary-easing period around 2019 showed "
        "that reductions in the policy repo rate were followed by changes "
        "in lending rates. However, the response of fresh loans and "
        "outstanding loans was different, demonstrating that transmission "
        "is not always immediate."
    )
)

story.append(
    P(
        "The introduction of external benchmark-based lending rates for "
        "certain categories of loans strengthened the linkage between "
        "policy rates and lending rates for new loans. RBI analysis has "
        "reported stronger transmission under this framework."
    )
)

story.append(
    P(
        "During the tightening cycle beginning in 2022, RBI analysis "
        "reported substantial increases in lending rates following the "
        "increase in the policy repo rate. However, the transmission to "
        "outstanding loans was smaller than the change in the repo rate."
    )
)

story.append(P("6. Research Gap", heading_style))

story.append(
    P(
        "Existing RBI publications provide detailed analysis of individual "
        "monetary-policy periods and transmission mechanisms. The present "
        "project adds a practical data-analysis perspective by combining "
        "repo-rate data and bank-group WALR data into a consistent quarterly "
        "dataset covering a longer period."
    )
)

story.append(
    P(
        "The project also examines not only the level of rates but also "
        "quarterly changes and a one-quarter lag. This provides additional "
        "information about the timing and strength of co-movement."
    )
)

story.append(P("7. Objectives", heading_style))

for item in [
    "Study the historical movement of the RBI repo rate.",
    "Analyse bank lending trends using WALR.",
    "Compare lending rates across different bank groups.",
    "Measure the relationship between repo rate and All SCBs WALR.",
    "Analyse quarter-to-quarter changes in both rates.",
    "Examine a one-quarter lag in repo-rate changes.",
    "Present the results through Python, SQL and Power BI."
]:
    story.append(bullet(item))

story.append(P("8. Data Sources and Methodology", heading_style))

story.append(
    P(
        "The primary data source is the Reserve Bank of India. Repo-rate "
        "data is obtained from the RBI table covering major monetary-policy "
        "measures. WALR data is obtained from the RBI table containing "
        "bank-group-wise Weighted Average Lending Rates on outstanding "
        "rupee loans."
    )
)

story.append(
    P(
        "The datasets are imported into Python using Pandas. Dates and "
        "numeric columns are standardised, records are sorted and missing "
        "values and duplicates are checked. The repo-rate observations "
        "are converted to quarterly frequency and aligned with WALR."
    )
)

story.append(
    P(
        "The final dataset contains 55 quarterly observations from June "
        "2012 to June 2026. The March 2012 WALR observation is excluded "
        "because a matching repo-rate observation was not available in "
        "the prepared analytical dataset."
    )
)

story.append(P("9. Analytical Framework", heading_style))

story.append(
    P(
        "The study calculates descriptive statistics, maximum and minimum "
        "rates, Pearson correlation, quarterly changes and a one-quarter "
        "lag. The correlation between rate levels measures linear "
        "association over the selected period. Change correlation focuses "
        "more directly on short-term movements."
    )
)

story.append(
    P(
        "Forward-filling is used where required to carry the latest "
        "available repo-rate observation between policy observations. "
        "This is a data-preparation method for creating the quarterly "
        "analytical series and should not be interpreted as evidence that "
        "the rate was economically unchanged on every day."
    )
)

story.append(P("10. Dataset Variables", heading_style))

data = [
    ["Variable", "Purpose"],
    ["Quarter", "Quarter-end analytical date"],
    ["Repo", "RBI policy repo rate"],
    ["Public Sector Banks", "Public-sector bank WALR"],
    ["Private Sector Banks", "Private-bank WALR"],
    ["Foreign Banks", "Foreign-bank WALR"],
    ["All SCBs", "Aggregate bank WALR"],
    ["Repo_Change", "Quarterly repo-rate change"],
    ["WALR_Change", "Quarterly WALR change"]
]

table = Table(
    [[P(x, small_style), P(y, small_style)] for x, y in data],
    colWidths=[5.0 * cm, 11.0 * cm],
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

story.append(P("11. Findings from the Project Analysis", heading_style))

story.append(
    P(
        "The final analytical dataset contains 55 quarterly observations "
        "from June 2012 to June 2026. The maximum repo rate observed is "
        "<b>8.00%</b> and the minimum is <b>4.00%</b>."
    )
)

story.append(
    P(
        "For All SCBs WALR, the maximum observed value is <b>12.40%</b> "
        "and the minimum is <b>8.74%</b>. These values show that the "
        "Indian banking system experienced different interest-rate "
        "environments during the study period."
    )
)

story.append(P("12. Correlation Results", heading_style))

story.append(
    P(
        "The Pearson correlation between the repo rate and All SCBs WALR "
        "is approximately <b>0.856</b>. This indicates a strong positive "
        "statistical association between the two rate levels in the "
        "prepared dataset."
    )
)

story.append(
    P(
        "The correlation between quarterly changes in repo rate and WALR "
        "is approximately <b>0.602</b>. This is lower than the level "
        "correlation, which indicates that long-term co-movement and "
        "short-term movements are not identical."
    )
)

story.append(
    P(
        "The one-quarter lag analysis produces a correlation of approximately "
        "<b>0.656</b>. This supports examining timing when studying monetary "
        "transmission because outstanding loan rates may not respond "
        "immediately to policy-rate changes."
    )
)

story.append(P("13. Bank Group Analysis", heading_style))

story.append(
    P(
        "The project compares WALR across Public Sector Banks, Private "
        "Sector Banks and Foreign Banks. Differences between these groups "
        "can arise because of variations in funding structure, customer "
        "mix, competition, loan portfolios and pricing strategies."
    )
)

story.append(
    P(
        "The Power BI dashboard presents these bank groups through a "
        "clustered column chart. This allows users to compare the lending "
        "rate levels across groups while the Python analysis provides "
        "additional statistical and time-series analysis."
    )
)

story.append(P("14. Key Observations", heading_style))

for item in [
    "Repo rate and All SCBs WALR show strong positive association.",
    "The level correlation is approximately 0.856.",
    "The quarterly-change correlation is approximately 0.602.",
    "The one-quarter lag correlation is approximately 0.656.",
    "Outstanding-loan WALR may adjust more slowly than policy rates.",
    "WALR differs across bank groups.",
    "Correlation represents association and does not prove causation."
]:
    story.append(bullet(item))

story.append(P("15. Significance of the Study", heading_style))

story.append(
    P(
        "The study is useful for understanding how monetary-policy changes "
        "can be reflected in bank lending conditions. Borrowers can use "
        "lending-rate trends to understand the broader cost of credit, "
        "while analysts can use the data to examine interest-rate cycles."
    )
)

story.append(
    P(
        "For data analysts, the project provides a practical example of "
        "combining economic concepts with real-world official data. It "
        "also demonstrates how raw financial data can be transformed into "
        "meaningful statistical findings and interactive dashboards."
    )
)

story.append(P("16. Limitations", heading_style))

for item in [
    "The study is observational and does not establish causality.",
    "Other variables such as inflation, GDP, liquidity and deposit rates are not included.",
    "Outstanding-loan WALR may react more slowly than fresh-loan rates.",
    "Quarterly alignment simplifies the exact timing of policy decisions.",
    "The one-quarter lag is exploratory and does not establish an exact transmission period."
]:
    story.append(bullet(item))

story.append(P("17. Future Scope", heading_style))

story.append(
    P(
        "Future research can include fresh-loan WALR, deposit rates, "
        "inflation, GDP growth, credit growth and liquidity indicators. "
        "Multiple lag periods can also be tested. Regression, time-series "
        "models and causality tests could provide deeper analysis."
    )
)

story.append(P("18. Conclusion", heading_style))

story.append(
    P(
        "This study examined the relationship between the RBI repo rate "
        "and bank lending rates in India using RBI data and a quarterly "
        "data-analysis framework. The project found a strong positive "
        "association between repo rate and All SCBs WALR, while change "
        "and lag analysis provided additional information about short-term "
        "movement and timing."
    )
)

story.append(
    P(
        "The findings demonstrate that repo rates and bank lending rates "
        "are closely related, but lending rates are influenced by several "
        "factors and may adjust with a delay. Therefore, the results should "
        "be interpreted as statistical association rather than direct "
        "causation."
    )
)

story.append(P("19. References", heading_style))

references = [
    "Reserve Bank of India, Major Monetary Policy Measures – Bank Rate, CRR, SLR and Policy Rates.",
    "Reserve Bank of India, Lending Rates of Scheduled Commercial Banks (Excluding RRBs), Table 7: Bank Group-wise WALR on Outstanding Rupee Loans.",
    "Reserve Bank of India, RBI Bulletin – Monetary Policy Transmission related articles.",
    "Reserve Bank of India, Annual Report 2023–24.",
    "Reserve Bank of India, Database on Indian Economy (DBIE), Financial Sector Statistics."
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
print("PAPER 1 CREATED")
print("=" * 60)
print(f"Output: {OUTPUT_FILE}")
print("Pages: 3")
print("=" * 60)