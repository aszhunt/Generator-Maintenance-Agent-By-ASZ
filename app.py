import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Generator Maintenance Assistant By ASZ",
    page_icon="⚡",
    layout="wide"
)

# Expert Master Knowledge Base (30+ Comprehensive Diesel Generator Errors - Low to High Severity)
DG_EXPERT_KNOWLEDGE = {
    "1. Air Filter Dust Restriction (Early Stage)": {
        "severity": "Low",
        "urgency": "Low",
        "causes": ["Dust accumulation on primary paper filter element in dusty industrial environment", "Premature choking due to high ambient particulate matter"],
        "actions": ["Inspect air filter restriction indicator on housing", "Remove primary filter element and clean gently with compressed air from inside out", "Check sealing gaskets to prevent unfiltered air bypass"],
        "spares": ["Primary Air Filter Element", "Secondary Safety Air Element"]
    },
    "2. Day Tank Fuel Level Low Warning": {
        "severity": "Low",
        "urgency": "Low",
        "causes": ["Fuel transfer pump set in manual mode instead of auto", "Float switch sticking in low position"],
        "actions": ["Check fuel transfer pump control panel switch position", "Inspect and clean day tank float level switch contacts", "Verify manual fuel transfer valve alignment"],
        "spares": ["Tank Float Level Switch", "Fuel Transfer Pump Relay"]
    },
    "3. Coolant Temperature Sensor Signal Drift / Intermittent": {
        "severity": "Low",
        "urgency": "Low",
        "causes": ["Loose sensor wiring connector plug", "Corrosion on sender terminal pin"],
        "actions": ["Unplug coolant temperature sensor connector, clean with contact spray, and reseat firmly", "Verify resistance reading across sensor pins against ambient engine temp"],
        "spares": ["Coolant Temperature Sender Unit", "Electrical Contact Cleaner Spray"]
    },
    "4. Battery Charging Alternator Low Voltage Output": {
        "severity": "Low",
        "urgency": "Medium",
        "causes": ["Loose alternator drive belt tension", "Internal diode rectifier fatigue"],
        "actions": ["Check V-belt deflection and tensioning bolts", "Measure DC voltage directly across alternator output terminals while engine runs (should exceed 27.5V for 24V system)"],
        "spares": ["Alternator Drive Belt", "Internal Rectifier Diode Assembly"]
    },
    "5. Fuel Water Separator Bowl High Water Level": {
        "severity": "Low",
        "urgency": "Medium",
        "causes": ["Condensation accumulation inside bulk underground diesel storage tank", "High humidity weather forming water in primary filter"],
        "actions": ["Open drain valve at bottom of water separator bowl and drain water into container until clean diesel flows", "Check bulk fuel storage quality"],
        "spares": ["Water Separator Drain Valve", "Fuel Pre-filter Assembly"]
    },
    "6. Exhaust Manifold Gaint Joint Minor Soot Leak": {
        "severity": "Low",
        "urgency": "Medium",
        "causes": ["Thermal expansion loosening exhaust stud nuts", "Aged graphite composite gasket"],
        "actions": ["Retorque exhaust manifold mounting nuts to manufacturer spec in star pattern", "Replace affected graphite gasket during next scheduled shutdown"],
        "spares": ["Graphite Exhaust Gasket", "High-Tensile Manifold Stud Nuts"]
    },
    "7. Electronic Governor Speed Potentiometer Drift": {
        "severity": "Medium",
        "urgency": "Medium",
        "causes": ["Vibration causing multi-turn potentiometer setpoint shift", "Internal dust inside controller casing"],
        "actions": ["Re-calibrate idle and rated speed potentiometer on electronic governor module", "Lock potentiometer locking nut with threadlocker"],
        "spares": ["Speed Control Potentiometer Unit", "Threadlocker Adhesive"]
    },
    "8. Minor Oil Seepage from Rocker Arm Valve Cover Gasket": {
        "severity": "Medium",
        "urgency": "Low",
        "causes": ["Cork/rubber gasket hardening due to high engine heat cycles", "Uneven bolt torque"],
        "actions": ["Clean leaked oil area with solvent", "Retorque valve cover bolts evenly", "Replace rubber seal during major service"],
        "spares": ["Valve Cover Rubber Gasket Set", "Sealing Washer"]
    },
    "9. Cooling Fan V-Belt Squeal / Slip on Startup": {
        "severity": "Medium",
        "urgency": "Medium",
        "causes": ["Stretched fan drive belts", "Oil or coolant splashed onto pulley sheaves"],
        "actions": ["Degrease pulleys using solvent spray", "Adjust spring-loaded or mechanical belt tensioner to proper deflection specification"],
        "spares": ["Matched Fan Belt Set", "Pulley Sheave Cleaner"]
    },
    "10. Fuel Lift Pump Internal Valve Passing": {
        "severity": "Medium",
        "urgency": "Medium",
        "causes": ["Debris stuck under mechanical or electric lift pump non-return valve", "Weak internal check spring"],
        "actions": ["Clean lift pump inlet banjo fitting and internal strainer screen", "Test fuel delivery pressure (should be 0.3 to 0.6 bar minimum)"],
        "spares": ["Fuel Lift Pump Assembly", "Banjo Sealing Washers"]
    },
    "11. Control Panel HMI Screen Backlight Dim / Flickering": {
        "severity": "Medium",
        "urgency": "Low",
        "causes": ["Control module internal power supply capacitor aging", "Loose 24V supply wire in control cabinet terminal strip"],
        "actions": ["Check 24VDC incoming power stability with oscilloscope/multimeter", "Tighten terminal block screws inside generator control panel"],
        "spares": ["24VDC Industrial Power Supply Unit", "Terminal Block Strip"]
    },
    "12. Crankcase Breather Tube Dripping Oil Condensate": {
        "severity": "Medium",
        "urgency": "Low",
        "causes": ["Normal accumulation of oil vapor blow-by in heavy duty cycle", "Blocked internal mesh trap in breather canister"],
        "actions": ["Inspect breather drain tube position into catch bottle", "Clean internal mesh filter inside crankcase breather assembly"],
        "spares": ["Breather Filter Element", "Drain Tubing"]
    },
    "13. Radiator Core External Fin Choking": {
        "severity": "Medium",
        "urgency": "Medium",
        "causes": ["Industrial dust, cotton lint, or insect buildup blocking airflow across radiator fins"],
        "actions": ["Blow compressed air from engine fan side outwards, followed by low-pressure warm water wash with commercial coil cleaner"],
        "spares": ["Industrial Fin Comb Tool", "Aluminium Radiator Cleaner Chemical"]
    },
    "14. Jacket Water Heater Thermostat Cycling Failure": {
        "severity": "Medium",
        "urgency": "Low",
        "causes": ["Block heater thermostat stuck in open/closed position", "Air pocket trapped inside heater chamber"],
        "actions": ["Bleed cooling air pocket from heater hose", "Test thermostat switching continuity at preset temperature (40°C)"],
        "spares": ["Block Heater Thermostat Switch", "Immersion Heater Element"]
    },
    "15. Current Transformers (CT) Wiring Loose Connection": {
        "severity": "High",
        "urgency": "High",
        "causes": ["Vibration shaking loose CT secondary terminal screws", "High resistance causing inaccurate metering"],
        "actions": ["⚠️ CRITICAL SAFETY: Never open CT secondary circuit while generator is loaded! Shut down generator completely before tightening CT wiring terminals.", "Check all shorting blocks and meter wiring"],
        "spares": ["CT Terminal Lug Connectors", "Heat Shrink Tubing"]
    },
    "16. Fuel Injection Pump Delivery Valve Seepage": {
        "severity": "High",
        "urgency": "High",
        "causes": ["O-ring degradation under fuel pump delivery valve holder", "Cracked copper sealing washer"],
        "actions": ["Isolate fuel rail pressure, clean area, replace high-pressure delivery valve copper seal and O-ring on affected cylinder plunger"],
        "spares": ["Delivery Valve O-Ring Kit", "Copper Sealing Washer Set"]
    },
    "17. Turbocharger Wastegate Actuator Linkage Stuck": {
        "severity": "High",
        "urgency": "High",
        "causes": ["Carbon soot accumulation freezing wastegate butterfly spindle", "Corroded vacuum/pressure actuator diaphragm"],
        "actions": ["Spray penetrating oil on wastegate shaft hinge, manually free linkage motion", "Test actuator diaphragm pressure response with hand pump"],
        "spares": ["Turbocharger Wastegate Actuator", "Penetrating Lubricant Spray"]
    },
    "18. Alternator Bearing Dryness / Early Spalling Noise": {
        "severity": "High",
        "urgency": "High",
        "causes": ["Over-greasing or under-greasing bearing housing during routine maintenance", "Bearing fatigue from continuous vibration"],
        "actions": ["Listen to bearing housing with stethoscope", "Verify grease type compatibility (do not mix lithium and polyurea greases); inject exact calculated quantity of high-temp grease"],
        "spares": ["SKF/NSK Deep Groove Ball Bearing", "High-Temperature Polyurea Grease"]
    },
    "19. Magnetic Pickup Sensor (MPU) Air Gap Misalignment": {
        "severity": "High",
        "urgency": "High",
        "causes": ["MPU sensor touching flywheel ring gear teeth due to loose lock nut", "Accumulation of metallic iron wear particles on sensor tip"],
        "actions": ["Remove MPU sensor, wipe magnetic tip clean of metal shavings", "Screw in until touching ring gear lightly, then back off 3/4 turn (approx 0.8mm gap) and lock nut"],
        "spares": ["Magnetic Pickup Sensor (MPU)", "Lock Nut"]
    },
    "20. Fuel Return Line Restriction / Backpressure": {
        "severity": "High",
        "urgency": "High",
        "causes": ["Kinked or swollen rubber fuel return hose", "Internal check valve restriction in return manifold"],
        "actions": ["Check fuel return line flow back to day tank", "Replace degraded rubber lines with reinforced diesel-rated tubing"],
        "spares": ["Diesel Fuel Return Hose (Braided)", "Hose Clamp Set"]
    },
    "21. Control Panel 24VDC Power Supply Intermittent Dip": {
        "severity": "High",
        "urgency": "High",
        "causes": ["Failing rectifier inside battery charger unit", "Oxidized main DC supply fuse holder"],
        "actions": ["Measure DC bus ripple voltage", "Clean fuse holder contacts with sandpaper, apply dielectric grease, and replace weak DC power supply module"],
        "spares": ["Battery Charger Unit (24V 10A)", "Blade Fuse Assorted Kit"]
    },
    "22. Flexible Exhaust Bellows Rupture / Leak": {
        "severity": "High",
        "urgency": "High",
        "causes": ["Engine vibration fatigue exceeding stainless steel bellows flexibility limits", "Inadequate rigid exhaust pipe hanging support"],
        "actions": ["Check exhaust pipe counterweights and spring hangers", "Cut out damaged stainless steel exhaust expansion bellows and weld in new braided unit"],
        "spares": ["Stainless Steel Flexible Exhaust Bellows", "Exhaust Flange Gaskets"]
    },
    "23. Very Low Voltage / No Voltage Generation on Startup (Loss of Excitation)": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Complete loss of alternator residual magnetism", "Blown AVR fast-acting fuse", "Main rotating diode short circuit"],
        "actions": ["Flash alternator field using external 12V battery across F+ and F- terminals for 2 seconds while running", "Check AVR fuse and test rotating diodes"],
        "spares": ["AVR Protection Fuse", "Rotating Diode Bridge Kit", "Automatic Voltage Regulator (AVR)"]
    },
    "24. High Engine Coolant Temperature (Overheating Shutdown)": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Thermostat stuck closed", "Water pump impeller eroded/damaged", "Radiator core internal scaling", "Severe engine overload (>110%)"],
        "actions": ["Test thermostat in boiling water container", "Inspect water pump internal ceramic seal and impeller blades", "Perform acid descaling flush of cooling jacket"],
        "spares": ["Engine Thermostat Valve", "Water Pump Repair Kit", "Heavy-Duty Coolant Concentrate"]
    },
    "25. Low Lube Oil Pressure Trip (Critical Engine Protection)": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Worn main crankshaft bearings allowing oil pressure bypass", "Lube oil suction strainer fully choked with carbon/sludge", "Oil pump internal gear wear"],
        "actions": ["Check oil pressure with mechanical master gauge immediately", "Drop oil pan, inspect suction pickup screen, and check main bearing clearance with plastigage"],
        "spares": ["Main & Big-End Bearing Set", "Oil Pump Gear Assembly", "Engine Oil Suction Strainer"]
    },
    "26. Engine Overspeed Trip (Emergency Shutdown)": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Fuel injection pump rack stuck in full-fuel position", "Electronic governor controller failure sending runaway signal", "Turbocharger oil seal failure feeding engine lube oil into cylinders as uncontrolled fuel"],
        "actions": ["Check manual emergency air intake flap/guillotine shutoff valve", "Inspect governor actuator linkage freedom", "Check turbocharger for oil leakage into intake manifold"],
        "spares": ["Emergency Air Shutoff Flap Seal", "Electronic Governor Controller", "Turbocharger Cartridge"]
    },
    "27. Alternator Overvoltage / Undervoltage Trip": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["AVR sensing wires loose", "Faulty permanent magnet generator (PMG) excitation coil", "Sudden heavy load rejection causing voltage surge"],
        "actions": ["Verify AVR sensing wire tightness at terminal block", "Check PMG output AC voltage across phases", "Replace faulty AVR unit"],
        "spares": ["Automatic Voltage Regulator (AVR)", "PMG Stator Coil Assembly"]
    },
    "28. High Crankcase Blow-by Pressure (Ring Sticking / Liner Wear)": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Piston rings broken or stuck in grooves from overheating", "Scored cylinder liners from abrasive dust ingestion"],
        "actions": ["Perform blow-by flow meter test", "Remove cylinder heads and pull pistons to inspect ring gaps and liner walls; schedule major overhaul"],
        "spares": ["Cylinder Liner & Piston Kit", "Piston Ring Set", "Head Gasket Set"]
    },
    "29. Common Rail High Pressure Fuel Pump Internal Seizure": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Water or microscopic particulate (cat-fines) in high pressure diesel fuel passing through Bosch/Delphi HP pump", "Fuel starvation causing dry running"],
        "actions": ["Replace complete high pressure fuel pump, rail, and all injectors due to metal debris contamination", "Flush entire fuel tank and lines thoroughly"],
        "spares": ["Common Rail High Pressure Fuel Pump", "High Pressure Fuel Injectors", "Fuel Rail Assembly"]
    },
    "30. Flywheel Housing Alignment & Bell Housing Crack": {
        "severity": "Critical",
        "urgency": "Critical",
        "causes": ["Generator skid base twisting from uneven foundation settling", "Excessive torsional vibration resonance breaking bell housing bolts"],
        "actions": ["Check generator set alignment with dial indicator (radial & axial runout within 0.05mm)", "Inspect bell housing structural integrity and retorque foundation grouting"],
        "spares": ["Flywheel Housing Cast Iron Casting", "High-Tensile Mounting Bolts Set", "Base Vibration Isolator Pads"]
    }
}

