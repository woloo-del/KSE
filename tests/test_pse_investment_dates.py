import unittest
from connectors.pse.investment_dates import TITLE,portal_completion_year,annual_report_completion_year
from scripts.build_radkowice_investment_review import build


class InvestmentDateTests(unittest.TestCase):
    def test_neighbor_year_never_used(self):
        html=f'<h4>{TITLE} (zakończona)</h4><p>No year</p><h4>OTHER</h4><p>Inwestycja zakończona w 2020 r.</p>'
        with self.assertRaisesRegex(ValueError,'YEAR'):portal_completion_year(html)

    def test_duplicate_title_requires_review(self):
        block=f'<h4>{TITLE} (zakończona)</h4><p>Inwestycja zakończona w 2025 r.</p>'
        with self.assertRaisesRegex(ValueError,'AMBIGUOUS'):portal_completion_year(block+block)

    def test_missing_context_rejected(self):
        with self.assertRaises(ValueError):annual_report_completion_year('2023',TITLE)

    def test_footnote_not_silently_applied(self):
        context='Realizacja zadań inwestycyjnych wynikających z PRSP Nakłady PSE na realizację zadań inwestycyjnych w 2023 r. Najważniejszymi zadaniami zakończonymi w tym roku były:'
        with self.assertRaisesRegex(ValueError,'FOOTNOTE'):annual_report_completion_year(context,TITLE+'*')

    def test_real_snapshots_keep_both_years_and_no_capacity(self):
        result=build()
        self.assertEqual([c['completion_year_reported'] for c in result['claims']],[2023,2025])
        self.assertEqual(result['status'],'UNRESOLVED_DATE_OR_SCOPE')
        self.assertIsNone(result['selected_completion_year'])
        self.assertIsNone(result['additional_available_capacity_MW'])
        self.assertEqual(result['same_project_identity'],'UNCONFIRMED')
