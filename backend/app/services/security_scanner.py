import os
import re


# ==========================================
# ACTUAL SECURITY SCANNER
# ==========================================

def scan_project(project_path="."):

    findings = []

    allowed_extensions = (
        ".py",
        ".js",
        ".html",
        ".css",
        ".json",
        ".env",
        ".txt",
        ".yml",
        ".yaml",
    )

    # ==========================================
    # SECRET PATTERNS
    # ==========================================

    secret_patterns = [
        r'password\s*=\s*["\'][^"\']+["\']',
        r'secret\s*=\s*["\'][^"\']+["\']',
        r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
        r'access[_-]?token\s*=\s*["\'][^"\']+["\']',
    ]

    # ==========================================
    # DIRECTORIES TO IGNORE
    # ==========================================

    ignored_directories = {
        "venv",
        ".venv",
        "__pycache__",
        ".git",
        "node_modules",
        ".idea",
        ".vscode",
    }

    # ==========================================
    # SCAN PROJECT FILES
    # ==========================================

    for root, dirs, files in os.walk(project_path):

        # Ignore unnecessary directories
        dirs[:] = [
            directory
            for directory in dirs
            if directory not in ignored_directories
        ]

        for filename in files:

            # Do not scan this scanner itself
            if filename.lower() == "security_scanner.py":
                continue

            # Scan only supported files
            if not filename.lower().endswith(
                allowed_extensions
            ):
                continue

            filepath = os.path.join(
                root,
                filename
            )

            try:

                with open(
                    filepath,
                    "r",
                    encoding="utf-8",
                    errors="ignore",
                ) as file:

                    content = file.read()

                # ======================================
                # 1. HARDCODED SECRET CHECK
                # ======================================

                secret_found = False

                for pattern in secret_patterns:

                    if re.search(
                        pattern,
                        content,
                        re.IGNORECASE,
                    ):

                        findings.append({

                            "name":
                                "Hardcoded Secret",

                            "severity":
                                "High",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "A possible hardcoded password, secret, API key or access token was detected.",

                            "recommendation":
                                "Move sensitive values to environment variables or a secure secret manager."

                        })

                        secret_found = True

                        break

                # ======================================
                # 2. DEBUG MODE CHECK
                # ======================================

                debug_patterns = [
                    r'debug\s*=\s*True',
                    r'debug\s*:\s*true',
                    r'DEBUG\s*=\s*True',
                ]

                for pattern in debug_patterns:

                    if re.search(
                        pattern,
                        content,
                        re.IGNORECASE,
                    ):

                        findings.append({

                            "name":
                                "Debug Mode Enabled",

                            "severity":
                                "Medium",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "Debug mode appears to be enabled in the application configuration.",

                            "recommendation":
                                "Disable debug mode before production deployment."

                        })

                        break

                # ======================================
                # 3. CORS CHECK
                # ======================================

                if "allow_origins" in content:

                    cors_permissive = re.search(
                        r'allow_origins\s*=\s*\[[^\]]*["\']\*["\']',
                        content,
                        re.IGNORECASE,
                    )

                    if cors_permissive:

                        findings.append({

                            "name":
                                "Permissive CORS Configuration",

                            "severity":
                                "Medium",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "CORS configuration allows requests from all origins.",

                            "recommendation":
                                "Restrict allowed origins to trusted application domains."

                        })

                # ======================================
                # 4. INSECURE HTTP URL CHECK
                # ======================================

                http_urls = re.findall(
                    r'http://[^\s"\']+',
                    content,
                    re.IGNORECASE,
                )

                if http_urls:

                    # Ignore localhost development URLs
                    external_http_urls = [
                        url
                        for url in http_urls
                        if "localhost" not in url.lower()
                        and "127.0.0.1" not in url.lower()
                    ]

                    if external_http_urls:

                        findings.append({

                            "name":
                                "Insecure HTTP Connection",

                            "severity":
                                "Medium",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "An external HTTP connection was detected. Data may be transmitted without encryption.",

                            "recommendation":
                                "Use HTTPS for external application and API connections."

                        })

                # ======================================
                # 5. SQL INJECTION RISK CHECK
                # ======================================

                sql_patterns = [
                    r'execute\s*\(\s*[fF]["\']',
                    r'execute\s*\(\s*["\'].*\+',
                    r'query\s*\(\s*[fF]["\']',
                ]

                for pattern in sql_patterns:

                    if re.search(
                        pattern,
                        content,
                        re.IGNORECASE,
                    ):

                        findings.append({

                            "name":
                                "Potential SQL Injection Risk",

                            "severity":
                                "High",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "Potential dynamically constructed SQL query was detected.",

                            "recommendation":
                                "Use parameterized queries or ORM methods instead of dynamically constructed SQL."

                        })

                        break

                # ======================================
                # 6. WEAK PASSWORD CHECK
                # ======================================

                weak_password_patterns = [
                    r'password\s*=\s*["\']123456["\']',
                    r'password\s*=\s*["\']12345["\']',
                    r'password\s*=\s*["\']password["\']',
                    r'password\s*=\s*["\']admin["\']',
                ]

                for pattern in weak_password_patterns:

                    if re.search(
                        pattern,
                        content,
                        re.IGNORECASE,
                    ):

                        findings.append({

                            "name":
                                "Weak Password Detected",

                            "severity":
                                "High",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "A commonly used weak password was detected in the source code.",

                            "recommendation":
                                "Use strong passwords and store credentials securely using environment variables or a secret manager."

                        })

                        break

                # ======================================
                # 7. DISABLED SSL VERIFICATION
                # ======================================

                ssl_patterns = [
                    r'verify\s*=\s*False',
                    r'verify_ssl\s*=\s*False',
                ]

                for pattern in ssl_patterns:

                    if re.search(
                        pattern,
                        content,
                        re.IGNORECASE,
                    ):

                        findings.append({

                            "name":
                                "SSL Verification Disabled",

                            "severity":
                                "High",

                            "status":
                                "Warning",

                            "file":
                                filepath,

                            "description":
                                "SSL certificate verification appears to be disabled.",

                            "recommendation":
                                "Enable SSL/TLS certificate verification for secure communications."

                        })

                        break

            except Exception as error:

                print(
                    f"Unable to scan {filepath}: {error}"
                )

    # ==========================================
    # NO FINDINGS
    # ==========================================

    if not findings:

        findings.append({

            "name":
                "Security Configuration",

            "severity":
                "Low",

            "status":
                "Passed",

            "file":
                "-",

            "description":
                "No obvious security configuration issues were detected.",

            "recommendation":
                "Continue regular security scanning."

        })

    return findings


# ==========================================
# SECURITY SCORE
# ==========================================

def calculate_security_score(findings):

    if not findings:
        return 100

    score = 100

    for finding in findings:

        if finding["status"] != "Warning":
            continue

        severity = finding["severity"]

        if severity == "Critical":
            score -= 40

        elif severity == "High":
            score -= 25

        elif severity == "Medium":
            score -= 15

        elif severity == "Low":
            score -= 5

    # Minimum score = 0
    return max(score, 0)


# ==========================================
# SECURITY SUMMARY
# ==========================================

def get_security_summary(findings):

    critical = 0
    high = 0
    medium = 0
    low = 0

    for finding in findings:

        if finding["status"] != "Warning":
            continue

        severity = finding["severity"]

        if severity == "Critical":
            critical += 1

        elif severity == "High":
            high += 1

        elif severity == "Medium":
            medium += 1

        elif severity == "Low":
            low += 1

    return {

        "critical":
            critical,

        "high":
            high,

        "medium":
            medium,

        "low":
            low,

    }