# App Header
st.title("⚡ Generator Maintenance Assistant By ASZ")
st.markdown("### Expert Diesel Generator Diagnostics & Troubleshooting Platform (20+ Years Field Engineering Standards)")

# Sidebar Inputs
st.sidebar.header("Generator Specifications")

# 1. Engine Brand / Company Selection
companies = [
    "Perkins", "Cummins", "Caterpillar", "Volvo Penta", "MTU", 
    "Mitsubishi", "Doosan", "JCB", "Yanmar", "Kajeli", "Ford", "Mercedes", "Kanopi"
]
selected_company = st.sidebar.selectbox("Engine Brand / Company", companies)

# 2. Control System / CC Selection
control_panels = [
    "DSE 3500", "DSE 2000", "DSE 7320", "DSE 4520", 
    "ComAp InteliLite", "ComAp InteliGen", "Woodward easYgen", 
    "DEIF AGC 150", "SmartGen HGM", "OEM Analog Control Panel"
]
selected_cc = st.sidebar.selectbox("Control System / CC Model", control_panels)

# 3. Capacity Selection in kVA / kW
capacity_kva = st.sidebar.slider("Generator Capacity (kVA)", min_value=15, max_value=3000, value=500, step=10)
capacity_kw = int(capacity_kva * 0.8)
st.sidebar.info(f"Rated Active Power: **{capacity_kw} kW** (PF 0.8)")

