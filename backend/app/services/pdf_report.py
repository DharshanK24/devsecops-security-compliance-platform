from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    PageBreak,
)


# ==========================================
# GENERATE DEVSECOPS PDF REPORT
# ==========================================

def generate_combined_report(
    filepath,
    username,
    email,
    security_data,
    compliance_data
):

    # ======================================
    # DOCUMENT
    # ======================================

    document = SimpleDocTemplate(
        filepath,
        pagesize=A4,

        rightMargin=10 * mm,
        leftMargin=10 * mm,

        topMargin=10 * mm,
        bottomMargin=14 * mm,

        title="DevSecOps Security & Compliance Report",
        author="DevSecOps Security & Compliance Platform",
    )

    # ======================================
    # STYLES
    # ======================================

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=18,
        leading=21,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=3,
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=8,
        leading=9,
        alignment=TA_CENTER,
        textColor=colors.grey,
        spaceBefore=0,
        spaceAfter=5,
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=11,
        leading=13,
        spaceBefore=4,
        spaceAfter=5,
    )

    subheading_style = ParagraphStyle(
        "SubHeading",
        parent=styles["Heading3"],
        fontSize=9.5,
        leading=11,
        spaceBefore=3,
        spaceAfter=3,
    )

    normal_style = ParagraphStyle(
        "NormalCustom",
        parent=styles["Normal"],
        fontSize=8,
        leading=10,
        spaceBefore=0,
        spaceAfter=0,
    )

    small_style = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontSize=7.5,
        leading=9,
        spaceBefore=0,
        spaceAfter=0,
    )

    score_style = ParagraphStyle(
        "Score",
        parent=styles["Normal"],
        fontSize=12,
        leading=14,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=0,
    )

    footer_style = ParagraphStyle(
        "FooterStyle",
        parent=styles["Normal"],
        fontSize=7,
        leading=8,
        alignment=TA_CENTER,
        textColor=colors.grey,
        spaceBefore=0,
        spaceAfter=0,
    )

    story = []

    # ======================================
    # SAFE DATA
    # ======================================

    security_data = security_data or {}
    compliance_data = compliance_data or {}

    security_score = (
        security_data.get("security_score", 0) or 0
    )

    security_scan_id = (
        security_data.get("scan_id")
    )

    security_total = (
        security_data.get("total_checks", 0) or 0
    )

    security_passed = (
        security_data.get("passed_checks", 0) or 0
    )

    security_failed = security_data.get(
        "failed_checks",
        security_total - security_passed
    )

    if security_failed is None:
        security_failed = (
            security_total - security_passed
        )

    findings = (
        security_data.get("findings", {}) or {}
    )

    critical = (
        findings.get("critical", 0) or 0
    )

    high = (
        findings.get("high", 0) or 0
    )

    medium = (
        findings.get("medium", 0) or 0
    )

    low = (
        findings.get("low", 0) or 0
    )

    security_summary = (
        security_data.get("summary", {}) or {}
    )

    total_vulnerabilities = security_summary.get(
        "total_vulnerabilities",
        critical + high + medium + low
    ) or 0

    compliance_scan_id = (
        compliance_data.get("scan_id")
    )

    compliance_score = (
        compliance_data.get("compliance_score", 0)
        or 0
    )

    compliance_total = (
        compliance_data.get("total_checks", 0)
        or 0
    )

    compliant_checks = (
        compliance_data.get("compliant_checks", 0)
        or 0
    )

    review_required = (
        compliance_data.get("review_required", 0)
        or 0
    )

    compliance_status = (
        compliance_data.get("status", "No Scan")
        or "No Scan"
    )

    security_date = (
        security_data.get("created_at")
    )

    compliance_date = (
        compliance_data.get("created_at")
    )

    # ======================================
    # TITLE
    # ======================================

    story.append(
        Paragraph(
            "DevSecOps Security & Compliance Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Automated Security Assessment Report",
            subtitle_style
        )
    )

    story.append(
        HRFlowable(
            width="100%",
            thickness=0.8,
            color=colors.HexColor("#2563eb"),
            spaceBefore=0,
            spaceAfter=7,
        )
    )

    # ======================================
    # USER INFORMATION
    # ======================================

    story.append(
        Paragraph(
            "User Information",
            heading_style
        )
    )

    user_table = Table(
        [
            [
                Paragraph(
                    "<b>Username</b>",
                    normal_style
                ),
                Paragraph(
                    str(username or "User"),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Email</b>",
                    normal_style
                ),
                Paragraph(
                    str(email or "-"),
                    normal_style
                )
            ]
        ],
        colWidths=[
            40 * mm,
            137 * mm
        ]
    )

    user_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#f3f4f6")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                5
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                5
            )
        ])
    )

    story.append(user_table)
    story.append(Spacer(1, 8))

    # ======================================
    # EXECUTIVE SUMMARY
    # ======================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    summary_table = Table(
        [
            [
                Paragraph(
                    "<b>Security Score</b>",
                    normal_style
                ),
                Paragraph(
                    f"<b>{security_score}%</b>",
                    score_style
                ),
                Paragraph(
                    "<b>Compliance Score</b>",
                    normal_style
                ),
                Paragraph(
                    f"<b>{compliance_score}%</b>",
                    score_style
                )
            ],
            [
                Paragraph(
                    "<b>Vulnerabilities</b>",
                    normal_style
                ),
                Paragraph(
                    f"<b>{total_vulnerabilities}</b>",
                    score_style
                ),
                Paragraph(
                    "<b>Review Required</b>",
                    normal_style
                ),
                Paragraph(
                    f"<b>{review_required}</b>",
                    score_style
                )
            ]
        ],
        colWidths=[
            40 * mm,
            30 * mm,
            45 * mm,
            62 * mm
        ]
    )

    summary_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                colors.HexColor("#f8fafc")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.6,
                colors.HexColor("#cbd5e1")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "ALIGN",
                (1, 0),
                (1, -1),
                "CENTER"
            ),
            (
                "ALIGN",
                (3, 0),
                (3, -1),
                "CENTER"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                7
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                7
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(summary_table)
    story.append(Spacer(1, 9))

    # ======================================
    # SECURITY ASSESSMENT
    # ======================================

    story.append(
        Paragraph(
            "1. Security Assessment",
            heading_style
        )
    )

    security_table = Table(
        [
            [
                Paragraph(
                    "<b>Scan ID</b>",
                    normal_style
                ),
                Paragraph(
                    f"#{security_scan_id}"
                    if security_scan_id is not None
                    else "No Scan",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Security Score</b>",
                    normal_style
                ),
                Paragraph(
                    f"{security_score}%",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Total Checks</b>",
                    normal_style
                ),
                Paragraph(
                    str(security_total),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Passed Checks</b>",
                    normal_style
                ),
                Paragraph(
                    str(security_passed),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Failed Checks</b>",
                    normal_style
                ),
                Paragraph(
                    str(security_failed),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Total Vulnerabilities</b>",
                    normal_style
                ),
                Paragraph(
                    str(total_vulnerabilities),
                    normal_style
                )
            ]
        ],
        colWidths=[
            60 * mm,
            117 * mm
        ]
    )

    security_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#f3f4f6")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                4
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                4
            )
        ])
    )

    story.append(security_table)
    story.append(Spacer(1, 7))

    # ======================================
    # SECURITY FINDINGS
    # ======================================

    story.append(
        Paragraph(
            "Security Findings",
            subheading_style
        )
    )

    findings_table = Table(
        [
            [
                Paragraph(
                    "<b>Severity</b>",
                    small_style
                ),
                Paragraph(
                    "<b>Count</b>",
                    small_style
                ),
                Paragraph(
                    "<b>Status</b>",
                    small_style
                )
            ],
            [
                Paragraph(
                    "Critical",
                    small_style
                ),
                Paragraph(
                    str(critical),
                    small_style
                ),
                Paragraph(
                    "Detected"
                    if critical > 0
                    else "None",
                    small_style
                )
            ],
            [
                Paragraph(
                    "High",
                    small_style
                ),
                Paragraph(
                    str(high),
                    small_style
                ),
                Paragraph(
                    "Detected"
                    if high > 0
                    else "None",
                    small_style
                )
            ],
            [
                Paragraph(
                    "Medium",
                    small_style
                ),
                Paragraph(
                    str(medium),
                    small_style
                ),
                Paragraph(
                    "Detected"
                    if medium > 0
                    else "None",
                    small_style
                )
            ],
            [
                Paragraph(
                    "Low",
                    small_style
                ),
                Paragraph(
                    str(low),
                    small_style
                ),
                Paragraph(
                    "Detected"
                    if low > 0
                    else "None",
                    small_style
                )
            ]
        ],
        colWidths=[
            55 * mm,
            30 * mm,
            92 * mm
        ]
    )

    findings_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#111827")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "ALIGN",
                (1, 1),
                (1, -1),
                "CENTER"
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                5
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                5
            )
        ])
    )

    story.append(findings_table)
    story.append(Spacer(1, 9))

    # ======================================
    # COMPLIANCE ASSESSMENT
    # ======================================

    story.append(
        Paragraph(
            "2. Compliance Assessment",
            heading_style
        )
    )

    compliance_table = Table(
        [
            [
                Paragraph(
                    "<b>Scan ID</b>",
                    normal_style
                ),
                Paragraph(
                    f"#{compliance_scan_id}"
                    if compliance_scan_id is not None
                    else "No Scan",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Compliance Score</b>",
                    normal_style
                ),
                Paragraph(
                    f"{compliance_score}%",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Total Checks</b>",
                    normal_style
                ),
                Paragraph(
                    str(compliance_total),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Compliant Checks</b>",
                    normal_style
                ),
                Paragraph(
                    str(compliant_checks),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Review Required</b>",
                    normal_style
                ),
                Paragraph(
                    str(review_required),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Status</b>",
                    normal_style
                ),
                Paragraph(
                    str(compliance_status),
                    normal_style
                )
            ]
        ],
        colWidths=[
            60 * mm,
            117 * mm
        ]
    )

    compliance_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#f3f4f6")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                4
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                4
            )
        ])
    )

    story.append(compliance_table)
    story.append(Spacer(1, 7))

    # ======================================
    # COMPLIANCE STATUS
    # ======================================

    story.append(
        Paragraph(
            "Compliance Status",
            subheading_style
        )
    )

    if compliance_score >= 80:

        compliance_message = (
            "The compliance assessment is compliant."
        )

    else:

        compliance_message = (
            "The compliance assessment requires review "
            "before production deployment."
        )

    story.append(
        Paragraph(
            compliance_message,
            normal_style
        )
    )

    # ======================================
    # FORCE PAGE 2
    # ======================================

    story.append(
        PageBreak()
    )

    # ======================================
    # PAGE 2 - OVERALL SECURITY SUMMARY
    # ======================================

    story.append(
        Paragraph(
            "3. Overall Security Summary",
            heading_style
        )
    )

    overall_table = Table(
        [
            [
                Paragraph(
                    "<b>Security Score</b>",
                    normal_style
                ),
                Paragraph(
                    f"{security_score}%",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Compliance Score</b>",
                    normal_style
                ),
                Paragraph(
                    f"{compliance_score}%",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Security Vulnerabilities</b>",
                    normal_style
                ),
                Paragraph(
                    str(total_vulnerabilities),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Compliance Review Items</b>",
                    normal_style
                ),
                Paragraph(
                    str(review_required),
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Compliance Status</b>",
                    normal_style
                ),
                Paragraph(
                    str(compliance_status),
                    normal_style
                )
            ]
        ],
        colWidths=[
            85 * mm,
            92 * mm
        ]
    )

    overall_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#f3f4f6")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(
        overall_table
    )

    story.append(
        Spacer(1, 15)
    )

    # ======================================
    # RECOMMENDATIONS
    # ======================================

    story.append(
        Paragraph(
            "4. Recommendations",
            heading_style
        )
    )

    recommendations = []

    if critical > 0:

        recommendations.append(
            "Critical vulnerabilities should be addressed immediately."
        )

    if high > 0:

        recommendations.append(
            "High severity security issues should be reviewed "
            "and remediated."
        )

    if medium > 0:

        recommendations.append(
            "Medium severity security issues should be reviewed "
            "and appropriate security controls should be applied."
        )

    if low > 0:

        recommendations.append(
            "Low severity security issues should be monitored "
            "and fixed when appropriate."
        )

    if review_required > 0:

        recommendations.append(
            "Compliance review items should be addressed "
            "before production deployment."
        )

    if compliance_score < 80:

        recommendations.append(
            "Improve compliance controls to achieve a target "
            "compliance score of at least 80%."
        )

    if security_score < 80:

        recommendations.append(
            "Security controls should be strengthened to improve "
            "the overall security score."
        )

    if not recommendations:

        recommendations.append(
            "No immediate security recommendations were identified."
        )

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        story.append(
            Paragraph(
                f"{index}. {recommendation}",
                normal_style
            )
        )

        story.append(
            Spacer(1, 6)
        )

    # ======================================
    # REPORT INFORMATION
    # ======================================

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            "Report Information",
            heading_style
        )
    )

    metadata_table = Table(
        [
            [
                Paragraph(
                    "<b>Security Scan Date</b>",
                    normal_style
                ),
                Paragraph(
                    str(security_date)
                    if security_date
                    else "N/A",
                    normal_style
                )
            ],
            [
                Paragraph(
                    "<b>Compliance Scan Date</b>",
                    normal_style
                ),
                Paragraph(
                    str(compliance_date)
                    if compliance_date
                    else "N/A",
                    normal_style
                )
            ]
        ],
        colWidths=[
            60 * mm,
            117 * mm
        ]
    )

    metadata_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#f3f4f6")
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.HexColor("#d1d5db")
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                5
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                5
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                6
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(
        metadata_table
    )

    story.append(
        Spacer(1, 15)
    )

    # ======================================
    # FOOTER
    # ======================================

    story.append(
        HRFlowable(
            width="100%",
            thickness=0.5,
            color=colors.HexColor("#d1d5db"),
            spaceBefore=3,
            spaceAfter=5
        )
    )

    story.append(
        Paragraph(
            "Generated by DevSecOps Security & Compliance Platform",
            footer_style
        )
    )

    # ======================================
    # PAGE NUMBER
    # ======================================

    def add_page_number(canvas, doc):

        canvas.saveState()

        canvas.setFont(
            "Helvetica",
            7
        )

        canvas.setFillColor(
            colors.grey
        )

        canvas.drawCentredString(
            A4[0] / 2,
            6 * mm,
            f"Page {doc.page}"
        )

        canvas.restoreState()

    # ======================================
    # BUILD PDF
    # ======================================

    document.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )