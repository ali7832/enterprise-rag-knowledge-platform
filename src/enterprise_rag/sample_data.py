from enterprise_rag.schemas import Document


def sample_documents() -> list[Document]:
    return [
        Document(
            doc_id='security-policy',
            title='Security Policy',
            text='All enterprise systems require multi-factor authentication, least privilege access, audit logging, and quarterly access reviews.',
        ),
        Document(
            doc_id='support-playbook',
            title='Support Playbook',
            text='Customer support tickets should be categorized by urgency, routed to the correct team, and escalated when SLA risk is detected.',
        ),
        Document(
            doc_id='ml-platform',
            title='ML Platform Guide',
            text='Machine learning services should include model evaluation, versioned artifacts, monitoring, rollback plans, and clear ownership.',
        ),
    ]
