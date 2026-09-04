// ==========================================
// AUTHENTICATION
// ==========================================

const token = localStorage.getItem("access_token");

if (!token) {
    alert("Please login first.");
    window.location.href = "login.html";
}


// ==========================================
// LOGOUT
// ==========================================

function logout() {

    localStorage.removeItem("access_token");

    alert("Logged out successfully.");

    window.location.href = "login.html";
}


// ==========================================
// LOAD DASHBOARD
// ==========================================

async function loadDashboard() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/dashboard/",
            {
                method: "GET",

                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Accept": "application/json"
                }
            }
        );


        const data = await response.json();

        console.log("Dashboard response:", data);


        // ==========================================
        // CHECK RESPONSE
        // ==========================================

        if (!response.ok) {

            alert(
                data.detail ||
                data.message ||
                "Unable to load dashboard"
            );

            return;
        }


        // ==========================================
        // DISPLAY USERNAME
        // ==========================================

        if (data.user) {

            const usernameDisplay =
                document.getElementById("usernameDisplay");

            if (usernameDisplay) {

                usernameDisplay.textContent =
                    "👤 " + data.user.username;
            }
        }


        // ==========================================
        // GET SECURITY DATA
        // ==========================================

        const security =
            data.security ||
            data.data?.security ||
            data;


        // ==========================================
        // GET COMPLIANCE DATA
        // ==========================================

        const compliance =
            data.compliance ||
            data.data?.compliance ||
            data;


        console.log("Security:", security);
        console.log("Compliance:", compliance);


        // ==========================================
        // SECURITY SCORE
        // ==========================================

        const securityScore =
            security.security_score ??
            security.score ??
            data.security_score ??
            0;


        const securityScoreElement =
            document.getElementById("securityScore");

        if (securityScoreElement) {

            securityScoreElement.textContent =
                securityScore + "%";
        }


        // ==========================================
        // VULNERABILITIES
        // ==========================================

        const vulnerabilities =
            security.vulnerabilities ??
            (
                (security.critical ?? 0) +
                (security.high ?? 0) +
                (security.medium ?? 0) +
                (security.low ?? 0)
            );


        const vulnerabilitiesElement =
            document.getElementById("vulnerabilities");

        if (vulnerabilitiesElement) {

            vulnerabilitiesElement.textContent =
                vulnerabilities;
        }


        // ==========================================
        // COMPLIANCE SCORE
        // ==========================================

        const complianceScore =
            compliance.compliance_score ??
            compliance.score ??
            data.compliance_score ??
            0;


        const complianceScoreElement =
            document.getElementById("complianceScore");

        if (complianceScoreElement) {

            complianceScoreElement.textContent =
                complianceScore + "%";
        }


        // ==========================================
        // COMPLIANCE STATUS
        // ==========================================

        const complianceStatus =
            compliance.status ??
            data.status ??
            "Unknown";


        const complianceStatusElement =
            document.getElementById("complianceStatus");

        if (complianceStatusElement) {

            complianceStatusElement.textContent =
                complianceStatus;
        }


        // ==========================================
        // SECURITY SUMMARY
        // ==========================================

        const securityDetails =
            document.getElementById("securityDetails");


        if (securityDetails) {

            securityDetails.innerHTML = `

                <p>
                    <strong>Security Score:</strong>
                    ${securityScore}%
                </p>

                <p>
                    <strong>Critical:</strong>
                    ${security.critical ?? 0}
                </p>

                <p>
                    <strong>High:</strong>
                    ${security.high ?? 0}
                </p>

                <p>
                    <strong>Medium:</strong>
                    ${security.medium ?? 0}
                </p>

                <p>
                    <strong>Low:</strong>
                    ${security.low ?? 0}
                </p>

                <p>
                    <strong>Total Vulnerabilities:</strong>
                    ${vulnerabilities}
                </p>

            `;
        }


        // ==========================================
        // COMPLIANCE SUMMARY
        // ==========================================

        const complianceDetails =
            document.getElementById("complianceDetails");


        if (complianceDetails) {

            complianceDetails.innerHTML = `

                <p>
                    <strong>Compliance Score:</strong>
                    ${complianceScore}%
                </p>

                <p>
                    <strong>Status:</strong>
                    ${complianceStatus}
                </p>

                <p>
                    <strong>Total Checks:</strong>
                    ${compliance.total_checks ?? 0}
                </p>

                <p>
                    <strong>Compliant Checks:</strong>
                    ${compliance.compliant_checks ?? 0}
                </p>

                <p>
                    <strong>Review Required:</strong>
                    ${compliance.review_required ?? 0}
                </p>

            `;
        }


        // ==========================================
        // SECURITY BREAKDOWN
        // ==========================================

        const criticalCount =
            security.critical ?? 0;

        const highCount =
            security.high ?? 0;

        const mediumCount =
            security.medium ?? 0;

        const lowCount =
            security.low ?? 0;


        const criticalElement =
            document.getElementById("criticalCount");

        const highElement =
            document.getElementById("highCount");

        const mediumElement =
            document.getElementById("mediumCount");

        const lowElement =
            document.getElementById("lowCount");


        if (criticalElement) {
            criticalElement.textContent = criticalCount;
        }

        if (highElement) {
            highElement.textContent = highCount;
        }

        if (mediumElement) {
            mediumElement.textContent = mediumCount;
        }

        if (lowElement) {
            lowElement.textContent = lowCount;
        }


        // ==========================================
        // COMPLIANCE BREAKDOWN
        // ==========================================

        const totalChecks =
            compliance.total_checks ?? 0;

        const compliantChecks =
            compliance.compliant_checks ?? 0;

        const reviewRequired =
            compliance.review_required ?? 0;


        const totalChecksElement =
            document.getElementById("totalChecks");

        const compliantChecksElement =
            document.getElementById("compliantChecks");

        const reviewRequiredElement =
            document.getElementById("reviewRequired");


        if (totalChecksElement) {
            totalChecksElement.textContent = totalChecks;
        }

        if (compliantChecksElement) {
            compliantChecksElement.textContent = compliantChecks;
        }

        if (reviewRequiredElement) {
            reviewRequiredElement.textContent = reviewRequired;
        }


        // ==========================================
        // COMPLIANCE PROGRESS
        // ==========================================

        const progressText =
            document.getElementById(
                "complianceProgressText"
            );

        const progressBar =
            document.getElementById(
                "complianceProgress"
            );


        const progress =
            Math.max(
                0,
                Math.min(
                    100,
                    Number(complianceScore)
                )
            );


        if (progressText) {

            progressText.textContent =
                progress + "%";
        }

        if (progressBar) {

            progressBar.style.width =
                progress + "%";
        }


        // ==========================================
        // LOAD SECURITY FINDINGS
        // ==========================================

        await loadSecurityIssues();

    }
    catch (error) {

        console.error(
            "Dashboard Error:",
            error
        );

        alert(
            "Unable to connect to backend."
        );
    }
}


