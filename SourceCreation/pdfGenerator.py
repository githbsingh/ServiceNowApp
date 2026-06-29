import os
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {
        size: A4;
        margin: 20mm 15mm 25mm 15mm;
        @top-right {
            content: "Doc ID: SOP-LOG-073 | Rev 3.0";
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 8pt;
            color: #7f8c8d;
        }
        @bottom-left {
            content: "CONFIDENTIAL - GLOBAL LOGISTICS & COURIER OPERATIONS";
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 7.5pt;
            color: #95a5a6;
            font-weight: bold;
        }
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 8pt;
            color: #7f8c8d;
        }
    }
    
    *, *::before, *::after {
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #2c3e50;
        line-height: 1.6;
        font-size: 10.5pt;
        margin: 0;
        padding: 0;
        background-color: #ffffff;
    }
    
    /* Header Area */
    .header-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 30px;
    }
    .header-table td {
        border: 1px solid #bdc3c7;
        padding: 12px;
        vertical-align: middle;
    }
    .logo-area {
        width: 30%;
        font-weight: bold;
        font-size: 13pt;
        color: #0b4f6c;
        text-transform: uppercase;
        letter-spacing: 1px;
        line-height: 1.2;
    }
    .title-area {
        width: 45%;
        text-align: center;
    }
    .title-area h1 {
        margin: 0;
        font-size: 15pt;
        color: #0b4f6c;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .meta-area {
        width: 25%;
        font-size: 8.5pt;
        color: #34495e;
        line-height: 1.4;
    }
    .meta-line {
        margin-bottom: 3px;
    }
    .meta-label {
        font-weight: bold;
        color: #0b4f6c;
    }
    
    /* Headings */
    h2 {
        font-size: 12pt;
        color: #0b4f6c;
        border-left: 4px solid #01baef;
        padding-left: 10px;
        margin-top: 25px;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        page-break-after: avoid;
    }
    
    p {
        margin-top: 0;
        margin-bottom: 12px;
        text-align: justify;
    }
    
    ul {
        margin-top: 0;
        margin-bottom: 15px;
        padding-left: 20px;
    }
    
    li {
        margin-bottom: 6px;
    }
    
    /* Tables */
    .data-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        margin-bottom: 25px;
        page-break-inside: avoid;
    }
    .data-table th {
        background-color: #0b4f6c;
        color: #ffffff;
        font-weight: bold;
        text-align: left;
        padding: 10px 12px;
        font-size: 9.5pt;
        border: 1px solid #0b4f6c;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .data-table td {
        padding: 10px 12px;
        border: 1px solid #d2d6dc;
        font-size: 9.5pt;
        vertical-align: top;
        line-height: 1.5;
    }
    .data-table tr:nth-child(even) {
        background-color: #f4f9f9;
    }
    
    /* Severity Badges */
    .badge {
        display: block;
        padding: 4px 6px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 8.5pt;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-low { background-color: #e3f2fd; color: #0d47a1; border: 1px solid #90caf9; }
    .badge-medium { background-color: #fff8e1; color: #ff6f00; border: 1px solid #ffe082; }
    .badge-high { background-color: #fbe9e7; color: #d84315; border: 1px solid #ffcc80; }
    .badge-critical { background-color: #ffebee; color: #c62828; border: 1px solid #ffcdd2; }

    /* Callout Box */
    .callout-box {
        background-color: #f0fdfa;
        border-left: 4px solid #0d9488;
        padding: 15px;
        margin-top: 15px;
        margin-bottom: 20px;
        font-size: 9.5pt;
        page-break-inside: avoid;
    }
    .callout-title {
        font-weight: bold;
        color: #0f766e;
        margin-bottom: 6px;
        text-transform: uppercase;
        font-size: 9pt;
        letter-spacing: 0.5px;
    }
    
    /* Administration Control Tables */
    .control-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 30px;
        page-break-inside: avoid;
    }
    .control-table td, .control-table th {
        border: 1px solid #bdc3c7;
        padding: 10px;
        font-size: 9pt;
    }
    .control-table th {
        background-color: #f8f9fa;
        text-align: left;
        color: #34495e;
        font-weight: bold;
    }
</style>
</head>
<body>

    <!-- Header Block -->
    <table class="header-table">
        <tr>
            <td class="logo-area" rowspan="2">
                NEXUS LOGISTICS<br><span style="font-size: 8.5pt; color: #7f8c8d; font-weight: normal; letter-spacing: 2px;">FORWARDING INC.</span>
            </td>
            <td class="title-area" rowspan="2">
                <h1>Standard Operating Procedure</h1>
                <div style="font-weight: bold; margin-top: 6px; color: #4b5563; font-size: 11pt;">Logistics Disruption Management SOP</div>
            </td>
            <td class="meta-area">
                <div class="meta-line"><span class="meta-label">Doc ID:</span> SOP-LOG-073</div>
                <div class="meta-line"><span class="meta-label">Version:</span> 3.0</div>
                <div class="meta-line"><span class="meta-label">Effective Date:</span> June 21, 2026</div>
            </td>
        </tr>
        <tr>
            <td class="meta-area">
                <div class="meta-line"><span class="meta-label">Review Cycle:</span> Biennial</div>
                <div class="meta-line"><span class="meta-label">Security Tier:</span> Internal Only</div>
            </td>
        </tr>
    </table>

    <!-- Section 1 -->
    <h2>1. Purpose</h2>
    <p>The primary purpose of this Standard Operating Procedure (SOP) is to formalize operational guidelines that proactively minimize transportation delays, secure supply line continuity, and effectively manage sudden freight disruptions. By standardizing tactical interventions, this framework limits negative impacts on material arrival timelines, safeguards operational flow, and ensures corporate delivery commitments remain resilient against global transit vulnerabilities.</p>

    <!-- Section 2 -->
    <h2>2. Disruption Types</h2>
    <p>This protocol governs the handling of unexpected transit bottlenecks across all modes of transport. Sourcing and transport managers must execute response strategies based on the following specific categories of friction:</p>
    <ul>
        <li><strong>Port Congestion:</strong> Excessive terminal yard utilization, truck queuing backlogs, or infrastructure capacity overloads that restrict quick offloading and container drayage.</li>
        <li><strong>Customs Hold:</strong> Regulatory enforcement delays, compliance audits, paperwork discrepancies, or security screening holds initiated by border agencies.</li>
        <li><strong>Weather Impact:</strong> Severe meteorological anomalies including typhoons, heavy blizzards, route icing, or severe fog banks that force transit route standstills.</li>
        <li><strong>Carrier Strike:</strong> Organized industrial labor actions, union walkouts, or driver lockouts that freeze activity across specific shipping lines, rail hubs, or trucking networks.</li>
        <li><strong>Vessel Delay:</strong> Ocean or rail mechanical failures, schedule slide-outs, missed transshipment windows, or blank sailings originating directly from the primary carrier.</li>
        <li><strong>Route Blockage:</strong> Severe infrastructural bottlenecks, closed canals, physical land slips, or multi-vehicle transit blockages restricting structural freight thoroughfares.</li>
    </ul>

    <!-- Section 3 -->
    <h2>3. Severity Classification</h2>
    <p>Logistics tracking systems dynamically calculate disruption tiers based on actual or projected delays compared against baseline Estimated Time of Arrival (ETA) windows. Actions escalate according to the following thresholds:</p>

    <table class="data-table">
        <thead>
            <tr>
                <th style="width: 25%;">Severity Tier</th>
                <th style="width: 25%;">Delay Horizon</th>
                <th style="width: 50%;">Operational Management Stance</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span class="badge badge-low">Low</span></td>
                <td>Delay &lt; 24 Hours</td>
                <td>Standard automated milestone tracking. Minor shift in local delivery windows with minimal downstream disruption.</td>
            </tr>
            <tr>
                <td><span class="badge badge-medium">Medium</span></td>
                <td>Delay 1 – 3 Days</td>
                <td>Active exception logging. Notify regional distribution yards to dynamically shuffle local labor scheduling.</td>
            </tr>
            <tr>
                <td><span class="badge badge-high">High</span></td>
                <td>Delay 3 – 7 Days</td>
                <td>Mandatory material cross-check. Formally evaluate safety buffer erosion and prepare fallback delivery plans.</td>
            </tr>
            <tr>
                <td><span class="badge badge-critical">Critical</span></td>
                <td>Delay &gt; 7 Days</td>
                <td>Immediate corporate notification. Initiate emergency multi-modal freight substitutions and notify executive stakeholders.</td>
            </tr>
        </tbody>
    </table>

    <!-- Section 4 -->
    <h2>4. Targeted Response Actions</h2>
    <p>Upon validation of a transit exception, logistics handlers must execute the dedicated action tracks specified below for the root cause identified:</p>

    <table class="data-table">
        <thead>
            <tr>
                <th style="width: 30%;">Disruption Source</th>
                <th style="width: 70%;">Mandated Execution Protocol</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Port Congestion</strong></td>
                <td>
                    <ul>
                        <li>Immediately contact the regional logistics provider or freight forwarder for terminal-level intelligence.</li>
                        <li>Assess and execute re-routing mechanisms to divert downstream containers to adjacent under-utilized ports.</li>
                        <li>Enforce manual tracking check-ins to monitor carrier ETA on a strict daily update frequency.</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td><strong>Customs Hold</strong></td>
                <td>
                    <ul>
                        <li>Initiate urgent communication with the designated customs broker to pinpoint the specific hold code.</li>
                        <li>Conduct an immediate comprehensive audit of international trade invoices, commercial logs, and declarations.</li>
                        <li>Formally escalate the event to the corporate trade compliance team if clearance is not resolved within 24 hours.</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td><strong>Weather Disruption</strong></td>
                <td>
                    <ul>
                        <li>Coordinate with dispatch teams to map and deploy alternate surface or maritime bypass routes.</li>
                        <li>Immediately evaluate air freight spot-market options if line-stoppage risks exceed acceptable safety parameters.</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td><strong>Carrier Strike</strong></td>
                <td>
                    <ul>
                        <li>Declare a localized carrier contingency state and freeze further container hand-offs to the affected carrier.</li>
                        <li>Formally engage pre-qualified alternate non-unionized carriers or fallback spot-market providers to absorb volume.</li>
                    </ul>
                </td>
            </tr>
        </tbody>
    </table>

    <div class="callout-box">
        <div class="callout-title">AIR FREIGHT CONVERSION THRESHOLD</div>
        Air freight conversions generate significant financial premiums. Conversion approvals are restricted to situations where an ongoing High or Critical disruption (Weather or Strike) threatens to completely deplete factory floor safety stock.
    </div>

    <!-- Section 5 -->
    <h2>5. Key Performance Indicators (KPIs)</h2>
    <p>Operational compliance and network health are evaluated through strict performance thresholds calculated monthly across all transport channels:</p>

    <ul>
        <li><strong>Shipment Visibility (&gt; 98.0%):</strong> Total percentage of active transit milestones tracked via real-time electronic data interchange (EDI) or API telemetry without manual gaps.</li>
        <li><strong>On-Time Delivery (OTD) (&gt; 95.0%):</strong> Proportion of total inbound and outbound shipments arriving at destination docks within the contractually allowed delivery grace period.</li>
    </ul>

    <!-- Section 6 -->
    <h2>6. Document Administration & Approvals</h2>
    <p>This SOP is an actively managed corporate artifact. Major structural changes require full sign-offs via electronic document control protocols.</p>

    <table class="control-table">
        <thead>
            <tr>
                <th style="width: 20%;">Role</th>
                <th style="width: 40%;">Authorized Signatory / Title</th>
                <th style="width: 20%;">Signature</th>
                <th style="width: 20%;">Date Signed</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Prepared By</th>
                <td>David Vance<br><span style="font-size:8pt; color:#7f8c8d;">Global Logistics Network Architect</span></td>
                <td>[ELECTRONIC]</td>
                <td>June 12, 2026</td>
            </tr>
            <tr>
                <th>Reviewed By</th>
                <td>Helena Rove<br><span style="font-size:8pt; color:#7f8c8d;">Director of Supply Chain Risk</span></td>
                <td>[ELECTRONIC]</td>
                <td>June 15, 2026</td>
            </tr>
            <tr>
                <th>Approved By</th>
                <td>Arthur Pendelton<br><span style="font-size:8pt; color:#7f8c8d;">VP of Global Transportation & Logistics</span></td>
                <td>[ELECTRONIC]</td>
                <td>June 21, 2026</td>
            </tr>
        </tbody>
    </table>

    <table class="control-table" style="margin-top: 15px;">
        <thead>
            <tr>
                <th style="width: 15%;">Revision</th>
                <th style="width: 20%;">Date</th>
                <th style="width: 65%;">Nature of Change</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1.0</td>
                <td>August 04, 2021</td>
                <td>Initial release of basic regional logistics disruption guidelines.</td>
            </tr>
            <tr>
                <td>2.0</td>
                <td>October 14, 2024</td>
                <td>Expanded definitions to include targeted customs compliance tracking paths.</td>
            </tr>
            <tr>
                <td>3.0</td>
                <td>June 21, 2026</td>
                <td>Integrated modern API/EDI visibility metrics and standardized severity horizons.</td>
            </tr>
        </tbody>
    </table>

</body>
</html>
"""

output_path = "logistics_disruption_management_sop.pdf"
HTML(string=html_content).write_pdf(output_path)
print(f"File created successfully: {output_path}")