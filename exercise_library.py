import os
import json
from workout_structure import EXERCISE_DATA

# All 39 exercises with real images in mobile_app/images
EXERCISE_LIBRARY = [
    # CHEST
    {
        "id": "flat_db_press",
        "name": "Flat Dumbbell Press",
        "category": "Chest",
        "target": "Chest (Pectoralis Major)",
        "sets": "4 Sets",
        "reps": "16, 14, 12, 10 Reps (Pyramid)",
        "notes": "Drive through the chest, maintain arch and retracted scapula.",
        "image": "Flat Dumbbel Press.jfif"
    },
    {
        "id": "incline_bb_press",
        "name": "Incline Bench Press",
        "category": "Chest",
        "target": "Upper Chest (Clavicular Head)",
        "sets": "4 Sets",
        "reps": "16, 14, 12, 10 Reps",
        "notes": "30-degree incline angle. Focus on upper chest squeeze at top.",
        "image": "Incline bench press.jfif"
    },
    {
        "id": "incline_db_fly",
        "name": "Incline Dumbbell Fly",
        "category": "Chest",
        "target": "Upper Chest Stretch & Contraction",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Slight bend at elbows. Deep stretch at bottom, squeeze at peak.",
        "image": "incline dumbbell fly.jfif"
    },
    {
        "id": "butterfly_pec_deck",
        "name": "Butterfly Machine (Pec Deck)",
        "category": "Chest",
        "target": "Inner & Middle Chest",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Seat height set so handles are mid-chest. 2-second peak contraction.",
        "image": "butterfly machine.jfif"
    },
    {
        "id": "decline_bb_press",
        "name": "Decline Barbell Press",
        "category": "Chest",
        "target": "Lower Chest (Costal Head)",
        "sets": "4 Sets",
        "reps": "16, 14, 12, 10 Reps",
        "notes": "Secure legs under rollers. Lower bar strictly to lower sternum.",
        "image": "decline barbell press.jfif"
    },
    {
        "id": "decline_fly",
        "name": "Decline Dumbbell Fly",
        "category": "Chest",
        "target": "Lower & Outer Pectorals",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Controlled descent focusing on stretch at bottom position.",
        "image": "decline fly.jfif"
    },
    {
        "id": "chest_press_machine",
        "name": "Machine Chest Press",
        "category": "Chest",
        "target": "Full Chest Mass & Density",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Explosive concentric press, slow 3-second negative descent.",
        "image": "chest press machine.jfif"
    },
    {
        "id": "flat_bench_db_press",
        "name": "Flat Bench Dumbbell Press",
        "category": "Chest",
        "target": "Pectoralis Major & Stabilizers",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Full depth stretch and explosive press bringing bells together.",
        "image": "flat bench dumbell press.jfif"
    },
    {
        "id": "push_up",
        "name": "Bodyweight Push-Ups",
        "category": "Chest",
        "target": "Chest, Triceps & Core Stabilizers",
        "sets": "3 Sets",
        "reps": "Failure (20-30 Reps)",
        "notes": "Strict plank position. Touch chest to ground and lock out.",
        "image": "push up.jfif"
    },

    # TRICEPS
    {
        "id": "cabel_triceps_curl",
        "name": "Cable Triceps Pushdown",
        "category": "Triceps",
        "target": "Triceps Lateral & Medial Heads",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Keep elbows pinned to your ribs; flare rope or push rod at bottom.",
        "image": "cabel triceps curl.jfif"
    },
    {
        "id": "reverse_rod_triceps",
        "name": "Reverse Grip Triceps Extension",
        "category": "Triceps",
        "target": "Triceps Medial Head",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Underhand supinated grip on rod; isolate elbow extension.",
        "image": "reverse rod triceps curls.jfif"
    },
    {
        "id": "skull_crushers",
        "name": "EZ Bar Skull Crushers",
        "category": "Triceps",
        "target": "Triceps Long Head (Stretch Position)",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Lower bar toward forehead/behind head; elbows point at ceiling.",
        "image": "skull crushers.jfif"
    },
    {
        "id": "smith_close_grip_bench",
        "name": "Smith Close-Grip Bench Press",
        "category": "Triceps",
        "target": "Triceps Mass & Lockout Strength",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Shoulder-width grip. Keep elbows tucked 45 degrees to torso.",
        "image": "smith close grip bench press.jfif"
    },

    # BACK
    {
        "id": "lat_pulldown",
        "name": "Wide Grip Lat Pulldown",
        "category": "Back",
        "target": "Lats (Latissimus Dorsi Width)",
        "sets": "4 Sets",
        "reps": "16, 14, 12, 10 Reps (Pyramid)",
        "notes": "Pull to upper chest. Squeeze shoulder blades down and back.",
        "image": "lat pull down.jfif"
    },
    {
        "id": "close_grip_pulldown",
        "name": "Close Grip V-Bar Pulldown",
        "category": "Back",
        "target": "Lower Lats & Mid-Back Thickness",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Drive elbows straight down to hip pockets with torso arched.",
        "image": "close grip pull down.jfif"
    },
    {
        "id": "iso_lateral_lat_pulldown",
        "name": "Iso-Lateral Lat Pulldown",
        "category": "Back",
        "target": "Unilateral Lat Symmetry",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Allows independent arm motion for maximal contraction.",
        "image": "iso lateral lat pulldown.jfif"
    },
    {
        "id": "seated_row",
        "name": "Cable Seated Row",
        "category": "Back",
        "target": "Rhomboids, Mid-Traps & Lats",
        "sets": "4 Sets",
        "reps": "10-15 Reps",
        "notes": "Keep upright posture; drive elbows back and pinch scapulae.",
        "image": "seated row.jfif"
    },
    {
        "id": "incline_db_bentrow",
        "name": "Incline Dumbbell Bent-Over Row",
        "category": "Back",
        "target": "Upper Back & Rear Delts",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Chest supported on incline bench; eliminates momentum.",
        "image": "incline dumbbell bentrow.jfif"
    },
    {
        "id": "rack_pull",
        "name": "Power Rack Pulls",
        "category": "Back",
        "target": "Spinal Orectors, Traps & Glutes",
        "sets": "4 Sets",
        "reps": "8-10 Reps (Heavy)",
        "notes": "Bar set just below knees. Drive hips forward and lock out.",
        "image": "rack pull.jfif"
    },
    {
        "id": "shrugs",
        "name": "Dumbbell Trap Shrugs",
        "category": "Back",
        "target": "Upper Trapezius",
        "sets": "4 Sets",
        "reps": "15-20 Reps",
        "notes": "Straight up toward ears, 2-sec hold at peak. No rolling.",
        "image": "shrugs.jfif"
    },

    # BICEPS
    {
        "id": "standing_biceps_curl",
        "name": "Standing Biceps Curl",
        "category": "Biceps",
        "target": "Biceps Brachii Mass",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Supinate wrists at top; keep upper arms locked vertically.",
        "image": "biceps curl.jfif"
    },
    {
        "id": "preacher_bicep_curl",
        "name": "Preacher Bicep Curl",
        "category": "Biceps",
        "target": "Biceps Short Head & Peak",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Triceps flush against pad; prevent shoulder compensation.",
        "image": "preacher bicep curl.jfif"
    },
    {
        "id": "hammer_cabel_curl",
        "name": "Cable Hammer Curl",
        "category": "Biceps",
        "target": "Brachialis & Brachioradialis",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Neutral thumbs-up grip with rope; builds forearm and arm width.",
        "image": "hammer cabel curl.jpg"
    },
    {
        "id": "wall_biceps_curl",
        "name": "Strict Wall Bicep Curl",
        "category": "Biceps",
        "target": "Strict Isolated Biceps",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Back, head, and glutes pinned against wall to prevent cheating.",
        "image": "wall biceps curl.jfif"
    },

    # SHOULDERS
    {
        "id": "smith_shoulder_press",
        "name": "Smith Machine Shoulder Press",
        "category": "Shoulders",
        "target": "Anterior & Lateral Deltoids",
        "sets": "4 Sets",
        "reps": "16, 14, 12, 10 Reps (Pyramid)",
        "notes": "Lower bar to chin level; explode up without locking elbows.",
        "image": "smith shoulder press.jfif"
    },
    {
        "id": "overhead_db_press",
        "name": "Seated Overhead Dumbbell Press",
        "category": "Shoulders",
        "target": "Deltoid Mass & Overhead Power",
        "sets": "4 Sets",
        "reps": "10-12 Reps",
        "notes": "Keep core tight. Press upward in arc until bells almost touch.",
        "image": "overhead dumbbell press.jfif"
    },
    {
        "id": "front_raises",
        "name": "Front Dumbbell Raises",
        "category": "Shoulders",
        "target": "Anterior (Front) Deltoid",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Raise to eye level; control the 3-second descent.",
        "image": "Front raises.jfif"
    },
    {
        "id": "upright_row",
        "name": "Cable Upright Row",
        "category": "Shoulders",
        "target": "Lateral Delts & Traps",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Lead with elbows high; pull to mid-chest with hands wide.",
        "image": "upright row.jfif"
    },
    {
        "id": "upright_row_reverse_fly",
        "name": "Upright Row & Reverse Fly",
        "category": "Shoulders",
        "target": "Lateral & Posterior Delts Superset",
        "sets": "4 Sets",
        "reps": "12 Reps Each",
        "notes": "Superset combo for round 3D deltoid development.",
        "image": "upright row and reverse fly.jfif"
    },

    # LEGS
    {
        "id": "front_squat",
        "name": "Barbell Front Squats",
        "category": "Legs",
        "target": "Quadriceps & Core Stability",
        "sets": "4 Sets",
        "reps": "16, 14, 12, 10 Reps",
        "notes": "High elbows rack position. Keep torso upright; break parallel.",
        "image": "fornt squart.jfif"
    },
    {
        "id": "goblet_squats",
        "name": "Dumbbell Goblet Squats",
        "category": "Legs",
        "target": "Quads & Adductors Depth",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Hold heavy dumbbell tight to chest; push knees out in descent.",
        "image": "goblet squats.jfif"
    },
    {
        "id": "wide_grip_leg_press",
        "name": "Wide-Stance Leg Press",
        "category": "Legs",
        "target": "Inner Thighs, Quads & Glutes",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Feet high and wide on platform. Full depth without pelvis lifting.",
        "image": "wide grip leg press.jfif"
    },
    {
        "id": "leg_extension",
        "name": "Leg Extension Machine",
        "category": "Legs",
        "target": "Quadriceps Isolation & Rectus Femoris",
        "sets": "4 Sets",
        "reps": "15-20 Reps",
        "notes": "Hold 1-sec squeeze at top contraction. Control descent.",
        "image": "leg extension.jfif"
    },
    {
        "id": "hamstring_curl",
        "name": "Lying Hamstring Curl",
        "category": "Legs",
        "target": "Biceps Femoris (Hamstrings)",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Keep hips pressed firmly into bench; avoid lower back arching.",
        "image": "hamstring curl.jfif"
    },
    {
        "id": "walking_lunges",
        "name": "Walking Dumbbell Lunges",
        "category": "Legs",
        "target": "Quads, Glutes & Unilateral Balance",
        "sets": "4 Sets",
        "reps": "12-16 Steps per leg",
        "notes": "Knee reaches 90-degree angle lightly above floor. Drive forward.",
        "image": "lunges.jfif"
    },
    {
        "id": "glute_bridge",
        "name": "Barbell Glute Bridge",
        "category": "Legs",
        "target": "Gluteus Maximus & Hamstrings",
        "sets": "4 Sets",
        "reps": "12-15 Reps",
        "notes": "Drive through heels, squeeze glutes hard for 2 seconds at lockout.",
        "image": "glute bridge.jfif"
    },
    {
        "id": "seated_calves_raise",
        "name": "Seated Calf Raise",
        "category": "Legs",
        "target": "Soleus Muscle (Deep Calves)",
        "sets": "4 Sets",
        "reps": "15-20 Reps",
        "notes": "Full stretch at bottom, slow 2-second raise onto toes.",
        "image": "seated calves raise.jfif"
    },
    {
        "id": "standing_calves_raise",
        "name": "Standing Calf Machine Raise",
        "category": "Legs",
        "target": "Gastrocnemius (Upper Calves)",
        "sets": "4 Sets",
        "reps": "15-20 Reps",
        "notes": "Knees locked straight; full dorsiflexion stretch and plantar flexion.",
        "image": "standing calves raise.jfif"
    },

    # CORE
    {
        "id": "weighted_plank",
        "name": "Weighted Core Plank",
        "category": "Core",
        "target": "Transverse Abdominis & Deep Core",
        "sets": "4 Sets",
        "reps": "45-60 Seconds Hold",
        "notes": "Rigid bodyline from head to heels. Squeeze glutes and brace abs.",
        "image": "planks.jfif"
    }
]

print(f"Total verified library items: {len(EXERCISE_LIBRARY)}")
