import streamlit as st

# Page Configuration with Wide Layout
st.set_page_config(
    page_title="Generator Maintenance Assistant By ASZ",
    page_icon="⚡",
    layout="wide"
)

# 50 Detailed Errors Master Knowledge Base (Strictly Categorized by Diesel & Petrol)
MASTER_KNOWLEDGE_BASE = {
    # --- DIESEL ENGINE ERRORS (25) ---
    "1. Diesel: Air Filter Choked (Dust Restriction)": {
        "type": "Diesel", "severity": "Low", "urgency": "Low",
        "causes": ["Heavy dust accumulation in intake paper filter element", "High ambient particulate matter blocking airflow"],
        "actions": ["Inspect air filter restriction indicator", "Clean element carefully with compressed air from inside out", "Check sealing gaskets"],
        "spares": ["Primary Air Filter Element", "Secondary Safety Element"]
    },
    "2. Diesel: Day Tank Low Fuel Level Warning": {
        "type": "Diesel", "severity": "Low", "urgency": "Low",
        "causes": ["Fuel transfer pump set in manual mode", "Float switch stuck in low position"],
        "actions": ["Check fuel transfer switch position", "Inspect and clean float level switch contacts", "Verify manual valves"],
        "spares": ["Tank Float Level Switch", "Transfer Pump Relay"]
    },
    "3. Diesel: Coolant Temperature Sensor Intermittent": {
        "type": "Diesel", "severity": "Low", "urgency": "Low",
        "causes": ["Loose sensor wiring plug connector", "Corrosion on sender terminal pins"],
        "actions": ["Unplug connector, clean with contact spray, and reseat firmly", "Verify sensor resistance against engine temperature"],
        "spares": ["Coolant Temp Sender Unit", "Contact Cleaner Spray"]
    },
    "4. Diesel: Alternator Low Charging Voltage": {
        "type": "Diesel", "severity": "Low", "urgency": "Medium",
        "causes": ["Loose alternator drive V-belt tension", "Internal diode rectifier fatigue"],
        "actions": ["Check belt deflection", "Measure DC voltage across alternator output terminals while running (should exceed 27.5V)"],
        "spares": ["Alternator Drive Belt", "Internal Rectifier Assembly"]
    },
    "5. Diesel: Water Separator Bowl Full": {
        "type": "Diesel", "severity": "Low", "urgency": "Medium",
        "causes": ["Moisture condensation inside bulk underground diesel storage tank"],
        "actions": ["Open drain valve at bottom of water separator bowl and drain water until clean diesel flows"],
        "spares": ["Water Separator Drain Valve", "Fuel Pre-filter Assembly"]
    },
    "6. Diesel: Exhaust Manifold Minor Soot Leak": {
        "type": "Diesel", "severity": "Medium", "urgency": "Medium",
        "causes": ["Thermal expansion loosening exhaust stud nuts", "Aged graphite composite gasket"],
        "actions": ["Retorque exhaust manifold mounting nuts in star pattern", "Replace graphite gasket during next shutdown"],
        "spares": ["Graphite Exhaust Gasket", "Manifold Stud Nuts"]
    },
    "7. Diesel: Governor Speed Potentiometer Drift": {
        "type": "Diesel", "severity": "Medium", "urgency": "Medium",
        "causes": ["Vibration causing multi-turn potentiometer setpoint shift"],
        "actions": ["Recalibrate idle and rated speed on governor module", "Lock potentiometer nut with threadlocker"],
        "spares": ["Speed Potentiometer Unit", "Threadlocker Adhesive"]
    },
    "8. Diesel: Rocker Cover Gasket Oil Seepage": {
        "type": "Diesel", "severity": "Medium", "urgency": "Low",
        "causes": ["Rubber gasket hardening due to high heat cycles", "Uneven bolt torque"],
        "actions": ["Clean leaked oil area", "Retorque valve cover bolts evenly", "Replace rubber seal during major service"],
        "spares": ["Valve Cover Rubber Gasket Set"]
    },
    "9. Diesel: Cooling Fan Belt Squeal": {
        "type": "Diesel", "severity": "Medium", "urgency": "Medium",
        "causes": ["Stretched fan drive belts", "Oil or coolant splashed onto pulleys"],
        "actions": ["Degrease pulleys using solvent spray", "Adjust spring-loaded tensioner to proper deflection"],
        "spares": ["Matched Fan Belt Set", "Pulley Cleaner Spray"]
    },
    "10. Diesel: Fuel Lift Pump Internal Passing": {
        "type": "Diesel", "severity": "Medium", "urgency": "Medium",
        "causes": ["Debris stuck under mechanical/electric lift pump non-return valve"],
        "actions": ["Clean lift pump inlet banjo fitting and internal strainer screen", "Test delivery pressure (0.3 - 0.6 bar)"],
        "spares": ["Fuel Lift Pump Assembly", "Banjo Sealing Washers"]
    },
    "11. Diesel: Control Panel HMI Display Flickering": {
        "type": "Diesel", "severity": "Medium", "urgency": "Low",
        "causes": ["Control module internal power supply capacitor aging", "Loose 24V supply wire"],
        "actions": ["Check 24VDC incoming power stability", "Tighten terminal block screws inside control cabinet"],
        "spares": ["24VDC Industrial Power Supply", "Terminal Block Strip"]
    },
    "12. Diesel: Crankcase Breather Dripping Oil": {
        "type": "Diesel", "severity": "Medium", "urgency": "Low",
        "causes": ["Normal accumulation of oil vapor blow-by", "Blocked internal mesh trap in breather canister"],
        "actions": ["Inspect breather drain tube", "Clean internal mesh filter inside crankcase breather assembly"],
        "spares": ["Breather Filter Element", "Drain Tubing"]
    },
    "13. Diesel: Radiator Core External Fin Choking": {
        "type": "Diesel", "severity": "Medium", "urgency": "Medium",
        "causes": ["Industrial dust, cotton lint, or insect buildup blocking airflow"],
        "actions": ["Blow compressed air from fan side outwards, followed by low-pressure warm water wash with coil cleaner"],
        "spares": ["Industrial Fin Comb Tool", "Radiator Cleaner Chemical"]
    },
    "14. Diesel: Block Heater Thermostat Failure": {
        "type": "Diesel", "severity": "Medium", "urgency": "Low",
        "causes": ["Block heater thermostat stuck", "Air pocket trapped inside heater chamber"],
        "actions": ["Bleed cooling air pocket from heater hose", "Test thermostat switching continuity at 40°C"],
        "spares": ["Block Heater Thermostat Switch", "Immersion Heater"]
    },
    "15. Diesel: CT Secondary Wiring Loose Connection": {
        "type": "Diesel", "severity": "High", "urgency": "High",
        "causes": ["Vibration shaking loose CT secondary terminal screws"],
        "actions": ["⚠️ CRITICAL SAFETY: Never open CT secondary circuit while loaded! Shut down generator before tightening CT terminals."],
        "spares": ["CT Terminal Lug Connectors", "Heat Shrink Tubing"]
    },
    "16. Diesel: Injection Pump Delivery Valve Seepage": {
        "type": "Diesel", "severity": "High", "urgency": "High",
        "causes": ["O-ring degradation under fuel pump delivery valve holder"],
        "actions": ["Isolate rail pressure, clean area, replace high-pressure delivery valve copper seal and O-ring"],
        "spares": ["Delivery Valve O-Ring Kit", "Copper Sealing Washer Set"]
    },
    "17. Diesel: Turbocharger Wastegate Linkage Stuck": {
        "type": "Diesel", "severity": "High", "urgency": "High",
        "causes": ["Carbon soot accumulation freezing wastegate butterfly spindle"],
        "actions": ["Spray penetrating oil on wastegate shaft hinge, manually free linkage motion"],
        "spares": ["Turbocharger Wastegate Actuator", "Penetrating Lubricant"]
    },
    "18. Diesel: Alternator Bearing Spalling Noise": {
        "type": "Diesel", "severity": "High", "urgency": "High",
        "causes": ["Over-greasing or under-greasing bearing housing during maintenance"],
        "actions": ["Listen with stethoscope", "Inject exact calculated quantity of high-temp polyurea grease"],
        "spares": ["Deep Groove Ball Bearing", "High-Temp Polyurea Grease"]
    },
    "19. Diesel: MPU Sensor Air Gap Misalignment": {
        "type": "Diesel", "severity": "High", "urgency": "High",
        "causes": ["MPU sensor touching flywheel ring gear teeth due to loose lock nut"],
        "actions": ["Remove MPU sensor, wipe magnetic tip clean", "Screw in until touching ring gear, back off 3/4 turn (0.8mm gap) and lock"],
        "spares": ["Magnetic Pickup Sensor (MPU)", "Lock Nut"]
    },
    "20. Diesel: Fuel Return Line Restriction": {
        "type": "Diesel", "severity": "High", "urgency": "High",
        "causes": ["Kinked or swollen rubber fuel return hose"],
        "actions": ["Check fuel return line flow back to day tank", "Replace degraded rubber lines with reinforced tubing"],
        "spares": ["Diesel Fuel Return Hose", "Hose Clamp Set"]
    },
    "21. Diesel: Very Low Voltage / No Excitation": {
        "type": "Diesel", "severity": "Critical", "urgency": "Critical",
        "causes": ["Complete loss of alternator residual magnetism", "Blown AVR fast-acting fuse"],
        "actions": ["Flash alternator field using external 12V battery across F+ and F- for 2 seconds while running", "Check AVR fuse"],
        "spares": ["AVR Protection Fuse", "Rotating Diode Bridge", "Automatic Voltage Regulator"]
    },
    "22. Diesel: High Coolant Temperature Overheating": {
        "type": "Diesel", "severity": "Critical", "urgency": "Critical",
        "causes": ["Thermostat stuck closed", "Water pump impeller eroded", "Radiator core internal scaling"],
        "actions": ["Test thermostat in boiling water", "Inspect water pump internal ceramic seal", "Perform acid descaling flush"],
        "spares": ["Engine Thermostat Valve", "Water Pump Repair Kit", "Coolant Concentrate"]
    },
    "23. Diesel: Low Lube Oil Pressure Trip": {
        "type": "Diesel", "severity": "Critical", "urgency": "Critical",
        "causes": ["Worn main crankshaft bearings", "Oil suction strainer fully choked with carbon/sludge"],
        "actions": ["Check oil pressure with mechanical master gauge", "Drop oil pan, inspect suction pickup screen and bearing clearance"],
        "spares": ["Main & Big-End Bearing Set", "Oil Pump Gear", "Suction Strainer"]
    },
    "24. Diesel: Engine Overspeed Trip (Runaway)": {
        "type": "Diesel", "severity": "Critical", "urgency": "Critical",
        "causes": ["Fuel injection pump rack stuck in full-fuel position", "Turbocharger oil seal failure feeding engine lube oil"],
        "actions": ["Check manual emergency air intake flap/guillotine shutoff valve", "Inspect turbocharger for oil leakage"],
        "spares": ["Emergency Air Shutoff Flap", "Electronic Governor Controller", "Turbocharger Cartridge"]
    },
    "25. Diesel: Common Rail High Pressure Pump Seizure": {
        "type": "Diesel", "severity": "Critical", "urgency": "Critical",
        "causes": ["Water or microscopic cat-fines in high pressure diesel fuel passing through HP pump"],
        "actions": ["Replace complete high pressure fuel pump, rail, and all injectors due to metal debris contamination", "Flush fuel tank"],
        "spares": ["Common Rail High Pressure Pump", "High Pressure Fuel Injectors", "Fuel Rail Assembly"]
    },

    # --- PETROL / GASOLINE ENGINE ERRORS (25) ---
    "26. Petrol: Spark Plug Fouled / Carbon Deposit": {
        "type": "Petrol", "severity": "Low", "urgency": "Low",
        "causes": ["Rich air-fuel mixture or excessive oil burning past valve guides"],
        "actions": ["Remove spark plugs, clean carbon soot with wire brush, check gap (0.7-0.8mm)", "Replace if electrode is worn"],
        "spares": ["Spark Plug Set", "Spark Plug Gapping Tool"]
    },
    "27. Petrol: Carburetor Main Jet Minor Choke": {
        "type": "Petrol", "severity": "Low", "urgency": "Medium",
        "causes": ["Stale petrol gum and varnish deposits inside carburetor float bowl"],
        "actions": ["Drain carburetor float bowl, spray carburetor cleaner into jets, blow compressed air through passages"],
        "spares": ["Carb Repair Kit (Gaskets/Jets)", "Carb Cleaner Spray"]
    },
    "28. Petrol: Automatic Choke Valve Sticking": {
        "type": "Petrol", "severity": "Low", "urgency": "Medium",
        "causes": ["Thermostatic spring or linkage gummed up with old fuel residue"],
        "actions": ["Clean automatic choke linkage with solvent, lubricate pivot points with light machine oil"],
        "spares": ["Choke Thermostatic Spring", "Carb Linkage Pin"]
    },
    "29. Petrol: Fuel Tank Cap Air Vent Blocked": {
        "type": "Petrol", "severity": "Low", "urgency": "Low",
        "causes": ["Dirt blocking small breather hole in petrol tank cap, creating vacuum lock"],
        "actions": ["Clear vent hole in fuel cap with fine needle, test fuel flow to carburetor"],
        "spares": ["Petrol Tank Cap Assembly"]
    },
    "30. Petrol: Pull-Starter Recoil Cord Fraying": {
        "type": "Petrol", "severity": "Low", "urgency": "Low",
        "causes": ["Friction against starter housing eyelet during aggressive pulling"],
        "actions": ["Inspect recoil starter rope, unwind and replace frayed nylon cord before it snaps inside housing"],
        "spares": ["Nylon Starter Rope", "Recoil Spring Assembly"]
    },
    "31. Petrol: Ignition Coil Resistance High / Weak Spark": {
        "type": "Petrol", "severity": "Medium", "urgency": "Medium",
        "causes": ["Thermal breakdown of ignition coil winding insulation"],
        "actions": ["Test ignition coil primary and secondary resistance with multimeter against specs", "Replace coil if spark is weak yellow"],
        "spares": ["Solid State Ignition Coil Module", "Spark Plug Cap"]
    },
    "32. Petrol: Low Idle Engine Speed / Stalling on Load": {
        "type": "Petrol", "severity": "Medium", "urgency": "Medium",
        "causes": ["Idle mixture screw out of adjustment", "Throttle stop screw loose"],
        "actions": ["Adjust idle speed screw until engine idles smoothly at 1500-1800 RPM", "Check governor linkage spring tension"],
        "spares": ["Governor Spring Set", "Idle Mixture Screw"]
    },
    "33. Petrol: Fuel Sediment Cup Filter Sludge": {
        "type": "Petrol", "severity": "Medium", "urgency": "Low",
        "causes": ["Rust and sediment from unlined steel petrol tank settling in glass sediment bowl"],
        "actions": ["Shut off fuel valve, unscrew sediment bowl, wash mesh screen in clean petrol, replace O-ring"],
        "spares": ["Sediment Bowl Mesh Filter", "Rubber Bowl O-Ring"]
    },
    "34. Petrol: Crankcase Oil Dilution by Petrol": {
        "type": "Petrol", "severity": "Medium", "urgency": "High",
        "causes": ["Carburetor float needle valve passing fuel when engine stopped, leaking petrol into crankcase"],
        "actions": ["Check engine oil level (if oil smells of petrol and level is high, drain immediately)", "Repair carburetor float needle valve"],
        "spares": ["Carburetor Float & Needle Valve", "Engine Oil (SAE 10W30/15W40)"]
    },
    "35. Petrol: Exhaust Muffler Spark Arrester Choked": {
        "type": "Petrol", "severity": "Medium", "urgency": "Medium",
        "causes": ["Carbon soot accumulation on internal spark arrester wire mesh screen"],
        "actions": ["Remove muffler end cap, pull out spark arrester screen, burn off carbon with torch or wire brush"],
        "spares": ["Spark Arrester Screen", "Muffler Gasket"]
    },
    "36. Petrol: Inverter Module Overload / Fault Light ON": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["Connecting appliance exceeding inverter generator peak watt rating", "Internal inverter circuit board short"],
        "actions": ["Reset inverter overload circuit breaker", "Disconnect heavy loads, check sine wave inverter board for burnt transistors"],
        "spares": ["Inverter Control PCB", "Overload Reset Switch"]
    },
    "37. Petrol: Flywheel Permanent Magnet Demagnetization": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["External heat source or physical impact weakening flywheel neodymium/alnico magnets"],
        "actions": ["Check spark voltage and generator AC output", "Replace flywheel rotor if magnetic field strength is insufficient"],
        "spares": ["Flywheel Magnet Rotor Assembly", "Woodruff Key"]
    },
    "38. Petrol: Governor Arm Spring Fatigue / Stretching": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["Mechanical governor spring losing tension over extended operating hours"],
        "actions": ["Check governor arm linkage play and spring tension", "Replace stretched governor spring to restore frequency stability under load"],
        "spares": ["Governor Control Spring Set", "Linkage Rod Clip"]
    },
    "39. Petrol: Intake Manifold Vacuum Leak (O-Ring Hardening)": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["Phenolic spacer insulator O-ring between carburetor and cylinder head cracked, causing lean mixture surge"],
        "actions": ["Spray starter fluid around carburetor flange while idling; if RPM surges, replace intake insulator O-rings"],
        "spares": ["Carb Insulator O-Ring Kit", "Phenolic Spacer Plate"]
    },
    "40. Petrol: Recoil Starter Pawl / Ratchet Breakage": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["Forceful pulling breaking starter cup metal pawl or return spring"],
        "actions": ["Remove recoil starter assembly, inspect internal plastic/metal dog pawls and return spring"],
        "spares": ["Recoil Starter Assembly", "Starter Dog Pawl Kit"]
    },
    "41. Petrol: Low Compression Due to Exhaust Valve Burnout": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Running with tight valve clearance, causing exhaust valve to remain slightly open and burn seat"],
        "actions": ["Perform cylinder compression test", "Remove cylinder head, lap or replace burnt exhaust valve and reset valve lash (0.15mm)"],
        "spares": ["Exhaust Valve & Guide", "Cylinder Head Gasket", "Valve Spring"]
    },
    "42. Petrol: Ignition Timing Advance Key Sheared": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Sudden kickback or overload shearing flywheel Woodruff key, throwing ignition timing off"],
        "actions": ["Remove flywheel nut and flywheel puller, inspect Woodruff key slot, replace sheared half-moon key and torque nut to spec"],
        "spares": ["Flywheel Woodruff Key", "Flywheel Nut"]
    },
    "43. Petrol: Crankshaft Connecting Rod Bearing Seizure": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Running air-cooled petrol generator with low engine oil or no oil (triggering low oil alert failure)"],
        "actions": ["Engine locked solid; dismantle crankcase, replace connecting rod, grind or replace crankshaft journal"],
        "spares": ["Connecting Rod Assembly", "Crankshaft", "Oil Alert Switch"]
    },
    "44. Petrol: Automatic Voltage Regulator (AVR) Burnt": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Short circuit in generator power output receptacle or lightning surge"],
        "actions": ["Inspect round or square AVR module inside alternator rear cover for charred resin and burnt diodes", "Replace AVR"],
        "spares": ["Generator AVR (Brushless Type)", "Carbon Brushes"]
    },
    "45. Petrol: Low Oil Alert Sensor False Tripping": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Low oil sensor float stuck in open position even with full oil, killing ignition spark"],
        "actions": ["Check engine oil dipstick level first", "Disconnect low oil sensor wire temporarily to test if engine starts; replace faulty sensor switch"],
        "spares": ["Low Oil Level Sensor Switch", "Crankcase Gasket"]
    },
    "46. Petrol: Fuel Shutoff Solenoid (Electric) Failure": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["Carburetor fuel solenoid plunger stuck closed due to gummed fuel, preventing fuel entry"],
        "actions": ["Check 12V power supply to carburetor fuel solenoid on key ON", "Clean plunger pin or replace solenoid valve"],
        "spares": ["Carb Fuel Shutoff Solenoid Valve"]
    },
    "47. Petrol: Stator Winding Insulation Breakdown": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Generator stored in damp outdoor rainy environment without running, absorbing moisture in copper windings"],
        "actions": ["Measure winding insulation resistance with megger tester (<1 Megaohm is unsafe)", "Bake/dry windings using heat gun"],
        "spares": ["Insulation Varnish Spray", "Stator Winding Assembly"]
    },
    "48. Petrol: Fuel Tank Internal Rust Flakes Choking Petcock": {
        "type": "Petrol", "severity": "High", "urgency": "High",
        "causes": ["Unlined metal petrol tank rusting internally, sending flakes down to fuel valve screen"],
        "actions": ["Remove fuel tank petcock valve, clean internal strainer finger screen, flush tank with rust remover solution"],
        "spares": ["Fuel Tank Petcock Valve", "Tank Seal Ring"]
    },
    "49. Petrol: Cylinder Head Warpage Causing Compression Blow": {
        "type": "Petrol", "severity": "Critical", "urgency": "Critical",
        "causes": ["Severe overheating from running low on oil or overloaded in extreme ambient heat"],
        "actions": ["Check cylinder head mating surface with feeler gauge and straight edge against surface plate", "Resurface or replace head"],
        "spares": ["Cylinder Head Casting", "Head Gasket", "Valve Cover Gasket"]
    },
    "50. Petrol: Starting Recoil Spring Uncoiled / Broken": {
        "type": "Petrol", "severity": "Medium", "urgency": "Medium",
        "causes": ["Pulling starter rope past maximum limit or letting snap back violently"],
        "actions": ["Carefully rewind or replace broken recoil flat spring inside starter pulley reel (wear safety glasses)"],
        "spares": ["Recoil Starter Flat Spring", "Starter Reel Pulley"]
    }
}

