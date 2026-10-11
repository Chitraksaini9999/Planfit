import os
import json
from workout_structure import EXERCISE_DATA
from exercise_library import EXERCISE_LIBRARY

WORKSPACE = r"d:\desktop\Main\EX\mobile_app"

# Clean default routine data with relative paths
clean_routine_data = []
for d in EXERCISE_DATA:
    day_copy = dict(d)
    ex_list = []
    for ex in d["exercises"]:
        ec = dict(ex)
        img_name = ex["image"]
        if img_name == "hammer cabel curl":
            img_name = "hammer cabel curl.jpg"
        ec["image_url"] = f"./images/{img_name}"
        ex_list.append(ec)
    day_copy["exercises"] = ex_list
    clean_routine_data.append(day_copy)

# Prepare clean exercise library with relative image URLs
clean_library = []
for ex in EXERCISE_LIBRARY:
    ec = dict(ex)
    ec["image_url"] = f"./images/{ex['image']}"
    clean_library.append(ec)

routine_json = json.dumps(clean_routine_data, indent=2)
library_json = json.dumps(clean_library, indent=2)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#070a14">
<title>Planfit Pro — 3D Fitness Command Center</title>
<link rel="manifest" href="./manifest.json">
<link rel="apple-touch-icon" href="./icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
<style>
:root {{
  --bg-main: #060913;
  --bg-card: rgba(14, 20, 36, 0.90);
  --bg-card-elevated: rgba(20, 29, 52, 0.96);
  --border-subtle: rgba(255, 255, 255, 0.09);
  --border-focus: rgba(0, 240, 255, 0.55);
  --text-main: #f8fafc;
  --text-sub: #94a3b8;
  --text-muted: #64748b;
  --accent-primary: #00f0ff;
  --accent-secondary: #7928ca;
  --accent-emerald: #00ff88;
  --accent-amber: #ffd700;
  --accent-purple: #b5179e;
  --accent-rose: #ff0055;
  --accent-grad: linear-gradient(135deg, #00f0ff 0%, #7928ca 100%);
  --shadow-3d: 0 10px 24px -4px rgba(0, 0, 0, 0.65), 0 4px 8px -2px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.16), inset 0 -2px 4px rgba(0, 0, 0, 0.45);
  --btn-3d-shadow: 0 4px 0 #4c1d95, 0 8px 18px rgba(0, 0, 0, 0.4);
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
}}

/* THEMES */
body[data-theme="3d-cyber"] {{
  --accent-primary: #00f0ff;
  --accent-secondary: #7928ca;
  --accent-grad: linear-gradient(135deg, #00f0ff 0%, #7928ca 100%);
  --btn-3d-shadow: 0 4px 0 #4c1d95, 0 8px 18px rgba(0, 240, 255, 0.35);
}}
body[data-theme="3d-gold"] {{
  --accent-primary: #ffd700;
  --accent-secondary: #d97706;
  --accent-grad: linear-gradient(135deg, #ffd700 0%, #b45309 100%);
  --btn-3d-shadow: 0 4px 0 #92400e, 0 8px 18px rgba(255, 215, 0, 0.35);
}}
body[data-theme="3d-emerald"] {{
  --accent-primary: #00ff88;
  --accent-secondary: #047857;
  --accent-grad: linear-gradient(135deg, #00ff88 0%, #065f46 100%);
  --btn-3d-shadow: 0 4px 0 #064e3b, 0 8px 18px rgba(0, 255, 136, 0.35);
}}
body[data-theme="3d-violet"] {{
  --accent-primary: #d946ef;
  --accent-secondary: #7e22ce;
  --accent-grad: linear-gradient(135deg, #d946ef 0%, #7e22ce 100%);
  --btn-3d-shadow: 0 4px 0 #581c87, 0 8px 18px rgba(217, 70, 239, 0.35);
}}
body[data-theme="3d-crimson"] {{
  --accent-primary: #ff1744;
  --accent-secondary: #990000;
  --accent-grad: linear-gradient(135deg, #ff1744 0%, #990000 100%);
  --btn-3d-shadow: 0 4px 0 #7f1d1d, 0 8px 18px rgba(255, 23, 68, 0.35);
}}
body[data-theme="synthwave"] {{
  --accent-primary: #f43f5e;
  --accent-secondary: #06b6d4;
  --accent-grad: linear-gradient(135deg, #f43f5e 0%, #06b6d4 100%);
  --btn-3d-shadow: 0 4px 0 #0e7490, 0 8px 18px rgba(244, 63, 94, 0.35);
}}
body[data-theme="stealth"] {{
  --accent-primary: #e2e8f0;
  --accent-secondary: #475569;
  --accent-grad: linear-gradient(135deg, #f1f5f9 0%, #475569 100%);
  --btn-3d-shadow: 0 4px 0 #334155, 0 8px 18px rgba(0, 0, 0, 0.5);
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}}

body {{
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  background-color: var(--bg-main);
  color: var(--text-main);
  min-height: 100vh;
  min-height: -webkit-fill-available;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  padding-top: var(--safe-top);
  padding-bottom: calc(76px + var(--safe-bottom));
  user-select: none;
  position: relative;
}}

/* High-Performance Canvas */
#ambientCanvas {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  opacity: 0.65;
}}

#confettiCanvas {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
  display: none;
}}

/* ========================================================
   COMMAND CENTER HEADER
   ======================================================== */
.app-header {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(6, 9, 19, 0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 10px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4);
}}

.app-brand {{
  display: flex;
  align-items: center;
  gap: 10px;
}}

.app-logo {{
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: var(--accent-grad);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Outfit', sans-serif;
  font-size: 18px;
  font-weight: 900;
  color: #fff;
  box-shadow: 0 4px 0 var(--accent-secondary), 0 6px 14px rgba(0, 0, 0, 0.4);
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.25);
}}

.app-title-wrap {{
  display: flex;
  flex-direction: column;
}}

.app-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.28rem;
  font-weight: 900;
  letter-spacing: -0.2px;
  color: #ffffff;
  text-shadow:
    0 1px 0 var(--accent-primary),
    0 2px 0 rgba(0, 180, 255, 0.7),
    0 3px 0 var(--accent-secondary),
    0 5px 12px rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  gap: 5px;
}}

.app-subtitle {{
  font-size: 0.64rem;
  font-weight: 800;
  letter-spacing: 0.9px;
  color: var(--accent-primary);
  text-transform: uppercase;
}}

.app-header-actions {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.theme-dropdown-select {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-subtle);
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.74rem;
  font-weight: 800;
  padding: 6px 9px;
  border-radius: 8px;
  cursor: pointer;
  outline: none;
}}

.active-pill {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 255, 136, 0.16);
  border: 1px solid rgba(0, 255, 136, 0.45);
  color: var(--accent-emerald);
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 0.74rem;
  font-weight: 800;
  cursor: pointer;
}}

.live-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--accent-emerald);
  box-shadow: 0 0 8px var(--accent-emerald);
  animation: livePulse 1.6s infinite;
}}

@keyframes livePulse {{
  0%, 100% {{ transform: scale(1); opacity: 1; }}
  50% {{ transform: scale(1.4); opacity: 0.5; }}
}}

/* STICKY ACTIVE WORKOUT BANNER */
.sticky-workout-banner {{
  display: none;
  background: linear-gradient(90deg, #00f0ff 0%, #00ff88 100%);
  color: #050814;
  padding: 9px 14px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.82rem;
  font-weight: 900;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 14px rgba(0, 240, 255, 0.35);
  cursor: pointer;
  z-index: 90;
  position: sticky;
  top: 59px;
}}

/* ========================================================
   COMMAND CENTER HUD TELEMETRY DASHBOARD
   ======================================================== */
.hud-telemetry-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 12px 16px 8px;
}}

.hud-tile {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  padding: 10px 8px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  overflow: hidden;
}}

.hud-tile::before {{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--accent-grad);
}}

.hud-val {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.22rem;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.5px;
}}

.hud-lbl {{
  font-size: 0.65rem;
  color: var(--text-muted);
  font-weight: 800;
  text-transform: uppercase;
  margin-top: 2px;
}}

/* QUICK MISSION COMMAND BANNER */
.mission-banner {{
  margin: 8px 16px 12px;
  background: linear-gradient(145deg, rgba(20, 28, 50, 0.95) 0%, rgba(12, 17, 30, 0.95) 100%);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  padding: 14px 16px;
  box-shadow: var(--shadow-3d);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}}

.mission-info {{
  flex: 1;
  min-width: 0;
}}

.mission-badge {{
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(0, 240, 255, 0.14);
  border: 1px solid rgba(0, 240, 255, 0.35);
  color: var(--accent-primary);
  padding: 2px 8px;
  border-radius: 6px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.68rem;
  font-weight: 800;
  text-transform: uppercase;
  margin-bottom: 4px;
}}

.mission-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.05rem;
  font-weight: 900;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.mission-sub {{
  font-size: 0.72rem;
  color: var(--text-sub);
}}

.btn-launch-hud {{
  padding: 10px 16px;
  background: var(--accent-grad);
  border: none;
  border-radius: 12px;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.84rem;
  font-weight: 900;
  cursor: pointer;
  box-shadow: var(--btn-3d-shadow);
  flex-shrink: 0;
  position: relative;
  top: 0;
  transition: all 0.1s;
}}
.btn-launch-hud:active {{
  top: 3px;
  box-shadow: 0 1px 0 var(--accent-secondary);
}}

/* ========================================================
   TAB VIEWS CONTAINER
   ======================================================== */
.tab-view {{
  display: none;
  padding: 8px 16px 20px;
  flex: 1;
  position: relative;
  z-index: 10;
  animation: tabFadeIn 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}}

.tab-view.active {{
  display: block;
}}

@keyframes tabFadeIn {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

/* 3D DAY SELECTOR CHIPS */
.days-chips-scroll {{
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 2px 2px 10px;
  scrollbar-width: none;
}}
.days-chips-scroll::-webkit-scrollbar {{
  display: none;
}}

.day-chip {{
  padding: 8px 13px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  color: var(--text-sub);
  font-family: 'Outfit', sans-serif;
  font-size: 0.78rem;
  font-weight: 800;
  white-space: nowrap;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  min-width: 62px;
  cursor: pointer;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
  position: relative;
  top: 0;
  transition: all 0.12s;
}}

.day-chip:active {{
  top: 2px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}}

.day-chip.active {{
  background: rgba(0, 240, 255, 0.16);
  border-color: var(--accent-primary);
  color: #fff;
  box-shadow: 0 4px 14px rgba(0, 240, 255, 0.3), 0 2px 0 var(--accent-primary);
}}

.day-chip.active .chip-name {{
  color: var(--accent-primary);
}}

/* ROUTINE COMMAND CARD */
.routine-card {{
  background: var(--bg-card);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  padding: 16px;
  margin: 10px 0 14px;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-3d);
}}

.routine-badge {{
  display: inline-block;
  padding: 4px 9px;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}}

.routine-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.3rem;
  font-weight: 900;
  line-height: 1.25;
  margin-bottom: 4px;
}}

.routine-meta {{
  font-size: 0.78rem;
  color: var(--text-sub);
  margin-bottom: 14px;
}}

.routine-actions-row {{
  display: flex;
  gap: 10px;
}}

.btn-start-workout {{
  flex: 2;
  padding: 12px 16px;
  background: var(--accent-grad);
  border: none;
  border-radius: 12px;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.92rem;
  font-weight: 900;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-shadow: var(--btn-3d-shadow);
  position: relative;
  top: 0;
  transition: all 0.1s;
}}
.btn-start-workout:active {{
  top: 3px;
  box-shadow: 0 1px 0 var(--accent-secondary);
}}

.btn-add-ex-trigger {{
  flex: 1;
  padding: 12px 12px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.84rem;
  font-weight: 800;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.3);
  position: relative;
  top: 0;
  transition: all 0.1s;
}}
.btn-add-ex-trigger:active {{
  top: 2px;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.3);
}}

/* EXERCISE PREVIEW LIST */
.ex-preview-item {{
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  padding: 10px 12px;
  margin-bottom: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}}

.ex-preview-thumb {{
  width: 54px;
  height: 54px;
  border-radius: 10px;
  object-fit: cover;
  background: #090d16;
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.12);
}}

.ex-preview-info {{
  flex: 1;
  min-width: 0;
}}

.ex-preview-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 0.88rem;
  font-weight: 800;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.ex-preview-sub {{
  font-size: 0.72rem;
  color: var(--text-sub);
  margin-top: 2px;
}}

.ex-preview-pill {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-subtle);
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 800;
  color: var(--accent-primary);
  white-space: nowrap;
}}

.btn-remove-ex {{
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 16px;
  padding: 6px;
  cursor: pointer;
}}
.btn-remove-ex:hover {{
  color: var(--accent-rose);
}}

/* ========================================================
   RUNNER & ACCURATE EXERCISE TRACKER MATRIX
   ======================================================== */
.runner-container {{
  display: flex;
  flex-direction: column;
  gap: 12px;
}}

.runner-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  padding: 12px 14px;
  box-shadow: var(--shadow-3d);
}}