// ==========================================
// SECURITY ISSUES / FINDINGS
// ==========================================

async function loadSecurityIssues() {

    const securityIssues =
        document.getElementById("securityIssues");


    if (!securityIssues) {

        console.log(
            "Security Issues container not found."
        );

        return;
    }


    securityIssues.innerHTML = `

        <div class="security-issue-empty">

            <h3>
                ⏳ Loading Security Findings...
            </h3>

            <p>
                Please wait while findings are loaded.
            </p>

        </div>

    `;


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/scanner/",
            {
                method: "GET",

                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Accept": "application/json"
                }
            }
        );


        const data = await response.json();


        console.log(
            "Security Findings:",
            data
        );


        if (!response.ok) {

            securityIssues.innerHTML = `

                <div class="security-issue-empty">

                    <h3>
                        ⚠️ Unable to Load Findings
                    </h3>

                    <p>
                        ${
                            data.detail ||
                            data.message ||
                            "Security scan failed."
                        }
                    </p>

                </div>

            `;

            return;
        }


        // ==========================================
        // GET FINDINGS
        // ==========================================

        const findings =
            data.findings ?? [];


        // ==========================================
        // NO FINDINGS
        // ==========================================

        if (findings.length === 0) {

            securityIssues.innerHTML = `

                <div class="security-issue-empty">

                    <span class="empty-icon">
                        🛡️
                    </span>

                    <h3>
                        No Security Findings
                    </h3>

                    <p>
                        No security findings were returned
                        by the latest scan.
                    </p>

                </div>

            `;

            return;
        }


        // ==========================================
        // DISPLAY ALL FINDINGS
        // ==========================================

        let html = "";


        findings.forEach((finding) => {

            const severity =
                finding.severity ?? "Unknown";

            const status =
                finding.status ?? "Unknown";

            const name =
                finding.name ?? "Security Check";

            const description =
                finding.description ??
                "No description available.";


            const severityClass =
                severity.toLowerCase();


            const statusClass =
                status.toLowerCase() === "passed"
                    ? "status-passed"
                    : "status-warning";


            html += `

                <div class="security-issue">

                    <div class="issue-header">

                        <div>

                            <span
                                class="severity-badge ${severityClass}">

                                ${severity}

                            </span>


                            <h3>

                                ${name}

                            </h3>

                        </div>


                        <span
                            class="issue-status ${statusClass}">

                            ${status}

                        </span>

                    </div>


                    <p class="issue-description">

                        ${description}

                    </p>


                    <div class="issue-info">

                        <div>

                            <strong>
                                Severity
                            </strong>

                            <span>
                                ${severity}
                            </span>

                        </div>


                        <div>

                            <strong>
                                Status
                            </strong>

                            <span>
                                ${status}
                            </span>

                        </div>


                        <div>

                            <strong>
                                Category
                            </strong>

                            <span>
                                Security
                            </span>

                        </div>

                    </div>


                    ${
                        status !== "Passed"
                            ? `

                                <div class="recommendation">

                                    <strong>
                                        Recommendation
                                    </strong>

                                    <p>
                                        Review this security
                                        configuration and apply
                                        the recommended controls.
                                    </p>

                                </div>

                              `
                            : ""
                    }

                </div>

            `;

        });


        securityIssues.innerHTML =
            html;

    }
    catch (error) {

        console.error(
            "Security Issues Error:",
            error
        );


        securityIssues.innerHTML = `

            <div class="security-issue-empty">

                <h3>
                    ⚠️ Unable to Connect
                </h3>

                <p>
                    Make sure the FastAPI backend
                    is running.
                </p>

            </div>

        `;
    }
}


