from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white, gray
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Flowable
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.graphics.shapes import Drawing, Polygon
from reportlab.graphics import renderPDF
import math

output_path = "/home/elvis/Projects/StudyTime/Charles/UML_Diagram_Library_Management.pdf"

doc = SimpleDocTemplate(
    output_path, pagesize=A4,
    topMargin=2*cm, bottomMargin=2*cm,
    leftMargin=2.5*cm, rightMargin=2.5*cm,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('CustomTitle', parent=styles['Title'],
    fontSize=22, leading=28, spaceAfter=12, alignment=TA_CENTER, textColor=HexColor('#1a1a2e'))
heading1_style = ParagraphStyle('CustomH1', parent=styles['Heading1'],
    fontSize=16, leading=20, spaceBefore=20, spaceAfter=10, textColor=HexColor('#16213e'))
heading2_style = ParagraphStyle('CustomH2', parent=styles['Heading2'],
    fontSize=13, leading=17, spaceBefore=14, spaceAfter=6, textColor=HexColor('#0f3460'))
body_style = ParagraphStyle('CustomBody', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=6, alignment=TA_JUSTIFY)
bullet_style = ParagraphStyle('Bullet', parent=body_style,
    leftIndent=20, bulletIndent=10, spaceAfter=3)

story = []

# ── Title ──
story.append(Spacer(1, 3*cm))
story.append(Paragraph("UML Class Diagram", title_style))
story.append(Paragraph("Library Management System", ParagraphStyle(
    'Subtitle', parent=title_style, fontSize=16, leading=20, textColor=HexColor('#0f3460'))))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("Based on Java Implementation Reference", ParagraphStyle(
    'SubSub', parent=body_style, fontSize=11, alignment=TA_CENTER, textColor=gray)))
story.append(Spacer(1, 2*cm))

# ═══════════════════════════════════════════════════════════════
# UML Diagram Flowable
# ═══════════════════════════════════════════════════════════════

def draw_class_box(c, x, y, w, h, class_name, attrs, methods):
    c.setStrokeColor(black)
    c.setFillColor(HexColor('#e8eaf6'))
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    c.setFillColor(HexColor('#1a1a2e'))
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(x + w/2, y + h - 16, f"<<{class_name}>>")
    c.setFont('Helvetica', 10)
    c.setFillColor(HexColor('#1a237e'))
    c.drawCentredString(x + w/2, y + h - 30, class_name)
    c.setStrokeColor(black)
    c.line(x, y + h - 36, x + w, y + h - 36)
    c.setFont('Courier', 7.5)
    c.setFillColor(black)
    ay = y + h - 50
    for a in attrs:
        c.drawString(x + 6, ay, a); ay -= 11
    sep = ay + 4
    c.line(x, sep, x + w, sep)
    c.setFont('Courier', 7.5)
    my = sep - 14
    for m in methods:
        c.drawString(x + 6, my, m); my -= 11

def draw_arrow(c, x1, y1, x2, y2):
    c.setStrokeColor(black)
    c.setLineWidth(1)
    c.line(x1, y1, x2, y2)
    angle = math.atan2(y2 - y1, x2 - x1)
    sz = 8
    la = angle + math.radians(150)
    ra = angle - math.radians(150)
    tri = Polygon([x2, y2, x2 + sz*math.cos(la), y2 + sz*math.sin(la),
                   x2 + sz*math.cos(ra), y2 + sz*math.sin(ra)],
                  fillColor=black, strokeColor=black, strokeWidth=1)
    d = Drawing(20, 20); d.add(tri)
    renderPDF.draw(d, c, x2 - 10, y2 - 10)

def draw_diamond(c, x, y, angle):
    d_sz = 7
    ha = angle + math.radians(90)
    pts = [
        x, y,
        x + d_sz*math.cos(angle + math.radians(30)), y + d_sz*math.sin(angle + math.radians(30)),
        x + 2*d_sz*math.cos(angle), y + 2*d_sz*math.sin(angle),
        x + d_sz*math.cos(angle - math.radians(30)), y + d_sz*math.sin(angle - math.radians(30)),
    ]
    dia = Polygon(pts, fillColor=white, strokeColor=black, strokeWidth=1)
    d = Drawing(20, 20); d.add(dia)
    cx = x + 2*d_sz*math.cos(angle)
    cy = y + 2*d_sz*math.sin(angle)
    renderPDF.draw(d, c, cx - 10, cy - 10)