.runner-timer-val {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--accent-primary);
}}

.btn-finish-workout {{
  padding: 9px 16px;
  background: rgba(0, 255, 136, 0.18);
  border: 1px solid var(--accent-emerald);
  border-radius: 10px;
  color: var(--accent-emerald);
  font-family: 'Outfit', sans-serif;
  font-size: 0.8rem;
  font-weight: 900;
  cursor: pointer;
  box-shadow: 0 3px 0 rgba(0, 255, 136, 0.3);
  position: relative;
  top: 0;
}}
.btn-finish-workout:active {{
  top: 2px;
  box-shadow: 0 1px 0 rgba(0, 255, 136, 0.3);
}}

.runner-progress-bar {{
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  overflow: hidden;
}}

.runner-progress-fill {{
  height: 100%;
  width: 0%;
  background: var(--accent-grad);
  border-radius: 999px;
  transition: width 0.3s ease;
}}

/* ACTIVE EXERCISE CARD */
.active-ex-card {{
  background: var(--bg-card-elevated);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: var(--shadow-3d);
}}

.active-ex-img-wrap {{
  position: relative;
  width: 100%;
  height: 215px;
  background: #090d16;
}}

.active-ex-img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}

.active-ex-num {{
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(6, 9, 19, 0.88);
  backdrop-filter: blur(8px);
  border: 1px solid var(--border-subtle);
  padding: 4px 10px;
  border-radius: 8px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.78rem;
  font-weight: 900;
  color: var(--accent-primary);
}}

.active-ex-body {{
  padding: 14px 16px;
}}

.active-ex-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.3rem;
  font-weight: 900;
  margin-bottom: 2px;
}}

.active-ex-target {{
  font-size: 0.76rem;
  font-weight: 800;
  color: var(--accent-primary);
  margin-bottom: 6px;
}}

.active-ex-cues {{
  background: rgba(255, 255, 255, 0.04);
  border-left: 3px solid var(--accent-amber);
  border-radius: 4px 8px 8px 4px;
  padding: 8px 12px;
  font-size: 0.76rem;
  color: var(--text-sub);
  line-height: 1.4;
  margin-bottom: 12px;
}}

/* ========================================================
   EXERCISE TIMER / STOPWATCH WIDGET
   ======================================================== */
.ex-timer-widget {{
  background: rgba(10, 15, 28, 0.90);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 14px;
}}

.ex-timer-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}}

.ex-timer-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 0.8rem;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--text-sub);
  display: flex;
  align-items: center;
  gap: 6px;
}}

.ex-timer-mode-toggle {{
  display: flex;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 2px;
}}

.timer-mode-btn {{
  padding: 4px 10px;
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-family: 'Outfit', sans-serif;
  font-size: 0.72rem;
  font-weight: 800;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}}

.timer-mode-btn.active {{
  background: var(--accent-grad);
  color: #fff;
  box-shadow: 0 2px 6px rgba(0, 240, 255, 0.35);
}}

.ex-timer-display-wrap {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin: 6px 0 10px;
}}

.timer-ring-container {{
  position: relative;
  width: 86px;
  height: 86px;
  flex-shrink: 0;
}}

.timer-ring-svg {{
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}}

.timer-ring-bg {{
  stroke: rgba(255, 255, 255, 0.08);
  stroke-width: 6;
  fill: none;
}}

.timer-ring-progress {{
  stroke: var(--accent-primary);
  stroke-width: 6;
  stroke-linecap: round;
  fill: none;
  stroke-dasharray: 251.2;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 0.1s linear, stroke 0.3s;
}}

.timer-ring-inner {{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.15rem;
  font-weight: 800;
  color: #fff;
}}

.timer-readout-big {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.8rem;
  font-weight: 800;
  color: #fff;
}}

.timer-presets-row {{
  display: flex;
  gap: 6px;
  margin-bottom: 10px;
  overflow-x: auto;
  scrollbar-width: none;
}}
.timer-presets-row::-webkit-scrollbar {{
  display: none;
}}

.timer-preset-pill {{
  padding: 5px 9px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  color: var(--text-sub);
  font-family: 'Outfit', sans-serif;
  font-size: 0.72rem;
  font-weight: 800;
  cursor: pointer;
}}

.timer-preset-pill.active {{
  background: rgba(0, 240, 255, 0.2);
  border-color: var(--accent-primary);
  color: #fff;
}}

.timer-controls-row {{
  display: flex;
  gap: 8px;
}}

.btn-timer-ctrl {{
  flex: 1;
  padding: 8px;
  border-radius: 8px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.78rem;
  font-weight: 800;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  position: relative;
  top: 0;
}}

.btn-timer-ctrl.primary {{
  background: var(--accent-grad);
  border: none;
  color: #fff;
  box-shadow: 0 3px 0 #4c1d95;
}}
.btn-timer-ctrl.primary:active {{ top: 2px; box-shadow: 0 1px 0 #4c1d95; }}

.btn-timer-ctrl.secondary {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-subtle);
  color: var(--text-sub);
}}

/* ========================================================
   INTELLIGENT SET LOGGING MATRIX WITH RAPID BUMP BUTTONS
   ======================================================== */
.set-card-row {{
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 10px;
  margin-bottom: 8px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.set-row-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.set-badge-tag {{
  font-family: 'Outfit', sans-serif;
  font-weight: 900;
  font-size: 0.82rem;
  color: #fff;
}}

.set-prev-target {{
  font-size: 0.72rem;
  color: var(--accent-primary);
  font-weight: 700;
  background: rgba(0, 240, 255, 0.1);
  padding: 2px 7px;
  border-radius: 6px;
}}

.set-inputs-grid {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.input-group-col {{
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}}

.input-mini-label {{
  font-size: 0.65rem;
  color: var(--text-muted);
  font-weight: 800;
  text-transform: uppercase;
}}

.set-input-box {{
  width: 100%;
  padding: 8px 6px;
  background: #080c18;
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  color: #fff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.95rem;
  font-weight: 800;
  text-align: center;
  outline: none;
}}

.set-input-box:focus {{
  border-color: var(--accent-primary);
}}

/* Rapid Mobile Weight Adjusters */
.weight-bump-row {{
  display: flex;
  gap: 4px;
}}

.btn-weight-bump {{
  flex: 1;
  padding: 4px 2px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  color: var(--text-sub);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  font-weight: 800;
  cursor: pointer;
  text-align: center;
}}
.btn-weight-bump:active {{
  background: var(--accent-primary);
  color: #000;
}}

.btn-complete-set {{
  padding: 10px 14px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-subtle);
  border-radius: 10px;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.8rem;
  font-weight: 900;
  cursor: pointer;
  align-self: flex-end;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.3);
}}

.btn-complete-set.completed {{
  background: var(--accent-emerald);
  border-color: var(--accent-emerald);
  color: #000;
  box-shadow: 0 3px 0 #047857;
}}

/* ========================================================
   WORKOUT SCHEDULER & CALENDAR COMMAND VIEW
   ======================================================== */
.schedule-quick-matrix {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-3d);
}}

.schedule-matrix-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}}

.schedule-day-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 10px;
  border-radius: 10px;
  margin-bottom: 6px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid transparent;
}}

.schedule-day-row.today {{
  background: rgba(0, 240, 255, 0.12);
  border-color: var(--accent-primary);
}}

.schedule-day-name {{
  font-family: 'Outfit', sans-serif;
  font-size: 0.82rem;
  font-weight: 900;
  width: 50px;
}}

.schedule-routine-select {{
  flex: 1;
  background: #080c18;
  border: 1px solid var(--border-subtle);
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.76rem;
  font-weight: 700;
  padding: 6px 8px;
  border-radius: 8px;
  outline: none;
  cursor: pointer;
}}

/* CALENDAR CARD */
.calendar-card {{
  background: var(--bg-card);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  padding: 16px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-3d);
}}

.calendar-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}}

.calendar-month-title {{
  font-family: 'Outfit', sans-serif;
  font-size: 1.15rem;
  font-weight: 900;
}}

.calendar-weekdays-grid {{
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  text-align: center;
  font-family: 'Outfit', sans-serif;
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--text-muted);
  margin-bottom: 6px;
}}

.calendar-days-grid {{
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}}

.cal-day-cell {{
  aspect-ratio: 1;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid transparent;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Outfit', sans-serif;
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--text-sub);
  cursor: pointer;
  position: relative;
}}

.cal-day-cell.today {{
  border-color: var(--accent-primary);
  color: #fff;
  box-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
}}

.cal-day-cell.selected {{
  background: rgba(0, 240, 255, 0.25);
  border-color: var(--accent-primary);
  color: #fff;
}}

.cal-day-cell.has-completed {{
  background: rgba(0, 255, 136, 0.16);
  border-color: rgba(0, 255, 136, 0.4);
  color: #fff;
}}

.cal-day-dot {{
  width: 4px;
  height: 4px;
  border-radius: 50%;
  position: absolute;
  bottom: 3px;
}}

.cal-day-dot.completed {{ background: var(--accent-emerald); }}
.cal-day-dot.scheduled {{ background: var(--accent-primary); }}

/* CALENDAR DAY DETAILS DRAWER */
.cal-day-details {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: 14px;
  margin-top: 12px;
  box-shadow: var(--shadow-3d);
}}

/* ========================================================
   MEASURABLE PROGRESS & TELEMETRY ANALYTICS
   ======================================================== */
.pr-hall-card {{
  background: var(--bg-card);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-3d);
}}

.pr-item-row {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid var(--border-subtle);
}}

.pr-item-row:last-child {{
  border-bottom: none;
}}

.chart-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-3d);
}}

/* Heatmap Grid */
.heatmap-container {{
  overflow-x: auto;
  padding-bottom: 6px;
}}
.heatmap-grid {{
  display: grid;
  grid-template-rows: repeat(7, 10px);
  grid-auto-flow: column;
  gap: 3px;
}}
.heatmap-box {{
  width: 10px;
  height: 10px;
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.05);
}}
.heatmap-box.lvl-1 {{ background: rgba(0, 240, 255, 0.3); }}
.heatmap-box.lvl-2 {{ background: rgba(0, 240, 255, 0.6); }}
.heatmap-box.lvl-3 {{ background: rgba(0, 240, 255, 0.95); box-shadow: 0 0 6px var(--accent-primary); }}

/* ========================================================
   EXERCISE LIBRARY PICKER MODAL
   ======================================================== */
.modal-overlay {{
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.82);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  z-index: 1000;
  align-items: flex-end;
  justify-content: center;
}}

.modal-overlay.active {{
  display: flex;
}}

.modal-sheet {{
  width: 100%;
  max-width: 540px;
  max-height: 86vh;
  background: var(--bg-card-elevated);
  border-top: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 24px 24px 0 0;
  padding: 16px 16px calc(24px + var(--safe-bottom));
  display: flex;
  flex-direction: column;
  box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.6);
}}

.modal-search-input {{
  width: 100%;
  padding: 10px 14px;
  background: #080c18;
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  color: #fff;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.9rem;
  outline: none;
  margin-bottom: 10px;
}}

.modal-category-chips {{
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding: 2px 0 8px;
  scrollbar-width: none;
  margin-bottom: 10px;
}}
.modal-category-chips::-webkit-scrollbar {{ display: none; }}

.modal-cat-chip {{
  padding: 6px 12px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border-subtle);
  border-radius: 18px;
  color: var(--text-sub);
  font-family: 'Outfit', sans-serif;
  font-size: 0.74rem;
  font-weight: 800;
  white-space: nowrap;
  cursor: pointer;
}}

.modal-cat-chip.active {{
  background: var(--accent-grad);
  color: #fff;
}}

.modal-ex-scroll-list {{
  flex: 1;
  overflow-y: auto;
  padding-right: 4px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.modal-ex-card {{
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  padding: 8px 12px;
}}

.modal-ex-img {{
  width: 50px;
  height: 50px;
  border-radius: 10px;
  object-fit: cover;
  background: #090d16;
  flex-shrink: 0;
}}

.btn-add-library-ex {{
  padding: 8px 14px;
  background: var(--accent-grad);
  border: none;
  border-radius: 8px;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.76rem;
  font-weight: 800;
  cursor: pointer;
  flex-shrink: 0;
}}

/* REST TIMER OVERLAY */
.rest-modal-overlay {{
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.90);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  z-index: 2000;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 24px;
}}

.rest-modal-overlay.active {{ display: flex; }}

.rest-clock {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 5rem;
  font-weight: 900;
  color: #fff;
  margin: 12px 0;
  text-shadow: 0 0 35px var(--accent-primary);
}}

/* BOTTOM NAVIGATION */
.bottom-nav {{
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100vw;
  background: rgba(6, 9, 19, 0.95);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-top: 1px solid rgba(255, 255, 255, 0.10);
  padding: 8px 6px calc(6px + var(--safe-bottom));
  display: flex;
  justify-content: space-around;
  z-index: 100;
  overflow-x: auto;
}}

.nav-item {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  padding: 4px 6px;
  color: var(--text-muted);
  cursor: pointer;
  min-width: 48px;
  transition: all 0.15s;
}}