# App Header
st.title("⚡ Generator Maintenance Assistant By ASZ")
st.markdown("### Expert Generator Diagnostics & Troubleshooting Platform")

# Sidebar Inputs
st.sidebar.header("Generator Specifications")

# 1. STEP 1: User Selects Engine Fuel Type FIRST
engine_category = st.sidebar.selectbox("1. Select Engine Fuel Type", ["Diesel Engine", "Petrol / Gasoline Engine"])

# 2. STEP 2: Dynamically filter Brands based on fuel type selection
if engine_category == "Diesel Engine":
    companies = [
        "Perkins", "Cummins", "Caterpillar", "Volvo Penta", "MTU", 
        "Mitsubishi", "Doosan", "JCB", "Yanmar", "Ford", "Mercedes"
    ]
else:
    companies = [
        "Honda", "Yamaha", "Briggs & Stratton", "Kohler", "Generac", 
        "Champion", "Predator", "Loncin", "Hyundai", "Kawasaki"
    ]

selected_company = st.sidebar.selectbox("2. Select Engine Brand / Company", companies)

# 3. Control System / CC Selection
control_panels = [
    "DSE 3500", "DSE 2000", "DSE 7320", "DSE 4520", 
    "ComAp InteliLite", "Woodward easYgen", "DEIF AGC 150", 
    "SmartGen HGM", "OEM Analog Control Panel", "Manual Key Switch"
]
selected_cc = st.sidebar.selectbox("3. Select Control System (CC)", control_panels)

