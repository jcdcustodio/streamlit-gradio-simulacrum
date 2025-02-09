import streamlit as st
import numpy as np

def compute_capacity(b, h, fc, fy, Ag, As, P_u, M_u, V_u):
    # Compute Axial Capacity
    phi = 0.65  # Strength reduction factor for axial load
    P_n = 0.85 * fc * (Ag - As) + As * fy
    P_capacity = (phi * P_n) / 1000
    axial_ratio = P_u / P_capacity
    
    # Compute Flexural Capacity (Simplified Assumption)
    phi_flexure = 0.90
    Mn = As * fy * (h - 0.1 * h)  # Assumed lever arm 0.9d
    M_capacity = (phi_flexure * Mn) / (1000 ** 2)
    flexural_ratio = M_u / M_capacity
    
    # Compute Shear Capacity (Simplified Assumption)
    phi_shear = 0.75
    Vc = (0.17 * np.sqrt(fc) * b * h) / 1000  # Simplified shear strength of concrete
    V_capacity = phi_shear * Vc
    shear_ratio = V_u / V_capacity
    
    return axial_ratio, flexural_ratio, shear_ratio, P_capacity, M_capacity, V_capacity

st.title("Concrete Column Design (ACI 318-19, Metric)")

# User Inputs
b = st.number_input("Column Width (mm)", min_value=100, value=300)
h = st.number_input("Column Height (mm)", min_value=100, value=500)
fc = st.number_input("Concrete Strength f'c (MPa)", min_value=10.0, value=30.0)
fy = st.number_input("Steel Yield Strength (MPa)", min_value=200.0, value=420.0)
As = st.number_input("Total Steel Area As (mm²)", min_value=0.0, value=2000.0)
Ag = b * h  # Gross area of concrete section
P_u = st.number_input("Factored Axial Load Pu (kN)", min_value=0.0, value=1000.0)
M_u = st.number_input("Factored Moment Mu (kN-m)", min_value=0.0, value=50.0)
V_u = st.number_input("Factored Shear Vu (kN)", min_value=0.0, value=100.0)

if st.button("Compute Demand/Capacity Ratios"):
    axial_ratio, flexural_ratio, shear_ratio, P_cap, M_cap, V_cap = compute_capacity(b, h, fc, fy, Ag, As, P_u, M_u, V_u)
    
    st.subheader("Results")
    st.write(f"**Axial Demand/Capacity Ratio:** {axial_ratio:.2f}")
    st.write(f"**Flexural Demand/Capacity Ratio:** {flexural_ratio:.2f}")
    st.write(f"**Shear Demand/Capacity Ratio:** {shear_ratio:.2f}")
    
    st.subheader("Detailed Calculations")
    st.write(f"Axial Capacity: {P_cap:.2f} kN")
    st.write(f"Flexural Capacity: {M_cap:.2f} kN-m")
    st.write(f"Shear Capacity: {V_cap:.2f} kN")