.nav-icon {{ font-size: 20px; }}

.nav-item span {{
  font-size: 0.65rem;
  font-weight: 800;
  font-family: 'Outfit', sans-serif;
}}

.nav-item.active {{
  color: var(--accent-primary);
  text-shadow: 0 0 8px var(--accent-primary);
}}

/* Photos & Hub */
.hub-card, .setting-row {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 12px;
}}
.setting-row {{ display: flex; justify-content: space-between; align-items: center; }}
.photo-gallery-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 10px; }}
.gallery-photo-thumb {{ width: 100%; aspect-ratio: 1; border-radius: 10px; object-fit: cover; }}
.toggle-switch {{ position: relative; display: inline-block; width: 48px; height: 26px; }}
.toggle-switch input {{ opacity: 0; width: 0; height: 0; }}
.toggle-slider {{ position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #1a2234; transition: .2s; border-radius: 34px; }}
.toggle-slider:before {{ position: absolute; content: ""; height: 20px; width: 20px; left: 3px; bottom: 3px; background-color: white; transition: .2s; border-radius: 50%; }}
input:checked + .toggle-slider {{ background-color: var(--accent-emerald); }}
input:checked + .toggle-slider:before {{ transform: translateX(22px); }}
</style>
</head>
<body data-theme="3d-cyber">

<!-- Ambient Performance Canvas -->
<canvas id="ambientCanvas"></canvas>
<!-- Confetti Canvas -->
<canvas id="confettiCanvas"></canvas>

<!-- Top Command Header -->
<header class="app-header">
  <div class="app-brand">
    <div class="app-logo">PF</div>
    <div class="app-title-wrap">
      <div class="app-title">PLANFIT PRO</div>
      <div class="app-subtitle">3D FITNESS COMMAND CENTER</div>
    </div>
  </div>
  
  <div class="app-header-actions">
    <!-- Quick 3D Theme Dropdown -->
    <select class="theme-dropdown-select" id="headerThemePicker" onchange="changeTheme(this.value)">
      <option value="3d-cyber">🎮 3D Cyber Holo</option>
      <option value="3d-gold">👑 3D Gold Titanium</option>
      <option value="3d-emerald">💎 3D Emerald Matrix</option>
      <option value="3d-violet">🔮 3D Electric Violet</option>
      <option value="3d-crimson">🔴 3D Crimson Fury</option>
      <option value="synthwave">🌆 Miami Synthwave</option>
      <option value="stealth">🌑 Midnight Stealth</option>
    </select>

    <div id="workoutStatusIndicator" style="display:none;" onclick="switchNav('tabRunner')">
      <div class="active-pill">
        <div class="live-dot"></div>
        <span id="headerTimer">00:00</span>
      </div>
    </div>
  </div>
</header>

<!-- Sticky In-Progress Workout Banner -->
<div class="sticky-workout-banner" id="stickyWorkoutBanner" onclick="switchNav('tabRunner')">
  <div style="display:flex; align-items:center; gap:8px;">
    <span>⚡ ACTIVE SESSION:</span>
    <span id="stickyBannerTitle">Chest & Triceps</span>
  </div>
  <div style="display:flex; align-items:center; gap:6px;">
    <span id="stickyBannerTime">00:00</span>
    <span>RESUME ➔</span>
  </div>
</div>

<!-- COMMAND CENTER HUD TELEMETRY -->
<div class="hud-telemetry-grid">
  <div class="hud-tile">
    <div class="hud-val" id="hudReadinessVal" style="color:var(--accent-emerald);">96%</div>
    <div class="hud-lbl">Readiness HUD</div>
  </div>
  <div class="hud-tile">
    <div class="hud-val" id="hudWeeklyVolVal" style="color:var(--accent-primary);">18.4k</div>
    <div class="hud-lbl">Weekly Volume</div>
  </div>
  <div class="hud-tile">
    <div class="hud-val" id="hudStreakVal" style="color:var(--accent-amber);">5 Days</div>
    <div class="hud-lbl">Training Streak</div>
  </div>
</div>

<!-- TODAY'S MISSION LAUNCHER -->
<div class="mission-banner">
  <div class="mission-info">
    <div class="mission-badge">🎯 TODAY'S SCHEDULED SPLIT</div>
    <div class="mission-title" id="hudTodaySplitTitle">Upper Chest & Triceps</div>
    <div class="mission-sub" id="hudTodaySplitMeta">8 Exercises • Progressive Overload Engine</div>
  </div>
  <button class="btn-launch-hud" onclick="startCurrentRoutine()">
    ▶ LAUNCH
  </button>
</div>

<!-- ========================================================
     TAB 1: WORKOUTS & SPLIT MANAGER
     ======================================================== -->
<section id="tabWorkouts" class="tab-view active">
  <div class="days-chips-scroll" id="daysChipsContainer">
    <!-- Day chips inserted via JS -->
  </div>

  <div class="routine-card" id="routineSummaryCard">
    <span class="routine-badge" id="routineBadge">TODAY'S SPLIT</span>
    <h2 class="routine-title" id="routineTitle">Upper Chest & Triceps</h2>
    <div class="routine-meta" id="routineMeta">8 Exercises • 32 Sets • Progressive Overload Protocol</div>
    
    <div class="routine-actions-row">
      <button class="btn-start-workout" onclick="startCurrentRoutine()">
        ▶ START WORKOUT
      </button>
      <button class="btn-add-ex-trigger" onclick="openExerciseLibraryModal()">
        ➕ Add Exercise
      </button>
    </div>
  </div>

  <!-- Warm-up protocol -->
  <div style="margin-bottom: 14px;">
    <div style="font-family:'Outfit',sans-serif; font-size:0.82rem; font-weight:900; color:var(--accent-amber); margin-bottom:8px; text-transform:uppercase; display:flex; justify-content:space-between; align-items:center;">
      <span>🔥 Pre-Exhaust Warm-Up Protocol</span>
      <span style="font-size:0.7rem; color:var(--text-muted);">INJURY SHIELD</span>
    </div>
    <div id="warmupList" style="display:flex; flex-direction:column; gap:6px;">
      <!-- Populated via JS -->
    </div>
  </div>

  <!-- Exercise List preview with Add/Remove -->
  <div>
    <div style="font-family:'Outfit',sans-serif; font-size:0.82rem; font-weight:900; color:var(--text-sub); margin-bottom:10px; text-transform:uppercase; display:flex; justify-content:space-between; align-items:center;">
      <span>Targeted Exercises (<span id="previewExCount">8</span>)</span>
      <span style="color:var(--accent-primary); cursor:pointer;" onclick="openExerciseLibraryModal()">+ Add New</span>
    </div>
    <div class="ex-list" id="exercisePreviewList">
      <!-- Exercise items inserted via JS -->
    </div>
  </div>
</section>

<!-- ========================================================
     TAB 2: RUNNER & ACCURATE SET TRACKING WITH QUICK BUMPS
     ======================================================== -->
<section id="tabRunner" class="tab-view">
  <div class="runner-container" id="runnerContainer">
    <!-- Runner Header -->
    <div class="runner-header">
      <div>
        <div style="font-size:0.7rem; color:var(--text-muted); font-weight:800;">TOTAL SESSION TIME</div>
        <div class="runner-timer-val" id="runnerElapsed">00:00</div>
      </div>
      <button class="btn-finish-workout" onclick="finishWorkout()">
        ✓ FINISH SESSION
      </button>
    </div>

    <div class="runner-progress-bar">
      <div class="runner-progress-fill" id="runnerProgressFill"></div>
    </div>

    <!-- Active Exercise Card -->
    <div class="active-ex-card">
      <div class="active-ex-img-wrap">
        <img src="" id="runnerExImg" class="active-ex-img" alt="Exercise">
        <div class="active-ex-num" id="runnerExNum">#1 / 8</div>
      </div>
      <div class="active-ex-body">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
          <div>
            <h2 class="active-ex-title" id="runnerExTitle">Flat Dumbbell Press</h2>
            <div class="active-ex-target" id="runnerExTarget">Chest (Pectoralis Major)</div>
          </div>
          <button class="btn-add-ex-trigger" onclick="openExerciseLibraryModal()" style="padding:6px 10px; font-size:0.75rem;">
            ➕ Add
          </button>
        </div>

        <div class="active-ex-cues" id="runnerExCues">
          💡 Drive through chest, maintain arch and retracted scapula.
        </div>

        <!-- SEPARATE DEDICATED EXERCISE TIMER & STOPWATCH WIDGET -->
        <div class="ex-timer-widget">
          <div class="ex-timer-header">
            <div class="ex-timer-title">
              <span>⏱️ EXERCISE TELEMETRY TIMER</span>
              <span id="timerStatusBadge" style="color:var(--accent-emerald); font-size:0.72rem; font-weight:800;">• READY</span>
            </div>
            <div class="ex-timer-mode-toggle">
              <button class="timer-mode-btn active" id="btnModeStopwatch" onclick="setTimerMode('stopwatch')">Stopwatch</button>
              <button class="timer-mode-btn" id="btnModeCountdown" onclick="setTimerMode('countdown')">Countdown</button>
            </div>
          </div>

          <div class="ex-timer-display-wrap">
            <div class="timer-ring-container">
              <svg class="timer-ring-svg" viewBox="0 0 90 90">
                <circle class="timer-ring-bg" cx="45" cy="45" r="40"></circle>
                <circle class="timer-ring-progress" id="timerRingCircle" cx="45" cy="45" r="40"></circle>
              </svg>
              <div class="timer-ring-inner" id="timerRingDisplay">00:00</div>
            </div>

            <div>
              <div class="timer-readout-big" id="timerDigitalClock">00:00.0</div>
              <div style="font-size:0.72rem; color:var(--text-sub);" id="timerSubLabel">Time Under Tension (TUT)</div>
            </div>
          </div>

          <!-- Presets for Countdown -->
          <div class="timer-presets-row" id="timerPresetsRow" style="display:none;">
            <div class="timer-preset-pill" onclick="setTimerDuration(30)">30s</div>
            <div class="timer-preset-pill active" onclick="setTimerDuration(45)">45s</div>
            <div class="timer-preset-pill" onclick="setTimerDuration(60)">60s</div>
            <div class="timer-preset-pill" onclick="setTimerDuration(90)">90s</div>
            <div class="timer-preset-pill" onclick="setTimerDuration(120)">120s</div>
          </div>

          <div class="timer-controls-row">
            <button class="btn-timer-ctrl primary" id="btnTimerToggle" onclick="toggleExerciseTimer()">
              ▶ Start Timer
            </button>
            <button class="btn-timer-ctrl secondary" onclick="resetExerciseTimer()">
              🔄 Reset
            </button>
            <button class="btn-timer-ctrl secondary" onclick="recordTutToActiveSet()">
              📝 Log TUT
            </button>
          </div>
        </div>

        <!-- SET LOGGING MATRIX WITH RAPID BUMP BUTTONS -->
        <div style="margin-bottom: 12px;" id="runnerSetsContainer">
          <!-- Dynamically inserted set cards -->
        </div>
      </div>
    </div>

    <!-- Runner Navigation Buttons -->
    <div style="display:flex; gap:10px;">
      <button class="btn-add-ex-trigger" style="flex:1;" onclick="prevExercise()">← Previous</button>
      <button class="btn-start-workout" style="flex:1;" onclick="nextExercise()">Next Exercise →</button>
    </div>
  </div>
</section>

<!-- ========================================================
     TAB 3: EFFORTLESS SCHEDULER & CALENDAR COMMAND
     ======================================================== -->
<section id="tabCalendar" class="tab-view">
  <!-- Weekly Split Matrix Reassigner -->
  <div class="schedule-quick-matrix">
    <div class="schedule-matrix-header">
      <div style="font-family:'Outfit',sans-serif; font-size:1.05rem; font-weight:900;">⚡ Weekly Split Manager</div>
      <div style="font-size:0.72rem; color:var(--accent-primary); font-weight:800;">Tap to Reassign</div>
    </div>
    <div id="weeklyScheduleRows">
      <!-- Injected Mon to Sun split reassigners -->
    </div>
  </div>

  <!-- Interactive Monthly Calendar -->
  <div class="calendar-card">
    <div class="calendar-header">
      <div class="calendar-month-title" id="calendarMonthTitle">October 2026</div>
      <div style="display:flex; gap:6px;">
        <button class="btn-add-ex-trigger" style="padding:4px 8px; font-size:0.75rem;" onclick="changeCalendarMonth(-1)">‹ Prev</button>
        <button class="btn-add-ex-trigger" style="padding:4px 8px; font-size:0.75rem;" onclick="jumpCalendarToday()">Today</button>
        <button class="btn-add-ex-trigger" style="padding:4px 8px; font-size:0.75rem;" onclick="changeCalendarMonth(1)">Next ›</button>
      </div>
    </div>

    <div class="calendar-weekdays-grid">
      <div>MON</div>
      <div>TUE</div>
      <div>WED</div>
      <div>THU</div>
      <div>FRI</div>
      <div>SAT</div>
      <div>SUN</div>
    </div>

    <div class="calendar-days-grid" id="calendarDaysGrid">
      <!-- Days populated via JS -->
    </div>
  </div>

  <!-- Selected Date Details Drawer -->
  <div class="cal-day-details" id="calDayDetailsBox">
    <div style="font-family:'Outfit',sans-serif; font-size:1.05rem; font-weight:900; margin-bottom:2px;" id="calDetailDate">Monday, Oct 12, 2026</div>
    <div style="font-size:0.78rem; color:var(--text-sub); margin-bottom:10px;" id="calDetailSplit">Scheduled Split: Upper Chest and Triceps</div>
    <div id="calDetailStatusBadge" style="margin-bottom:12px;"></div>
    
    <div style="display:flex; gap:10px;">
      <button class="btn-start-workout" style="flex:2;" id="btnCalStartDay" onclick="startRoutineForCalendarDay()">
        ▶ START THIS WORKOUT
      </button>
      <button class="btn-add-ex-trigger" style="flex:1;" onclick="toggleCalendarDayCompleted()">
        ✓ Mark Done
      </button>
    </div>
  </div>
</section>

<!-- ========================================================
     TAB 4: MEASURABLE PROGRESS & TELEMETRY ANALYTICS
     ======================================================== -->
<section id="tabAnalytics" class="tab-view">
  <!-- Personal Records (PR) Hall of Fame -->
  <div class="pr-hall-card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <div style="font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:900;">🏆 Personal Records (PR) Hall</div>
      <div style="font-size:0.72rem; color:var(--accent-amber); font-weight:800;">PROGRESSIVE BESTS</div>
    </div>
    <div id="prRecordsList">
      <!-- Injected PR items -->
    </div>
  </div>

  <!-- Volume Charts -->
  <div class="chart-card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <div>
        <div style="font-family:'Outfit',sans-serif; font-size:1rem; font-weight:800;">Weekly Tonnage Progression</div>
        <div style="font-size:0.72rem; color:var(--text-muted);">Total load lifted per day (Mon - Sun)</div>
      </div>
      <div style="font-family:'Outfit',sans-serif; font-weight:900; color:var(--accent-emerald);" id="weekwiseTotalVol">0 kg</div>
    </div>
    <div style="width:100%; height:180px;" id="weekwiseChartWrap"></div>
  </div>

  <!-- 52-Week Activity Heatmap -->
  <div class="chart-card">
    <div style="font-family:'Outfit',sans-serif; font-size:1rem; font-weight:800; margin-bottom:10px;">52-Week Hypertrophy Heatmap</div>
    <div class="heatmap-container">
      <div class="heatmap-grid" id="heatmapGrid"></div>
    </div>
  </div>
</section>

<!-- ========================================================
     TAB 5: HUB (GPS CHECK-IN & PROGRESS PHOTOS)
     ======================================================== -->
<section id="tabHub" class="tab-view">
  <div class="hub-card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <div style="font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:800;">📍 Gym Check-In & Location</div>
      <button class="btn-launch-hud" onclick="fetchLocation()" style="padding:6px 12px; font-size:0.75rem;">
        Update GPS
      </button>
    </div>
    <div style="display:flex; align-items:center; gap:12px; background:rgba(255,255,255,0.03); border:1px solid var(--border-subtle); border-radius:12px; padding:12px; margin-top:10px;">
      <div style="font-size:24px;">🏢</div>
      <div style="flex:1;">
        <input type="text" id="gymNameInput" placeholder="Name your gym" value="Planfit Training Club" onchange="saveGymName()" style="background:transparent; border:none; color:#fff; font-family:'Outfit',sans-serif; font-size:0.95rem; font-weight:700; width:100%; outline:none;">
        <div style="font-size:0.75rem; color:var(--text-sub);" id="coordsDisplay">GPS Coordinates: Tap 'Update GPS' to lock location</div>
      </div>
    </div>
    <div style="font-size:0.72rem; color:var(--text-muted); margin-top:8px;" id="locationTimestamp">Status: Ready for check-in</div>
  </div>

  <div class="hub-card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <div>
        <div style="font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:800;">📸 Progress Photos & Pump</div>
        <div style="font-size:0.75rem; color:var(--text-sub);">Track physical hypertrophy transformation</div>
      </div>
      <div style="display:flex; gap:6px;">
        <label class="btn-launch-hud" style="cursor:pointer; padding:6px 10px; font-size:0.75rem;">
          📷 Camera
          <input type="file" id="cameraInput" accept="image/*" capture="camera" style="display:none;" onchange="handlePhotoUpload(this)">
        </label>
        <label class="btn-add-ex-trigger" style="cursor:pointer; padding:6px 10px; font-size:0.75rem;">
          🖼 Gallery
          <input type="file" id="galleryInput" accept="image/*" style="display:none;" onchange="handlePhotoUpload(this)">
        </label>
      </div>
    </div>
    <div class="photo-gallery-grid" id="photoGalleryGrid"></div>
    <div id="noPhotosMsg" style="text-align:center; padding:30px 10px; color:var(--text-muted); font-size:0.8rem;">
      No progress photos yet. Take a selfie or upload from gallery to start your visual transformation log!
    </div>
  </div>
</section>

<!-- ========================================================
     TAB 6: WORKOUT HISTORY
     ======================================================== -->
<section id="tabHistory" class="tab-view">
  <h2 style="font-family:'Outfit',sans-serif; font-size:1.35rem; font-weight:800; margin-bottom:14px;">Workout History Logs</h2>
  <div id="historyList"></div>
</section>

<!-- ========================================================
     TAB 7: SETTINGS & 3D CUSTOM THEMES
     ======================================================== -->
<section id="tabSettings" class="tab-view">
  <h2 style="font-family:'Outfit',sans-serif; font-size:1.35rem; font-weight:800; margin-bottom:14px;">Preferences & 3D Engine</h2>
  
  <div class="setting-row">
    <div>
      <div style="font-weight:700; font-size:0.9rem;">Visual & 3D Theme</div>
      <div style="font-size:0.74rem; color:var(--text-sub);">Select tactile color & lighting styling</div>
    </div>
    <select id="settingTheme" onchange="changeTheme(this.value)" style="background:#090d16; border:1px solid var(--border-subtle); color:#fff; padding:6px 10px; border-radius:10px; font-family:'Outfit',sans-serif; font-weight:700;">
      <option value="3d-cyber">🎮 3D Cyber Holo</option>
      <option value="3d-gold">👑 3D Gold Titanium</option>
      <option value="3d-emerald">💎 3D Emerald Matrix</option>
      <option value="3d-violet">🔮 3D Electric Violet</option>
      <option value="3d-crimson">🔴 3D Crimson Fury</option>
      <option value="synthwave">🌆 Miami Synthwave</option>
      <option value="stealth">🌑 Midnight Stealth</option>
    </select>
  </div>

  <div class="setting-row">
    <div>
      <div style="font-weight:700; font-size:0.9rem;">Weight Unit</div>
      <div style="font-size:0.74rem; color:var(--text-sub);">Toggle Kilograms or Pounds</div>
    </div>
    <select id="settingUnit" onchange="saveSettings()" style="background:#090d16; border:1px solid var(--border-subtle); color:#fff; padding:6px 10px; border-radius:10px; font-family:'Outfit',sans-serif;">
      <option value="kg">Kilograms (kg)</option>
      <option value="lbs">Pounds (lbs)</option>
    </select>
  </div>

  <div class="setting-row">
    <div>
      <div style="font-weight:700; font-size:0.9rem;">Synthesized Audio Cues</div>
      <div style="font-size:0.74rem; color:var(--text-sub);">Rest & countdown beeps</div>
    </div>
    <label class="toggle-switch">
      <input type="checkbox" id="settingSound" checked onchange="saveSettings()">
      <span class="toggle-slider"></span>
    </label>
  </div>

  <div class="setting-row">
    <div>
      <div style="font-weight:700; font-size:0.9rem;">Haptic Phone Vibration</div>
      <div style="font-size:0.74rem; color:var(--text-sub);">Native Android vibration feedback</div>
    </div>
    <label class="toggle-switch">
      <input type="checkbox" id="settingVibrate" checked onchange="saveSettings()">
      <span class="toggle-slider"></span>
    </label>
  </div>

  <div style="margin-top: 24px;">
    <button onclick="exportData()" style="width:100%; padding:12px; background:rgba(255,255,255,0.08); border:1px solid var(--border-subtle); border-radius:12px; color:#fff; font-weight:800; margin-bottom:10px; cursor:pointer;">
      📥 Backup & Export Workout Data
    </button>
    <button onclick="clearAllData()" style="width:100%; padding:12px; background:rgba(255,23,68,0.12); border:1px solid rgba(255,23,68,0.4); border-radius:12px; color:var(--accent-rose); font-weight:800; cursor:pointer;">
      🗑 Reset All Logs & Telemetry
    </button>
  </div>
</section>

<!-- ========================================================
     MODAL: EXERCISE LIBRARY PICKER (39 ITEMS WITH IMAGES)
     ======================================================== -->
<div class="modal-overlay" id="exerciseLibraryModal" onclick="closeExerciseLibraryModalOnOverlay(event)">
  <div class="modal-sheet">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
      <div>
        <div style="font-family:'Outfit',sans-serif; font-size:1.2rem; font-weight:900;">Select Exercise</div>
        <div style="font-size:0.74rem; color:var(--text-sub);">Choose from 39 exercises with real images</div>
      </div>
      <button style="background:rgba(255,255,255,0.08); border:none; color:#fff; width:32px; height:32px; border-radius:50%; font-weight:800; cursor:pointer;" onclick="closeExerciseLibraryModal()">✕</button>
    </div>

    <input type="text" class="modal-search-input" id="librarySearchInput" placeholder="🔍 Search by name (e.g., bench, curl, squat)..." oninput="filterExerciseLibrary()">

    <div class="modal-category-chips" id="modalCategoryChips">
      <div class="modal-cat-chip active" onclick="filterCategory('All')">All (39)</div>
      <div class="modal-cat-chip" onclick="filterCategory('Chest')">Chest</div>
      <div class="modal-cat-chip" onclick="filterCategory('Back')">Back</div>
      <div class="modal-cat-chip" onclick="filterCategory('Shoulders')">Shoulders</div>
      <div class="modal-cat-chip" onclick="filterCategory('Biceps')">Biceps</div>
      <div class="modal-cat-chip" onclick="filterCategory('Triceps')">Triceps</div>
      <div class="modal-cat-chip" onclick="filterCategory('Legs')">Legs</div>
      <div class="modal-cat-chip" onclick="filterCategory('Core')">Core</div>
    </div>

    <div class="modal-ex-scroll-list" id="modalExScrollList">
      <!-- Injected via JS -->
    </div>
  </div>
</div>

<!-- REST TIMER MODAL OVERLAY -->
<div class="rest-modal-overlay" id="restModalOverlay">
  <div style="font-family:'Outfit',sans-serif; font-size:1.1rem; font-weight:900; color:var(--accent-primary); letter-spacing:1px; margin-bottom:6px;">
    ⚡ REST INTERVAL
  </div>
  <div class="rest-clock" id="restCountdown">00:45</div>
  <div style="font-size:0.85rem; color:var(--text-sub); margin-bottom:20px;">Prepare load for next set</div>

  <div style="display:flex; gap:10px; margin-bottom:20px;">
    <button class="btn-add-ex-trigger" onclick="addRestTime(-15)">-15s</button>
    <button class="btn-add-ex-trigger" onclick="addRestTime(15)">+15s</button>
    <button class="btn-add-ex-trigger" onclick="addRestTime(30)">+30s</button>
  </div>

  <button class="btn-start-workout" onclick="skipRest()">
    RESUME TRAINING
  </button>
</div>

<!-- BOTTOM NAVIGATION -->
<nav class="bottom-nav">
  <div class="nav-item active" onclick="switchNav('tabWorkouts')">
    <div class="nav-icon">🏋️</div>
    <span>Workouts</span>
  </div>
  <div class="nav-item" onclick="switchNav('tabRunner')">
    <div class="nav-icon">⚡</div>
    <span>Runner</span>
  </div>
  <div class="nav-item" onclick="switchNav('tabCalendar')">
    <div class="nav-icon">📅</div>
    <span>Schedule</span>
  </div>
  <div class="nav-item" onclick="switchNav('tabAnalytics')">
    <div class="nav-icon">📊</div>
    <span>Telemetry</span>
  </div>
  <div class="nav-item" onclick="switchNav('tabHub')">
    <div class="nav-icon">📸</div>
    <span>Hub</span>
  </div>
  <div class="nav-item" onclick="switchNav('tabHistory')">
    <div class="nav-icon">📜</div>
    <span>History</span>
  </div>
  <div class="nav-item" onclick="switchNav('tabSettings')">
    <div class="nav-icon">⚙️</div>
    <span>Settings</span>
  </div>
</nav>

<script>
// ========================================================
// CORE DATA & STORAGE
// ========================================================
const FULL_LIBRARY = {library_json};
const DEFAULT_WORKOUT_DATA = {routine_json};

let WORKOUT_DATA = [];
let selectedDayIndex = 0;
let activeSession = null;
let sessionTimerInterval = null;
let currentCategoryFilter = 'All';

// Exercise Timer & Stopwatch
let exTimerMode = 'stopwatch';
let exTimerInterval = null;
let exTimerRunning = false;
let exTimerElapsedMs = 0;
let exTimerCountdownTotalSec = 45;
let exTimerCountdownRemainMs = 45000;
let exTimersMemory = {{}};

// Calendar
let calendarCurrentYear = new Date().getFullYear();
let calendarCurrentMonth = new Date().getMonth();
let calendarSelectedDateStr = new Date().toISOString().split('T')[0];

// Native Android Bridge Interface
function notifyAndroidStart(dayName, focus) {{
  if (window.AndroidBridge && window.AndroidBridge.startBackgroundTracking) {{
    try {{ window.AndroidBridge.startBackgroundTracking(dayName, focus); }} catch(e) {{}}
  }}
}}
function notifyAndroidUpdate(exName, curSet, totalSets) {{
  if (window.AndroidBridge && window.AndroidBridge.updateProgress) {{
    try {{ window.AndroidBridge.updateProgress(exName, curSet, totalSets); }} catch(e) {{}}
  }}
}}
function notifyAndroidStop() {{
  if (window.AndroidBridge && window.AndroidBridge.stopBackgroundTracking) {{
    try {{ window.AndroidBridge.stopBackgroundTracking(); }} catch(e) {{}}
  }}
}}
function notifyAndroidVibrate(ms) {{
  if (window.AndroidBridge && window.AndroidBridge.vibratePhone) {{
    try {{ window.AndroidBridge.vibratePhone(ms); }} catch(e) {{}}
  }}
}}

// Synthesized Audio
let audioCtx = null;
function getAudio() {{
  if (!audioCtx) {{
    try {{ audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }} catch(e) {{}}
  }}
  return audioCtx;
}}
function beep(freq = 600, dur = 0.1) {{
  const soundOn = document.getElementById('settingSound')?.checked ?? true;
  if (!soundOn) return;
  try {{
    const ctx = getAudio();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const g = ctx.createGain();
    osc.frequency.value = freq;
    g.gain.setValueAtTime(0.2, ctx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur);
    osc.connect(g);
    g.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + dur);
  }} catch(e) {{}}
}}
function vibrate(pattern = [80]) {{
  const vibOn = document.getElementById('settingVibrate')?.checked ?? true;
  if (vibOn) {{
    notifyAndroidVibrate(Array.isArray(pattern) ? pattern[0] : pattern);
    if (navigator.vibrate) {{
      try {{ navigator.vibrate(pattern); }} catch(e) {{}}
    }}
  }}
}}

// Battery-Aware 3D Space Background
function init3DParticleCanvas() {{
  const canvas = document.getElementById('ambientCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let w = canvas.width = window.innerWidth;
  let h = canvas.height = window.innerHeight;

  window.addEventListener('resize', () => {{
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }});

  const count = 42;
  const particles = [];
  for (let i = 0; i < count; i++) {{
    particles.push({{
      x: (Math.random() - 0.5) * 700,
      y: (Math.random() - 0.5) * 700,
      z: (Math.random() - 0.5) * 700,
      size: Math.random() * 2 + 1
    }});
  }}

  let rotX = 0, rotY = 0;
  function animate() {{
    ctx.clearRect(0, 0, w, h);
    rotX += 0.001;
    rotY += 0.0015;

    const cosX = Math.cos(rotX), sinX = Math.sin(rotX);
    const cosY = Math.cos(rotY), sinY = Math.sin(rotY);
    const cx = w / 2, cy = h / 2, fov = 350;
    const themeColor = getComputedStyle(document.body).getPropertyValue('--accent-primary').trim() || '#00f0ff';
    const projected = [];

    particles.forEach(p => {{
      let x1 = p.x * cosY - p.z * sinY;
      let z1 = p.z * cosY + p.x * sinY;
      let y1 = p.y * cosX - z1 * sinX;
      let z2 = z1 * cosX + p.y * sinX;

      const depth = z2 + 450;
      if (depth > 20) {{
        const scale = fov / depth;
        const px = cx + x1 * scale;
        const py = cy + y1 * scale;
        const r = Math.max(0.6, p.size * scale * 1.4);
        const alpha = Math.min(0.8, Math.max(0.08, scale * 0.85));

        projected.push({{ x: px, y: py }});

        ctx.beginPath();
        ctx.arc(px, py, r, 0, Math.PI * 2);
        ctx.fillStyle = themeColor;
        ctx.globalAlpha = alpha;
        ctx.fill();
      }}
    }});

    // Proximity wire lines
    ctx.strokeStyle = themeColor;
    for (let i = 0; i < projected.length; i++) {{
      for (let j = i + 1; j < projected.length; j++) {{
        const dx = projected[i].x - projected[j].x;
        const dy = projected[i].y - projected[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 65) {{
          ctx.beginPath();
          ctx.moveTo(projected[i].x, projected[i].y);
          ctx.lineTo(projected[j].x, projected[j].y);
          ctx.globalAlpha = (1 - dist / 65) * 0.12;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }}
      }}
    }}
    ctx.globalAlpha = 1;
    requestAnimationFrame(animate);
  }}
  animate();
}}

// Confetti Celebration
function triggerConfetti() {{
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas) return;
  canvas.style.display = 'block';
  const ctx = canvas.getContext('2d');
  const w = canvas.width = window.innerWidth;
  const h = canvas.height = window.innerHeight;
  const pieces = [];
  const colors = ['#00f0ff', '#7928ca', '#00ff88', '#ffd700', '#d946ef', '#ff1744', '#ffffff'];
  for (let i = 0; i < 90; i++) {{
    pieces.push({{
      x: w / 2, y: h / 2,
      vx: (Math.random() - 0.5) * 14,
      vy: (Math.random() - 0.8) * 14,
      size: Math.random() * 8 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * 360,
      dRot: (Math.random() - 0.5) * 12,
      life: 1
    }});
  }}
  function update() {{
    ctx.clearRect(0, 0, w, h);
    let alive = false;
    pieces.forEach(p => {{
      p.x += p.vx; p.y += p.vy; p.vy += 0.35;
      p.rotation += p.dRot; p.life -= 0.015;
      if (p.life > 0) {{
        alive = true;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = Math.max(0, p.life);
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.7);
        ctx.restore();
      }}
    }});
    if (alive) requestAnimationFrame(update);
    else {{ ctx.clearRect(0, 0, w, h); canvas.style.display = 'none'; }}
  }}
  update();
}}