// ==========================================
// SECURITY SCAN
// ==========================================

async function runSecurityScan() {

    const button =
        document.getElementById(
            "securityScanBtn"
        );


    try {

        if (button) {

            button.disabled = true;

            button.textContent =
                "⏳ Running Security Scan...";
        }


        // ======================================
        // START NEW SECURITY SCAN
        // ======================================

        const response = await fetch(
            "http://127.0.0.1:8000/scanner/scan",
            {
                method: "POST",

                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Accept": "application/json"
                }
            }
        );


        const data =
            await response.json();


        console.log(
            "Security Scan:",
            data
        );


        if (!response.ok) {

            alert(
                data.detail ||
                data.message ||
                "Security scan failed"
            );

            return;
        }


        const score =
            data.security_score ??
            data.score ??
            data.data?.security_score ??
            0;


        alert(
            "Security Scan Completed!\n\n" +
            "Security Score: " +
            score +
            "%"
        );


        // ======================================
        // REFRESH DASHBOARD
        // ======================================

        await loadDashboard();

        await loadScanHistory();

    }
    catch (error) {

        console.error(
            "Security Scan Error:",
            error
        );

        alert(
            "Unable to connect to backend."
        );

    }
    finally {

        if (button) {

            button.disabled = false;

            button.innerHTML =
                "<span>🛡️</span> Run Security Scan";
        }
    }
}


// ==========================================
// COMPLIANCE SCAN
// ==========================================

async function runComplianceScan() {

    const button =
        document.getElementById(
            "complianceScanBtn"
        );


    try {

        if (button) {

            button.disabled = true;

            button.textContent =
                "⏳ Running Compliance Scan...";
        }


        // ======================================
        // START NEW COMPLIANCE SCAN
        // ======================================

        const response = await fetch(
            "http://127.0.0.1:8000/compliance/scan",
            {
                method: "POST",

                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Accept": "application/json"
                }
            }
        );


        const data =
            await response.json();


        console.log(
            "Compliance Scan:",
            data
        );


        if (!response.ok) {

            alert(
                data.detail ||
                data.message ||
                "Compliance scan failed"
            );

            return;
        }


        const score =
            data.compliance_score ??
            data.score ??
            data.data?.compliance_score ??
            0;


        alert(
            "Compliance Scan Completed!\n\n" +
            "Compliance Score: " +
            score +
            "%"
        );


        // ======================================
        // REFRESH DASHBOARD
        // ======================================

        await loadDashboard();

        await loadScanHistory();

    }
    catch (error) {

        console.error(
            "Compliance Scan Error:",
            error
        );

        alert(
            "Unable to connect to backend."
        );

    }
    finally {

        if (button) {

            button.disabled = false;

            button.innerHTML =
                "<span>✓</span> Run Compliance Scan";
        }
    }
}


// ==========================================
// LOAD SCAN HISTORY
// ==========================================

