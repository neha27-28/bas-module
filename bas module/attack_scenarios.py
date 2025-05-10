SCENARIOS = {
    "Credential Theft": [
        "User logs in from new location",
        "Multiple failed login attempts",
        "MFA disabled",
        "New login from IP 192.168.56.101",
        "PowerShell used to list AD users",
        "Password reset request from unfamiliar location",
        "Brute-force attack detected",
        "Suspicious login pattern (same time every day)",
        "VPN login from unusual IP",
        "Login from TOR network"
    ],
    "Lateral Movement": [
        "Remote Desktop session started",
        "Accessed C$ share on another machine",
        "Used PSExec to run remote command",
        "Account used on multiple systems",
        "Suspicious admin tool downloaded",
        "Remote PowerShell command execution",
        "Admin account used on non-administrative systems",
        "Account compromise followed by lateral movement",
        "Credential dump from system memory",
        "Mimikatz or other credential dump tool detected"
    ],
    "Data Exfiltration": [
        "Large file compressed",
        "File uploaded to unknown domain",
        "Tor process detected",
        "External device plugged in",
        "Traffic to Dropbox observed",
        "Massive data download initiated",
        "Large volume of data being transferred at odd hours",
        "Unusual cloud storage access",
        "Unusual HTTP/FTP traffic detected",
        "Data transferred to external IP address"
    ],
    "Privilege Escalation": [
        "Exploit found in system to gain root/admin access",
        "Elevation of privileges detected using local exploit tools",
        "Sudo command executed by non-privileged user",
        "Unauthorized use of admin credentials",
        "System security settings changed unexpectedly",
        "Zero-day exploit attempt detected",
        "Modification of /etc/sudoers or similar privilege files",
        "Privilege escalation via unpatched vulnerability",
        "User added to an admin group without proper authorization"
    ],
    "Ransomware Attack": [
        "Unusual file encryption activity detected",
        "Suspicious file extensions being added to files",
        "Ransomware communication detected (e.g., C2 server traffic)",
        "Files being renamed with a specific ransom extension",
        "Suspicious process named after a known ransomware family",
        "Encrypted files reported by users",
        "Ransom note found on multiple systems",
        "Malicious attachment in email opened",
        "Email received with suspicious subject line and attachment"
    ],
    "Phishing Attack": [
        "Suspicious email with unknown attachment received",
        "Email from seemingly legitimate source requesting credentials",
        "Unusual domain name in email sender's address",
        "User clicked on link from phishing email",
        "Spoofed email masquerading as IT support",
        "Suspicious email with a sense of urgency (e.g., 'Immediate Action Required')",
        "Unusual file type attached to email (e.g., .exe, .zip)",
        "Redirect from known site to a phishing page",
        "Fake login page detected"
    ],
    "Denial of Service (DoS)": [
        "Unexpected increase in network traffic from one source",
        "Server is unreachable due to high traffic",
        "High rate of HTTP requests detected",
        "ICMP flood detected",
        "UDP flood observed",
        "Server performance degraded due to excessive requests",
        "Network device performance impacted due to DDoS",
        "Suspicious volume of SYN packets being sent"
    ],
    "Supply Chain Attack": [
        "Malicious code inserted into third-party software update",
        "Unexpected changes in software dependencies",
        "Abnormal activity in a trusted vendor's network",
        "Compromised update downloaded from a trusted source",
        "Suspicious connection made to vendor's server",
        "Unexpected change in software version from trusted repository",
        "Legitimate software package modified with malicious code"
    ],
    "Insider Threat": [
        "Employee accessing sensitive data without authorization",
        "Employee transferring files to an external device",
        "Unusual pattern of access to critical infrastructure",
        "Employee leaves organization with sensitive data",
        "Increased use of privileged access by non-administrators",
        "Employees accessing files not relevant to their job role",
        "Unauthorised user gaining access via compromised employee account",
        "User logs in after hours without valid reason"
    ]
}