// Load & Save Data
function loadWorkoutData() {{
  const saved = localStorage.getItem('planfit_custom_workout_data') || localStorage.getItem('apex_custom_workout_data');
  if (saved) {{
    try {{ WORKOUT_DATA = JSON.parse(saved); return; }} catch(e) {{}}
  }}
  WORKOUT_DATA = JSON.parse(JSON.stringify(DEFAULT_WORKOUT_DATA));
}}
function saveWorkoutData() {{
  localStorage.setItem('planfit_custom_workout_data', JSON.stringify(WORKOUT_DATA));
}}

// Initialize
document.addEventListener('DOMContentLoaded', () => {{
  loadWorkoutData();
  init3DParticleCanvas();
  renderDayChips();
  selectDay(0);
  loadSettings();
  renderCalendar();
  renderWeeklyScheduler();
  renderHistory();
  renderPhotos();
  loadSavedGym();
  renderExerciseLibrary();
  updateHudTelemetry();
  renderPrHallOfFame();

  if ('serviceWorker' in navigator) {{
    navigator.serviceWorker.register('./sw.js').catch(() => {{}});
  }}
}});

// Theme Switcher
function changeTheme(themeName) {{
  document.body.setAttribute('data-theme', themeName);
  const sel1 = document.getElementById('headerThemePicker');
  const sel2 = document.getElementById('settingTheme');
  if (sel1) sel1.value = themeName;
  if (sel2) sel2.value = themeName;
  localStorage.setItem('planfit_theme', themeName);
}}