def draw_label(c, x, y, text):
    c.setFont('Helvetica-Oblique', 8)
    c.setFillColor(HexColor('#333333'))
    c.drawCentredString(x, y, text)

class UMLDiagram(Flowable):
    def __init__(self):
        Flowable.__init__(self)
        self.width = 480
        self.height = 400

    def draw(self):
        c = self.canv
        x_off, y_off = 10, 10
        bw, bh = 130, 90
        gx, gy = 160, 130

        # positions
        lib = (x_off + gx, y_off)
        bk = (x_off + gx, y_off + gy*2)
        mb = (x_off + gx*2 + bw, y_off + gy*2)
        ln = (x_off + gx*1.5 + bw//2, y_off + gy)

        # frame
        c.setStrokeColor(HexColor('#bbdefb'))
        c.setLineWidth(0.5)
        c.rect(x_off - 10, y_off - 20, self.width, self.height, fill=0, stroke=1)

        # draw class boxes
        draw_class_box(c, lib[0], lib[1], bw, bh, "Library",
            ["- books: List<Book>", "- members: List<Member>", "- loans: List<Loan>"],
            ["+ addBook()", "+ registerMember()", "+ lendBook()", "+ returnBook()", "+ searchBookByTitle()"])

        draw_class_box(c, bk[0], bk[1], bw, bh, "Book",
            ["- isbn: String", "- title: String", "- author: String", "- available: boolean"],
            ["+ getters/setters", "+ toString()"])

        draw_class_box(c, mb[0], mb[1], bw, bh, "Member",
            ["- memberId: String", "- name: String", "- loans: List<Loan>"],
            ["+ getters/setters", "+ toString()", "+ addLoan()"])

        draw_class_box(c, ln[0], ln[1], bw, bh, "Loan",
            ["- borrowDate: Date", "- dueDate: Date", "- member: Member", "- book: Book"],
            ["+ getters/setters", "+ toString()"])

        # Library --<> Book: aggregation
        lx1, ly1 = lib[0] + bw, lib[1] + bh*0.3
        bx1, by1 = bk[0], bk[1] + bh*0.3
        ang1 = math.atan2(by1 - ly1, bx1 - lx1)
        draw_diamond(c, lx1, ly1, ang1)
        draw_arrow(c, lx1, ly1, bx1, by1)
        mx1, my1 = (lx1+bx1)/2, (ly1+by1)/2
        draw_label(c, mx1, my1 + 8, "1")
        draw_label(c, mx1, my1 - 10, "1..*")

        # Library --<> Member: aggregation
        lx2, ly2 = lib[0] + bw, lib[1] + bh*0.7
        mx2, my2 = mb[0], mb[1] + bh*0.7
        ang2 = math.atan2(my2 - ly2, mx2 - lx2)
        draw_diamond(c, lx2, ly2, ang2)
        draw_arrow(c, lx2, ly2, mx2, my2)
        mx2m, my2m = (lx2+mx2)/2, (ly2+my2)/2
        draw_label(c, mx2m, my2m + 8, "1")
        draw_label(c, mx2m, my2m - 10, "0..*")

        # Member --- Loan: association
        mlx, mly = mb[0] + bw*0.3, mb[1]
        llx, lly = ln[0] + bw*0.3, ln[1] + bh
        draw_arrow(c, mlx, mly, llx, lly)
        mmlx, mmly = (mlx+llx)/2, (mly+lly)/2
        draw_label(c, mmlx, mmly + 8, "1")
        draw_label(c, mmlx, mmly - 10, "0..*")

        # Loan --- Book: association
        blx, bly = bk[0] + bw*0.7, bk[1]
        llx2, lly2 = ln[0] + bw*0.7, ln[1] + bh
        draw_arrow(c, blx, bly, llx2, lly2)
        mblx, mbly = (blx+llx2)/2, (bly+lly2)/2
        draw_label(c, mblx, mbly + 8, "1")
        draw_label(c, mblx, mbly - 10, "1")

        # Legend
        c.setFont('Helvetica', 9)
        c.setFillColor(HexColor('#1a1a2e'))
        c.drawString(x_off + 10, y_off + 10, "Legend:")
        c.setFont('Courier', 8)
        c.drawString(x_off + 10, y_off - 4, "--<>  Aggregation")
        c.drawString(x_off + 10, y_off - 18, "----> Association")

story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("The diagram below shows the four classes and their relationships:", body_style))
story.append(Spacer(1, 0.3*cm))
story.append(UMLDiagram())
story.append(Spacer(1, 0.5*cm))

