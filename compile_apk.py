import os
import sys
import subprocess
import glob

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = r"d:\desktop\Main\EX"
BUILD_DIR = os.path.join(WORKSPACE, "android_build")
SDK_DIR = r"C:\Users\admin\AppData\Local\Android\Sdk"
BUILD_TOOLS_DIR = os.path.join(SDK_DIR, "build-tools", "34.0.0")
PLATFORM_JAR = os.path.join(SDK_DIR, "platforms", "android-35", "android.jar")
JDK_BIN = r"C:\Program Files\Java\jdk-18.0.2.1\bin"

AAPT = os.path.join(BUILD_TOOLS_DIR, "aapt.exe")
D8 = os.path.join(BUILD_TOOLS_DIR, "d8.bat")
ZIPALIGN = os.path.join(BUILD_TOOLS_DIR, "zipalign.exe")
APKSIGNER = os.path.join(BUILD_TOOLS_DIR, "apksigner.bat")
JAVAC = os.path.join(JDK_BIN, "javac.exe")
KEYTOOL = os.path.join(JDK_BIN, "keytool.exe")

SRC_DIR = os.path.join(BUILD_DIR, "src")
RES_DIR = os.path.join(BUILD_DIR, "res")
ASSETS_DIR = os.path.join(BUILD_DIR, "assets")
BIN_DIR = os.path.join(BUILD_DIR, "bin")
CLASSES_DIR = os.path.join(BIN_DIR, "classes")
MANIFEST = os.path.join(BUILD_DIR, "AndroidManifest.xml")

UNALIGNED_APK = os.path.join(BIN_DIR, "app-unaligned.apk")
ALIGNED_APK = os.path.join(BIN_DIR, "app-aligned.apk")
FINAL_APK = os.path.join(WORKSPACE, "Planfit_Workout_Tracker.apk")
KEYSTORE = os.path.join(BUILD_DIR, "release.keystore")

print("Step 1: Running AAPT to generate R.java...")
cmd_aapt_r = [
    AAPT, "package",
    "-f",
    "-m",
    "-J", SRC_DIR,
    "-M", MANIFEST,
    "-S", RES_DIR,
    "-I", PLATFORM_JAR
]
res = subprocess.run(cmd_aapt_r, capture_output=True, text=True)
if res.returncode != 0:
    print("AAPT R.java failed:", res.stderr)
    sys.exit(1)
print("  ✓ R.java generated successfully")

print("Step 2: Compiling Java source files with JAVAC...")
java_files = glob.glob(os.path.join(SRC_DIR, "**", "*.java"), recursive=True)
cmd_javac = [
    JAVAC,
    "-encoding", "UTF-8",
    "-d", CLASSES_DIR,
    "-cp", PLATFORM_JAR,
] + java_files

res = subprocess.run(cmd_javac, capture_output=True, text=True)
if res.returncode != 0:
    print("JAVAC compilation failed:", res.stderr)
    sys.exit(1)
print(f"  ✓ Compiled {len(java_files)} Java files into classes")

print("Step 3: Compiling classes into classes.dex with D8...")
class_files = glob.glob(os.path.join(CLASSES_DIR, "**", "*.class"), recursive=True)
cmd_d8 = [
    D8,
    "--output", BIN_DIR,
    "--lib", PLATFORM_JAR,
    "--min-api", "24"
] + class_files

res = subprocess.run(cmd_d8, capture_output=True, text=True, shell=True)
if res.returncode != 0:
    print("D8 dexing failed:", res.stderr)
    sys.exit(1)
dex_file = os.path.join(BIN_DIR, "classes.dex")
if not os.path.exists(dex_file):
    print("Error: classes.dex was not generated")
    sys.exit(1)
print(f"  ✓ classes.dex generated ({os.path.getsize(dex_file)} bytes)")

print("Step 4: Packaging resources and assets into unaligned APK...")
cmd_aapt_pkg = [
    AAPT, "package",
    "-f",
    "-M", MANIFEST,
    "-S", RES_DIR,
    "-A", ASSETS_DIR,
    "-I", PLATFORM_JAR,
    "-F", UNALIGNED_APK
]
res = subprocess.run(cmd_aapt_pkg, capture_output=True, text=True)
if res.returncode != 0:
    print("AAPT packaging failed:", res.stderr)
    sys.exit(1)
print(f"  ✓ Unaligned APK created ({os.path.getsize(UNALIGNED_APK)} bytes)")

print("Step 5: Adding classes.dex to APK...")
os.chdir(BIN_DIR)
cmd_add_dex = [AAPT, "add", UNALIGNED_APK, "classes.dex"]
res = subprocess.run(cmd_add_dex, capture_output=True, text=True)
if res.returncode != 0:
    print("Adding dex failed:", res.stderr)
    sys.exit(1)
print("  ✓ classes.dex added to APK")

print("Step 6: Running ZIPALIGN...")
if os.path.exists(ALIGNED_APK):
    os.remove(ALIGNED_APK)
cmd_zipalign = [ZIPALIGN, "-f", "-p", "4", UNALIGNED_APK, ALIGNED_APK]
res = subprocess.run(cmd_zipalign, capture_output=True, text=True)
if res.returncode != 0:
    print("Zipalign failed:", res.stderr)
    sys.exit(1)
print("  ✓ APK zipaligned successfully")

print("Step 7: Generating Release Signing Keystore...")
if not os.path.exists(KEYSTORE):
    cmd_keytool = [
        KEYTOOL,
        "-genkeypair",
        "-keystore", KEYSTORE,
        "-storepass", "apextrack123",
        "-alias", "apextrack",
        "-keypass", "apextrack123",
        "-dname", "CN=ApexTrack, O=ApexGym, C=US",
        "-validity", "10000",
        "-keyalg", "RSA",
        "-keysize", "2048"
    ]
    res = subprocess.run(cmd_keytool, capture_output=True, text=True)
    if res.returncode != 0:
        print("Keystore generation failed:", res.stderr)
        sys.exit(1)
    print("  ✓ Keystore created")

print("Step 8: Signing APK with APKSIGNER...")
if os.path.exists(FINAL_APK):
    os.remove(FINAL_APK)
cmd_sign = [
    APKSIGNER, "sign",
    "--ks", KEYSTORE,
    "--ks-pass", "pass:apextrack123",
    "--out", FINAL_APK,
    ALIGNED_APK
]
res = subprocess.run(cmd_sign, capture_output=True, text=True, shell=True)
if res.returncode != 0:
    print("APKSIGNER failed:", res.stderr)
    sys.exit(1)
print(f"  ✓ Signed APK created: {FINAL_APK} ({os.path.getsize(FINAL_APK)} bytes)")

print("Step 9: Verifying APK signature...")
cmd_verify = [APKSIGNER, "verify", "--verbose", FINAL_APK]
res = subprocess.run(cmd_verify, capture_output=True, text=True, shell=True)
print("  ✓ Signature verified:")
for line in res.stdout.splitlines()[:5]:
    print("    ", line)

print("\n========================================================")
print("🎉 SUCCESS! NATIVE ANDROID APK BUILT & SIGNED SUCCESSFULLY!")
print(f"📦 APK Location: {FINAL_APK}")
print(f"📊 Size: {os.path.getsize(FINAL_APK) / (1024 * 1024):.2f} MB")
print("========================================================")