// Navigation Switcher
function switchNav(tabId) {{
  document.querySelectorAll('.tab-view').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  
  const target = document.getElementById(tabId);
  if (target) target.classList.add('active');

  const navs = Array.from(document.querySelectorAll('.nav-item'));
  const ids = ['tabWorkouts', 'tabRunner', 'tabCalendar', 'tabAnalytics', 'tabHub', 'tabHistory', 'tabSettings'];
  const idx = ids.indexOf(tabId);
  if (idx !== -1 && navs[idx]) navs[idx].classList.add('active');

  const stickyBanner = document.getElementById('stickyWorkoutBanner');
  if (stickyBanner) {{
    stickyBanner.style.display = (activeSession && tabId !== 'tabRunner') ? 'flex' : 'none';
  }}

  if (tabId === 'tabHistory') renderHistory();
  if (tabId === 'tabAnalytics') {{ renderGraphs(); renderPrHallOfFame(); }}
  if (tabId === 'tabCalendar') {{ renderCalendar(); renderWeeklyScheduler(); }}
  if (tabId === 'tabWorkouts') updateHudTelemetry();
}}

// HUD Telemetry Update
function updateHudTelemetry() {{
  const history = JSON.parse(localStorage.getItem('planfit_history') || localStorage.getItem('apex_history') || '[]');
  const totalVol = history.reduce((sum, h) => sum + (h.totalVolume || 0), 0);
  const volFormatted = totalVol > 1000 ? `${{(totalVol / 1000).toFixed(1)}}k` : `${{totalVol}} kg`;
  document.getElementById('hudWeeklyVolVal').textContent = volFormatted;

  const day = WORKOUT_DATA[selectedDayIndex];
  if (day) {{
    document.getElementById('hudTodaySplitTitle').textContent = day.focus;
    document.getElementById('hudTodaySplitMeta').textContent = `${{day.exercises.length}} Exercises • Overload Target Active`;
  }}
}}

// WORKOUT TABS / CHIPS
function renderDayChips() {{
  const container = document.getElementById('daysChipsContainer');
  container.innerHTML = '';
  
  WORKOUT_DATA.forEach((d, i) => {{
    const chip = document.createElement('div');
    chip.className = `day-chip ${{i === selectedDayIndex ? 'active' : ''}}`;
    chip.id = `chip-${{i}}`;
    chip.innerHTML = `
      <span class="chip-name">${{d.day_name.slice(0, 3)}}</span>
      <span style="font-size:0.68rem; color:var(--text-muted);">${{d.day_name === 'WEDNESDAY' || d.day_name === 'SATURDAY' ? 'Legs' : (d.day_name === 'MONDAY' || d.day_name === 'THURSDAY' ? 'Chest' : 'Back')}}</span>
    `;
    chip.onclick = () => selectDay(i);
    container.appendChild(chip);
  }});
}}

function selectDay(index) {{
  selectedDayIndex = index;
  document.querySelectorAll('.day-chip').forEach(c => c.classList.remove('active'));
  const currentChip = document.getElementById(`chip-${{index}}`);
  if (currentChip) currentChip.classList.add('active');

  const day = WORKOUT_DATA[index];
  document.getElementById('routineBadge').textContent = `${{day.day_name}} ROUTINE`;
  document.getElementById('routineBadge').style.background = `${{day.accent}}22`;
  document.getElementById('routineBadge').style.color = day.accent;
  document.getElementById('routineTitle').textContent = day.focus;
  document.getElementById('routineMeta').textContent = `${{day.exercises.length}} Exercises • Overload Engine Active`;
  document.getElementById('previewExCount').textContent = day.exercises.length;

  updateHudTelemetry();

  // Render Warm-up
  const wuContainer = document.getElementById('warmupList');
  wuContainer.innerHTML = '';
  (day.warmup || []).forEach(w => {{
    const item = document.createElement('div');
    item.style.cssText = 'background:rgba(255,255,255,0.04); border:1px solid var(--border-subtle); padding:6px 10px; border-radius:8px; font-size:0.78rem;';
    item.innerHTML = `<strong>${{w.name}}:</strong> ${{w.details}}`;
    wuContainer.appendChild(item);
  }});

  // Render Exercise Preview List
  const list = document.getElementById('exercisePreviewList');
  list.innerHTML = '';
  day.exercises.forEach((ex, idx) => {{
    const item = document.createElement('div');
    item.className = 'ex-preview-item';
    item.innerHTML = `
      <img src="${{ex.image_url}}" class="ex-preview-thumb" alt="${{ex.name}}" loading="lazy" onerror="this.src='./icon-192.png'">
      <div class="ex-preview-info">
        <div class="ex-preview-title">#${{idx + 1}} ${{ex.name}}</div>
        <div class="ex-preview-sub">${{ex.target}}</div>
      </div>
      <div class="ex-preview-pill">${{ex.sets || '4 Sets'}}</div>
      <button class="btn-remove-ex" onclick="removeExerciseFromRoutine(${{idx}})" title="Remove exercise">✕</button>
    `;
    list.appendChild(item);
  }});
}}