# ── Class Descriptions ──
story.append(PageBreak())
story.append(Paragraph("1. Class Descriptions", heading1_style))

classes_info = [
    ("Book", [
        ("Attributes", [
            "- isbn : String  (private)",
            "- title : String  (private)",
            "- author : String  (private)",
            "- available : boolean  (private)",
        ]),
        ("Methods", [
            "+ Book(isbn, title)  (public)",
            "+ Book(isbn, title, author)  (public)",
            "+ getIsbn() : String  (public)",
            "+ getTitle() : String  (public)",
            "+ getAuthor() : String  (public)",
            "+ getStatus() : boolean  (public)",
            "+ setStatus(available : boolean) : void  (public)",
            "+ toString() : String  (public)",
        ]),
    ]),
    ("Member", [
        ("Attributes", [
            "- memberId : String  (private)",
            "- name : String  (private)",
            "- loans : List<Loan>  (private)",
        ]),
        ("Methods", [
            "+ Member(memberId, name)  (public)",
            "+ getMemberId() : String  (public)",
            "+ getName() : String  (public)",
            "+ addLoan(loan : Loan) : void  (public)",
            "+ toString() : String  (public)",
        ]),
    ]),
    ("Loan", [
        ("Attributes", [
            "- borrowDate : Date  (private)",
            "- dueDate : Date  (private)",
            "- member : Member  (private)",
            "- book : Book  (private)",
        ]),
        ("Methods", [
            "+ Loan(member, book, bDate, dDate)  (public)",
            "+ getBorrowDate() : Date  (public)",
            "+ getDueDate() : Date  (public)",
            "+ getMember() : Member  (public)",
            "+ getBook() : Book  (public)",
            "+ toString() : String  (public)",
        ]),
    ]),
    ("Library", [
        ("Attributes", [
            "- books : List<Book>  (private)",
            "- members : List<Member>  (private)",
        ]),
        ("Methods", [
            "+ addBook(book : Book) : void  (public)",
            "+ registerMember(member : Member) : void  (public)",
            "+ lendBook(borrower, book, bDate, dDate) : void  (public)",
            "+ returnBook(book : Book) : void  (public)",
            "+ searchBookByTitle(title : String) : Book  (public)",
        ]),
    ]),
]

for cname, sections in classes_info:
    story.append(Paragraph(f"<b>{cname}</b>", heading2_style))
    for sec_title, items in sections:
        story.append(Paragraph(f"<b>{sec_title}:</b>", body_style))
        for item in items:
            story.append(Paragraph(f"&bull; {item}", bullet_style))

# ── Visibility Symbols ──
story.append(PageBreak())
story.append(Paragraph("2. Visibility Symbols", heading1_style))
story.append(Paragraph(
    "In UML, visibility symbols indicate the accessibility of class members:", body_style))

vis_data = [
    [Paragraph("<b>Symbol</b>", body_style), Paragraph("<b>Visibility</b>", body_style), Paragraph("<b>Meaning</b>", body_style)],
    [Paragraph("+", body_style), Paragraph("Public", body_style), Paragraph("Accessible from any other class.", body_style)],
    [Paragraph("-", body_style), Paragraph("Private", body_style), Paragraph("Accessible only within the class itself.", body_style)],
    [Paragraph("#", body_style), Paragraph("Protected", body_style), Paragraph("Accessible within the class and subclasses.", body_style)],
    [Paragraph("~", body_style), Paragraph("Package", body_style), Paragraph("Accessible within the same package.", body_style)],
]
vis_table = Table(vis_data, colWidths=[60, 80, 280])
vis_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, gray), ('INNERGRID', (0,0), (-1,-1), 0.25, gray),
    ('BACKGROUND', (0,0), (-1,0), HexColor('#e8eaf6')), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(vis_table)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "In our system, all attributes are <b>private (-)</b> and all methods are <b>public (+)</b>, "
    "following proper encapsulation principles.", body_style))

