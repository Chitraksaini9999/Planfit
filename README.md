# ⚡ Planfit Pro — 3D Fitness Command Center & Mobile APK

[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Web%20%7C%20PWA-00f0ff?style=for-the-badge&logo=android)](Planfit_Workout_Tracker.apk)
[![License](https://img.shields.io/badge/License-MIT-00ff88?style=for-the-badge)](LICENSE)
[![APK Size](https://img.shields.io/badge/APK%20Size-1.09%20MB-ffd700?style=for-the-badge)](Planfit_Workout_Tracker.apk)
[![Offline Ready](https://img.shields.io/badge/Offline-100%25%20Self--Contained-d946ef?style=for-the-badge)](#features)

**Planfit Pro** is an executive-grade, 3D mobile workout runner, hypertrophy planner, and telemetry command center. Designed for serious strength athletes, lifters, and fitness enthusiasts who prioritize functionality, accurate tracking, effortless scheduling, and measurable progressive overload.

---

## 📱 Quick Download

* 📦 **Pre-built Signed Android APK**: [Download `Planfit_Workout_Tracker.apk`](Planfit_Workout_Tracker.apk) *(1.09 MB, Android 7.0+ / API 24-35)*
* 📱 **PWA & Mobile Browser**: Works 100% offline via local Wi-Fi or any modern browser.

---

## ✨ Features & Architecture

### 🎛️ 1. Tactical Command Center HUD
* **Readiness Telemetry**: Real-time physical readiness score evaluated from recovery density and training frequency.
* **Weekly Volume Radar**: Real-time tonnage accumulation meter measuring progressive overload.
* **Consistency Streak**: Visual flame counter tracking unbroken training streaks.
* **1-Tap Mission Launcher**: Highlights today's scheduled split with single-tap instant session launch.

### 📅 2. Effortless Workout Scheduling
* **Weekly Split Matrix (Mon – Sun)**: Reassign or swap splits across any day with one tap.
* **Interactive Command Calendar**: Full monthly calendar tracking scheduled splits, completed sessions (green badges), and volume history.
* **Date Command Drawer**: Inspect workout history for any date or schedule future sessions.

### 🎯 3. High-Accuracy Exercise Tracking
* **Previous Performance Reference**: Displays previous session's load and reps directly on the card to guide progressive overload.
* **Rapid Mobile Weight Adjusters (`[-5] [-2.5] [+2.5] [+5]`)**: Modify weights with rapid touch buttons without keyboard delays.
* **Live 1RM Telemetry**: Auto-calculates estimated One Rep Max for each set using the Epley formula ($1\text{RM} = \text{weight} \times (1 + \text{reps}/30)$).
* **Dual-Mode Exercise Telemetry Timer**:
  * **Stopwatch**: Precision Time Under Tension (TUT) tracking with 1-tap set logging.
  * **Countdown Timer**: 30s, 45s, 60s, 90s, 120s presets with circular SVG animated progress ring, audio cues, and haptic phone vibration.

### 📈 4. Measurable Hypertrophy & Analytics
* **🏆 Personal Records (PR) Hall**: Tracks all-time bests (Max Load, Peak Volume Set, and Estimated 1RM) per exercise.
* **Weekly Tonnage Progression**: SVG bar telemetry visualizing daily load distribution.
* **52-Week Hypertrophy Heatmap**: Annual density grid mapping consistency across all 52 weeks.

### 📚 5. 39-Exercise Choice Library
* Searchable and filterable by muscle groups: Chest, Back, Shoulders, Biceps, Triceps, Legs, and Core.
* Real visual exercise demonstrations for all 39 exercises.
* 1-tap Add to Routine / Remove from Routine with local storage persistence.

### 🧊 6. 3D Visual Themes & Tactile Mechanics
* **3D Tactile Buttons**: Physical 3D extrusion (`box-shadow: 0 4px 0 #4c1d95`) that depresses on touch (`translateY(3px)`).
* **Battery-Aware 3D Depth Field**: Lightweight mathematical 3D perspective projection that throttles when idle.
* **7 Curated 3D Themes**: 3D Cyber Holo, 3D Gold Titanium, 3D Emerald Matrix, 3D Electric Violet, 3D Crimson Fury, Miami Synthwave, and Midnight Stealth.

---

## 📂 Repository Structure

```
planfit-github-repo/
├── mobile_app/                  # Core Web Application & PWA
│   ├── index.html              # 3D Fitness Command Center interface
│   ├── manifest.json           # Web App Manifest
│   ├── sw.js                   # Offline Service Worker
│   ├── serve_mobile.py         # Local Python server with terminal QR code
│   ├── icon-192.png            # App Icon (192x192)
│   ├── icon-512.png            # App Icon (512x512)
│   └── images/                 # 39 demonstration exercise photos
│
├── release/                     # Release Binaries
│   └── Planfit_Workout_Tracker.apk
│
├── build_command_center.py      # App generator & HTML builder script
├── exercise_library.py          # 39 exercise library data definitions
├── workout_structure.py         # 6-day hypertrophy routine data
├── prepare_android.py           # Android build asset & Java bridge preparer
├── compile_apk.py               # Android APK compilation & signing script
├── start_mobile_app.bat         # 1-click Windows server launcher
├── start_mobile_app.sh          # 1-click Linux/macOS server launcher
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Option A: Install Native Android APK
1. Download [`Planfit_Workout_Tracker.apk`](Planfit_Workout_Tracker.apk).
2. Transfer to your Android phone and install.
3. Enjoy 100% offline workout tracking with background timer services.

### Option B: Run Locally on Wi-Fi (Any Device)
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/planfit-pro.git
   cd planfit-pro
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   * **Windows**: Double-click `start_mobile_app.bat` or run:
     ```bash
     python mobile_app/serve_mobile.py
     ```
   * **Linux / macOS**: Run:
     ```bash
     bash start_mobile_app.sh
     ```
4. Scan the QR code displayed in the terminal with your phone camera or visit the printed URL.

---

### Option C: Compiling the Native Android APK from Source
Prerequisites: Android SDK (`build-tools`, `platforms/android-35`) and JDK 17+.

```bash
# 1. Prepare Android build structure & copy assets
python prepare_android.py

# 2. Compile, dex, zipalign, and sign APK
python compile_apk.py
```
The compiled signed APK will be output at `Planfit_Workout_Tracker.apk`.

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
