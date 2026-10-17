import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="SIM SCM Ayam Geprek Papua", page_icon="🍗", layout="wide")

st.title("🍗 SIM SCM Ayam Geprek Papua")
st.caption("Sistem Rantai Pasok Otomatis - Tugas 3 SIM F&B")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard FEFO", "🧮 BOM & Auto-PO", "📲 Telegram Alert"])

# Data Stok & Resep
inventory = {
    "Daging Ayam Segar": {"stock": 4.0, "unit": "kg", "buffer": 5.0, "exp": "2026-10-17"},
    "Tepung Crispy": {"stock": 10.0, "unit": "kg", "buffer": 2.0, "exp": "2026-11-15"},
    "Cabai & Bumbu": {"stock": 0.8, "unit": "kg", "buffer": 1.0, "exp": "2026-10-18"},
    "Minyak Goreng": {"stock": 12.0, "unit": "L", "buffer": 5.0, "exp": "2026-12-01"}
}

with tab1:
    st.header("📊 Status Stok & FEFO (D-2 Expired)")
    df = pd.DataFrame.from_dict(inventory, orient="index")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.header("🧮 Kalkulator BOM Explosion")
    porsi = st.number_input("Target Porsi Ayam Geprek:", min_value=10, value=100)
    
    data_po = []
    recipe = {"Daging Ayam Segar": 0.2, "Tepung Crispy": 0.05, "Cabai & Bumbu": 0.03, "Minyak Goreng": 0.025}
    
    for item, qty in recipe.items():
        gross = porsi * qty
        curr = inventory[item]["stock"]
        buff = inventory[item]["buffer"]
        net = max(0.0, gross + buff - curr)
        data_po.append({"Bahan": item, "Gross Needed": gross, "Stok": curr, "Auto-PO (Net)": net})
        
    st.dataframe(pd.DataFrame(data_po), use_container_width=True)

with tab3:
    st.header("📲 Simulasi Alert Telegram")
    st.code("[ALERT SCM] Stok Daging Ayam Segar KRITIS (4.0 kg < Buffer 5.0 kg). Rekomendasi Auto-PO: 21.0 kg.", language="markdown")
