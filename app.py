import re
import streamlit as st
import pandas as pd

# ═══════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════
st.set_page_config(
    page_title="SimpleRISC Assembler",
    page_icon="🔩",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════
#  GLOBAL STYLE
# ═══════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Unbounded:wght@400;700;900&display=swap');

html, body, [class*="css"] { background: #06080f; color: #d4ddf0; }
.stApp { background: #06080f; }
#MainMenu, footer, header { visibility: hidden; }

h1,h2,h3,h4,h5,h6,
.stMarkdown h1,.stMarkdown h2,.stMarkdown h3 {
    font-family: 'Unbounded', sans-serif !important;
    letter-spacing: -0.02em;
}

[data-testid="stSidebar"] {
    background: #080b14 !important;
    border-right: 1px solid #151c2e !important;
}
[data-testid="stSidebar"] * { color: #8899bb !important; }

textarea {
    background: #09111f !important;
    color: #c5d5f0 !important;
    border: 1px solid #1a2540 !important;
    border-radius: 6px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 15px !important;
    line-height: 1.75 !important;
    caret-color: #4af !important;
}
textarea:focus { border-color: #2255aa !important; box-shadow: 0 0 0 2px #1133553d !important; }

.stButton>button {
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    background: #0d1a35 !important;
    color: #4af !important;
    border: 1px solid #1d3d77 !important;
    border-radius: 4px !important;
    padding: 0.45rem 1.2rem !important;
    transition: all 0.12s ease !important;
}
.stButton>button:hover {
    background: #1a3a77 !important;
    border-color: #3399ff !important;
    color: #fff !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px #0055ff33 !important;
}

[data-testid="stMetric"] {
    background: #09111f;
    border: 1px solid #151c2e;
    border-radius: 8px;
    padding: 12px 16px !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Space Mono', monospace !important;
    font-size: 2.2rem !important;
    color: #3af !important;
}
[data-testid="stMetricLabel"] {
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    color: #445577 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid #151c2e !important;
    border-radius: 8px !important;
    overflow: hidden;
}

.stSelectbox > div > div {
    background: #09111f !important;
    border: 1px solid #1a2540 !important;
    color: #aabbcc !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 14px !important;
    border-radius: 4px !important;
}

.stAlert { border-radius: 6px !important; font-family: 'Space Mono', monospace !important; font-size: 13px !important; }

.stDownloadButton>button {
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    background: #051508 !important;
    color: #4caf80 !important;
    border: 1px solid #1a4a2a !important;
    border-radius: 4px !important;
}
.stDownloadButton>button:hover {
    background: #0a3015 !important;
    color: #7fff9a !important;
    border-color: #3aaf60 !important;
    box-shadow: 0 4px 16px #00ff5533 !important;
}

.streamlit-expanderHeader {
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    letter-spacing: 0.08em !important;
    color: #4466aa !important;
    background: #09111f !important;
    border: 1px solid #151c2e !important;
    border-radius: 4px !important;
}
[data-testid="stExpander"] > div:nth-child(2) {
    background: #09111f !important;
    border: 1px solid #151c2e !important;
    border-top: none !important;
}

hr { border-color: #151c2e !important; }

:root, [data-theme="light"], [data-theme="dark"] { color-scheme: dark !important; }
html { color-scheme: dark !important; }

[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stBottom"],
.stApp, .main, .block-container,
section[data-testid="stSidebar"] {
    background-color: #06080f !important;
    color: #d4ddf0 !important;
}

[data-testid="collapsedControl"] {
    background: #09111f !important;
    border: 1px solid #1a2540 !important;
    border-radius: 6px !important;
    color: #44aaff !important;
}
[data-testid="collapsedControl"]:hover {
    background: #1a2540 !important;
    border-color: #3399ff !important;
}
[data-testid="collapsedControl"] svg {
    fill: #44aaff !important;
    stroke: #44aaff !important;
}

input, select, option {
    background: #09111f !important;
    color: #c5d5f0 !important;
    border-color: #1a2540 !important;
}
p, span, label, div { color: #d4ddf0; }

.stTabs [data-baseweb="tab-list"] {
    background: #09111f !important;
    border-bottom: 1px solid #151c2e !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    letter-spacing: 0.08em !important;
    color: #445577 !important;
    background: transparent !important;
    border-bottom: 2px solid transparent !important;
    padding: 8px 20px !important;
}
.stTabs [aria-selected="true"] {
    color: #44aaff !important;
    border-bottom: 2px solid #44aaff !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: #09111f !important;
    border: 1px solid #151c2e !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
    padding: 1rem !important;
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#  LENIS SMOOTH SCROLL
# ═══════════════════════════════════════════════════════
st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
<script>
(function() {
    function initLenis() {
        var scrollEl = document.querySelector('.main') ||
                       document.querySelector('[data-testid="stAppViewContainer"]') ||
                       document.documentElement;
        var lenis = new Lenis({
            wrapper: scrollEl, content: scrollEl,
            duration: 1.4,
            easing: function(t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
            direction: 'vertical', smoothWheel: true,
            wheelMultiplier: 0.9, touchMultiplier: 1.8, infinite: false,
        });
        function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
        requestAnimationFrame(raf);
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLenis);
    } else { setTimeout(initLenis, 500); }
})();
</script>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
#  ISA CONFIG
# ═══════════════════════════════════════════════════════
OPCODES = {
    'add': 0,  'sub': 1,  'mul': 2,  'div': 3,  'mod': 4,
    'cmp': 5,  'and': 6,  'or': 7,   'not': 8,  'mov': 9,
    'lsl': 10, 'lsr': 11, 'asr': 12, 'nop': 13, 'ld': 14,
    'st': 15,  'beq': 16, 'bgt': 17, 'b': 18,   'call': 19, 'ret': 20,
}

MODIFIER_BITS = { '': 0b00, 'u': 0b01, 'h': 0b10 }

def split_modifier(op):
    if op.endswith('u') and op[:-1] in OPCODES: return op[:-1], 'u'
    if op.endswith('h') and op[:-1] in OPCODES: return op[:-1], 'h'
    return op, ''

REGISTERS = {f"r{i}": i for i in range(16)}
REGISTERS['sp'] = 14
REGISTERS['ra'] = 15

ISA_TABLE = {
    "Mnemonic": ["add","addu","addh","sub","subu","subh","mul","div","mod",
                 "cmp","and","or","not","mov","movu","movh",
                 "lsl","lsr","asr","nop","ld","st","beq","bgt","b","call","ret"],
    "Opcode":   ["00000","00000","00000","00001","00001","00001","00010","00011","00100",
                 "00101","00110","00111","01000","01001","01001","01001",
                 "01010","01011","01100","01101","01110","01111",
                 "10000","10001","10010","10011","10100"],
    "Type":     ["ALU","ALU","ALU","ALU","ALU","ALU","ALU","ALU","ALU",
                 "CMP","ALU","ALU","ALU","MOV","MOV","MOV",
                 "SHIFT","SHIFT","SHIFT","NOP","MEM","MEM","BR","BR","BR","BR","BR"],
    "imm[17:16]":["00","01","10","00","01","10","00","00","00",
                  "00","00","00","00","00","01","10",
                  "00","00","00","—","—","—","—","—","—","—","—"],
    "Syntax":   ["add rd,rs1,rs2/imm","addu rd,rs1,imm","addh rd,rs1,imm",
                 "sub rd,rs1,rs2/imm","subu rd,rs1,imm","subh rd,rs1,imm",
                 "mul rd,rs1,rs2/imm","div rd,rs1,rs2/imm","mod rd,rs1,rs2/imm",
                 "cmp rs1,rs2/imm","and rd,rs1,rs2/imm","or rd,rs1,rs2/imm",
                 "not rd,rs2/imm",
                 "mov rd,imm (signed)","movu rd,imm (unsigned)","movh rd,imm (<<16)",
                 "lsl rd,rs1,rs2/imm","lsr rd,rs1,rs2/imm","asr rd,rs1,rs2/imm",
                 "nop","ld rd,imm[rs1]","st rd,imm[rs1]",
                 "beq label","bgt label","b label","call label","ret"],
}

EXAMPLES = {
    "── Pick an example ──": "",
    "Basic ALU": """\
// Basic ALU operations
mov r1, 5        // r1 = 5
mov r2, 10       // r2 = 10
add r3, r1, r2   // r3 = r1 + r2  = 15
sub r4, r2, r1   // r4 = r2 - r1  = 5
mul r5, r1, r2   // r5 = r1 * r2  = 50
nop""",

    "Loop (sum 1..5)": """\
// Loop: r3 = 1+2+3+4+5 = 15
mov r1, 1        // counter = 1
mov r2, 5        // limit = 5
mov r3, 0        // sum = 0
loop: add r3, r3, r1
add r1, r1, 1
cmp r1, r2
bgt end
b loop
end: nop""",

    "Load / Store": """\
// Memory access example
mov r1, 0xAB     // r1 = 171
st  r1, 0[r0]    // mem[0] = r1
ld  r2, 0[r0]    // r2 = mem[0]
cmp r1, r2
beq same
b done
same: mov r3, 1
done: nop""",

    "Branch & Compare": """\
// Compare and branch
mov r1, 10
mov r2, 20
cmp r1, r2
beq equal
bgt greater
b less
equal:   mov r3, 0
b done
greater: mov r3, 1
b done
less:    mov r3, -1
done: nop""",

    "Function Call": """\
// Function call / return
mov r1, 7
mov r2, 3
call add_func
b end
add_func: add r3, r1, r2
ret
end: nop""",

    "Shift Operations": """\
// Shift examples
mov r1, 0b00001111  // r1 = 15
lsl r2, r1, 2       // r2 = r1 << 2 = 60
lsr r3, r1, 1       // r3 = r1 >> 1 = 7
asr r4, r1, 1       // r4 = arithmetic r1 >> 1
nop""",

    "Modifiers (u/h)": """\
// Modifier example: Load r1 with 0xC3D5A1B2
// movh  imm[17:16] = 10  (left shift 16)
// addu  imm[17:16] = 01  (unsigned)
// mov   imm[17:16] = 00  (signed, default)
movh r1, 0xC3D5     // r1 = 0xC3D50000
addu r1, r1, 0xA1B2 // r1 = 0xC3D5A1B2
mov  r2, 0xA1B2     // signed sign-extended
movu r3, 0xA1B2     // unsigned zero-extended
nop""",
}


# ═══════════════════════════════════════════════════════
#  CORE ASSEMBLER
# ═══════════════════════════════════════════════════════
def parse_reg(s):
    return REGISTERS.get(s.strip().lower(), 0)

def parse_imm(s):
    orig = s
    s = s.strip()
    neg = False
    if s.startswith('-'):
        neg = True
        s = s[1:].strip()
    try:
        if s.lower().startswith('0x'):
            val = int(s, 16)
        elif s.lower().startswith('0b'):
            val = int(s, 2)
        elif s.startswith('#'):
            val = int(s[1:], 16)
        elif re.fullmatch(r'\d+', s):
            val = int(s, 10)
        elif re.fullmatch(r'[0-9a-fA-F]+', s) and re.search(r'[a-fA-F]', s):
            val = int(s, 16)
        else:
            val = int(s, 10)
    except ValueError:
        raise ValueError(f"Invalid immediate: '{orig}'")
    return -val if neg else val

def assemble(src):
    lines  = src.split('\n')
    labels = {}
    insts  = []
    addr   = 0

    for raw in lines:
        line = raw.split('//')[0].strip()
        if not line:
            continue
        if ':' in line:
            idx = line.index(':')
            labels[line[:idx].strip()] = addr
            line = line[idx+1:].strip()
            if not line:
                continue
        insts.append((addr, line))
        addr += 4

    results = []
    errors  = []

    for pc, inst in insts:
        parts  = [p for p in re.split(r'[\s,]+', inst) if p]
        raw_op = parts[0].lower()
        base_op, modifier = split_modifier(raw_op)

        if base_op not in OPCODES:
            errors.append(f"PC 0x{pc:04X}  Unknown opcode: '{raw_op}'")
            continue

        op  = base_op
        opc = OPCODES[op]
        enc = 0
        try:
            if op in ('nop', 'ret'):
                enc = opc << 27

            elif op in ('b', 'beq', 'bgt', 'call'):
                lbl    = parts[1]
                offset = ((labels[lbl] - pc) // 4) if lbl in labels else parse_imm(lbl)
                enc    = (opc << 27) | (offset & 0x7FFFFFF)

            elif op in ('ld', 'st'):
                rd  = parse_reg(parts[1])
                m   = re.match(r'(-?\w+)\[(\w+)\]', parts[2])
                imm = parse_imm(m.group(1)) if m else 0
                rs1 = parse_reg(m.group(2)) if m else 0
                enc = (opc << 27) | (1 << 26) | (rd << 22) | (rs1 << 18) | (imm & 0x3FFFF)

            else:
                if op in ('mov', 'not'):
                    rd, rs1, op2 = parse_reg(parts[1]), 0, parts[2]
                elif op == 'cmp':
                    rd, rs1, op2 = 0, parse_reg(parts[1]), parts[2]
                else:
                    rd, rs1, op2 = parse_reg(parts[1]), parse_reg(parts[2]), parts[3]

                if op2.lower() in REGISTERS:
                    enc = (opc << 27) | (parse_reg(op2) << 14) | (rd << 22) | (rs1 << 18)
                else:
                    imm_val  = parse_imm(op2)
                    mod_bits = MODIFIER_BITS.get(modifier, 0b00)
                    imm18    = (mod_bits << 16) | (imm_val & 0xFFFF)
                    enc      = (opc << 27) | (1 << 26) | (rd << 22) | (rs1 << 18) | imm18

        except Exception as e:
            errors.append(f"PC 0x{pc:04X}  Syntax error in '{inst}': {e}")
            continue

        enc  &= 0xFFFFFFFF
        b     = f"{enc:032b}"
        b_fmt = f"{b[0:5]} {b[5]} {b[6:10]} {b[10:14]} {b[14:]}"

        results.append({
            "PC":            f"0x{pc:04X}",
            "PC_dec":        pc,
            "Binary":        b_fmt,
            "opcode[31:27]": b[0:5],
            "I[26]":         b[5],
            "rd[25:22]":     b[6:10],
            "rs1[21:18]":    b[10:14],
            "imm/rs2[17:0]": b[14:],
            "Instruction":   inst.strip(),
        })

    return results, errors



# ═══════════════════════════════════════════════════════
#  MAIN HEADER
# ═══════════════════════════════════════════════════════
st.markdown(
    '<h1 style="font-family:Unbounded,sans-serif;font-size:2.6rem;font-weight:900;'
    'background:linear-gradient(90deg,#3af 0%,#88f 50%,#3fa 100%);'
    '-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
    'background-clip:text;margin-bottom:0">SimpleRISC Assembler</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<p style="font-family:Space Mono,monospace;color:#2a3f60;font-size:14px;'
    'letter-spacing:0.1em;margin-top:4px">ASSEMBLY  →  32-BIT MACHINE CODE  ·  BINARY + PC ADDRESS</p>',
    unsafe_allow_html=True
)
st.markdown("---")


# ═══════════════════════════════════════════════════════
#  LAYOUT: EDITOR  |  OUTPUT
# ═══════════════════════════════════════════════════════
editor_col, output_col = st.columns([1, 1], gap="large")

# ── LEFT: EDITOR ──────────────────────────────────────
with editor_col:
    st.markdown(
        '<p style="font-family:Space Mono,monospace;font-size:13px;color:#3af;'
        'letter-spacing:0.15em;text-transform:uppercase;margin-bottom:6px">▶ Assembly Input</p>',
        unsafe_allow_html=True
    )

    default_code = """\
// SimpleRISC Assembler — Write your code

mov r1, 5
mov r2, 10
add r3, r1, r2
sub r4, r2, r1
nop"""

    if "code_cache" not in st.session_state:
        st.session_state["code_cache"] = default_code
    if "editor_key" not in st.session_state:
        st.session_state["editor_key"] = 0

    # ── Example dropdown — main page ──
    ex = st.selectbox(
        "Load Example",
        list(EXAMPLES.keys()),
        key="example_select",
        label_visibility="collapsed",
    )

    if ex != "── Pick an example ──":
        new_val = EXAMPLES.get(ex, "")
        if new_val and new_val != st.session_state.get("last_ex_loaded", ""):
            st.session_state["code_cache"] = new_val
            st.session_state["last_ex_loaded"] = new_val
            st.session_state["editor_key"] += 1

    b1, b2 = st.columns([2, 1])
    with b1:
        run   = st.button("⚙  Assemble", use_container_width=True)
    with b2:
        clear = st.button("✕  Clear", use_container_width=True)

    if clear:
        st.session_state["code_cache"] = ""
        st.session_state["last_ex_loaded"] = ""
        st.session_state["asm_result"] = []
        st.session_state["asm_errors"] = []
        st.session_state["editor_key"] += 1
        st.rerun()

    code = st.text_area(
        "",
        value=st.session_state["code_cache"],
        height=400,
        label_visibility="collapsed",
        key=f"asm_editor_{st.session_state['editor_key']}",
        placeholder="// Assembly code yahan likhein...",
    )
    st.session_state["code_cache"] = code

# ── RIGHT: OUTPUT ──────────────────────────────────────
with output_col:
    st.markdown(
        '<p style="font-family:Space Mono,monospace;font-size:13px;color:#8f6;'
        'letter-spacing:0.15em;text-transform:uppercase;margin-bottom:6px">◉ Machine Code Output</p>',
        unsafe_allow_html=True
    )

    if run:
        src = code.strip()
        if src:
            res, errs = assemble(src)
            st.session_state["asm_result"] = res
            st.session_state["asm_errors"] = errs
        else:
            st.session_state["asm_result"] = []
            st.session_state["asm_errors"] = ["Pehle code likho!"]

    res  = st.session_state.get("asm_result", [])
    errs = st.session_state.get("asm_errors", [])

    if errs:
        for e in errs:
            st.error(f"❌  {e}")

    if res:
        n         = len(res)
        nb        = n * 4
        imm_count = sum(1 for r in res if r["I[26]"] == "1")
        reg_count = sum(1 for r in res if r["I[26]"] == "0")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Instructions", n)
        m2.metric("Bytes", nb)
        m3.metric("Imm Ops", imm_count)
        m4.metric("Reg Ops", reg_count)

        st.markdown("<br>", unsafe_allow_html=True)

        tab_main, tab_fields, tab_raw = st.tabs([
            "  Full Table  ", "  Field Breakdown  ", "  Raw Output  "
        ])

        with tab_main:
            df_main = pd.DataFrame([{
                "PC":          r["PC"],
                "Binary":      r["Binary"],
                "Instruction": r["Instruction"],
            } for r in res])
            st.dataframe(
                df_main,
                use_container_width=True,
                hide_index=True,
                height=min(40 * n + 50, 520),
                column_config={
                    "PC":          st.column_config.TextColumn("PC (Hex)", width=100),
                    "Binary":      st.column_config.TextColumn("Binary  (opc · I · rd · rs1 · imm)", width=270),
                    "Instruction": st.column_config.TextColumn("Instruction", width=210),
                }
            )

        with tab_fields:
            df_fields = pd.DataFrame([{
                "PC":            r["PC"],
                "opcode[31:27]": r["opcode[31:27]"],
                "I[26]":         r["I[26]"],
                "rd[25:22]":     r["rd[25:22]"],
                "rs1[21:18]":    r["rs1[21:18]"],
                "imm/rs2[17:0]": r["imm/rs2[17:0]"],
                "Instruction":   r["Instruction"],
            } for r in res])
            st.dataframe(
                df_fields,
                use_container_width=True,
                hide_index=True,
                height=min(40 * n + 50, 520),
            )

        with tab_raw:
            raw_lines = "\n".join(
                f"{r['PC']}  {r['Binary']}  // {r['Instruction']}"
                for r in res
            )
            st.code(raw_lines, language="text")

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Download (.txt only) ──
        txt_data  = "PC (Hex)  | Binary                              | Instruction\n"
        txt_data += "-" * 78 + "\n"
        for r in res:
            txt_data += f"{r['PC']:<10}| {r['Binary']:<37}| {r['Instruction']}\n"

        st.download_button(
            "⬇  Download Output (.txt)",
            data=txt_data,
            file_name="machine_code.txt",
            mime="text/plain",
            use_container_width=True,
        )

    elif not errs:
        st.markdown(
            '<div style="height:220px;display:flex;align-items:center;'
            'justify-content:center;border:1px dashed #151c2e;border-radius:8px;">'
            '<p style="font-family:Space Mono,monospace;font-size:14px;color:#1e2d45;">'
            '// Assemble dabao → output yahan aayega</p></div>',
            unsafe_allow_html=True
        )


# ═══════════════════════════════════════════════════════
#  BOTTOM SECTION
# ═══════════════════════════════════════════════════════
st.markdown("---")

col_isa, col_fmt = st.columns([1, 1], gap="large")

with col_isa:
    with st.expander("📖  Full ISA Reference — 27 Mnemonics"):
        df_isa = pd.DataFrame(ISA_TABLE)
        st.dataframe(
            df_isa,
            use_container_width=True,
            hide_index=True,
            height=480,
            column_config={
                "Mnemonic":   st.column_config.TextColumn("Mnemonic",      width=90),
                "Opcode":     st.column_config.TextColumn("Opcode (5-bit)", width=110),
                "Type":       st.column_config.TextColumn("Type",           width=70),
                "imm[17:16]": st.column_config.TextColumn("imm[17:16]",    width=90),
                "Syntax":     st.column_config.TextColumn("Syntax",         width=240),
            }
        )

with col_fmt:
    with st.expander("ℹ️  Instruction Format Legend"):
        st.markdown("""
**32-bit Instruction Layout:**

```
[31:27] opcode   — 5 bits
[26]    I-bit    — 1 = immediate,  0 = register
[25:22] rd       — destination register  (4 bits)
[21:18] rs1      — source register 1     (4 bits)
[17:0]  imm/rs2  — immediate (18 bits)  OR  rs2 (4 bits)
```

**Immediate modifier bits imm[17:16]:**
```
00  →  signed,   sign-extended  (default)
01  →  unsigned, zero-extended  (u suffix)
10  →  left shift by 16         (h suffix)
```

**Branch Format:**
```
[31:27] opcode | [26:0] offset (27 bits, PC-relative)
offset = (target_addr - current_pc) / 4
```

**Registers:**
- `r0 – r13`  general purpose
- `r14 = sp`  stack pointer
- `r15 = ra`  return address
        """)

st.markdown(
    '<p style="text-align:center;font-family:Space Mono,monospace;font-size:11px;'
    'color:#111c2e;letter-spacing:0.15em;margin-top:2rem">'
    'SIMPLERISC ASSEMBLER  ·  32-BIT RISC ARCHITECTURE</p>',
    unsafe_allow_html=True
)