st.sidebar.markdown("---")
st.sidebar.header("Fault & Operating Parameters")

# Comprehensive Errors List (Low to High)
error_list = list(DG_EXPERT_KNOWLEDGE.keys())
selected_error = st.sidebar.selectbox("Observed Generator Fault / Error", error_list)

operating_hours = st.sidebar.number_input("Generator Running Hours", min_value=0, max_value=75000, value=3500, step=100)

# Financial & Downtime Settings
st.sidebar.markdown("---")
st.sidebar.header("Financial & Outage Impact")
hourly_outage_loss = st.sidebar.number_input("Power Failure Loss ($ per Hour)", min_value=0, value=1200, step=100)
estimated_repair_hours = st.sidebar.slider("Estimated Repair Hours", min_value=1, max_value=72, value=4)

run_diagnosis = st.sidebar.button("Run ASZ Diagnostic Analysis")

if run_diagnosis:
    with st.spinner("Running 20-year expert diagnostic engine and calculating financial impact..."):
        fault_data = DG_EXPERT_KNOWLEDGE[selected_error]
        
        risk_level = "Normal"
        if operating_hours > 6000 and fault_data["severity"] in ["High", "Critical"]:
            risk_level = "High Operational Risk (Extended Operating Hours)"
            
        total_outage_loss = hourly_outage_loss * estimated_repair_hours
        
        # Layout Columns
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📊 Generator Asset Summary")
            st.metric(label="Engine Brand", value=selected_company)
            st.metric(label="Control System (CC)", value=selected_cc)
            st.metric(label="Capacity", value=f"{capacity_kva} kVA / {capacity_kw} kW")
            st.metric(label="Selected Fault", value=selected_error)
            
            # Severity / Urgency Alert Box with Color Coding
            urgency = fault_data["urgency"]
            severity = fault_data["severity"]
            
            if urgency == "Critical":
                st.error(f"🚨 SEVERITY: {severity} | URGENCY: {urgency} — IMMEDIATE SHUTDOWN REQUIRED!")
            elif urgency == "High":
                st.warning(f"⚠️ SEVERITY: {severity} | URGENCY: {urgency} — Immediate Intervention Needed!")
            elif urgency == "Medium":
                st.info(f"🟡 SEVERITY: {severity} | URGENCY: {urgency} — Schedule Inspection Soon.")
            else:
                st.success(f"🟢 SEVERITY: {severity} | URGENCY: {urgency} — Low Risk / Routine Maintenance.")
                
            st.write(f"**Engineering Risk Status:** {risk_level}")
            st.metric(label="Estimated Financial Impact (Downtime Loss)", value=f"${total_outage_loss:,} USD")

        with col2:
            st.subheader("🔍 Expert Root Cause Analysis (20 Yrs Experience)")
            for idx, cause in enumerate(fault_data["causes"], 1):
                st.write(f"{idx}. {cause}")
                
            st.subheader("🛠️ Step-by-Step Corrective Action Plan")
            for idx, action in enumerate(fault_data["actions"], 1):
                st.success(f"Step {idx}: {action}")
                
            st.subheader("📦 Required Spare Parts & Consumables")
            for spare in fault_data["spares"]:
                st.markdown(f"- 🔧 **{spare}**")
            
else:
    st.info("👈 Configure your generator specifications and fault selection in the sidebar, then click **'Run ASZ Diagnostic Analysis'**.")