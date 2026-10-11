import os
import base64
import subprocess
import json
from io import BytesIO
from PIL import Image
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

WORKSPACE = r"d:\desktop\Main\EX"

# Image mapping verified
EXERCISE_DATA = [
    {
        "day_id": "monday",
        "day_name": "MONDAY",
        "focus": "Upper Chest and Triceps",
        "accent": "#38bdf8", # Sky blue
        "warmup": [
            {"name": "Light weight shoulder press", "details": "2 × 20 reps (use light weight)"},
            {"name": "Flat Bench Press", "details": "2 × 20 reps (warm-up pump)"}
        ],
        "exercises": [
            {
                "num": "1",
                "name": "Flat Dumbbell Press",
                "target": "Chest (Pectoralis Major)",
                "sets": "4 Sets",
                "reps": "16, 14, 12, 10 Reps (Pyramid)",
                "notes": "Drive through the chest, maintain arch and retracted scapula.",
                "image": "Flat Dumbbel Press.jfif"
            },
            {
                "num": "2",
                "name": "Incline Bench Press",
                "target": "Upper Chest (Clavicular Head)",
                "sets": "4 Sets",
                "reps": "16, 14, 12, 10 Reps",
                "notes": "30-degree incline angle. Focus on upper chest squeeze at top.",
                "image": "Incline bench press.jfif"
            },
            {
                "num": "3",
                "name": "Incline Dumbbell Fly",
                "target": "Upper Chest Stretch & Contraction",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Slight bend at elbows. Deep stretch at bottom, squeeze at peak.",
                "image": "incline dumbbell fly.jfif"
            },
            {
                "num": "4",
                "name": "Butterfly (Pec Deck)",
                "target": "Inner & Middle Chest",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Keep chest high, elbows pinned slightly flared, pause at full contraction.",
                "image": "butterfly machine.jfif"
            },
            {
                "num": "5",
                "name": "Smith Close Grip Bench Press",
                "target": "Triceps (Lateral & Medial Heads)",
                "sets": "3 Sets",
                "reps": "10-15 Reps",
                "notes": "Shoulder-width grip. Keep elbows tucked close to torso.",
                "image": "smith close grip bench press.jfif"
            },
            {
                "num": "6",
                "name": "Skull Crusher",
                "target": "Triceps (Long Head)",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Lower bar toward crown/behind forehead. Keep upper arms stationary.",
                "image": "skull crushers.jfif"
            },
            {
                "num": "7",
                "name": "Reverse Rod Triceps Curls",
                "target": "Triceps & Forearms",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Underhand grip on cable rod. Lock elbows and flex triceps fully.",
                "image": "reverse rod triceps curls.jfif"
            },
            {
                "num": "8",
                "name": "50 Push Ups",
                "target": "Chest & Triceps Burnout Finisher",
                "sets": "Burnout",
                "reps": "50 Total Reps (Break into rest-pause as needed)",
                "notes": "Strict form, chest touches 2 inches above ground.",
                "image": "push up.jfif"
            }
        ],
        "cardio": "15-20 mins Cardio (Moderate Steady State / Incline Walk)"
    },
    {
        "day_id": "tuesday",
        "day_name": "TUESDAY",
        "focus": "Back and Biceps",
        "accent": "#34d399", # Emerald green
        "warmup": [
            {"name": "Rotator Cuff Warm Up", "details": "2 × 10 each side (external/internal rotations)"},
            {"name": "Lat Pull Down", "details": "2 × 20 reps (light weight blood flow)"},
            {"name": "Cable Biceps Curls", "details": "2 × 30 reps (light pump)"}
        ],
        "exercises": [
            {
                "num": "1",
                "name": "Lats Pull Down",
                "target": "Upper Lats & V-Taper Width",
                "sets": "4 Sets",
                "reps": "16, 14, 12, 10 Reps (Pyramid)",
                "notes": "Pull to upper chest, drive elbows down, retract scapulae.",
                "image": "lat pull down.jfif"
            },
            {
                "num": "2",
                "name": "Close Grip Pull Down",
                "target": "Lower Lats & Mid-Back Thickness",
                "sets": "4 Sets",
                "reps": "16, 12, 10, 8 Reps",
                "notes": "Neutral narrow V-bar attachment. Full stretch at top, pull to sternum.",
                "image": "close grip pull down.jfif"
            },
            {
                "num": "3",
                "name": "Iso Lateral Lat Pulldown",
                "target": "Unilateral Lat Symmetry",
                "sets": "4 Sets",
                "reps": "10-15 Reps each side",
                "notes": "Independent lever arms. Focus on deep contraction one arm at a time.",
                "image": "iso lateral lat pulldown.jfif"
            },
            {
                "num": "4",
                "name": "Incline Dumbbell Bent-Over Row",
                "target": "Upper Back, Rhomboids & Rear Lats",
                "sets": "4 Sets",
                "reps": "10-15 Reps each side",
                "notes": "Chest supported on incline bench. Eliminate swinging momentum.",
                "image": "incline dumbbell bentrow.jfif"
            },
            {
                "num": "5",
                "name": "Biceps Curls (Standing Dumbbell)",
                "target": "Biceps Brachii",
                "sets": "4 Sets",
                "reps": "10-15 Reps each side",
                "notes": "Supinate wrist at peak contraction. Control the negative descent.",
                "image": "biceps curl.jfif"
            },
            {
                "num": "6",
                "name": "Preacher Biceps Curls",
                "target": "Biceps Short Head & Peak",
                "sets": "4 Sets",
                "reps": "10-12 Reps each side",
                "notes": "Upper arm locked against pad. Avoid bouncing at bottom stretch.",
                "image": "preacher bicep curl.jfif"
            },
            {
                "num": "7",
                "name": "Hammer Cable Curls",
                "target": "Brachialis & Brachioradialis",
                "sets": "4 Sets",
                "reps": "10-15 Reps each side",
                "notes": "Rope attachment, neutral palms. Builds upper arm width and grip.",
                "image": "hammer cabel curl"
            }
        ],
        "cardio": "15 mins Cardio (Stairmaster or HIIT intervals)"
    },
    {
        "day_id": "wednesday",
        "day_name": "WEDNESDAY",
        "focus": "Quads, Shoulders and Abs",
        "accent": "#f59e0b", # Amber
        "warmup": [
            {"name": "Free Weight Squats", "details": "2 × 30 reps (bodyweight mobility)"},
            {"name": "Bodyweight Lunges", "details": "2 × 20 reps (glute/quad dynamic warmup)"}
        ],
        "exercises": [
            {
                "num": "1",
                "name": "Front Squats",
                "target": "Quads & Core Stability",
                "sets": "4 Sets",
                "reps": "16, 14, 12, 10 Reps (Pyramid)",
                "notes": "Clean grip or cross-arm. Keep torso upright to maximize quad tension.",
                "image": "fornt squart.jfif"
            },
            {
                "num": "2",
                "name": "Lunges (Walking/Static)",
                "target": "Quads, Glutes & Adductors",
                "sets": "4 Sets",
                "reps": "10-15 Reps per leg",
                "notes": "90-degree bend in front knee. Keep torso tall and core tight.",
                "image": "lunges.jfif"
            },
            {
                "num": "3",
                "name": "Leg Extension",
                "target": "Quadriceps Isolation & Rectus Femoris",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "2-second peak hold at lockout. Slow 3-second eccentric lowering.",
                "image": "leg extension.jfif"
            },
            {
                "num": "4",
                "name": "Smith Shoulder Press",
                "target": "Anterior & Lateral Deltoids",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Lower to chin level, press overhead without fully locking elbows.",
                "image": "smith shoulder press.jfif"
            },
            {
                "num": "5",
                "name": "Upright Row",
                "target": "Lateral Delts & Upper Traps",
                "sets": "4 Sets",
                "reps": "16, 12, 10, 8 Reps",
                "notes": "Lead with elbows, keep bar close to body. Pull to mid-chest.",
                "image": "upright row.jfif"
            },
            {
                "num": "6",
                "name": "Front Raises",
                "target": "Anterior Deltoids",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Raise to eye level with controlled cadence. Avoid swinging hips.",
                "image": "Front raises.jfif"
            },
            {
                "num": "7",
                "name": "Planks",
                "target": "Transverse Abdominis & Core Bracing",
                "sets": "4 Sets",
                "reps": "45-60 sec Hold",
                "notes": "Squeeze glutes, pack ribs down, maintain neutral cervical spine.",
                "image": "planks.jfif"
            }
        ],
        "abs_circuit": {
            "title": "Abs Circuit — 6 Rounds in 15 Mins",
            "exercises": [
                "Lying Leg Raises — 10 reps",
                "Cable Crunches — 10 reps",
                "Seated Crunches — 10 reps"
            ]
        }
    },
    {
        "day_id": "thursday",
        "day_name": "THURSDAY",
        "focus": "Lower Chest and Triceps",
        "accent": "#ec4899", # Pink / Magenta
        "warmup": [
            {"name": "Rotator Cuff Movements", "details": "2 × 20 reps (cables/bands)"},
            {"name": "Machine Chest Press", "details": "2 × 20 reps (activation sets)"}
        ],
        "exercises": [
            {
                "num": "1",
                "name": "Flat Bench Dumbbell Press",
                "target": "Mid Chest & Overall Pectoral Mass",
                "sets": "4 Sets",
                "reps": "18, 16, 12, 10 Reps",
                "notes": "Full range of motion, flare elbows at 45 degrees, explode on press.",
                "image": "flat bench dumbell press.jfif"
            },
            {
                "num": "2",
                "name": "Chest Press Machine",
                "target": "Pectoral Isolation",
                "sets": "3 Sets",
                "reps": "18, 16, 12 Reps",
                "notes": "Constant mechanical tension. Focus on inner pectoral squeeze.",
                "image": "chest press machine.jfif"
            },
            {
                "num": "3",
                "name": "Decline Barbell Press",
                "target": "Lower Chest (Sternocostal Head)",
                "sets": "4 Sets",
                "reps": "18, 16, 12, 10 Reps",
                "notes": "Bar touches lower chest/inframammary fold. Great for chest thickness.",
                "image": "decline barbell press.jfif"
            },
            {
                "num": "4",
                "name": "SUPERSET: Decline Fly & Around The World Fly (Flat Bench)",
                "target": "Lower Chest & Full Pectoral Expansion",
                "sets": "3 Sets",
                "reps": "10 Reps each exercise back-to-back",
                "notes": "Smooth arc motion. Maintain slight elbow bend throughout.",
                "image": "decline fly.jfif"
            },
            {
                "num": "5",
                "name": "Cable Triceps Curls / Pushdowns",
                "target": "Triceps Lateral & Medial Heads",
                "sets": "4 Sets",
                "reps": "18, 16, 12, 10 Reps",
                "notes": "Pin elbows to ribs, full lockout and split cable at bottom.",
                "image": "cabel triceps curl.jfif"
            },
            {
                "num": "6",
                "name": "Overhead Dumbbell Extension / Press",
                "target": "Triceps Long Head Stretch",
                "sets": "4 Sets",
                "reps": "16, 12, 10, 10 Reps",
                "notes": "Both hands cupping dumbbell overhead. Lower deep behind head.",
                "image": "overhead dumbbell press.jfif"
            },
            {
                "num": "7",
                "name": "Planks",
                "target": "Core Stability & Spinal Health",
                "sets": "4 Sets",
                "reps": "45-60 sec Hold",
                "notes": "Forearms grounded, pelvis tucked, active glute tension.",
                "image": "planks.jfif"
            }
        ],
        "cardio": "10-15 mins Cardio (Treadmill Incline Walk / Rowing Machine)"
    },
    {
        "day_id": "friday",
        "day_name": "FRIDAY",
        "focus": "Back, Traps and Biceps",
        "accent": "#a855f7", # Purple
        "warmup": [
            {"name": "Rotator Cuff Warm Up", "details": "2 × 10 each side"},
            {"name": "Lats Pull Down", "details": "2 × 20 reps"},
            {"name": "Cable Biceps Curls", "details": "2 × 30 reps"}
        ],
        "exercises": [
            {
                "num": "1",
                "name": "Machine Lat Pull Down",
                "target": "Upper Back & Lat Width",
                "sets": "4 Sets",
                "reps": "16, 12, 10, 8 Reps",
                "notes": "Control the stack. Squeeze shoulder blades down and back.",
                "image": "lat pull down.jfif"
            },
            {
                "num": "2",
                "name": "Seated Cable Row",
                "target": "Mid Back, Rhomboids & Thickness",
                "sets": "4 Sets",
                "reps": "16, 14, 12, 10 Reps",
                "notes": "NEGATIVE REP SLOW (3-4 second eccentric release on every rep).",
                "image": "seated row.jfif"
            },
            {
                "num": "3",
                "name": "Rack Pull",
                "target": "Erector Spinae, Traps & Posterior Chain",
                "sets": "3 Sets",
                "reps": "12 Reps",
                "notes": "Bar set just below knees. Lockout hips and drive upper back tall.",
                "image": "rack pull.jfif"
            },
            {
                "num": "4",
                "name": "Incline Dumbbell Bent-Over Row",
                "target": "Lats & Scapular Retractors",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "3-SEC SQUEEZE AT PEAK with slow controlled rep cadence.",
                "image": "incline dumbbell bentrow.jfif"
            },
            {
                "num": "5",
                "name": "Shrugs (Dumbbell or Barbell)",
                "target": "Upper Trapezius",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "NEGATIVE REP SLOW. Direct vertical elevation, no shoulder rolling.",
                "image": "shrugs.jfif"
            },
            {
                "num": "6",
                "name": "SUPERSET: Upright Row & Reverse Fly",
                "target": "Traps, Lateral Delts & Rear Deltoids",
                "sets": "4 Sets",
                "reps": "10 Reps each movement back-to-back",
                "notes": "Seamless transition. Maximizes 3D shoulder & trap definition.",
                "image": "upright row and reverse fly.jfif"
            },
            {
                "num": "7",
                "name": "SUPERSET: Wall Biceps Curls & Concentration Biceps Curls",
                "target": "Biceps Full Peak & Strict Isolation",
                "sets": "Failure Protocol",
                "reps": "15 mins continuous failure sets with 30-45 sec rest intervals",
                "notes": "Back pinned against wall prevents any swing. Pure bicep exhaustion.",
                "image": "wall biceps curl.jfif"
            }
        ],
        "cardio": "15 mins Cardio (Moderate Intensity Cycling / Elliptical)"
    },
    {
        "day_id": "saturday",
        "day_name": "SATURDAY",
        "focus": "Hamstrings, Glutes and Calves",
        "accent": "#06b6d4", # Cyan / Teal
        "warmup": [
            {"name": "Cycling Warm-up", "details": "10 mins low-resistance cycling"},
            {"name": "Bodyweight Lunges", "details": "2 × 20 reps"},
            {"name": "Bodyweight Squats", "details": "2 × 20 reps"}
        ],
        "exercises": [
            {
                "num": "1",
                "name": "Wide Grip Leg Press",
                "target": "Hamstrings, Adductors & Glutes",
                "sets": "5 Sets",
                "reps": "20, 16, 14, 12, 10 Reps (Heavy Pyramid)",
                "notes": "High and wide foot placement shifts load directly to hamstrings/glutes.",
                "image": "wide grip leg press.jfif"
            },
            {
                "num": "2",
                "name": "SUPERSET: Bodyweight Lunges & Hamstring Curls",
                "target": "Glutes & Hamstring Biceps Femoris",
                "sets": "4 Sets",
                "reps": "10-15 Reps each back-to-back",
                "notes": "Perform lunges then go directly to machine hamstring curl pad.",
                "image": "hamstring curl.jfif"
            },
            {
                "num": "3",
                "name": "Goblet Squats (Bench Supported)",
                "target": "Quads, Glutes & Adductors",
                "sets": "4 Sets",
                "reps": "12 Reps",
                "notes": "Tap bench gently at bottom depth for consistent range of motion.",
                "image": "goblet squats.jfif"
            },
            {
                "num": "4",
                "name": "Glute Bridge",
                "target": "Gluteus Maximus Isolation",
                "sets": "4 Sets",
                "reps": "16, 14, 12, 10 Reps",
                "notes": "Drive through heels, squeeze glutes hard for 2 seconds at top.",
                "image": "glute bridge.jfif"
            },
            {
                "num": "5",
                "name": "Seated Calves Raises",
                "target": "Soleus (Deep Calf Muscle)",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Full deep stretch at bottom, explosive rise onto balls of feet.",
                "image": "seated calves raise.jfif"
            },
            {
                "num": "6",
                "name": "Standing Calves Raise",
                "target": "Gastrocnemius (Calf Diamond)",
                "sets": "4 Sets",
                "reps": "10-15 Reps",
                "notes": "Knees straight but not hyperextended. 2-second stretch pause.",
                "image": "standing calves raise.jfif"
            },
            {
                "num": "7",
                "name": "Planks",
                "target": "Core Stability & Hip Alignment",
                "sets": "4 Sets",
                "reps": "45-60 sec Hold",
                "notes": "Lock core, brace stomach against spine.",
                "image": "planks.jfif"
            }
        ],
        "abs_circuit": {
            "title": "Abs Circuit — 6 Rounds in 15 Mins",
            "exercises": [
                "Lying Down Leg Raises — 15 reps",
                "Normal Crunches — 15 reps",
                "Cable Side Bend — 15 reps each side"
            ]
        }
    }
]

print("Loaded workout structure with", len(EXERCISE_DATA), "days.")