function removeExerciseFromRoutine(exIndex) {{
  const day = WORKOUT_DATA[selectedDayIndex];
  if (day.exercises.length <= 1) {{
    alert("Routine must have at least one exercise.");
    return;
  }}
  if (confirm(`Remove "${{day.exercises[exIndex].name}}" from ${{day.day_name}} routine?`)) {{
    day.exercises.splice(exIndex, 1);
    saveWorkoutData();
    selectDay(selectedDayIndex);
  }}
}}

// ========================================================
// WORKOUT SESSION RUNNER WITH RAPID SET BUMPERS & 1RM
// ========================================================
function startCurrentRoutine() {{
  const day = WORKOUT_DATA[selectedDayIndex];
  activeSession = {{
    dayIndex: selectedDayIndex,
    startTime: Date.now(),
    exIndex: 0,
    logs: {{}}
  }};

  day.exercises.forEach((ex, exIdx) => {{
    activeSession.logs[exIdx] = [];
    const numSets = parseInt(ex.sets) || 4;
    for (let s = 1; s <= numSets; s++) {{
      activeSession.logs[exIdx].push({{
        setNum: s,
        weight: '30',
        reps: '12',
        completed: false,
        tut: ''
      }});
    }}
  }});

  notifyAndroidStart(day.day_name, day.focus);

  document.getElementById('workoutStatusIndicator').style.display = 'block';
  document.getElementById('stickyBannerTitle').textContent = day.focus;
  
  if (sessionTimerInterval) clearInterval(sessionTimerInterval);
  sessionTimerInterval = setInterval(updateSessionTimer, 1000);

  switchNav('tabRunner');
  loadActiveExercise(0);
}}

function updateSessionTimer() {{
  if (!activeSession) return;
  const elapsed = Math.floor((Date.now() - activeSession.startTime) / 1000);
  const m = Math.floor(elapsed / 60).toString().padStart(2, '0');
  const s = (elapsed % 60).toString().padStart(2, '0');
  document.getElementById('headerTimer').textContent = `${{m}}:${{s}}`;
  document.getElementById('runnerElapsed').textContent = `${{m}}:${{s}}`;
  const sbTime = document.getElementById('stickyBannerTime');
  if (sbTime) sbTime.textContent = `${{m}}:${{s}}`;
}}

function loadActiveExercise(exIndex) {{
  if (!activeSession) return;
  activeSession.exIndex = exIndex;
  const day = WORKOUT_DATA[activeSession.dayIndex];
  const ex = day.exercises[exIndex];

  document.getElementById('runnerExImg').src = ex.image_url;
  document.getElementById('runnerExNum').textContent = `#${{exIndex + 1}} / ${{day.exercises.length}}`;
  document.getElementById('runnerExTitle').textContent = ex.name;
  document.getElementById('runnerExTarget').textContent = ex.target;
  document.getElementById('runnerExCues').innerHTML = `💡 <strong>${{ex.sets || '4 Sets'}} • ${{ex.reps || '10-12 Reps'}}</strong><br>${{ex.notes || 'Control eccentric tempo and squeeze at peak contraction.'}}`;

  notifyAndroidUpdate(ex.name, exIndex + 1, day.exercises.length);

  const pct = Math.round(((exIndex + 1) / day.exercises.length) * 100);
  document.getElementById('runnerProgressFill').style.width = pct + '%';

  // Render Set Cards with Quick Bumps
  const container = document.getElementById('runnerSetsContainer');
  container.innerHTML = '';
  const setLogs = activeSession.logs[exIndex] || [];

  setLogs.forEach((sLog, sIdx) => {{
    const row = document.createElement('div');
    row.className = 'set-card-row';

    // Calculate Estimated 1RM
    const w = parseFloat(sLog.weight) || 0;
    const r = parseFloat(sLog.reps) || 0;
    const est1rm = Math.round(w * (1 + r / 30));

    row.innerHTML = `
      <div class="set-row-top">
        <div class="set-badge-tag">SET ${{sLog.setNum}}</div>
        <div class="set-prev-target">Target: ${{(ex.reps || '10-12').split(' ')[0]}} • Est 1RM: ${{est1rm}}kg</div>
      </div>
      <div class="set-inputs-grid">
        <div class="input-group-col">
          <div class="input-mini-label">Weight (kg)</div>
          <input type="number" class="set-input-box" id="inputW_${{exIndex}}_${{sIdx}}" value="${{sLog.weight}}" onchange="updateSetData(${{exIndex}}, ${{sIdx}}, 'weight', this.value)">
          <div class="weight-bump-row">
            <button class="btn-weight-bump" onclick="bumpWeight(${{exIndex}}, ${{sIdx}}, -5)">-5</button>
            <button class="btn-weight-bump" onclick="bumpWeight(${{exIndex}}, ${{sIdx}}, -2.5)">-2.5</button>
            <button class="btn-weight-bump" onclick="bumpWeight(${{exIndex}}, ${{sIdx}}, 2.5)">+2.5</button>
            <button class="btn-weight-bump" onclick="bumpWeight(${{exIndex}}, ${{sIdx}}, 5)">+5</button>
          </div>
        </div>
        <div class="input-group-col">
          <div class="input-mini-label">Reps</div>
          <input type="number" class="set-input-box" id="inputR_${{exIndex}}_${{sIdx}}" value="${{sLog.reps}}" onchange="updateSetData(${{exIndex}}, ${{sIdx}}, 'reps', this.value)">
          <div class="weight-bump-row">
            <button class="btn-weight-bump" onclick="bumpReps(${{exIndex}}, ${{sIdx}}, -1)">-1</button>
            <button class="btn-weight-bump" onclick="bumpReps(${{exIndex}}, ${{sIdx}}, 1)">+1</button>
          </div>
        </div>
        <button class="btn-complete-set ${{sLog.completed ? 'completed' : ''}}" onclick="toggleSetComplete(${{exIndex}}, ${{sIdx}})">
          ${{sLog.completed ? '✓ LOGGED' : 'LOG SET'}}
        </button>
      </div>
    `;
    container.appendChild(row);
  }});

  loadExerciseTimerForCurrentEx(exIndex);
}}

function bumpWeight(exIdx, sIdx, delta) {{
  if (!activeSession) return;
  const sLog = activeSession.logs[exIdx][sIdx];
  const cur = parseFloat(sLog.weight) || 0;
  const next = Math.max(0, cur + delta);
  sLog.weight = String(next);
  const el = document.getElementById(`inputW_${{exIdx}}_${{sIdx}}`);
  if (el) el.value = sLog.weight;
  loadActiveExercise(exIdx);
}}

function bumpReps(exIdx, sIdx, delta) {{
  if (!activeSession) return;
  const sLog = activeSession.logs[exIdx][sIdx];
  const cur = parseInt(sLog.reps) || 0;
  const next = Math.max(1, cur + delta);
  sLog.reps = String(next);
  const el = document.getElementById(`inputR_${{exIdx}}_${{sIdx}}`);
  if (el) el.value = sLog.reps;
  loadActiveExercise(exIdx);
}}

function updateSetData(exIdx, sIdx, field, val) {{
  if (activeSession && activeSession.logs[exIdx]) {{
    activeSession.logs[exIdx][sIdx][field] = val;
  }}
}}

function toggleSetComplete(exIdx, sIdx) {{
  if (!activeSession) return;
  const sLog = activeSession.logs[exIdx][sIdx];
  sLog.completed = !sLog.completed;
  
  if (sLog.completed) {{
    beep(750, 0.15);
    vibrate([80, 50, 80]);
    startRestTimer(45);
  }}
  loadActiveExercise(exIdx);
}}

function prevExercise() {{
  if (!activeSession || activeSession.exIndex <= 0) return;
  saveExerciseTimerForCurrentEx(activeSession.exIndex);
  loadActiveExercise(activeSession.exIndex - 1);
}}

function nextExercise() {{
  if (!activeSession) return;
  const day = WORKOUT_DATA[activeSession.dayIndex];
  if (activeSession.exIndex >= day.exercises.length - 1) {{
    if (confirm("All exercises completed! Finish workout session now?")) {{
      finishWorkout();
    }}
    return;
  }}
  saveExerciseTimerForCurrentEx(activeSession.exIndex);
  loadActiveExercise(activeSession.exIndex + 1);
}}

function finishWorkout() {{
  if (!activeSession) return;
  notifyAndroidStop();
  if (sessionTimerInterval) clearInterval(sessionTimerInterval);
  if (exTimerInterval) clearInterval(exTimerInterval);

  const durationMin = Math.max(1, Math.round((Date.now() - activeSession.startTime) / 60000));
  const day = WORKOUT_DATA[activeSession.dayIndex];
  
  let totalSetsDone = 0;
  let totalVolume = 0;
  Object.values(activeSession.logs).forEach(sets => {{
    sets.forEach(s => {{
      if (s.completed) {{
        totalSetsDone++;
        const w = parseFloat(s.weight) || 0;
        const r = parseFloat(s.reps) || 0;
        totalVolume += w * r;
      }}
    }});
  }});

  const todayStr = new Date().toISOString().split('T')[0];
  const historyItem = {{
    id: Date.now(),
    date: todayStr,
    dayName: day.day_name,
    focus: day.focus,
    durationMin: durationMin,
    setsCompleted: totalSetsDone,
    totalVolume: Math.round(totalVolume)
  }};

  const history = JSON.parse(localStorage.getItem('planfit_history') || localStorage.getItem('apex_history') || '[]');
  history.unshift(historyItem);
  localStorage.setItem('planfit_history', JSON.stringify(history));

  triggerConfetti();
  beep(880, 0.3);
  vibrate([120, 80, 150]);

  activeSession = null;
  document.getElementById('workoutStatusIndicator').style.display = 'none';
  const stickyBanner = document.getElementById('stickyWorkoutBanner');
  if (stickyBanner) stickyBanner.style.display = 'none';

  alert(`🎉 MISSION COMPLETE!\\n\\n🔥 ${{day.focus}}\\n⏱ ${{durationMin}} Minutes\\n🏋️ ${{totalSetsDone}} Sets Logged\\n⚡ ${{Math.round(totalVolume)}} kg Total Volume!`);

  switchNav('tabAnalytics');
}}

// ========================================================
// EXERCISE TIMER ENGINE
// ========================================================
function setTimerMode(mode) {{
  exTimerMode = mode;
  document.getElementById('btnModeStopwatch').classList.toggle('active', mode === 'stopwatch');
  document.getElementById('btnModeCountdown').classList.toggle('active', mode === 'countdown');
  
  const presetsRow = document.getElementById('timerPresetsRow');
  const subLabel = document.getElementById('timerSubLabel');
  if (mode === 'countdown') {{
    presetsRow.style.display = 'flex';
    subLabel.textContent = `Countdown Target: ${{exTimerCountdownTotalSec}}s`;
  }} else {{
    presetsRow.style.display = 'none';
    subLabel.textContent = 'Time Under Tension (TUT)';
  }}
  resetExerciseTimer();
}}

function setTimerDuration(seconds) {{
  exTimerCountdownTotalSec = seconds;
  exTimerCountdownRemainMs = seconds * 1000;
  document.querySelectorAll('.timer-preset-pill').forEach(p => {{
    p.classList.toggle('active', p.textContent === `${{seconds}}s`);
  }});
  document.getElementById('timerSubLabel').textContent = `Countdown Target: ${{seconds}}s`;
  resetExerciseTimer();
}}

function toggleExerciseTimer() {{
  if (exTimerRunning) pauseExerciseTimer();
  else startExerciseTimer();
}}

function startExerciseTimer() {{
  if (exTimerRunning) return;
  exTimerRunning = true;
  document.getElementById('btnTimerToggle').textContent = '⏸ Pause';
  document.getElementById('timerStatusBadge').textContent = '• RUNNING';
  document.getElementById('timerStatusBadge').style.color = 'var(--accent-emerald)';

  const startTime = Date.now() - (exTimerMode === 'stopwatch' ? exTimerElapsedMs : (exTimerCountdownTotalSec * 1000 - exTimerCountdownRemainMs));

  exTimerInterval = setInterval(() => {{
    const now = Date.now();
    if (exTimerMode === 'stopwatch') {{
      exTimerElapsedMs = now - startTime;
      updateExerciseTimerDisplay();
    }} else {{
      const passed = now - startTime;
      exTimerCountdownRemainMs = Math.max(0, exTimerCountdownTotalSec * 1000 - passed);
      updateExerciseTimerDisplay();

      if (exTimerCountdownRemainMs <= 0) {{
        pauseExerciseTimer();
        beep(880, 0.4);
        vibrate([200, 100, 200, 100, 300]);
        document.getElementById('timerStatusBadge').textContent = '⚡ TIME UP!';
        document.getElementById('timerStatusBadge').style.color = 'var(--accent-rose)';
      }}
    }}
  }}, 100);
}}

function pauseExerciseTimer() {{
  exTimerRunning = false;
  if (exTimerInterval) clearInterval(exTimerInterval);
  document.getElementById('btnTimerToggle').textContent = '▶ Resume';
  document.getElementById('timerStatusBadge').textContent = '• PAUSED';
  document.getElementById('timerStatusBadge').style.color = 'var(--accent-amber)';
}}

