#!/usr/bin/env python3
"""Engine Company Operations study guide PDF (NYS OFPC)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

RED = colors.HexColor("#B22222")
DARK = colors.HexColor("#1a1a1a")
GRAY = colors.HexColor("#555555")

ss = getSampleStyleSheet()
styles = {
    "title": ParagraphStyle("t", parent=ss["Title"], fontSize=22, textColor=RED, spaceAfter=4),
    "subtitle": ParagraphStyle("st", parent=ss["Normal"], fontSize=12, textColor=GRAY,
                               alignment=1, spaceAfter=2),
    "h1": ParagraphStyle("h1", parent=ss["Heading1"], fontSize=14, textColor=RED,
                         spaceBefore=14, spaceAfter=4, borderPadding=2),
    "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontSize=11.5, textColor=DARK,
                         spaceBefore=8, spaceAfter=2),
    "body": ParagraphStyle("b", parent=ss["Normal"], fontSize=9.5, leading=12.5, spaceAfter=3),
    "bullet": ParagraphStyle("bl", parent=ss["Normal"], fontSize=9.5, leading=12.5,
                             leftIndent=14, bulletIndent=4, spaceAfter=1.5),
    "key": ParagraphStyle("k", parent=ss["Normal"], fontSize=9.5, leading=12.5,
                          backColor=colors.HexColor("#FFF3E0"), borderPadding=4,
                          borderColor=colors.HexColor("#FFB74D"), borderWidth=0.7,
                          spaceBefore=4, spaceAfter=6),
}

story = []
def H1(t): story.append(Paragraph(t, styles["h1"]))
def H2(t): story.append(Paragraph(t, styles["h2"]))
def P(t): story.append(Paragraph(t, styles["body"]))
def B(items):
    for i in items:
        story.append(Paragraph(i, styles["bullet"], bulletText="•"))
def KEY(t): story.append(Paragraph("<b>TEST TIP:</b> " + t, styles["key"]))
def TBL(data, widths, header=True):
    t = Table([[Paragraph(c, styles["body"]) for c in row] for row in data], colWidths=widths)
    st = [("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#BBBBBB")),
          ("VALIGN", (0,0), (-1,-1), "TOP"),
          ("TOPPADDING", (0,0), (-1,-1), 3), ("BOTTOMPADDING", (0,0), (-1,-1), 3),
          ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F5F5F5")])]
    if header:
        st += [("BACKGROUND", (0,0), (-1,0), RED), ("TEXTCOLOR", (0,0), (-1,0), colors.white)]
        data2 = [[Paragraph(f"<b><font color='white'>{c}</font></b>", styles["body"]) for c in data[0]]]
        data2 += [[Paragraph(c, styles["body"]) for c in row] for row in data[1:]]
        t = Table(data2, colWidths=widths)
        t.setStyle(TableStyle(st))
    else:
        t.setStyle(TableStyle(st))
    story.append(t); story.append(Spacer(1, 6))

# ---------------- Title ----------------
story.append(Paragraph("Engine Company Operations", styles["title"]))
story.append(Paragraph("Study Guide &amp; Exam Prep — NYS DHSES OFPC Student Manual", styles["subtitle"]))
story.append(Paragraph("Comprehensive review by unit, with a quick-reference cram sheet at the end", styles["subtitle"]))
story.append(Spacer(1, 10))

# ---------------- Unit 1 ----------------
H1("Unit 1: Course Introduction")
B(["24-hour course: eight 3-hour sessions (classroom + practical), <b>two homework assignments</b>, and a <b>final exam</b>.",
   "Completion requires full attendance/participation, both homeworks satisfactorily submitted, and a passing final exam grade.",
   "Students must submit a completed <b>Chiefs Authorization form</b> (physically able to participate and use SCBA in an IDLH environment).",
   "Per OSHA, students must be <b>clean shaven</b> for all SCBA activities (no facial hair between mask and face)."])
P("<b>Terminal objective:</b> define pyrolysis, air track management, under-ventilated fires, and fire phenomena with 100% accuracy. "
  "<b>Enabling objectives:</b> complete size up, maintain situational awareness, develop leadership, define apparatus positioning, "
  "establish a positive water supply, select/deploy attack and backup lines, deploy master streams and appliances, augment fixed suppression systems.")

# ---------------- Unit 2 ----------------
H1("Unit 2: Fire Behavior")
H2("Only Vapors Burn")
B(["<b>Solids and liquids do not burn</b> — only the vapors they give off burn.",
   "<b>Pyrolysis:</b> heat (with sufficient oxygen) chemically decomposes a solid, producing vapors and char/ash; some vapors are flammable. It converts a solid into a flammable gas.",
   "<b>Pyrophoric degradation:</b> slow, long-term decomposition of a solid.",
   "Solids with a <b>high surface-to-mass ratio</b> combust more easily and rapidly.",
   "Law of Conservation of Matter: matter is neither created nor destroyed — only changed."])
H2("Heat Energy (BTUs)")
B(["<b>1 BTU</b> = heat needed to raise 1 lb of water 1°F.",
   "<b>Latent heat of vaporization:</b> 970 BTU to convert 1 lb of 212°F water to 212°F steam — about <b>7 times</b> the heat it took to make cold water hot.",
   "From 70°F: 142 BTU to reach 212°F, plus 970 BTU to steam = <b>1,112 BTU total absorbed per lb of water</b>."])
TBL([["Fuel", "BTU per pound"],
     ["Wood", "7,000"], ["Polyurethane", "14,000"], ["Polyvinyl chloride (PVC)", "17,900"],
     ["Polystyrene", "18,750"], ["Polypropylene", "20,000"], ["Polyethylene", "20,100"],
     ["Gasoline", "20,500 (126,000/gal)"]], [2.5*inch, 2.5*inch])
KEY("Synthetic fuels roughly double or triple wood's heat output. Today's fires produce 200–300% more heat, produce it faster, and make thicker, toxic, highly flammable smoke — dramatically shortening time to flashover.")
H2("Combustion Products")
B(["Oxygen readily available (complete combustion) → <b>carbon dioxide</b>: inert, heavier than air.",
   "Oxygen limited → <b>carbon monoxide</b>: vapor density 0.96 (slightly lighter than air) and <b>highly flammable</b>.",
   "<b>Smoke is fuel</b> — unburned hydrocarbons plus CO; it can ignite and drive serious fire development."])
H2("Fire Phenomena")
TBL([["Event", "Definition / keys"],
     ["Rollover", "Unburned combustible gases produced by the fire rise to the ceiling, spread horizontally, and ignite when they get what they were missing (usually oxygen)."],
     ["Flashover", "ALL contents of a compartment get hot enough, undergo pyrolysis, release flammable vapors, and ignite. Modern construction can flash over in as little as 5 minutes or less."],
     ["Backdraft", "Sudden eruption of fire due to accumulated superheated gases plus the introduction of fresh air. After an opening is made, the event may take 2–3 minutes while fresh air dilutes the smoke into its flammable range."],
     ["Smoke explosion", "COOL smoke that is rapidly heated and ignites — it already had the air it needed, it just needed heat."]],
    [1.2*inch, 5.3*inch])
B(["Backdrafts increasingly occur in <b>concealed spaces</b>: above drop ceilings, behind knee walls, closed rooms — in any void — even during interior operations at a vented fire.",
   "If entry is an absolute must at backdraft conditions: vent high (if practical), introduce fresh air low, then <b>wait</b> — enter only when safe (may take 2–3 minutes)."])
H2("Air Track / Flow Path")
B(["Fire needs air; it produces pressure and hot gases that must exit the structure. Identify the flow path — <b>a 360° size-up MUST be completed</b>.",
   "Air can only come from two places: behind the fire (open doors/windows) or the fire vent itself.",
   "<b>Under pressure:</b> smoke exiting due to pressure of combustion. <b>Negative pressure:</b> air being sucked back in, feeding the fire.",
   "Always ask: “Where is the air coming from that is feeding this fire?”"])

# ---------------- Unit 3 ----------------
H1("Unit 3: Fire Control")
P("Class A extinguishment: “put the wet stuff on the <b>base</b> of the red stuff.” Cooling stops pyrolytic decomposition → stops production of flammable vapors → <b>no flammable vapors = no fire</b>. You may have to control overhead heat/rollover first before reaching the base. Incident priorities NEVER change.")
H2("Water Facts")
B(["Weighs <b>8.33 lbs/gal</b>. 150 GPM = 1,250 lbs/min; 185 GPM = 1,541 lbs/min; 1,000 GPM = 8,000+ lbs/min (≈4 tons).",
   "<b>Non-compressible</b> and <b>conducts electricity</b>.",
   "States: below 32°F ice; 32–212°F liquid; above 212°F steam.",
   "Steam expansion: at 212°F water expands <b>1,700:1</b>; at 1,000°F, <b>4,200:1</b> — and it keeps expanding as it heats.",
   "Extinguishing properties of water: <b>cooling, smothering, and dilution</b>."])
KEY("It is the APPLICATION RATE (GPM) that extinguishes a fire — not the total water applied.")
H2("Improving Water")
B(["<b>Class A foam / CAFS:</b> estimated 4–5 times as effective as plain water on Class A fire; follow manufacturer procedures; ventilation even more important.",
   "<b>Wet water:</b> add ~6 oz dish detergent to a 500-gal booster tank (flush after) — breaks surface tension so water soaks into the fuel and absorbs heat. A low-cost version of Class A foam. It does NOT let water absorb more heat."])
H2("Minimum Flow &amp; the Studies")
B(["<b>NEVER use a hose/nozzle system flowing less than 150–185 GPM</b> — the industry standard for a one-room-and-contents fire in a slab house.",
   "<b>Iowa Study (1951–52, Royer &amp; Nelson):</b> “The rate of flow is the most important factor affecting fire extinguishment.” Nozzle type has little effect if the critical flow rate is met and the stream hits the base of the fire.",
   "<b>LAFD testing (1984, BC Claude Greasy):</b> 150 GPM ideal single attack line flow at 100 psi nozzle pressure (NR = 76 lbs). A 50 psi fog can flow 200 GPM with NR of 71 lbs.",
   "<b>Chicago FD (1995):</b> low-pressure nozzles delivered more water and cut firefighter stress by reducing nozzle reaction."])
H2("Nozzles")
B(["Purpose: <b>restrict flow to build velocity</b> and project the stream. Hose + nozzle are a matched SYSTEM.",
   "Attack lines must have: sufficient flow; easy to stretch/operate/advance; long enough; easily visible (your most important lifeline).",
   "<b>Smooth bore:</b> solid stream; controlled only by pump operator or opening/closing the nozzle.",
   "<b>Fixed gallonage fog:</b> one flow at one pressure (older: 125 GPM @ 100 psi; newer: 185 GPM @ 50 psi).",
   "<b>Selectable gallonage fog:</b> selector ring changes flow; fixed nozzle pressure, so flow changes require engine pressure changes.",
   "<b>Automatic (constant pressure) fog:</b> internal spring keeps outgoing pressure constant; pattern looks the same regardless of flow. <b>Must be exercised and lubricated regularly</b> or the spring may stick.",
   "<b>Dual-pressure automatic:</b> regular + emergency low-pressure setting (e.g., 100/55 or 75/45 psi) for low-pressure situations like standpipes.",
   "Over-pressuring a fixed/adjustable nozzle: stream breaks up, and eventually flow <b>decreases</b> as pressure rises."])
H2("Nozzle Reaction (NR)")
TBL([["Firefighters on the line", "Manageable nozzle reaction"],
     ["1 firefighter", "60 lbs"], ["2 firefighters", "75 lbs"], ["3 firefighters", "95 lbs"]],
    [3*inch, 3*inch])
B(["NR is a function of the <b>nozzle</b>, not the hose. Same GPM + same nozzle pressure = same NR (smooth bore or fog).",
   "A 100 psi nozzle suffers <b>42% more NR</b> than a comparable 50 psi nozzle. TFT: a 50 psi fog has only <b>9% less reach</b> than a 100 psi fog.",
   "Valve waterway: 1″ dia = 0.79 in²; 1-3/8″ dia = 1.48 in² (about twice the area). 1″ and 1.25″ waterways can't flow what today's fires require.",
   "Friction loss factors: hose diameter, hose liner, coupling size, kinks.",
   "Modern 200′ hose: 185 GPM @ 50 psi NP with 140 psi PDP; 250 GPM @ 50 psi NP with 170 psi PDP."])
KEY("First line pulled is often the most important. “The first 5 minutes determine the next 5 hours.” Things that start off wrong rarely get back on track.")

# ---------------- Unit 4 ----------------
H1("Unit 4: Tactical Positions &amp; Responsibilities")
P("All tasks must be performed even with fewer than 6 people — coordinate via SOP and training.")
TBL([["Position", "Key responsibilities"],
     ["Engine Officer", "Decisions that affect outcome: line selection, positive water supply, direct/indirect/transitional attack. Know apparatus, equipment, tactics. Protect the crew — do not risk your life for a building."],
     ["Nozzle Firefighter", "1st on line: responsible for 1st length and nozzle. Bring to a safe stretching spot (stairwell, hallway, front door). Bleed air when water is called. NEVER enter the fire area without water; NEVER pass fire. Door control; solid/straight stream; all members on the same side of the line; stay low and to the side. Advance by crawling, duck walk, or leg out."],
     ["Back-up Firefighter", "2nd on line: chock doors, flake hose, facilitate advancement. “The nozzle is only as good as the back-up.” Absorb as much NR as possible; position close to the nozzle FF; firm grasp, opposite and opposed."],
     ["Door Firefighter", "3rd on line: carry/flake hose, FEED hose to the nozzle team (don't push it), keep a little slack, watch fire conditions, don't turn your back on fire when withdrawing, chock doors (if not a flow-path factor)."],
     ["Control Firefighter", "Ensure sufficient lengths stretched; assist operator with hook-up on a short stretch; feed slack; eliminate kinks/folds outside and inside; ensure doors chocked."]],
    [1.3*inch, 5.2*inch])
B(["<b>Deflected water</b> covers a greater area, breaks up and cools superheated ceiling gases, absorbs more heat (more surface area), and helps prevent rollover and flashover."])

# ---------------- Unit 6 ----------------
H1("Unit 6: Size Up (R.E.C.E.O. V.S. / COAL WAS WEALTH)")
B(["<b>R.E.C.E.O. V.S.:</b> Rescue, Exposure, Confinement, Extinguishment, Overhaul — Ventilation, Salvage.",
   "Size-up is the front-right-seat rider's responsibility; it starts with pre-incident planning (before dispatch) and continues to the end of operations.",
   "<b>Incident priorities never change:</b> Life Safety, Incident Stabilization, Property Conservation.",
   "<b>COAL:</b> Construction, Occupancy, Area, Location. <b>WAS:</b> Water supply, Apparatus &amp; equipment, Street conditions. <b>WEALTH:</b> Weather, Exposures, Appliances, LIFE (yours first — evaluate survivability), Time, Height."])
H2("Building Construction Types")
TBL([["Type", "Name / concerns"],
     ["Type I", "Fire resistive — concrete frame, noncombustible. Concerns: access, long stretches, standpipes, FDCs."],
     ["Type II", "Non-combustible — unprotected steel bar joists/trusses. Concerns: big-box stores, horizontal water supply/remote standpipes, search ropes, roof construction."],
     ["Type III", "Ordinary — masonry/brick walls, wood joists and interior. Older “Main Street” towns. Common attics and basements. PRONE TO COLLAPSE FROM FIRE."],
     ["Type IV", "Heavy timber (mill) — dimensional lumber. Churches, former factories; consider reach of stream."],
     ["Type V", "Wood frame — lightweight construction, fast fire development, roof/floor collapse, unprotected stairwells. Platform, balloon, post &amp; beam, plank &amp; beam, log cabin."]],
    [0.9*inch, 5.6*inch])
KEY("Modern (lightweight) construction can flash over in as little as 5 minutes; legacy construction takes considerably longer. Know the construction type before interior operations.")
B(["“The fire goes as the 1st line goes.” A properly placed handline saves more lives than anything.",
   "Line placement drivers: confine the fire, protect occupants/means of egress, exposure protection. Check: proper placement, enough hose, enough personnel, doors chocked, kinks chased, hose secured."])

# ---------------- Unit 7 ----------------
H1("Unit 7: Engine Company Tactics")
B(["<b>Rule 1:</b> Fire attack must be properly supported. <b>Rule 2:</b> The water must hit the seat of the fire.",
   "Stretch the line — don't “pull and dump.”",
   "<b>Direct attack:</b> water on the base of the fire; cools fuel, stops vapor production; little disruption of thermal balance; minimal steam. Validated by University of Illinois (late 1980s–early 1990s).",
   "<b>Indirect attack:</b> water onto heated gases at the ceiling, raining down on the fire — bounce the stream off the ceiling (it deflects at a shallow angle).",
   "<b>Combination attack:</b> start indirect, switch to direct to finish the base.",
   "<b>Modes:</b> Interior Offensive; Exterior Offensive (formerly “defensive”) — often fastest/safest with limited staffing; Transitional — knock it down from outside, then move in for final extinguishment (also called Offensive Exterior Attack).",
   "Evaluate the fire first — complete a <b>7-sided, 360° size-up</b> before rushing in.",
   "<b>Hose streams do not push fire</b> (proven by testing).",
   "<b>Fire doubles every 30 seconds</b> — every 30 seconds it takes twice the flow rate to control."])
H2("Required Fire Flow")
B(["<b>NFPA 1410 &amp; 1710:</b> total initial required streams = minimum <b>300 GPM (two lines)</b> for a single room-and-contents fire (2,000 ft² structure on a slab).",
   "<b>NFA quick-calc formula: NFF = (Length × Width) ÷ 3</b> — gives GPM for 100% involvement of one floor. Reduce proportionally for partial involvement (e.g., 800 GPM × 0.25 = 200 GPM).",
   "<b>Interior exposures:</b> add 25% of the 100% figure for each floor above the fire floor (max 5 floors). <b>Exterior exposures:</b> add 25% for each side with an exposure facing the fire building.",
   "The NFA formula derives from the <b>Iowa formula: (L × W × H) ÷ 100</b>, built for compartment (shipboard) fires — apply it to the largest compartment, not the whole building. A common attic/cockloft makes the whole building one compartment.",
   "<b>1 GPM can theoretically control 3 ft² of fire</b> in a compartment when applied correctly.",
   "Worksheet examples: 30×30 → 300 GPM; 30×50 → 500 GPM."])
H2("Hand Line Selection")
TBL([["Line", "Use / numbers"],
     ["1¾″", "Residential fires. Flows 150+ (up to 250+) GPM possible; <b>180 GPM is ideal / minimum target</b>. 50′ full of water = 52 lbs."],
     ["2″", "Residential and larger flows. Newer technology; actual ID 1.88″. As maneuverable as 1¾″, flows like 2½″. Needs a properly matched nozzle."],
     ["2½″", "Larger fires, standpipes, long stretches, big-box/commercial, “McMansions.” 250+ GPM, reach, knockdown/penetrating power; reduces to smaller lines. 50′ full = 106 lbs. 1-1/8″ tip @ 50 psi ≈ 266 GPM (over a ton of water per minute)."]],
    [0.8*inch, 5.7*inch])
B(["Big fire = big water; small fire = small water. Don't go bear hunting with a BB gun.",
   "Overestimate the flow you're getting; underestimate friction loss — the industry now talks in GPM, not hose size.",
   "2½″ technique: “pin” the line with knees/ground, loop the line, use a hose strap or webbing with a water knot — otherwise it takes many firefighters."])
H2("Master Streams &amp; Nozzle Patterns")
B(["Deck gun limits: angle limitations (cab obstructions), positioning, apparatus piping may not deliver rated GPM, setup time.",
   "Portable master streams <b>MUST be properly secured</b> (rope, chain, straps); observe angle limits; flow limits in portable mode; semi-maneuverable when shut down.",
   "<b>Straight/solid stream:</b> safest for interior crews, least steam, best reach to base; least heat absorption per surface area.",
   "<b>Wide fog:</b> absorbs heat fastest (most surface area) but makes the most steam — a hazard for interior crews."])
H2("Line Management")
B(["First line in operation before back-up line is stretched. Crews spread out at choke points (top of stairs, landings, corners).",
   "<b>No more than 2 lines through one entry point; NO OPPOSING LINES.</b>",
   "Chock doors <b>LOW</b> (no higher than just above the bottom hinge); always consider whether the open door creates a flow path.",
   "Drop ceilings: fire resistive (not fire load), but don't hit them with the stream — water weight collapses them; the void above can hold oxygen-starved superheated gases and explode without warning.",
   "Burst length: serious danger — communicate, move to a safe area, and replace the burst section with <b>TWO lengths</b>. Practice in drills.",
   "NIOSH Case Study 2010-10 issues: uncoordinated ventilation, SCBA removal, inadequate command/control/accountability, insufficient staffing. Key recommendations: 360° size-up, risk vs. benefit, fire flow, hose/nozzle selection, crew integrity, understand fire behavior and ventilation effects, proper SCBA/PPE, accountability, safety officer."])

# ---------------- Unit 9 ----------------
H1("Unit 9: Standpipes &amp; Standpipe Operations")
B(["<b>NFPA 14</b> (2010 ed.): design, components, testing, maintenance of standpipe and hose systems.",
   "Building codes require standpipes in buildings <b>over 75 feet</b>; some codes: over 30 feet, areas without apparatus access (parking garages), long distances (airport terminals, tunnels, bridges).",
   "Components: FDC (2½″, 4″, or 5″), piping, hose connections (2½″, 1½″ or both), pressure-regulating devices.",
   "<b>Standard LDH supports only up to 185 psi.</b>"])
TBL([["Class", "User"],
     ["Class I", "Fire department use (2½″)"],
     ["Class II", "Occupant use"],
     ["Class III", "Both FD and occupant (“us, them, us and them”)"]],
    [1.5*inch, 5*inch])
B(["<b>Types:</b> automatic wet / automatic dry, manual wet / manual dry, combination (sprinkler + standpipe on a common riser).",
   "Wet systems hold water in the riser at all times (municipal main, gravity tank, pressure tank, or combination; may have a fire pump). Dry systems: water enters when air/inert gas releases at an open outlet; some have no municipal supply at all — <b>the FD provides the water</b>.",
   "Engine company duties: supply/augment the system (with <b>2½″ or larger hose</b>, independent + redundant supplies), transport hose/nozzle/fittings/tools, stretch and advance the line."])
H2("Operating from a Standpipe")
B(["Hook up at an outlet that protects the nozzle team — <b>the floor below the fire</b> or a protected stairwell. <b>Flush the outlet before connecting.</b>",
   "<b>Use an in-line pressure gauge at the outlet</b> — a safety issue; adjust pressure while water is flowing. A gated wye allows a second line.",
   "Each firefighter carries needed equipment; <b>minimum 3 lengths of hose</b>. Nozzle operator needs at least <b>50 feet of line per floor</b>.",
   "Standpipe kit: in-line gauge, 2 spanner wrenches, spare control wheels, pipe wrench, wire brush, door chocks, adapters (pipe thread &amp; NST).",
   "FDC/outlet problems: missing caps, debris-clogged connections, broken/jammed clappers (cap or gate the unused side, or attach a second supply line), damaged threads/swivels. Stuck caps: tap with a spanner; large spanner or 36″ pipe wrench; break a screw eye off vandal-proof caps.",
   "<b>Elevators:</b> never use unless the FD has complete control (Firefighter Phase 1 &amp; 2); <b>never take the car to the fire floor</b> — connect at the floor below.",
   "Bring irons to force doors/breach walls. Avoid occupant-use house hose — not pressure tested, lightweight, likely poor condition.",
   "High-rise stretch comparison (6th floor, 180 GPM, 50 psi tip): conventional stretch ≈ <b>230 psi</b> total vs. rope stretch ≈ <b>180 psi</b>."])

# ---------------- Unit 10 ----------------
H1("Unit 10: Hose Loads &amp; Estimating the Stretch")
B(["Know your own hose loads AND your mutual-aid departments' loads.",
   "<b>Pre-connected loads:</b> rapid removal; based on staffing and pre-planning; length/diameter based on required flow rates.",
   "<b>Flat load:</b> easy to assemble and deploy; use only the needed lengths; uncouple and connect to the pump panel.",
   "<b>Minuteman load:</b> pre-connect in the narrow hose bed section, one column, <b>nozzle at the bottom</b>; entire load is shouldered and plays out as you walk away.",
   "<b>Triple layer load:</b> pre-connect; pulls all hose out; forms an <b>“S” shape</b> on the ground; good with distance between apparatus and objective.",
   "<b>Finish load:</b> rides on top of a dead load (e.g., 150′ of 1¾″ on a gated wye with 3″ dead load to the apparatus); loaded flat, accordion, or horseshoe."])
H2("Estimating the Stretch")
B(["Know the exact fire location. <b>Rule of thumb: one 50′ length per floor.</b>",
   "Some SOPs: 2nd line is one length longer than the first; a 3rd line is stretched from the exterior.",
   "<b>Stairwell (well-hole) or rope stretches eliminate about one length per floor</b>; secure with hose straps. Rope stretch: drop a utility rope from the objective floor (or grab the nozzle bail with a hook).",
   "Hose is typically sold in 50′ lengths; consider 75′/100′ to cut friction loss and snag points. Decide your <b>target flow BEFORE</b> buying hose/nozzles. Consider 2″ for the first 100′ with 1¾″ for the working end.",
   "<b>KINKS ARE A TRAINING ISSUE!</b>"])

# ---------------- Cram sheet ----------------
story.append(PageBreak())
story.append(Paragraph("CRAM SHEET — Numbers &amp; One-Liners", styles["title"]))
story.append(Paragraph("The highest-yield facts. If you only review one thing before the exam, review this.", styles["subtitle"]))
story.append(Spacer(1, 8))
TBL([["Number", "What it is"],
     ["1 BTU", "Heat to raise 1 lb water 1°F"],
     ["970 BTU", "Converts 1 lb of 212°F water to steam (≈7× the heat to get it hot); 142 + 970 = 1,112 BTU total from 70°F"],
     ["1,700 : 1", "Steam expansion at 212°F (4,200 : 1 at 1,000°F)"],
     ["8.33 lbs", "Weight of 1 gallon of water"],
     ["150–185 GPM", "Minimum flow for ANY attack hose/nozzle system (one room &amp; contents)"],
     ["180 GPM", "Ideal / minimum target for 1¾″ line"],
     ["300 GPM", "NFPA 1410 / 1710 minimum total initial streams (2 lines, room &amp; contents, 2,000 ft² slab)"],
     ["(L × W) ÷ 3", "NFA Needed Fire Flow (100% of one floor); +25% per floor above (max 5) and per exposed side"],
     ["(L × W × H) ÷ 100", "Iowa fire flow formula (per compartment)"],
     ["1 GPM : 3 ft²", "One GPM controls 3 sq ft of fire, correctly applied"],
     ["30 seconds", "Fire doubles — and required flow doubles"],
     ["2–3 minutes", "Delay from making an opening to a backdraft occurring"],
     ["5 minutes", "Modern lightweight construction can flash over in as little as this"],
     ["60 / 75 / 95 lbs", "Manageable nozzle reaction for 1 / 2 / 3 firefighters"],
     ["42%", "Extra nozzle reaction of a 100 psi nozzle vs comparable 50 psi nozzle"],
     ["9%", "Reach lost by a 50 psi fog vs 100 psi fog (TFT)"],
     ["266 GPM", "2½″ line, 1-1/8″ tip @ 50 psi (over 1 ton/min)"],
     ["52 / 106 lbs", "50′ of charged 1¾″ / 2½″ hose"],
     ["4–5×", "CAFS effectiveness vs plain water on Class A"],
     ["6 oz", "Detergent in a 500-gal booster tank to make “wet water”"],
     ["0.96", "Vapor density of CO (slightly lighter than air, flammable)"],
     ["75 feet", "Building height at which codes require standpipes (NFPA 14)"],
     ["185 psi", "Maximum pressure standard LDH can support"],
     ["3 lengths", "Minimum hose each firefighter carries for standpipe ops"],
     ["50 feet / floor", "Estimating the stretch (and nozzle operator line per floor)"],
     ["7,000 / 20,500", "BTU per lb: wood / gasoline (synthetics ≈14,000–20,000)"]],
    [1.4*inch, 5.1*inch])
H2("Acronyms")
B(["<b>RECEO VS:</b> Rescue, Exposure, Confinement, Extinguishment, Overhaul — Ventilation, Salvage.",
   "<b>COAL WAS WEALTH:</b> Construction, Occupancy, Area, Location — Water supply, Apparatus/equipment, Street conditions — Weather, Exposures, Appliances, LIFE, Time, Height.",
   "<b>Incident priorities (never change):</b> Life Safety → Incident Stabilization → Property Conservation."])
H2("One-Liners the Exam Loves")
B(["Only vapors burn — solids and liquids do not.",
   "Application RATE (GPM), not total water, extinguishes fire.",
   "Rate of flow is the most important extinguishment factor (Iowa Study).",
   "Hose streams do NOT push fire.",
   "Never enter the fire area without water; never pass fire.",
   "The nozzle is only as good as the back-up firefighter.",
   "Smoke is fuel.",
   "CO2 = complete combustion; CO = oxygen-limited combustion.",
   "Nozzle reaction comes from the nozzle, not the hose.",
   "Standpipe hookup: floor below the fire; flush first; use an in-line gauge.",
   "Never take an elevator to the fire floor.",
   "Chock doors low; no opposing lines; max two lines per entry point.",
   "Straight/solid stream = safest inside (least steam); wide fog = fastest heat absorption but most steam.",
   "Type III “ordinary” construction is prone to collapse from fire.",
   "360° (7-sided) size-up before committing interior."])

doc = SimpleDocTemplate("/sessions/admiring-vigilant-curie/mnt/outputs/Engine_Company_Operations_Study_Guide.pdf",
                        pagesize=letter, topMargin=0.6*inch, bottomMargin=0.6*inch,
                        leftMargin=0.7*inch, rightMargin=0.7*inch,
                        title="Engine Company Operations Study Guide")
doc.build(story)
print("done")