# 4. Capacity Selection in kVA / kW
capacity_kva = st.sidebar.slider("4. Select Generator Capacity (kVA)", min_value=1, max_value=3000, value=500, step=10)
capacity_kw = int(capacity_kva * 0.8)
st.sidebar.info(f"Rated Active Power: **{capacity_kw} kW** (PF 0.8)")

st.sidebar.markdown("---")
st.sidebar.header("Fault & Operating Parameters")

# Filter errors dynamically based on user's primary choice (Diesel vs Petrol)
filtered_errors = {k: v for k, v in MASTER_KNOWLEDGE_BASE.items() if v["type"] in engine_category}
error_list = list(filtered_errors.keys())

selected_error = st.sidebar.selectbox("5. Select Observed Fault / Error", error_list)

operating_hours = st.sidebar.number_input("Generator Running Hours", min_value=0, max_value=75000, value=2500, step=100)

# Financial & Downtime Settings
st.sidebar.markdown("---")
st.sidebar.header("Financial & Outage Impact")
hourly_outage_loss = st.sidebar.number_input("Power Failure Loss ($ per Hour)", min_value=0, value=1000, step=100)
estimated_repair_hours = st.sidebar.slider("Estimated Repair Hours", min_value=1, max_value=72, value=4)

run_diagnosis = st.sidebar.button("Run ASZ Diagnostic Analysis")

if run_diagnosis:
    with st.spinner("Running diagnostic evaluation and calculating financial impact..."):
        fault_data = filtered_errors[selected_error]
        
        risk_level = "Normal"
        if operating_hours > 6000 and fault_data["severity"] in ["High", "Critical"]:
            risk_level = "High Operational Risk (Extended Operating Hours)"
            
        total_outage_loss = hourly_outage_loss * estimated_repair_hours
        
        # Layout Columns
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📊 Generator Asset Summary")
            st.metric(label="Engine Fuel Category", value=engine_category)
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
            st.subheader("🔍 Expert Root Cause Analysis")
            for idx, cause in enumerate(fault_data["causes"], 1):
                st.write(f"{idx}. {cause}")
                
            st.subheader("🛠️ Step-by-Step Corrective Action Plan")
            for idx, action in enumerate(fault_data["actions"], 1):
                st.success(f"Step {idx}: {action}")
                
            st.subheader("📦 Required Spare Parts & Consumables")
            for spare in fault_data["spares"]:
                st.markdown(f"- 🔧 **{spare}**")
            
else:
    st.info("👈 Please configure your generator specifications and fault selection in the sidebar, then click **'Run ASZ Diagnostic Analysis'**.")