# ── Relationships ──
story.append(PageBreak())
story.append(Paragraph("3. Relationships", heading1_style))

story.append(Paragraph("3.1 Association", heading2_style))
story.append(Paragraph(
    "<b>Definition:</b> Association represents a structural relationship between two or more "
    "classes, indicating that objects of one class are connected to objects of another class. "
    "It is the most basic form of relationship in OOP and UML.", body_style))
story.append(Paragraph("<b>Examples in our system:</b>", body_style))
story.append(Paragraph(
    "&bull; <b>Member &harr; Loan:</b> A Member borrows books, and each borrowing is recorded "
    "as a Loan. The Member class holds a list of Loans (<i>loans : List&lt;Loan&gt;</i>), "
    "and the Loan class holds a reference to the Member (<i>member : Member</i>). This is a "
    "bi-directional association.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Loan &harr; Book:</b> A Loan is associated with exactly one Book. The Loan class "
    "holds a reference <i>book : Book</i> to indicate which book was borrowed.", bullet_style))
story.append(Paragraph("<b>Key points about Association:</b>", body_style))
story.append(Paragraph(
    "&bull; It can be unidirectional (one class knows about the other) or bidirectional "
    "(both classes know about each other).", bullet_style))
story.append(Paragraph(
    "&bull; It can have a label (e.g., \"borrows\") and multiplicity at each end.", bullet_style))
story.append(Paragraph(
    "&bull; In Java, associations are typically implemented as reference fields (object pointers).", bullet_style))

story.append(Paragraph("3.2 Aggregation", heading2_style))
story.append(Paragraph(
    "<b>Definition:</b> Aggregation is a specialized form of Association that represents a "
    "\"has-a\" or \"whole-part\" relationship where the part can exist independently of the "
    "whole. It is often called \"weak aggregation\" because the lifecycle of the part is not "
    "tied to the lifecycle of the whole.", body_style))
story.append(Paragraph("<b>Why Library and Book represent Aggregation:</b>", body_style))
story.append(Paragraph(
    "A Library <i>has</i> Books, but a Book can exist independently of the Library. "
    "A Book could be removed from this Library and added to another Library, or it could "
    "exist before being added to any Library. The Book has its own independent lifecycle. "
    "This is the defining characteristic of aggregation &mdash; the \"part\" (Book) can "
    "exist without the \"whole\" (Library).", body_style))
story.append(Paragraph("<b>Why Library and Member represent Aggregation:</b>", body_style))
story.append(Paragraph(
    "Similarly, a Library <i>has</i> Members, but a Member is a person who can exist "
    "independently. A Member could be registered in multiple libraries or move between "
    "libraries. The Member object has its own lifecycle separate from the Library.", body_style))
story.append(Paragraph(
    "<b>UML Notation:</b> Aggregation is shown as a hollow diamond on the \"whole\" side "
    "(Library) connected by a line to the \"part\" side (Book or Member).", body_style))

story.append(Paragraph("3.3 Composition", heading2_style))
story.append(Paragraph(
    "<b>Definition:</b> Composition is a stronger form of Aggregation where the part cannot "
    "exist independently of the whole. If the whole is destroyed, the parts are also "
    "destroyed. This is a \"strong has-a\" or \"owns-a\" relationship with lifecycle "
    "dependency.", body_style))
story.append(Paragraph("<b>How Composition differs from Aggregation:</b>", body_style))

comp_data = [
    [Paragraph("<b>Feature</b>", body_style), Paragraph("<b>Aggregation</b>", body_style), Paragraph("<b>Composition</b>", body_style)],
    [Paragraph("Lifecycle", body_style), Paragraph("Parts exist independently", body_style), Paragraph("Parts depend on the whole", body_style)],
    [Paragraph("Relationship", body_style), Paragraph("\"Has-a\" (weak)", body_style), Paragraph("\"Owns-a\" (strong)", body_style)],
    [Paragraph("UML Notation", body_style), Paragraph("Hollow diamond", body_style), Paragraph("Filled diamond", body_style)],
    [Paragraph("Example", body_style), Paragraph("Library <> Book", body_style), Paragraph("House <> Room", body_style)],
]
comp_table = Table(comp_data, colWidths=[100, 150, 150])
comp_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, gray), ('INNERGRID', (0,0), (-1,-1), 0.25, gray),
    ('BACKGROUND', (0,0), (-1,0), HexColor('#e8eaf6')), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(comp_table)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("<b>Practical Example &mdash; House and Room:</b>", body_style))