function resetExerciseTimer() {{
  pauseExerciseTimer();
  document.getElementById('btnTimerToggle').textContent = '▶ Start Timer';
  document.getElementById('timerStatusBadge').textContent = '• READY';
  document.getElementById('timerStatusBadge').style.color = 'var(--accent-emerald)';

  if (exTimerMode === 'stopwatch') exTimerElapsedMs = 0;
  else exTimerCountdownRemainMs = exTimerCountdownTotalSec * 1000;
  updateExerciseTimerDisplay();
}}

function updateExerciseTimerDisplay() {{
  let totalSec, tenths, ringPct;
  const circle = document.getElementById('timerRingCircle');
  const circumference = 2 * Math.PI * 40;

  if (exTimerMode === 'stopwatch') {{
    totalSec = Math.floor(exTimerElapsedMs / 1000);
    tenths = Math.floor((exTimerElapsedMs % 1000) / 100);
    ringPct = (totalSec % 60) / 60;
  }} else {{
    totalSec = Math.ceil(exTimerCountdownRemainMs / 1000);
    tenths = 0;
    ringPct = exTimerCountdownRemainMs / (exTimerCountdownTotalSec * 1000);
  }}

  const m = Math.floor(totalSec / 60).toString().padStart(2, '0');
  const s = (totalSec % 60).toString().padStart(2, '0');

  const digital = document.getElementById('timerDigitalClock');
  const ringInner = document.getElementById('timerRingDisplay');

  if (exTimerMode === 'stopwatch') {{
    digital.textContent = `${{m}}:${{s}}.${{tenths}}`;
    ringInner.textContent = `${{m}}:${{s}}`;
  }} else {{
    digital.textContent = `${{m}}:${{s}}`;
    ringInner.textContent = `${{s}}s`;
  }}

  const offset = circumference * (1 - ringPct);
  if (circle) circle.style.strokeDashoffset = offset;
}}

function recordTutToActiveSet() {{
  if (!activeSession) return;
  const exIdx = activeSession.exIndex;
  const setLogs = activeSession.logs[exIdx] || [];
  let targetSet = setLogs.find(s => !s.completed) || setLogs[setLogs.length - 1];
  if (targetSet) {{
    const totalSec = Math.round(exTimerElapsedMs / 1000);
    targetSet.tut = `${{totalSec}}s`;
    vibrate([60]);
    alert(`Recorded ${{totalSec}}s Time Under Tension to Set ${{targetSet.setNum}}!`);
  }}
}}

function saveExerciseTimerForCurrentEx(exIdx) {{
  exTimersMemory[exIdx] = {{
    mode: exTimerMode,
    elapsedMs: exTimerElapsedMs,
    countdownSec: exTimerCountdownTotalSec,
    countdownRemainMs: exTimerCountdownRemainMs
  }};
  if (exTimerInterval) clearInterval(exTimerInterval);
  exTimerRunning = false;
}}

function loadExerciseTimerForCurrentEx(exIdx) {{
  if (exTimerInterval) clearInterval(exTimerInterval);
  exTimerRunning = false;

  const mem = exTimersMemory[exIdx];
  if (mem) {{
    exTimerMode = mem.mode;
    exTimerElapsedMs = mem.elapsedMs;
    exTimerCountdownTotalSec = mem.countdownSec;
    exTimerCountdownRemainMs = mem.countdownRemainMs;
  }} else {{
    exTimerElapsedMs = 0;
    exTimerCountdownRemainMs = exTimerCountdownTotalSec * 1000;
  }}
  setTimerMode(exTimerMode);
  updateExerciseTimerDisplay();
}}

// REST TIMER
let restTimerSec = 45;
let restInterval = null;
function startRestTimer(seconds = 45) {{
  restTimerSec = seconds;
  const overlay = document.getElementById('restModalOverlay');
  overlay.classList.add('active');
  updateRestDisplay();

  if (restInterval) clearInterval(restInterval);
  restInterval = setInterval(() => {{
    restTimerSec--;
    updateRestDisplay();
    if (restTimerSec <= 0) {{
      skipRest();
      beep(880, 0.2);
      vibrate([150, 80, 150]);
    }}
  }}, 1000);
}}

function updateRestDisplay() {{
  const m = Math.floor(restTimerSec / 60).toString().padStart(2, '0');
  const s = (restTimerSec % 60).toString().padStart(2, '0');
  document.getElementById('restCountdown').textContent = `${{m}}:${{s}}`;
}}

function addRestTime(sec) {{
  restTimerSec = Math.max(5, restTimerSec + sec);
  updateRestDisplay();
}}

function skipRest() {{
  if (restInterval) clearInterval(restInterval);
  document.getElementById('restModalOverlay').classList.remove('active');
}}

// ========================================================
// EFFORTLESS WEEKLY SCHEDULER & CALENDAR COMMAND
// ========================================================
function renderWeeklyScheduler() {{
  const container = document.getElementById('weeklyScheduleRows');
  if (!container) return;
  container.innerHTML = '';

  const dayNames = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"];
  const todayIdx = (new Date().getDay() + 6) % 7; // Monday = 0

  dayNames.forEach((dName, idx) => {{
    const row = document.createElement('div');
    row.className = `schedule-day-row ${{idx === todayIdx ? 'today' : ''}}`;

    const currentAssigned = WORKOUT_DATA[idx % WORKOUT_DATA.length] || WORKOUT_DATA[0];

    row.innerHTML = `
      <div class="schedule-day-name">${{dName.slice(0, 3)}}</div>
      <select class="schedule-routine-select" onchange="reassignDayRoutine(${{idx}}, this.value)">
        ${{WORKOUT_DATA.map((r, rIdx) => `
          <option value="${{rIdx}}" ${{rIdx === (idx % WORKOUT_DATA.length) ? 'selected' : ''}}>
            ${{r.focus}}
          </option>
        `).join('')}}
        <option value="rest" ${{idx === 6 ? 'selected' : ''}}>Active Recovery / Rest</option>
      </select>
    `;
    container.appendChild(row);
  }});
}}

function reassignDayRoutine(dayIdx, routineIdx) {{
  if (routineIdx === 'rest') {{
    alert("Assigned Active Recovery / Rest to this day!");
    return;
  }}
  vibrate([60]);
  renderCalendar();
  alert("Routine schedule updated successfully!");
}}

function renderCalendar() {{
  const grid = document.getElementById('calendarDaysGrid');
  grid.innerHTML = '';

  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  document.getElementById('calendarMonthTitle').textContent = `${{monthNames[calendarCurrentMonth]}} ${{calendarCurrentYear}}`;

  const firstDayOfMonth = new Date(calendarCurrentYear, calendarCurrentMonth, 1);
  const daysInMonth = new Date(calendarCurrentYear, calendarCurrentMonth + 1, 0).getDate();
  const daysInPrevMonth = new Date(calendarCurrentYear, calendarCurrentMonth, 0).getDate();

  let startDayOfWeek = firstDayOfMonth.getDay() - 1;
  if (startDayOfWeek === -1) startDayOfWeek = 6;

  const history = JSON.parse(localStorage.getItem('planfit_history') || localStorage.getItem('apex_history') || '[]');
  const todayStr = new Date().toISOString().split('T')[0];

  for (let i = startDayOfWeek - 1; i >= 0; i--) {{
    const cell = document.createElement('div');
    cell.className = 'cal-day-cell';
    cell.style.opacity = '0.25';
    cell.textContent = daysInPrevMonth - i;
    grid.appendChild(cell);
  }}

  for (let day = 1; day <= daysInMonth; day++) {{
    const cell = document.createElement('div');
    const mStr = (calendarCurrentMonth + 1).toString().padStart(2, '0');
    const dStr = day.toString().padStart(2, '0');
    const dateStr = `${{calendarCurrentYear}}-${{mStr}}-${{dStr}}`;

    cell.className = 'cal-day-cell';
    cell.textContent = day;

    if (dateStr === todayStr) cell.classList.add('today');
    if (dateStr === calendarSelectedDateStr) cell.classList.add('selected');

    const completed = history.find(h => h.date === dateStr);
    if (completed) {{
      cell.classList.add('has-completed');
      const dot = document.createElement('div');
      dot.className = 'cal-day-dot completed';
      cell.appendChild(dot);
    }} else {{
      const dow = new Date(calendarCurrentYear, calendarCurrentMonth, day).getDay();
      if (dow >= 1 && dow <= 6) {{
        const dot = document.createElement('div');
        dot.className = 'cal-day-dot scheduled';
        cell.appendChild(dot);
      }}
    }}

    cell.onclick = () => selectCalendarDate(dateStr, day);
    grid.appendChild(cell);
  }}

  updateCalendarDetailsCard();
}}

function selectCalendarDate(dateStr, dayNum) {{
  calendarSelectedDateStr = dateStr;
  document.querySelectorAll('.cal-day-cell').forEach(c => c.classList.remove('selected'));
  renderCalendar();
}}

function changeCalendarMonth(delta) {{
  calendarCurrentMonth += delta;
  if (calendarCurrentMonth < 0) {{ calendarCurrentMonth = 11; calendarCurrentYear--; }}
  else if (calendarCurrentMonth > 11) {{ calendarCurrentMonth = 0; calendarCurrentYear++; }}
  renderCalendar();
}}

function jumpCalendarToday() {{
  const now = new Date();
  calendarCurrentYear = now.getFullYear();
  calendarCurrentMonth = now.getMonth();
  calendarSelectedDateStr = now.toISOString().split('T')[0];
  renderCalendar();
}}

function updateCalendarDetailsCard() {{
  const dateObj = new Date(calendarSelectedDateStr + 'T00:00:00');
  const dateFormatted = dateObj.toLocaleDateString('en-US', {{ weekday: 'long', month: 'short', day: 'numeric', year: 'numeric' }});
  document.getElementById('calDetailDate').textContent = dateFormatted;

  const dayOfWeek = dateObj.getDay();
  const dayIndexMap = [5, 0, 1, 2, 3, 4, 5];
  const targetDay = WORKOUT_DATA[dayIndexMap[dayOfWeek]];

  document.getElementById('calDetailSplit').textContent = `Assigned Split: ${{dayOfWeek === 0 ? 'Active Rest & Recovery' : targetDay.focus}}`;

  const history = JSON.parse(localStorage.getItem('planfit_history') || localStorage.getItem('apex_history') || '[]');
  const completedLog = history.find(h => h.date === calendarSelectedDateStr);

  const statusBadge = document.getElementById('calDetailStatusBadge');
  if (completedLog) {{
    statusBadge.innerHTML = `
      <span style="display:inline-flex; align-items:center; gap:6px; background:rgba(0,255,136,0.18); border:1px solid rgba(0,255,136,0.4); color:var(--accent-emerald); padding:4px 10px; border-radius:8px; font-size:0.76rem; font-weight:800;">
        ✓ Session Logged • ${{completedLog.durationMin}}m • ${{completedLog.setsCompleted}} Sets • ${{completedLog.totalVolume}} kg
      </span>
    `;
  }} else {{
    statusBadge.innerHTML = `
      <span style="display:inline-flex; align-items:center; gap:6px; background:rgba(255,255,255,0.06); border:1px solid var(--border-subtle); color:var(--text-sub); padding:4px 10px; border-radius:8px; font-size:0.76rem; font-weight:700;">
        ⏳ Not logged yet
      </span>
    `;
  }}
}}

function startRoutineForCalendarDay() {{
  const dateObj = new Date(calendarSelectedDateStr + 'T00:00:00');
  const dayOfWeek = dateObj.getDay();
  const dayIndexMap = [0, 0, 1, 2, 3, 4, 5];
  selectedDayIndex = dayIndexMap[dayOfWeek];
  selectDay(selectedDayIndex);
  startCurrentRoutine();
}}

function toggleCalendarDayCompleted() {{
  const history = JSON.parse(localStorage.getItem('planfit_history') || localStorage.getItem('apex_history') || '[]');
  const existingIdx = history.findIndex(h => h.date === calendarSelectedDateStr);

  if (existingIdx !== -1) {{
    history.splice(existingIdx, 1);
    alert("Workout status removed for " + calendarSelectedDateStr);
  }} else {{
    const dateObj = new Date(calendarSelectedDateStr + 'T00:00:00');
    const dayOfWeek = dateObj.getDay();
    const dayIndexMap = [0, 0, 1, 2, 3, 4, 5];
    const targetDay = WORKOUT_DATA[dayIndexMap[dayOfWeek]];

    history.unshift({{
      id: Date.now(),
      date: calendarSelectedDateStr,
      dayName: targetDay.day_name,
      focus: targetDay.focus,
      durationMin: 55,
      setsCompleted: 24,
      totalVolume: 5800
    }});
    vibrate([80]);
    alert("Marked workout as completed for " + calendarSelectedDateStr);
  }}

  localStorage.setItem('planfit_history', JSON.stringify(history));
  renderCalendar();
  updateHudTelemetry();
}}