async function loadScanHistory() {

    const historyContainer =
        document.getElementById("scanHistory");


    if (!historyContainer) {

        console.log(
            "Scan History container not found."
        );

        return;
    }


    historyContainer.innerHTML =
        "<p>Loading scan history...</p>";


    try {

        // ======================================
        // SECURITY HISTORY
        // ======================================

        const securityResponse =
            await fetch(
                "http://127.0.0.1:8000/scanner/history",
                {
                    method: "GET",

                    headers: {
                        "Authorization": `Bearer ${token}`,
                        "Accept": "application/json"
                    }
                }
            );


        const securityData =
            await securityResponse.json();


        console.log(
            "Security History:",
            securityData
        );


        // ======================================
        // COMPLIANCE HISTORY
        // ======================================

        const complianceResponse =
            await fetch(
                "http://127.0.0.1:8000/compliance/history",
                {
                    method: "GET",

                    headers: {
                        "Authorization": `Bearer ${token}`,
                        "Accept": "application/json"
                    }
                }
            );


        const complianceData =
            await complianceResponse.json();


        console.log(
            "Compliance History:",
            complianceData
        );


        // ======================================
        // GET ARRAYS
        // ======================================

        const securityHistory =
            securityData.history ?? [];


        const complianceHistory =
            complianceData.history ?? [];


        // ======================================
        // NO HISTORY
        // ======================================

        if (
            securityHistory.length === 0 &&
            complianceHistory.length === 0
        ) {

            historyContainer.innerHTML = `

                <div class="security-issue">

                    <h3>
                        📭 No Scan History
                    </h3>

                    <p>
                        Run a security or compliance scan
                        to create scan history.
                    </p>

                </div>

            `;

            return;
        }


        // ======================================
        // COMBINE HISTORY
        // ======================================

        const history = [];


        securityHistory.forEach(scan => {

            history.push({

                type: "Security",

                id: scan.scan_id,

                score: scan.security_score,

                checks: scan.total_checks,

                passed: scan.passed_checks,

                review: "-",

                status:
                    scan.security_score >= 80
                        ? "Good"
                        : "Needs Review",

                created_at:
                    scan.created_at
            });

        });


        complianceHistory.forEach(scan => {

            history.push({

                type: "Compliance",

                id: scan.scan_id,

                score: scan.compliance_score,

                checks: scan.total_checks,

                passed: scan.compliant_checks,

                review: scan.review_required,

                status: scan.status,

                created_at:
                    scan.created_at
            });

        });


        // ======================================
        // SORT NEWEST FIRST
        // ======================================

        history.sort(
            (a, b) =>
                new Date(b.created_at) -
                new Date(a.created_at)
        );


        // ======================================
        // CREATE TABLE
        // ======================================

        let html = `

            <div class="history-table-wrapper">

                <table class="history-table">

                    <thead>

                        <tr>

                            <th>Type</th>

                            <th>Scan ID</th>

                            <th>Score</th>

                            <th>Total Checks</th>

                            <th>Passed / Compliant</th>

                            <th>Review</th>

                            <th>Status</th>

                            <th>Date</th>

                        </tr>

                    </thead>

                    <tbody>

        `;


        history.forEach(scan => {

            const date =
                scan.created_at
                    ? new Date(
                        scan.created_at
                    ).toLocaleString()
                    : "-";


            const statusClass =
                scan.status === "Compliant" ||
                scan.status === "Good"
                    ? "history-good"
                    : "history-warning";


            html += `

                <tr>

                    <td>
                        <strong>
                            ${scan.type}
                        </strong>
                    </td>

                    <td>
                        #${scan.id}
                    </td>

                    <td>
                        <strong>
                            ${scan.score}%
                        </strong>
                    </td>

                    <td>
                        ${scan.checks}
                    </td>

                    <td>
                        ${scan.passed}
                    </td>

                    <td>
                        ${scan.review}
                    </td>

                    <td>

                        <span class="${statusClass}">
                            ${scan.status}
                        </span>

                    </td>

                    <td>
                        ${date}
                    </td>

                </tr>

            `;

        });


        html += `

                    </tbody>

                </table>

            </div>

        `;


        historyContainer.innerHTML =
            html;

    }
    catch (error) {

        console.error(
            "Scan History Error:",
            error
        );


        historyContainer.innerHTML = `

            <div class="security-issue">

                <h3>
                    ⚠️ Unable to Load Scan History
                </h3>

                <p>
                    Please make sure the backend
                    server is running.
                </p>

            </div>

        `;
    }
}


// ==========================================
// START DASHBOARD
// ==========================================

async function startDashboard() {

    await loadDashboard();

    await loadScanHistory();

}


// ==========================================
// START APPLICATION
// ==========================================

startDashboard();