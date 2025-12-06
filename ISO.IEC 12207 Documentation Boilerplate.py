import os

folders = {
    "docs/01_requirements/business_requirements":
        "Business Requirements — high-level business needs and objectives.",
    "docs/01_requirements/stakeholder_requirements":
        "Stakeholder Requirements — expectations and constraints from stakeholders.",
    "docs/01_requirements/system_requirements":
        "System Requirements Specification (SyRS).",
    "docs/01_requirements/software_requirements":
        "Software Requirements Specification (SRS).",
    "docs/01_requirements/use_cases":
        "Use Cases and User Stories.",

    "docs/02_architecture/system_architecture":
        "System architecture description (SAD).",
    "docs/02_architecture/software_architecture":
        "Software architecture, modules, components.",
    "docs/02_architecture/data_architecture":
        "Data models, ER diagrams, schemas.",

    "docs/03_design/high_level_design":
        "High-Level Design (HLD).",
    "docs/03_design/detailed_design":
        "Detailed Design Description (DDD).",
    "docs/03_design/interface_specifications":
        "API/interface specifications.",

    "docs/04_implementation/coding_standards":
        "Coding guidelines and conventions.",
    "docs/04_implementation/build_instructions":
        "Build and installation instructions.",
    "docs/04_implementation/configuration_guides":
        "Runtime configuration documentation.",

    "docs/05_verification/test_plans":
        "Software Test Plan (STP).",
    "docs/05_verification/test_designs":
        "Test design specifications.",
    "docs/05_verification/test_cases":
        "Detailed test cases (STD).",
    "docs/05_verification/test_reports":
        "Test execution reports (STR).",

    "docs/06_validation/acceptance_documents":
        "User/Customer Acceptance Testing documents.",

    "docs/07_operation/user_manuals":
        "User-facing manuals and guides.",
    "docs/07_operation/operator_manuals":
        "Operational procedures for operators.",
    "docs/07_operation/installation_guides":
        "Installation and deployment guides.",

    "docs/08_maintenance/maintenance_plans":
        "Software maintenance plans.",
    "docs/08_maintenance/issue_reports":
        "Bug and issue reports.",
    "docs/08_maintenance/patch_notes":
        "Release patch and update notes.",

    "docs/09_project_management/project_plans":
        "Project Management Plan (PMP).",
    "docs/09_project_management/schedules":
        "Schedules, milestones, timelines.",
    "docs/09_project_management/communication_plans":
        "Stakeholder communication strategies.",
    "docs/09_project_management/progress_reports":
        "Weekly/monthly project status reports.",

    "docs/10_quality_assurance/qa_plans":
        "Quality Assurance Plan (QAP).",
    "docs/10_quality_assurance/audit_reports":
        "Quality audits and reviews.",
    "docs/10_quality_assurance/quality_records":
        "Quality measurement records.",

    "docs/11_configuration_management/cm_plan":
        "Configuration Management Plan.",
    "docs/11_configuration_management/versioning":
        "Version control and branching model.",
    "docs/11_configuration_management/change_control":
        "Change request and approval workflows.",

    "docs/12_risk_management/risk_registers":
        "Risk register with severity/impact.",
    "docs/12_risk_management/mitigation_plans":
        "Plans to mitigate identified risks.",

    "docs/13_release/release_notes":
        "Release notes for each software version.",
    "docs/13_release/change_logs":
        "Change logs (Changelog.md).",
    "docs/13_release/deployment_records":
        "Deployment validation records.",

    "docs/14_support/support_procedures":
        "Support workflows and procedures.",
    "docs/14_support/service_level_agreements":
        "SLAs (Service Level Agreements).",
    "docs/14_support/ticket_records":
        "Support ticket logs.",

    "docs/15_acquisition/procurement_documents":
        "Procurement and acquisition documentation.",
    "docs/15_acquisition/supplier_management":
        "Supplier evaluation and management.",
    "docs/15_acquisition/acceptance_records":
        "Formal acceptance records.",

    "docs/16_glossaries/terminology":
        "Glossaries, abbreviations, and domain terms."
}

for folder, desc in folders.items():
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {folder}\n\n{desc}\n")

print("Full ISO/IEC 12207 Documentation Boilerplate created successfully!")