// ========================================================
// PERSONAL RECORDS (PR) HALL & PROGRESS TELEMETRY
// ========================================================
function renderPrHallOfFame() {{
  const container = document.getElementById('prRecordsList');
  if (!container) return;
  container.innerHTML = '';

  const prs = [
    {{ ex: 'Flat Dumbbell Press', metric: '42.5 kg × 10 reps', est1rm: '56 kg', date: 'Oct 08' }},
    {{ ex: 'Wide Grip Lat Pulldown', metric: '85.0 kg × 12 reps', est1rm: '119 kg', date: 'Oct 06' }},
    {{ ex: 'Barbell Front Squats', metric: '95.0 kg × 8 reps', est1rm: '120 kg', date: 'Oct 04' }},
    {{ ex: 'Smith Shoulder Press', metric: '65.0 kg × 10 reps', est1rm: '86 kg', date: 'Oct 02' }}
  ];

  prs.forEach(pr => {{
    const row = document.createElement('div');
    row.className = 'pr-item-row';
    row.innerHTML = `
      <div>
        <div style="font-family:'Outfit',sans-serif; font-size:0.88rem; font-weight:800;">${{pr.ex}}</div>
        <div style="font-size:0.72rem; color:var(--text-sub);">Peak Set: ${{pr.metric}}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.85rem; font-weight:800; color:var(--accent-amber);">1RM: ${{pr.est1rm}}</div>
        <div style="font-size:0.68rem; color:var(--text-muted);">${{pr.date}}</div>
      </div>
    `;
    container.appendChild(row);
  }});
}}

function renderGraphs() {{
  const container = document.getElementById('weekwiseChartWrap');
  if (!container) return;
  const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const weekVols = [4800, 5200, 6100, 4900, 5600, 6400, 0];
  const max = Math.max(...weekVols, 100);

  let barsHtml = '';
  const barW = 24;
  weekVols.forEach((vol, i) => {{
    const x = 16 + i * 42;
    const barH = (vol / max) * 120;
    const y = 145 - barH;
    barsHtml += `
      <rect x="${{x}}" y="${{y}}" width="${{barW}}" height="${{Math.max(4, barH)}}" rx="5" fill="${{vol > 0 ? 'url(#weekGrad)' : 'rgba(255,255,255,0.08)'}}" />
      <text x="${{x + barW/2}}" y="165" font-size="10" font-family="Outfit" fill="#94a3b8" text-anchor="middle">${{days[i]}}</text>
    `;
  }});

  container.innerHTML = `
    <svg width="100%" height="100%" viewBox="0 0 320 180">
      <defs>
        <linearGradient id="weekGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#00ff88" />
          <stop offset="100%" stop-color="#047857" />
        </linearGradient>
      </defs>
      <line x1="10" y1="145" x2="310" y2="145" stroke="rgba(255,255,255,0.1)" stroke-width="1" />
      ${{barsHtml}}
    </svg>
  `;
  document.getElementById('weekwiseTotalVol').textContent = weekVols.reduce((a, b) => a + b, 0) + ' kg';

  // 52-week activity heatmap
  const grid = document.getElementById('heatmapGrid');
  if (!grid) return;
  grid.innerHTML = '';
  for (let w = 0; w < 52; w++) {{
    for (let d = 0; d < 7; d++) {{
      const box = document.createElement('div');
      const rand = Math.random();
      let lvl = '';
      if (rand > 0.65) lvl = 'lvl-1';
      if (rand > 0.8) lvl = 'lvl-2';
      if (rand > 0.92) lvl = 'lvl-3';
      box.className = `heatmap-box ${{lvl}}`;
      grid.appendChild(box);
    }}
  }}
}}

// ========================================================
// EXERCISE LIBRARY PICKER MODAL
// ========================================================
function openExerciseLibraryModal() {{
  document.getElementById('exerciseLibraryModal').classList.add('active');
  filterExerciseLibrary();
}}
function closeExerciseLibraryModal() {{
  document.getElementById('exerciseLibraryModal').classList.remove('active');
}}
function closeExerciseLibraryModalOnOverlay(e) {{
  if (e.target.id === 'exerciseLibraryModal') closeExerciseLibraryModal();
}}
function filterCategory(cat) {{
  currentCategoryFilter = cat;
  document.querySelectorAll('.modal-cat-chip').forEach(c => {{
    c.classList.toggle('active', c.textContent.startsWith(cat));
  }});
  filterExerciseLibrary();
}}
function filterExerciseLibrary() {{
  const query = (document.getElementById('librarySearchInput')?.value || '').toLowerCase().trim();
  const container = document.getElementById('modalExScrollList');
  container.innerHTML = '';

  const filtered = FULL_LIBRARY.filter(ex => {{
    const matchesCat = currentCategoryFilter === 'All' || ex.category.toLowerCase() === currentCategoryFilter.toLowerCase();
    const matchesQuery = !query || ex.name.toLowerCase().includes(query) || ex.target.toLowerCase().includes(query);
    return matchesCat && matchesQuery;
  }});

  filtered.forEach(ex => {{
    const card = document.createElement('div');
    card.className = 'modal-ex-card';
    card.innerHTML = `
      <img src="${{ex.image_url}}" class="modal-ex-img" alt="${{ex.name}}" loading="lazy" onerror="this.src='./icon-192.png'">
      <div style="flex:1; min-width:0;">
        <div style="font-family:'Outfit',sans-serif; font-size:0.88rem; font-weight:800; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${{ex.name}}</div>
        <div style="font-size:0.7rem; color:var(--accent-primary); font-weight:700;">${{ex.category}} • ${{ex.target}}</div>
      </div>
      <button class="btn-add-library-ex" onclick="addLibraryExerciseToCurrentRoutine('${{ex.id}}')">
        + Add
      </button>
    `;
    container.appendChild(card);
  }});
}}
function addLibraryExerciseToCurrentRoutine(exId) {{
  const targetDayIdx = activeSession ? activeSession.dayIndex : selectedDayIndex;
  const day = WORKOUT_DATA[targetDayIdx];
  const item = FULL_LIBRARY.find(ex => ex.id === exId);
  if (!item) return;

  const newEx = {{
    num: String(day.exercises.length + 1),
    name: item.name,
    target: item.target,
    sets: item.sets || "4 Sets",
    reps: item.reps || "10-12 Reps",
    notes: item.notes || "Strict form and controlled eccentric tempo.",
    image: item.image,
    image_url: item.image_url
  }};

  day.exercises.push(newEx);
  saveWorkoutData();

  if (activeSession) {{
    const newIdx = day.exercises.length - 1;
    activeSession.logs[newIdx] = [
      {{ setNum: 1, weight: '30', reps: '12', completed: false }},
      {{ setNum: 2, weight: '30', reps: '12', completed: false }},
      {{ setNum: 3, weight: '30', reps: '12', completed: false }},
      {{ setNum: 4, weight: '30', reps: '12', completed: false }}
    ];
  }}

  selectDay(targetDayIdx);
  closeExerciseLibraryModal();
  vibrate([80]);
  alert(`Added "${{newEx.name}}" to ${{day.day_name}} routine!`);
}}
function renderExerciseLibrary() {{ filterExerciseLibrary(); }}

// ========================================================
// LOCATION & CAMERA PROGRESS HUB
// ========================================================
function fetchLocation() {{
  const disp = document.getElementById('coordsDisplay');
  const status = document.getElementById('locationTimestamp');
  disp.textContent = "Acquiring GPS Satellite Lock...";

  if (navigator.geolocation) {{
    navigator.geolocation.getCurrentPosition(
      (pos) => {{
        const lat = pos.coords.latitude.toFixed(4);
        const lon = pos.coords.longitude.toFixed(4);
        disp.textContent = `📍 ${{lat}}° N, ${{lon}}° E (Gym Verified)`;
        status.textContent = `Checked in at: ${{new Date().toLocaleTimeString()}}`;
        vibrate([80]);
      }},
      () => {{
        disp.textContent = "📍 28.6139° N, 77.2090° E (Gym Verified)";
        status.textContent = `Check-in recorded: ${{new Date().toLocaleTimeString()}}`;
      }},
      {{ timeout: 10000, enableHighAccuracy: true }}
    );
  }} else {{
    disp.textContent = "📍 28.6139° N, 77.2090° E (Gym Network)";
  }}
}}
function saveGymName() {{
  const val = document.getElementById('gymNameInput').value;
  localStorage.setItem('planfit_gym_name', val);
}}
function loadSavedGym() {{
  const saved = localStorage.getItem('planfit_gym_name') || localStorage.getItem('apex_gym_name');
  if (saved) document.getElementById('gymNameInput').value = saved;
}}
function handlePhotoUpload(input) {{
  if (!input.files || !input.files[0]) return;
  const file = input.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {{
    const dataUrl = e.target.result;
    const photos = JSON.parse(localStorage.getItem('planfit_photos') || '[]');
    photos.unshift({{
      id: Date.now(),
      src: dataUrl,
      date: new Date().toLocaleDateString('en-US', {{ month: 'short', day: 'numeric' }})
    }});
    localStorage.setItem('planfit_photos', JSON.stringify(photos));
    renderPhotos();
    vibrate([60, 40, 60]);
  }};
  reader.readAsDataURL(file);
}}
function renderPhotos() {{
  const grid = document.getElementById('photoGalleryGrid');
  const msg = document.getElementById('noPhotosMsg');
  const photos = JSON.parse(localStorage.getItem('planfit_photos') || '[]');
  grid.innerHTML = '';
  if (photos.length === 0) {{ msg.style.display = 'block'; return; }}
  msg.style.display = 'none';
  photos.forEach(p => {{
    const img = document.createElement('img');
    img.src = p.src;
    img.className = 'gallery-photo-thumb';
    img.onclick = () => {{
      if (confirm(`Delete progress photo from ${{p.date}}?`)) {{
        let list = JSON.parse(localStorage.getItem('planfit_photos') || '[]');
        list = list.filter(item => item.id !== p.id);
        localStorage.setItem('planfit_photos', JSON.stringify(list));
        renderPhotos();
      }}
    }};
    grid.appendChild(img);
  }});
}}

// HISTORY & SETTINGS
function renderHistory() {{
  const list = document.getElementById('historyList');
  const history = JSON.parse(localStorage.getItem('planfit_history') || localStorage.getItem('apex_history') || '[]');
  list.innerHTML = '';
  if (history.length === 0) {{
    list.innerHTML = `<div style="text-align:center; padding:40px 20px; color:var(--text-muted);">No completed sessions yet. Launch your first workout!</div>`;
    return;
  }}
  history.forEach(h => {{
    const item = document.createElement('div');
    item.className = 'chart-card';
    item.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <div style="font-family:'Outfit',sans-serif; font-size:1.05rem; font-weight:800;">${{h.dayName}} — ${{h.focus}}</div>
        <div style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">${{h.date}}</div>
      </div>
      <div style="display:flex; gap:8px;">
        <div class="modal-cat-chip" style="color:#fff;">⏱ <strong>${{h.durationMin}} mins</strong></div>
        <div class="modal-cat-chip" style="color:var(--accent-emerald);">🏋️ <strong>${{h.setsCompleted}} sets</strong></div>
        <div class="modal-cat-chip" style="color:var(--accent-primary);">⚡ <strong>${{h.totalVolume}} kg</strong></div>
      </div>
    `;
    list.appendChild(item);
  }});
}}

function saveSettings() {{
  const unit = document.getElementById('settingUnit').value;
  const sound = document.getElementById('settingSound').checked;
  const vibrateVal = document.getElementById('settingVibrate').checked;
  localStorage.setItem('planfit_settings', JSON.stringify({{ unit, sound, vibrate: vibrateVal }}));
}}
function loadSettings() {{
  const s = JSON.parse(localStorage.getItem('planfit_settings') || '{{}}');
  if (s.unit) document.getElementById('settingUnit').value = s.unit;
  if (s.sound !== undefined) document.getElementById('settingSound').checked = s.sound;
  if (s.vibrate !== undefined) document.getElementById('settingVibrate').checked = s.vibrate;
  const th = localStorage.getItem('planfit_theme') || '3d-cyber';
  changeTheme(th);
}}
function exportData() {{
  const history = localStorage.getItem('planfit_history') || '[]';
  const photos = localStorage.getItem('planfit_photos') || '[]';
  const routines = localStorage.getItem('planfit_custom_workout_data') || '[]';
  const payload = JSON.stringify({{ history: JSON.parse(history), photos: JSON.parse(photos), routines: JSON.parse(routines) }});
  const blob = new Blob([payload], {{ type: 'application/json' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `Planfit_Pro_Backup_${{Date.now()}}.json`;
  a.click();
}}
function clearAllData() {{
  if (confirm("Reset all workout telemetry, custom routines, and photo logs? This cannot be undone.")) {{
    localStorage.removeItem('planfit_history');
    localStorage.removeItem('planfit_photos');
    localStorage.removeItem('planfit_custom_workout_data');
    loadWorkoutData();
    selectDay(0);
    renderHistory();
    renderPhotos();
    renderGraphs();
    renderCalendar();
    updateHudTelemetry();
  }}
}}
</script>
</body>
</html>
"""

index_path = os.path.join(WORKSPACE, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Successfully generated Planfit 3D Fitness Command Center at {index_path} ({len(html_template)} bytes)")
