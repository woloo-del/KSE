"""Bounded documentary extraction for the Radkowice transformer investment."""
from html.parser import HTMLParser
import re

TITLE = 'Wymiana transformatora wraz z dostosowaniem infrastruktury w stacji 220/110 kV Radkowice'


def normalized(text: str) -> str:
    return ' '.join(text.split())


class Sections(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks=[]
        self.heading=None
        self.body=[]
        self.in_heading=False

    def handle_starttag(self, tag, attrs):
        if tag=='h4':
            if self.heading is not None: self.blocks.append((normalized(self.heading),normalized(' '.join(self.body))))
            self.heading='';self.body=[];self.in_heading=True

    def handle_endtag(self, tag):
        if tag=='h4': self.in_heading=False

    def handle_data(self, data):
        if self.in_heading: self.heading+=data
        elif self.heading is not None: self.body.append(data)

    def finish(self):
        if self.heading is not None:self.blocks.append((normalized(self.heading),normalized(' '.join(self.body))))


def portal_completion_year(html: str) -> int:
    parser=Sections();parser.feed(html);parser.close();parser.finish()
    blocks=[body for title,body in parser.blocks if title==TITLE+' (zakończona)']
    if len(blocks)!=1: raise ValueError('MISSING_OR_AMBIGUOUS_INVESTMENT_SECTION')
    years=re.findall(r'Inwestycja zakończona w (\d{4}) r\.',blocks[0])
    if len(years)!=1: raise ValueError('MISSING_OR_AMBIGUOUS_COMPLETION_YEAR')
    return int(years[0])


def annual_report_completion_year(previous_page: str, listing_page: str) -> int:
    context=normalized(previous_page).split('Realizacja zadań inwestycyjnych wynikających z PRSP')
    if len(context)!=2: raise ValueError('ANNUAL_REPORT_CONTEXT_CHANGED')
    match=re.search(r'Nakłady PSE na realizację zadań inwestycyjnych w (\d{4}) r\..*?Najważniejszymi zadaniami zakończonymi w tym roku były:',context[1])
    listing=normalized(listing_page)
    if not match or listing.count(TITLE)!=1: raise ValueError('ANNUAL_REPORT_LIST_CHANGED')
    if TITLE+'*' in listing or TITLE+' *' in listing: raise ValueError('FOOTNOTE_REQUIRES_REVIEW')
    return int(match.group(1))
