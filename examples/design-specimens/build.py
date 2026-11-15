"""Original document specimens. Run with Python, python-docx, Matplotlib and Pillow.

All factual datasets here are purpose-written fixtures. No upstream page, font,
template, logo, or image is copied into these documents.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_BREAK
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
INK, MUTED, GREEN, SAND, AMBER = "152B27", "596862", "30594C", "F3EBDD", "AD6D32"


def shade(el, fill):
    pr = el.get_or_add_pPr() if hasattr(el, "get_or_add_pPr") else el.get_or_add_tcPr()
    x = OxmlElement("w:shd"); x.set(qn("w:fill"), fill); pr.append(x)


def font(run, size=None, bold=False, color=INK, face="Liberation Sans"):
    run.font.name = face
    if size: run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)
    rpr = run._element.get_or_add_rPr()
    for x in list(rpr):
        if x.tag == qn("w:color"): x.attrib.pop(qn("w:themeColor"), None)
    return run


def para(doc, text="", size=11, bold=False, color=INK, before=0, after=6,
         face="Liberation Sans", style=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.16
    p.paragraph_format.widow_control = True
    font(p.add_run(text), size, bold, color, face)
    return p


def make(title, subject, accent=GREEN):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Mm(210), Mm(297)
    s.top_margin, s.bottom_margin = Mm(17), Mm(17)
    s.left_margin, s.right_margin = Mm(18), Mm(18)
    for sty in d.styles:
        if sty.type in (1, 2):
            sty.font.name = "Liberation Sans"
            sty.font.color.rgb = RGBColor.from_string("000000")
    for el in list(d.styles.element.xpath(".//w:pBdr")):
        el.getparent().remove(el)
    normal = d.styles["Normal"]
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    for n in ("Heading 1", "Heading 2"):
        d.styles[n].paragraph_format.keep_with_next = True
    d.core_properties.author = "Doc designer specimens"
    d.core_properties.last_modified_by = "Doc designer specimens"
    d.core_properties.title = title
    d.core_properties.subject = subject
    d.core_properties.comments = ""
    return d


def label(d, text, color=MUTED):
    p = para(d, text, size=8.5, bold=True, color=color, after=8)
    sp = OxmlElement("w:spacing"); sp.set(qn("w:val"), "18")
    p.runs[0]._element.get_or_add_rPr().append(sp)
    return p


def title(d, text, size=37):
    p = para(d, text, size=size, color="000000", face="Liberation Serif",
             after=7, style="Title")
    p.paragraph_format.keep_with_next = True
    return p


def heading(d, text, color=GREEN, before=8):
    return para(d, text, size=13, bold=True, color=color, before=before,
                after=5, style="Heading 1")


def table(d, headers, rows, widths, accent=GREEN, emphasis=None):
    t = d.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for col,w in zip(t.columns,widths): col.width = Mm(w)
    for c,w,h in zip(t.rows[0].cells,widths,headers):
        c.width=Mm(w); c.text=""
        shade(c._tc,accent)
        p=c.paragraphs[0];p.paragraph_format.space_after=Pt(0)
        font(p.add_run(h),9.5,True,"FFFFFF")
    hdr=OxmlElement("w:tblHeader"); t.rows[0]._tr.get_or_add_trPr().append(hdr)
    for ri,row in enumerate(rows):
        cells=t.add_row().cells
        for ci,(c,w,value) in enumerate(zip(cells,widths,row)):
            c.width=Mm(w);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            c.text=""
            p=c.paragraphs[0]
            p.paragraph_format.space_after=Pt(1)
            p.paragraph_format.space_before=Pt(1)
            if ci==emphasis:
                font(p.add_run(str(value)),14,True,accent)
            else:font(p.add_run(str(value)),10.5,ci==0,INK)
            if ci==emphasis: p.alignment=WD_ALIGN_PARAGRAPH.CENTER
            pr=c._tc.get_or_add_tcPr()
            borders=OxmlElement("w:tcBorders")
            b=OxmlElement("w:bottom");b.set(qn("w:val"),"single")
            b.set(qn("w:sz"),"4");b.set(qn("w:color"),"CAD6CF")
            borders.append(b);pr.append(borders)
        nosplit=OxmlElement("w:cantSplit");t.rows[-1]._tr.get_or_add_trPr().append(nosplit)
    for row in t.rows:
        for c in row.cells:
            pr=c._tc.get_or_add_tcPr();mar=OxmlElement("w:tcMar")
            for edge,value in [("top",95),("bottom",95),("left",100),("right",100)]:
                e=OxmlElement("w:"+edge);e.set(qn("w:w"),str(value));e.set(qn("w:type"),"dxa");mar.append(e)
            pr.append(mar)
    return t


def step(d, n, name, body):
    p=para(d,before=6,after=3)
    p.paragraph_format.left_indent=Mm(12)
    p.paragraph_format.first_line_indent=Mm(-12)
    p.paragraph_format.tab_stops.add_tab_stop(Mm(12))
    font(p.add_run(n+"\t"),11,True,AMBER)
    font(p.add_run(name),12,True,GREEN)
    p.paragraph_format.keep_with_next=True
    q=para(d,body,size=10.5,after=4)
    q.paragraph_format.left_indent=Mm(12)


def footer(d, text):
    p=d.sections[0].footer.paragraphs[0]
    p.paragraph_format.space_before=Pt(0)
    font(p.add_run(text),8,color=MUTED)


def columns(d, widths, gap=10):
    section=d.add_section(WD_SECTION_START.CONTINUOUS)
    cols=section._sectPr.find(qn("w:cols"))
    for child in list(cols):cols.remove(child)
    cols.set(qn("w:num"),str(len(widths)))
    cols.set(qn("w:equalWidth"),"0")
    cols.set(qn("w:space"),str(Mm(gap).twips))
    for i,w in enumerate(widths):
        el=OxmlElement("w:col");el.set(qn("w:w"),str(Mm(w).twips))
        el.set(qn("w:space"),str(Mm(gap if i<len(widths)-1 else 0).twips));cols.append(el)


def column_break(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.COLUMN)


def writing_line(d):
    p=para(d,"",after=10)
    p.paragraph_format.line_spacing=1
    p.paragraph_format.space_before=Pt(5)
    b=OxmlElement("w:pBdr");edge=OxmlElement("w:bottom")
    edge.set(qn("w:val"),"single");edge.set(qn("w:sz"),"3")
    edge.set(qn("w:color"),"CAD6CF");b.append(edge);p._p.get_or_add_pPr().append(b)


def picture(d, path, width, description):
    p=d.add_paragraph(); p.paragraph_format.space_after=Pt(0)
    pic=p.add_run().add_picture(str(path),width=Mm(width))
    pic._inline.docPr.set("descr",description)
    return p


def draw_tool_ribbon():
    fig,ax=plt.subplots(figsize=(7,0.58),dpi=240)
    fig.patch.set_facecolor("#F0F4F0");ax.set_facecolor("#F0F4F0")
    ax.set_xlim(0,10);ax.set_ylim(0,1);ax.axis("off")
    # Original simple line art: drill, saw, and a small toolkit.
    ax.plot([.25,.25,1.1,1.1,.85,.85,.6,.6,.25],[.65,.85,.85,.6,.6,.16,.16,.6,.65],color="#30594C",lw=2)
    ax.plot([1.1,1.5],[.74,.74],color="#30594C",lw=2)
    ax.plot([3.7,4.6,4.35,3.7,3.7],[.73,.73,.3,.3,.73],color="#30594C",lw=2)
    ax.plot([4.6,5.05,5.05,4.6],[.73,.73,.3,.3],color="#30594C",lw=2)
    ax.add_patch(plt.Rectangle((7.4,.23),1.05,.51,fill=False,lw=2,ec="#30594C"))
    ax.plot([7.7,7.7,8.15,8.15],[.74,.9,.9,.74],color="#30594C",lw=2)
    ax.text(1.7,.48,"DRILLS",va="center",fontsize=9,color="#30594C",fontweight="bold")
    ax.text(5.2,.48,"SAWS",va="center",fontsize=9,color="#30594C",fontweight="bold")
    ax.text(8.6,.48,"KITS",va="center",fontsize=9,color="#30594C",fontweight="bold")
    fig.subplots_adjust(0,0,1,1)
    for ext in ["png","svg"]:fig.savefig(ASSETS/f"tool-ribbon.{ext}",facecolor=fig.get_facecolor(),dpi=240)
    plt.close(fig)


def guide():
    d=make("Borrow a tool","Fictional community guide specimen")
    label(d,"NORTHBANK  /  COMMUNITY TOOL LIBRARY")
    title(d,"Borrow a tool")
    para(d,"A quick guide to the fictional Northbank Tool Library",size=11.5,color=MUTED,after=10)
    p=picture(d,ASSETS/"tool-ribbon.png",174,"Decorative line drawings of a drill, hand saw and toolkit.")
    p.paragraph_format.space_after=Pt(8)
    p=para(d,after=10)
    p.paragraph_format.tab_stops.add_tab_stop(Mm(89))
    font(p.add_run("WEDNESDAY  "),8.5,True,GREEN);font(p.add_run("16:00–19:00\t"),11)
    font(p.add_run("SATURDAY  "),8.5,True,GREEN);font(p.add_run("10:00–13:00"),11)
    columns(d,[80,84],gap=10)
    step(d,"01","Join at the desk","Membership is free. Ask at the desk to join. Members may borrow one item at a time.")
    step(d,"02","Choose your tool","Choose an available tool. The desk records the item and its return date.")
    step(d,"03","Check the date","Check the return date before leaving.")
    step(d,"04","Bring it back","Bring the item back during opening hours. Return it clean and with all included parts.")
    p=para(d,"RUNNING LATE",size=8.5,bold=True,color=AMBER,before=10,after=2);shade(p._p,SAND)
    p=para(d,"If you expect to be late, contact the desk before the return date.",size=10.5,after=0);shade(p._p,SAND)
    column_break(d)
    heading(d,"Loan periods",before=0)
    table(d,["Tool","Loan period","Included"],[
        ["Cordless drill","7 days","Drill, battery, charger"],
        ["Hand saw","14 days","Saw and blade cover"],
        ["Repair kit","7 days","Kit and contents checklist"]],[28,23,33],emphasis=1)
    footer(d,"NORTHBANK TOOL LIBRARY     •     Visitor guide")
    d.save(ROOT/"community-guide.docx")


def draw_study_chart():
    fig,ax=plt.subplots(figsize=(6.8,2.5),dpi=240)
    vals=[12,18,9];names=["Morning","Afternoon","Evening"]
    bars=ax.barh(names,vals,color=["#C9D6D1","#30594C","#D8BA90"],height=.55)
    ax.invert_yaxis();ax.set_xlim(0,22)
    for y,v in enumerate(vals):ax.text(v+.4,y,str(v),va="center",fontsize=13,color="#152B27",fontweight="bold")
    ax.set_xticks([0,6,12,18]);ax.set_xlabel("Requests processed",fontsize=10,labelpad=10)
    ax.tick_params(axis="y",length=0,labelsize=11);ax.tick_params(axis="x",length=0,labelsize=9,colors="#596862")
    for sp in ax.spines.values():sp.set_visible(False)
    ax.grid(axis="x",color="#E1E6E2",lw=.7);ax.set_axisbelow(True)
    fig.subplots_adjust(left=.19,right=.98,top=.92,bottom=.25)
    for ext in ["png","svg"]:fig.savefig(ASSETS/f"study-chart.{ext}",dpi=240,facecolor="white")
    plt.close(fig)


def study():
    d=make("Read a chart","Original chart-reading study specimen")
    label(d,"DATA SKILLS  /  QUICK PRACTICE",AMBER)
    title(d,"Read a chart",size=39)
    para(d,"Start with the labels. Compare values. Explain the difference.",size=12,color=MUTED,after=12)
    heading(d,"What the chart tells you",color=INK,before=0)
    para(d,"A fictional service desk counted the requests processed during three shifts. The unit is requests, not hours or percentages.",size=11,after=2)
    picture(d,ASSETS/"study-chart.png",174,"Requests processed: Morning 12, Afternoon 18, Evening 9. Horizontal bars start at zero.")
    para(d,"Practice dataset  •  Morning 12  /  Afternoon 18  /  Evening 9",size=8.5,color=MUTED,after=12)
    columns(d,[100,64],gap=10)
    heading(d,"Work through one comparison",color=INK,before=0)
    para(d,"How much higher is the afternoon count than the morning count?",size=11,bold=True,after=7)
    p=para(d,"18 − 12 = 6 more requests",size=17,bold=True,color=GREEN,after=4)
    para(d,"The afternoon shift processed six more requests. This is the absolute difference.",size=10.5,after=8)
    p=para(d,"6 ÷ 12 × 100 = 50% higher",size=17,bold=True,color=AMBER,after=4)
    para(d,"For the percentage change, use the morning value as the starting point.",size=10.5,after=10)
    p=para(d,"COMMON ERROR",size=8.5,bold=True,color=AMBER,after=1);shade(p._p,SAND)
    p=para(d,"A difference of 6 requests is not an increase of 6%. Keep the unit and the comparison base visible.",size=10.5,after=0);shade(p._p,SAND)
    column_break(d)
    heading(d,"Try it yourself",color=INK,before=0)
    para(d,"1   How many requests were processed across all three shifts?",size=11,after=7)
    writing_line(d);writing_line(d)
    para(d,"2   How many more requests did the afternoon shift process than the evening shift?",size=11,before=5,after=7)
    writing_line(d);writing_line(d)
    footer(d,"CHART READING     •     Answers  1  39 requests     2  9 requests")
    d.save(ROOT/"study-sheet.docx")


def draw_budget_chart():
    fig,ax=plt.subplots(figsize=(6.8,2.0),dpi=240)
    cats=["Paper","Ink","Binding"];q1=[120,80,50];q2=[180,90,60]
    for y,(a,b) in enumerate(zip(q1,q2)):
        ax.plot([a,b],[y,y],color="#BFCAC5",lw=4,zorder=1)
        ax.scatter([a],[y],s=70,c="#D1D9D4",zorder=2)
        ax.scatter([b],[y],s=85,c="#30594C",zorder=3)
        ax.text(a-7,y-.16,f"€{a}",ha="right",va="center",fontsize=9,color="#596862")
        ax.text(b+7,y+.03,f"€{b}",ha="left",va="center",fontsize=11,fontweight="bold",color="#152B27")
    ax.set_yticks(range(3),cats);ax.invert_yaxis();ax.set_xlim(0,220)
    ax.set_xticks([0,50,100,150,200]);ax.tick_params(length=0,labelsize=9)
    for sp in ax.spines.values():sp.set_visible(False)
    ax.grid(axis="x",color="#E3E7E4",lw=.7);ax.set_axisbelow(True)
    ax.set_xlabel("Quarter 1  ● light     Quarter 2  ● dark   |   EUR",fontsize=8.5,color="#596862")
    fig.subplots_adjust(left=.15,right=.98,top=.95,bottom=.26)
    for ext in ["png","svg"]:fig.savefig(ASSETS/f"budget-chart.{ext}",dpi=240,facecolor="white")
    plt.close(fig)


def analysis():
    d=make("Paper drives the increase","Fictional studio budget analysis specimen")
    label(d,"SHARED STUDIO  /  SUPPLIES REVIEW")
    title(d,"Paper drives the increase",size=33)
    para(d,"Quarter 2 spending rose from €250 to €330. Paper accounts for €60 of the €80 increase.",size=12,color=MUTED,after=9)
    p=para(d,after=4)
    font(p.add_run("75%"),42,False,AMBER,"Liberation Serif")
    font(p.add_run("   of the rise comes from paper"),13,True,INK)
    para(d,"This identifies the largest contributor to the increase. It does not explain whether the cause was price, quantity, or waste.",size=10.5,after=8)
    picture(d,ASSETS/"budget-chart.png",174,"Quarter 1 to Quarter 2 spending in EUR: Paper 120 to 180; Ink 80 to 90; Binding 50 to 60. Values also appear in the editable table.")
    para(d,"Paired values show the size of each category's change.",size=8.5,color=MUTED,after=10)
    heading(d,"The figures behind the finding",before=0)
    table(d,["Supply","Quarter 1","Quarter 2","Change"],[
        ["Paper","€120","€180","+€60"],["Ink","€80","€90","+€10"],
        ["Binding","€50","€60","+€10"],["Total","€250","€330","+€80"]],[57,39,39,39])
    heading(d,"Suggested next step",before=12)
    para(d,"Review paper purchasing first. Compare invoice prices and quantities before deciding whether any reduction is appropriate.",size=11,after=8)
    p=para(d,"KEEP THE LIMIT IN VIEW",size=8.5,bold=True,color=AMBER,after=1);shade(p._p,SAND)
    p=para(d,"Total spending rose by 32%. The ledger alone cannot tell us whether the studio received less value for money.",size=10.5,after=0);shade(p._p,SAND)
    footer(d,"ILLUSTRATIVE STUDIO LEDGER     •     Amounts in EUR")
    d.save(ROOT/"analytical-brief.docx")


if __name__=="__main__":
    plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none"})
    draw_tool_ribbon();draw_study_chart();draw_budget_chart()
    guide();study();analysis()
    data={"study":{"Morning":12,"Afternoon":18,"Evening":9},
          "budget":{"Paper":[120,180],"Ink":[80,90],"Binding":[50,60]}}
    (ROOT/"fixtures.json").write_text(json.dumps(data,indent=2)+"\n")
    print("Built three original DOCX specimens and editable SVG sources.")