story.append(Paragraph(
    "A House contains Rooms. If the House is demolished (destroyed), the Rooms cease to "
    "exist as well. A Room cannot exist without being part of some House. This is "
    "Composition. In contrast, a Library contains Books, but if the Library closes, the "
    "Books still exist and can be transferred elsewhere &mdash; this is Aggregation.", body_style))

# ── Multiplicity ──
story.append(PageBreak())
story.append(Paragraph("4. Multiplicity", heading1_style))
story.append(Paragraph(
    "<b>Definition:</b> Multiplicity defines how many instances of one class can be "
    "associated with instances of another class in a relationship. It specifies the "
    "quantitative aspect of the relationship.", body_style))

story.append(Paragraph("Common multiplicity values:", body_style))
multi_data = [
    [Paragraph("<b>Notation</b>", body_style), Paragraph("<b>Meaning</b>", body_style), Paragraph("<b>Example</b>", body_style)],
    [Paragraph("<b>1</b>", body_style), Paragraph("Exactly one instance", body_style), Paragraph("Loan -- 1 -- Book (one loan is for exactly one book)", body_style)],
    [Paragraph("<b>0..1</b>", body_style), Paragraph("Zero or one instance (optional)", body_style), Paragraph("A person may have zero or one passport", body_style)],
    [Paragraph("<b>0..*</b>", body_style), Paragraph("Zero or more instances (any number)", body_style), Paragraph("Member -- 0..* -- Loan (a member can have zero or many loans)", body_style)],
    [Paragraph("<b>1..*</b>", body_style), Paragraph("One or more instances (at least one)", body_style), Paragraph("Library -- 1..* -- Book (a library must have at least one book)", body_style)],
]
multi_table = Table(multi_data, colWidths=[60, 180, 180])
multi_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, gray), ('INNERGRID', (0,0), (-1,-1), 0.25, gray),
    ('BACKGROUND', (0,0), (-1,0), HexColor('#e8eaf6')), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(multi_table)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Multiplicity examples from our system:", body_style))
story.append(Paragraph(
    "&bull; <b>Member 1 &mdash; 0..* Loan:</b> One Member can have zero or more Loans. "
    "A new member may have no loans yet, but over time they can borrow many books.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Loan 1 &mdash; 1 Book:</b> Each Loan is for exactly one Book. "
    "A loan cannot be for multiple books.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Library 1 &mdash; 1..* Book:</b> A Library must contain at least one Book "
    "but can hold many. It would not be a library with zero books.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Library 1 &mdash; 0..* Member:</b> A Library can have zero or more registered "
    "Members. A new library may start with no members and grow over time.", bullet_style))

# ── Summary ──
story.append(PageBreak())
story.append(Paragraph("5. Summary", heading1_style))
story.append(Paragraph(
    "The UML Class Diagram for the Library Management System models four key classes "
    "(<b>Library</b>, <b>Book</b>, <b>Member</b>, <b>Loan</b>) with the following "
    "relationships:", body_style))
story.append(Paragraph(
    "&bull; <b>Aggregation</b> between Library and Book (hollow diamond) &mdash; "
    "Library has Books, but Books exist independently.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Aggregation</b> between Library and Member (hollow diamond) &mdash; "
    "Library registers Members, but Members exist independently.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Association</b> between Member and Loan &mdash; Members take out Loans.", bullet_style))
story.append(Paragraph(
    "&bull; <b>Association</b> between Loan and Book &mdash; A Loan references a Book.", bullet_style))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "All attributes are <b>private (-)</b> to enforce encapsulation, and methods are "
    "<b>public (+)</b> to provide controlled access to the object's state. Multiplicities "
    "define the cardinality of each relationship, ensuring the model accurately reflects "
    "real-world library operations.", body_style))

doc.build(story)
print(f"PDF generated: {output_path}")
