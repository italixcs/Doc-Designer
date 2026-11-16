"""Build original, deliberately basic redesign inputs using free python-docx.

Run with a Python environment containing python-docx. PDF export is separate.
No upstream templates, images, fonts or content are bundled.
"""
from pathlib import Path
import csv,json,re,sqlite3
from docx import Document
from docx.shared import Mm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parent

def document(title):
 d=Document();s=d.sections[0]
 s.page_width,s.page_height=Mm(210),Mm(297)
 s.top_margin=s.bottom_margin=Mm(20);s.left_margin=s.right_margin=Mm(20)
 for style in d.styles:
  if style.type in (1,2):
   style.font.name='Liberation Sans';style.font.color.rgb=RGBColor(0,0,0)
 for border in list(d.styles.element.xpath('.//w:pBdr')):border.getparent().remove(border)
 d.styles['Normal'].font.size=Pt(10.5)
 d.styles['Normal'].paragraph_format.space_after=Pt(7)
 d.styles['Normal'].paragraph_format.line_spacing=1.10
 d.styles['Title'].font.size=Pt(19)
 d.styles['Heading 1'].font.size=Pt(13)
 d.styles['Heading 1'].paragraph_format.space_before=Pt(10)
 d.core_properties.author='Doc designer public exercises'
 d.core_properties.last_modified_by='Doc designer public exercises'
 d.core_properties.title=title;d.core_properties.subject='Purpose-written fictional redesign input'
 d.core_properties.comments=''
 return d

def table(d,headers,rows):
 t=d.add_table(rows=1,cols=len(headers));t.style='Table Grid'
 for c,v in zip(t.rows[0].cells,headers):c.text=str(v)
 h=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(h)
 for row in rows:
  for c,v in zip(t.add_row().cells,row):c.text=str(v)
 for row in t.rows:
  for c in row.cells:
   for p in c.paragraphs:
    p.paragraph_format.space_after=Pt(3)
    p.paragraph_format.space_before=Pt(3)
 return t

def short():
 d=document('Print a postcard');lines=(ROOT/'short/content.md').read_text().splitlines();i=0
 while i<len(lines):
  line=lines[i]
  if line.startswith('# '):d.add_paragraph(line[2:],style='Title')
  elif line.startswith('## '):d.add_heading(line[3:],1)
  elif line.startswith('|'):
   headers=[x.strip() for x in line.strip('|').split('|')];i+=2;rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    rows.append([x.strip() for x in lines[i].strip('|').split('|')]);i+=1
   table(d,headers,rows);continue
  elif line.strip():d.add_paragraph(line)
  i+=1
 d.save(ROOT/'short/before.docx')

def long():
 data=json.loads((ROOT/'long/content.json').read_text());d=document(data['title'])
 for i,section in enumerate(data['sections']):
  if i:d.add_page_break()
  if i==0:
   d.add_paragraph(data['title'],style='Title');d.add_paragraph(data['subtitle'])
  d.add_heading(section['heading'],1)
  for p in section['paragraphs']:d.add_paragraph(p)
  if 'table' in section:table(d,section['table']['headers'],section['table']['rows'])
  if 'code' in section:d.add_paragraph(section['code'])
 d.save(ROOT/'long/before.docx')
 # Creation input has the same content without a laid-out source file.
 lines=['# '+data['title'],'',data['subtitle'],'']
 for s in data['sections']:
  lines+=['## '+s['heading'],'']
  for p in s['paragraphs']:lines += [p,'']
  if 'table' in s:
   t=s['table'];lines+=['| '+' | '.join(t['headers'])+' |','| '+' | '.join(['---']*len(t['headers']))+' |']
   lines+=['| '+' | '.join(map(str,row))+' |' for row in t['rows']];lines+=['']
  if 'code' in s:lines+=['```sql',s['code'],'```','']
 (ROOT/'long/content.md').write_text('\n'.join(lines))
 chart=data['sections'][2]['table']
 with (ROOT/'long/activity.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(chart['headers']);w.writerows(chart['rows'])
 code=data['sections'][3]['code'];(ROOT/'long/query.sql').write_text(code+'\n')
 db=sqlite3.connect(':memory:');db.executescript((ROOT/'long/schema.sql').read_text());rows=db.execute(code).fetchall()
 assert rows==[('Postcards A','OBJ001','Harbor postcard','Confirm short title')]
 counts=list(zip(*chart['rows']));assert [sum(c) for c in counts[1:]]==[191,165,143]
 assert 120+80+40==240 and 240-191==49 and 240-143==97
 print('SQL fixture query and activity totals checked.')

if __name__=='__main__':short();long()
