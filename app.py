import streamlit as st
import plotly.graph_objects as go

# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(
    page_title="E-commerce Global BI Dashboard",
    layout="wide"
)

# =========================
# CSS VISUAL (STYLE BI)
# =========================
st.markdown("""
<style>
    .title {
        font-size: 34px;
        font-weight: 700;
        color: #002060;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 16px;
        color: #666;
        margin-bottom: 20px;
    }

    .kpi-box {
        background-color: #f5f7fb;
        padding: 18px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 1px 6px rgba(0,0,0,0.08);
    }

    .kpi-value {
        font-size: 26px;
        font-weight: 700;
        color: #002060;
    }

    .kpi-label {
        font-size: 14px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">E-commerce Global BI Dashboard 2025-2026</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Análise executiva da penetração do e-commerce no varejo global</div>', unsafe_allow_html=True)

# =========================
# DADOS
# =========================
paises = ['Brasil', 'EUA', 'Média Global', 'Reino Unido', 'China']
valores = [14, 18, 20, 33, 48]

# =========================
# FILTRO INTERATIVO
# =========================
pais_selecionado = st.selectbox(
    "Selecione um país para análise",
    paises
)

valor_selecionado = valores[paises.index(pais_selecionado)]

# =========================
# KPIs (DINÂMICOS)
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-value">{valor_selecionado}%</div>
        <div class="kpi-label">E-commerce em {pais_selecionado}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-value">20%</div>
        <div class="kpi-label">Média Global</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-value">48%</div>
        <div class="kpi-label">China (Líder)</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-value">14%</div>
        <div class="kpi-label">Brasil</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# GRÁFICO (DESTAQUE INTERATIVO)
# =========================
cores = []

for p in paises:
    if p == pais_selecionado:
        cores.append('#002060')  # destaque forte
    else:
        cores.append('#A6A6A6')  # neutro

fig = go.Figure(go.Bar(
    x=valores,
    y=paises,
    orientation='h',
    marker_color=cores,
    text=[f'{v}%' for v in valores],
    textposition='auto'
))

fig.update_layout(
    title="Penetração do E-commerce no Varejo Total",
    title_x=0.5,
    xaxis=dict(showgrid=False, showticklabels=False),
    yaxis=dict(autorange="reversed"),
    plot_bgcolor='rgba(0,0,0,0)',
    height=450,
    margin=dict(l=40, r=40, t=60, b=30)
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# INSIGHTS EXECUTIVOS
# =========================
st.markdown("### 🔎 Insights executivos")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
    • {pais_selecionado} possui {valor_selecionado}% de penetração  
    • Diferenças regionais ainda são significativas  
    • Mercado global segue em transição digital
    """)

with col2:
    st.warning("""
    • China lidera com modelo digital-first  
    • Ocidente segue modelo omnichannel  
    • Crescimento está ligado à eficiência operacional
    """)

# =========================
# FOOTER
# =========================
st.caption("Fontes: NielsenIQ (2026), RetailX, U.S. Census Bureau")