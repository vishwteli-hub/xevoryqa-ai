import html
from pathlib import Path

import streamlit as st

from detector import analyze_message
from ai_explainer import explain_message


# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="XEVORYQA AI | Message Security",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "xevoryqa_logo.png"
PERFORMANCE_IMAGE = BASE_DIR / "model_performance.png"


# =====================================================
# PREMIUM RESPONSIVE DESIGN
# =====================================================
st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');

:root {
    --bg: #080b10;
    --surface: #101720;
    --surface-2: #141e29;
    --line: rgba(166, 190, 177, .15);
    --lime: #baff52;
    --lime-soft: rgba(186, 255, 82, .10);
    --text: #f4f7f3;
    --muted: #98a6a2;
    --red: #ff7777;
    --amber: #ffc16c;
}

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp {
    color: var(--text);
    background:
      radial-gradient(ellipse at 12% 0%, rgba(91, 145, 72, .16), transparent 34%),
      radial-gradient(ellipse at 90% 12%, rgba(62, 105, 120, .13), transparent 32%),
      var(--bg);
}
.block-container { max-width: 1180px; padding: 1.5rem 2rem 3.5rem; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* Brand header */
.brandbar {
  display:flex; align-items:center; justify-content:space-between; gap:18px;
  padding: 8px 0 20px; border-bottom:1px solid var(--line); margin-bottom:42px;
}
.brand-word { font-size:19px; font-weight:800; letter-spacing:2px; color:var(--text); }
.brand-word span { color:var(--lime); }
.brand-caption { color:var(--muted); font:10px 'Space Mono',monospace; letter-spacing:1.6px; text-align:right; }
.status-pill {
 display:inline-flex; align-items:center; gap:8px; padding:8px 12px; border:1px solid var(--line);
 border-radius:999px; background:rgba(255,255,255,.025); color:#c7d2ca;
 font:10px 'Space Mono',monospace; letter-spacing:1px;
}
.status-dot { width:7px; height:7px; border-radius:50%; background:var(--lime); box-shadow:0 0 12px var(--lime); }

/* Hero */
.hero-wrap { padding: 12px 0 20px; }
.eyebrow { display:inline-flex; gap:8px; align-items:center; color:var(--lime); background:var(--lime-soft);
 border:1px solid rgba(186,255,82,.22); border-radius:999px; padding:8px 13px;
 font:10px 'Space Mono',monospace; letter-spacing:1.2px; }
.hero-title { color:var(--text); font-size:clamp(40px,6.5vw,72px); line-height:1.02; letter-spacing:-3.5px;
 font-weight:800; margin:22px 0 15px; }
.hero-title span { color:var(--lime); }
.hero-copy { max-width:600px; color:var(--muted); font-size:16px; line-height:1.8; }
.hero-side {
 background:linear-gradient(145deg, rgba(24,36,43,.92), rgba(12,18,25,.94));
 border:1px solid var(--line); border-radius:22px; padding:24px; min-height:235px;
 box-shadow:0 24px 70px rgba(0,0,0,.22); position:relative; overflow:hidden;
}
.hero-side:after { content:''; position:absolute; width:190px; height:190px; border:1px solid rgba(186,255,82,.13);
 border-radius:50%; right:-60px; top:-75px; box-shadow:0 0 0 22px rgba(186,255,82,.025),0 0 0 46px rgba(186,255,82,.02); }
.hero-side-label { color:var(--muted); font:10px 'Space Mono',monospace; letter-spacing:1.4px; }
.hero-side-title { font-size:23px; font-weight:700; margin:20px 0 8px; }
.hero-side-copy { color:var(--muted); font-size:13px; line-height:1.7; max-width:280px; }
.hero-side-line { margin-top:24px; display:flex; align-items:center; gap:9px; color:#d7e3d8; font-size:11px; }
.hero-side-line b { color:var(--lime); font-weight:600; }

/* Shared sections */
.section-kicker { color:var(--lime); font:10px 'Space Mono',monospace; letter-spacing:1.5px; margin-bottom:8px; }
.section-title { color:var(--text); font-size:25px; font-weight:750; letter-spacing:-.8px; margin:0 0 6px; }
.section-copy { color:var(--muted); font-size:13px; margin-bottom:20px; line-height:1.7; }
.feature-strip { display:flex; flex-wrap:wrap; gap:10px; margin:26px 0 54px; }
.feature-chip { border:1px solid var(--line); background:rgba(255,255,255,.025); color:#c8d3cc;
 padding:9px 12px; border-radius:9px; font-size:11px; }
.feature-chip span { color:var(--lime); margin-right:6px; }

/* Input panel */
div[data-testid="stForm"] {
 background:linear-gradient(145deg, rgba(21,31,39,.98), rgba(13,19,26,.98));
 border:1px solid var(--line); border-radius:18px; padding:22px; margin:0 0 10px;
 box-shadow:0 18px 55px rgba(0,0,0,.18);
}
.stTextArea textarea { background:#0a1016 !important; color:var(--text) !important;
 border:1px solid #34434a !important; border-radius:12px !important;
 font-family:'DM Sans',sans-serif !important; font-size:14px !important; line-height:1.7 !important; padding:14px !important; }
.stTextArea textarea:focus { border-color:var(--lime) !important; box-shadow:0 0 0 1px var(--lime) !important; }
.stTextArea label { color:#c3cec7 !important; font-size:12px !important; }
.stFormSubmitButton button {
 background:var(--lime) !important; color:#10170b !important; border:0 !important; border-radius:10px !important;
 min-height:49px !important; font-weight:800 !important; letter-spacing:.5px !important; transition:.2s ease !important;
}
.stFormSubmitButton button:hover { background:#d0ff8a !important; transform:translateY(-1px); }
.stButton button { background:#141e27 !important; color:#dce6df !important; border:1px solid var(--line) !important;
 border-radius:10px !important; min-height:42px !important; font-size:12px !important; }
.stButton button:hover { border-color:var(--lime) !important; color:var(--lime) !important; }

/* Results */
.result-panel { border:1px solid var(--line); border-radius:18px; padding:25px; margin:18px 0 15px;
 background:linear-gradient(135deg, rgba(23,34,41,.98), rgba(12,18,24,.98)); }
.result-label { color:var(--muted); font:10px 'Space Mono',monospace; letter-spacing:1.5px; }
.result-risk { font-size:clamp(30px,5vw,43px); font-weight:800; letter-spacing:-1.5px; margin:10px 0 4px; }
.risk-high { color:var(--red); } .risk-medium { color:var(--amber); } .risk-low { color:var(--lime); }
.result-note { color:var(--muted); font-size:12px; line-height:1.6; }
.warning-item { display:inline-block; background:rgba(255,193,108,.08); border:1px solid rgba(255,193,108,.24);
 color:var(--amber); padding:9px 12px; margin:4px 5px 4px 0; border-radius:9px; font-size:11px; }
.ai-panel { background:#101a20; border:1px solid rgba(186,255,82,.18); border-radius:15px; padding:18px 20px; margin:12px 0; }
.ai-label { color:var(--lime); font:10px 'Space Mono',monospace; letter-spacing:1.4px; }
div[data-testid="stMetric"] { background:rgba(18,28,35,.9); border:1px solid var(--line); padding:15px; border-radius:13px; }
div[data-testid="stMetricLabel"] { color:var(--muted); }
div[data-testid="stMetricValue"] { color:var(--lime); }
div[data-testid="stExpander"] { background:rgba(16,24,30,.88); border:1px solid var(--line); border-radius:12px; }
[data-testid="stAlert"] { border-radius:12px; }

/* Footer */
.footer { border-top:1px solid var(--line); margin-top:55px; padding-top:22px; display:flex; flex-wrap:wrap;
 justify-content:space-between; gap:12px; color:var(--muted); font-size:11px; }
.footer strong { color:var(--lime); letter-spacing:1px; }
.small-note { color:var(--muted); font-size:11px; line-height:1.7; }

@media(max-width:760px) {
 .block-container { padding:1rem 1rem 2.5rem; }
 .brandbar { margin-bottom:28px; }
 .brand-word { font-size:15px; }
 .brand-caption { font-size:8px; }
 .hero-title { font-size:clamp(38px,11vw,58px); letter-spacing:-2.2px; }
 .hero-copy { font-size:14px; }
 .feature-strip { margin:22px 0 38px; gap:7px; }
 .feature-chip { font-size:10px; }
 div[data-testid="stForm"] { padding:14px; }
 .result-panel { padding:19px; }
 .section-title { font-size:22px; }
}
</style>
""")


def render_html(content: str) -> None:
    """Render authored HTML through Streamlit's HTML component."""
    st.html(content)


def clear_analysis() -> None:
    for key in ("analysis_result", "analysis_message", "analysis_explanation"):
        st.session_state.pop(key, None)


# =====================================================
# HEADER + HERO
# =====================================================
header_left, header_right = st.columns([1.2, 1], vertical_alignment="center")
with header_left:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=215)
    else:
        st.markdown("### ⚡ XEVORYQA AI")
with header_right:
    render_html("""
    <div style="text-align:right">
      <span class="status-pill"><i class="status-dot"></i> MESSAGE SECURITY</span>
    </div>
    """)

hero_left, hero_right = st.columns([1.25, .85], gap="large", vertical_alignment="center")
with hero_left:
    render_html("""
    <div class="hero-wrap">
      <div class="eyebrow">✦ &nbsp; SMARTER DIGITAL SAFETY</div>
      <div class="hero-title">PAUSE.<br>CHECK.<br><span>THEN CLICK.</span></div>
      <div class="hero-copy">
        Suspicious SMS? Unexpected offer? Strange link? Examine the message,
        spot possible warning signs and get a clearer idea of what to do next.
      </div>
    </div>
    """)
with hero_right:
    render_html("""
    <div class="hero-side">
      <div class="hero-side-label">YOUR DIGITAL SAFETY ASSISTANT</div>
      <div class="hero-side-title">A second look<br>before you act.</div>
      <div class="hero-side-copy">Combine message classification, warning-sign checks and an AI-generated explanation.</div>
      <div class="hero-side-line"><b>01</b> &nbsp; Examine the message</div>
      <div class="hero-side-line"><b>02</b> &nbsp; Understand possible risks</div>
      <div class="hero-side-line"><b>03</b> &nbsp; Choose a safer next step</div>
    </div>
    """)

render_html("""
<div class="feature-strip">
  <div class="feature-chip"><span>✦</span> Machine-learning scan</div>
  <div class="feature-chip"><span>✦</span> Suspicious-pattern checks</div>
  <div class="feature-chip"><span>✦</span> Plain-English AI explanation</div>
</div>
""")


# =====================================================
# MESSAGE SCANNER
# =====================================================
render_html("""
<div class="section-kicker">THE MESSAGE CHECK</div>
<div class="section-title">What did you receive?</div>
<div class="section-copy">Paste the text below. You can try one of the sample messages first.</div>
""")

example1, example2, example3 = st.columns(3)
with example1:
    if st.button("🎁  Prize message", use_container_width=True):
        clear_analysis()
        st.session_state["message_input"] = (
            "Congratulations! You have won Rs. 50,000. "
            "Click this link to claim your prize immediately."
        )
with example2:
    if st.button("🏦  Bank alert", use_container_width=True):
        clear_analysis()
        st.session_state["message_input"] = (
            "Your bank account will be blocked today. "
            "Verify your account details immediately."
        )
with example3:
    if st.button("📦  Delivery update", use_container_width=True):
        clear_analysis()
        st.session_state["message_input"] = (
            "Your package has been delivered. Thank you for shopping with us."
        )

render_html('<div class="section-kicker" style="margin:20px 0 10px">✦ &nbsp; MESSAGE SCANNER</div>')
with st.form("xevoryqa_message_form", clear_on_submit=False):
    message = st.text_area(
        "Your message",
        placeholder="Paste an SMS, WhatsApp message, email text or suspicious message here...",
        height=165,
        key="message_input",
    )
    submitted = st.form_submit_button("⚡  ANALYSE MESSAGE", use_container_width=True)

st.markdown(
    '<div class="small-note">🔒 For your safety, do not paste real OTPs, passwords, card numbers, banking details or other confidential information.</div>',
    unsafe_allow_html=True,
)


# =====================================================
# ANALYSIS
# =====================================================
if submitted:
    if not message or not message.strip():
        clear_analysis()
        st.warning("Please paste a message before starting the scan.")
    else:
        try:
            with st.spinner("Examining the message and preparing your report..."):
                result = analyze_message(message)
                explanation = explain_message(
                    message,
                    result["prediction"],
                    result["spam_probability"],
                    result["indicators"],
                    result["risk_level"],
                )
            st.session_state.analysis_result = result
            st.session_state.analysis_message = message
            st.session_state.analysis_explanation = explanation
        except Exception as exc:
            st.error("We couldn't complete the analysis. Please try again.")
            st.caption(f"Technical detail: {type(exc).__name__}")


# =====================================================
# RESULTS
# =====================================================
if "analysis_result" in st.session_state:
    result = st.session_state.analysis_result
    risk = result["risk_level"]
    probability = result["spam_probability"]
    explanation = st.session_state.analysis_explanation

    risk_class = {
        "High Risk": "risk-high",
        "Potential Risk": "risk-medium",
        "Low Risk": "risk-low",
    }.get(risk, "risk-medium")

    st.markdown("---")
    render_html("""
    <div class="section-kicker">SCAN COMPLETE</div>
    <div class="section-title">Your security report</div>
    <div class="section-copy">Here are the signals found in the message you submitted.</div>
    """)

    render_html(f"""
    <div class="result-panel">
      <div class="result-label">OVERALL MESSAGE ASSESSMENT</div>
      <div class="result-risk {risk_class}">{html.escape(str(risk).upper())}</div>
      <div class="result-note">This is an initial automated risk assessment, not definitive proof that a message is fraudulent or safe.</div>
    </div>
    """)

    metric1, metric2, metric3 = st.columns(3)
    with metric1:
        st.metric("Estimated spam probability", f"{probability:.1%}")
    with metric2:
        prediction_label = "Spam" if result["prediction"] == "spam" else "Legitimate"
        st.metric("Model classification", prediction_label)
    with metric3:
        st.metric("Warning signs detected", len(result["indicators"]))

    st.caption("The spam probability is the model's estimate, not a guaranteed measure of scam risk.")

    render_html('<div class="section-title" style="margin-top:28px">Warning signs found</div>')
    if result["indicators"]:
        warning_html = "".join(
            f'<span class="warning-item">⚠ &nbsp;{html.escape(str(item))}</span>'
            for item in result["indicators"]
        )
        render_html(warning_html)
    else:
        st.info("The current pattern checks did not detect any of their listed warning signs. This does not guarantee that the message is safe.")

    render_html("""
    <div class="section-title" style="margin-top:30px">AI explanation</div>
    <div class="section-copy">A plain-English explanation of the possible risks and what to look out for.</div>
    <div class="ai-panel"><div class="ai-label">✦ &nbsp; XEVORYQA AI INSIGHT</div></div>
    """)
    st.markdown(explanation)

    render_html('<div class="section-title" style="margin-top:28px">Safer next steps</div>')
    if risk in ("High Risk", "Potential Risk"):
        st.warning(
            "Do not click suspicious links or reply with personal information. "
            "Never share OTPs, passwords or banking PINs. Verify the sender using an official channel."
        )
    else:
        st.info(
            "No major warning was triggered by the current checks. Still, verify unexpected requests independently "
            "and never share confidential information."
        )

    with st.expander("View the message you checked"):
        st.code(st.session_state.analysis_message, language=None)


# =====================================================
# ABOUT + TRANSPARENCY
# =====================================================
st.markdown("---")
render_html("""
<div class="section-kicker">ABOUT THE PROJECT</div>
<div class="section-title">Built to make digital messages easier to question.</div>
<div class="section-copy">XEVORYQA AI combines a machine-learning spam classifier, rule-based warning-sign checks and an AI-generated explanation to help people assess suspicious messages.</div>
""")

about1, about2 = st.columns(2, gap="large")
with about1:
    with st.expander("How does XEVORYQA AI work?"):
        st.markdown(
            "**1. Machine learning**\n\n"
            "A trained text-classification model estimates whether a message resembles spam.\n\n"
            "**2. Warning-sign checks**\n\n"
            "Pattern checks look for urgency, requests for sensitive information, prize claims and links.\n\n"
            "**3. AI explanation**\n\n"
            "Gemini generates a readable explanation and practical safety suggestions."
        )
with about2:
    with st.expander("Model evaluation and limitations"):
        st.metric("Held-out dataset accuracy", "97.67%")
        st.write("Measured on a held-out portion of the UCI SMS Spam Collection dataset.")
        if PERFORMANCE_IMAGE.exists():
            st.image(str(PERFORMANCE_IMAGE), use_container_width=True)
        st.info(
            "This dataset result is not a guarantee of real-world scam detection accuracy. "
            "The model can make mistakes, and a low-risk result does not prove a message is safe."
        )

render_html("""
<div class="footer">
  <div><strong>XEVORYQA AI</strong><br><span>THINK BEFORE YOU CLICK.</span></div>
  <div>AI + MACHINE LEARNING</div>
  <div>MADE FOR A SAFER DIGITAL WORLD</div>
</div>
""")
st.caption("XEVORYQA AI provides an initial automated assessment. It cannot guarantee that a message is safe or fraudulent.")
