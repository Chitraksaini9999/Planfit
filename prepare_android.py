import os
import sys
import shutil
import subprocess

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

print("Checking prerequisites...")
for name, path in [("AAPT", AAPT), ("D8", D8), ("ZIPALIGN", ZIPALIGN), ("APKSIGNER", APKSIGNER), ("JAVAC", JAVAC), ("KEYTOOL", KEYTOOL), ("PLATFORM_JAR", PLATFORM_JAR)]:
    if not os.path.exists(path):
        print(f"Error: missing {name} at {path}")
        sys.exit(1)
    else:
        print(f"  ✓ {name}: found")

# Clean build directory
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)

SRC_DIR = os.path.join(BUILD_DIR, "src", "com", "planfit", "workout")
RES_DIR = os.path.join(BUILD_DIR, "res")
ASSETS_DIR = os.path.join(BUILD_DIR, "assets")
BIN_DIR = os.path.join(BUILD_DIR, "bin")
CLASSES_DIR = os.path.join(BIN_DIR, "classes")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(os.path.join(RES_DIR, "values"), exist_ok=True)
os.makedirs(os.path.join(RES_DIR, "drawable"), exist_ok=True)
os.makedirs(os.path.join(RES_DIR, "xml"), exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(CLASSES_DIR, exist_ok=True)

# 1. AndroidManifest.xml
manifest_content = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.planfit.workout"
    android:versionCode="1"
    android:versionName="1.0.0">

    <uses-sdk
        android:minSdkVersion="24"
        android:targetSdkVersion="34" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_SPECIAL_USE" />

    <application
        android:label="@string/app_name"
        android:icon="@drawable/ic_launcher"
        android:roundIcon="@drawable/ic_launcher"
        android:allowBackup="true"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
        android:networkSecurityConfig="@xml/network_security_config">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <service
            android:name=".WorkoutBackgroundService"
            android:foregroundServiceType="specialUse"
            android:exported="false">
            <property
                android:name="android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE"
                android:value="Workout timer and exercise tracking in background" />
        </service>

    </application>
</manifest>
"""
manifest_path = os.path.join(BUILD_DIR, "AndroidManifest.xml")
with open(manifest_path, "w", encoding="utf-8") as f:
    f.write(manifest_content)

# 2. strings.xml
strings_content = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Planfit</string>
</resources>
"""
with open(os.path.join(RES_DIR, "values", "strings.xml"), "w", encoding="utf-8") as f:
    f.write(strings_content)

# 3. network_security_config.xml
net_sec_content = """<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="true" />
</network-security-config>
"""
with open(os.path.join(RES_DIR, "xml", "network_security_config.xml"), "w", encoding="utf-8") as f:
    f.write(net_sec_content)

# 4. Copy icons
icon_src = os.path.join(WORKSPACE, "mobile_app", "icon-192.png")
if os.path.exists(icon_src):
    shutil.copy2(icon_src, os.path.join(RES_DIR, "drawable", "ic_launcher.png"))
    shutil.copy2(icon_src, os.path.join(RES_DIR, "drawable", "ic_notification.png"))

# 5. Java files
main_activity_java = """package com.planfit.workout;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.os.Vibrator;
import android.os.VibrationEffect;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

public class MainActivity extends Activity {
    private WebView mWebView;
    private static final String PREFS_NAME = "PlanfitPrefs";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        mWebView = new WebView(this);
        setContentView(mWebView);

        WebSettings settings = mWebView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);

        mWebView.setWebViewClient(new WebViewClient());
        mWebView.setWebChromeClient(new WebChromeClient());

        mWebView.addJavascriptInterface(new WebAppInterface(this), "AndroidBridge");

        mWebView.loadUrl("file:///android_asset/index.html");
    }

    public class WebAppInterface {
        Context mContext;

        WebAppInterface(Context c) {
            mContext = c;
        }

        @JavascriptInterface
        public void startBackgroundTracking(String dayName, String focus) {
            Intent serviceIntent = new Intent(mContext, WorkoutBackgroundService.class);
            serviceIntent.setAction(WorkoutBackgroundService.ACTION_START);
            serviceIntent.putExtra("dayName", dayName);
            serviceIntent.putExtra("focus", focus);
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                mContext.startForegroundService(serviceIntent);
            } else {
                mContext.startService(serviceIntent);
            }
        }

        @JavascriptInterface
        public void updateProgress(String exerciseName, int currentSet, int totalSets) {
            Intent serviceIntent = new Intent(mContext, WorkoutBackgroundService.class);
            serviceIntent.setAction(WorkoutBackgroundService.ACTION_UPDATE);
            serviceIntent.putExtra("exerciseName", exerciseName);
            serviceIntent.putExtra("currentSet", currentSet);
            serviceIntent.putExtra("totalSets", totalSets);
            mContext.startService(serviceIntent);
        }

        @JavascriptInterface
        public void stopBackgroundTracking() {
            Intent serviceIntent = new Intent(mContext, WorkoutBackgroundService.class);
            serviceIntent.setAction(WorkoutBackgroundService.ACTION_STOP);
            mContext.startService(serviceIntent);
        }

        @JavascriptInterface
        public void saveWorkoutProgress(String jsonData) {
            SharedPreferences prefs = mContext.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
            prefs.edit().putString("saved_workout_data", jsonData).apply();
        }

        @JavascriptInterface
        public String getWorkoutProgress() {
            SharedPreferences prefs = mContext.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
            return prefs.getString("saved_workout_data", "[]");
        }

        @JavascriptInterface
        public void vibratePhone(int milliseconds) {
            Vibrator v = (Vibrator) mContext.getSystemService(Context.VIBRATOR_SERVICE);
            if (v != null && v.hasVibrator()) {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                    v.vibrate(VibrationEffect.createOneShot(milliseconds, VibrationEffect.DEFAULT_AMPLITUDE));
                } else {
                    v.vibrate(milliseconds);
                }
            }
        }

        @JavascriptInterface
        public void showToast(String message) {
            Toast.makeText(mContext, message, Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onBackPressed() {
        if (mWebView.canGoBack()) {
            mWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
"""

with open(os.path.join(SRC_DIR, "MainActivity.java"), "w", encoding="utf-8") as f:
    f.write(main_activity_java)

service_java = """package com.planfit.workout;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.os.Handler;
import android.os.IBinder;
import android.os.PowerManager;

public class WorkoutBackgroundService extends Service {
    public static final String ACTION_START = "ACTION_START";
    public static final String ACTION_UPDATE = "ACTION_UPDATE";
    public static final String ACTION_STOP = "ACTION_STOP";
    private static final String CHANNEL_ID = "PlanfitWorkoutChannel";
    private static final int NOTIF_ID = 1001;

    private PowerManager.WakeLock mWakeLock;
    private Handler mHandler;
    private int mElapsedSeconds = 0;
    private String mDayName = "Workout";
    private String mFocus = "In Progress";
    private String mExerciseStatus = "Active";

    private final Runnable mTimerRunnable = new Runnable() {
        @Override
        public void run() {
            mElapsedSeconds++;
            updateNotification();
            mHandler.postDelayed(this, 1000);
        }
    };

    @Override
    public void onCreate() {
        super.onCreate();
        createNotificationChannel();
        mHandler = new Handler();

        PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
        if (pm != null) {
            mWakeLock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "Planfit:WorkoutWakeLock");
            mWakeLock.acquire(4 * 60 * 60 * 1000L); // 4 hour safety timeout
        }
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (intent != null && intent.getAction() != null) {
            String action = intent.getAction();
            if (ACTION_START.equals(action)) {
                mDayName = intent.getStringExtra("dayName");
                if (mDayName == null) mDayName = "Workout";
                mFocus = intent.getStringExtra("focus");
                if (mFocus == null) mFocus = "Training Session";
                mElapsedSeconds = 0;
                startForeground(NOTIF_ID, buildNotification());
                mHandler.removeCallbacks(mTimerRunnable);
                mHandler.post(mTimerRunnable);
            } else if (ACTION_UPDATE.equals(action)) {
                String ex = intent.getStringExtra("exerciseName");
                int cur = intent.getIntExtra("currentSet", 1);
                int tot = intent.getIntExtra("totalSets", 4);
                mExerciseStatus = ex + " (Set " + cur + "/" + tot + ")";
                updateNotification();
            } else if (ACTION_STOP.equals(action)) {
                stopSelf();
            }
        }
        return START_STICKY;
    }

    private void updateNotification() {
        NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        if (nm != null) {
            nm.notify(NOTIF_ID, buildNotification());
        }
    }

    private Notification buildNotification() {
        int mins = mElapsedSeconds / 60;
        int secs = mElapsedSeconds % 60;
        String timeStr = String.format("%02d:%02d", mins, secs);

        Intent notificationIntent = new Intent(this, MainActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(
                this, 0, notificationIntent,
                Build.VERSION.SDK_INT >= Build.VERSION_CODES.M ? PendingIntent.FLAG_IMMUTABLE : 0
        );

        Notification.Builder builder;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            builder = new Notification.Builder(this, CHANNEL_ID);
        } else {
            builder = new Notification.Builder(this);
        }

        builder.setContentTitle("⚡ Planfit: " + mDayName + " [" + timeStr + "]")
               .setContentText(mFocus + " • " + mExerciseStatus)
               .setSmallIcon(R.drawable.ic_notification)
               .setContentIntent(pendingIntent)
               .setOngoing(true);

        return builder.build();
    }

    private void createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                    CHANNEL_ID,
                    "Workout Live Progress",
                    NotificationManager.IMPORTANCE_LOW
            );
            channel.setDescription("Ongoing timer and set tracking during workout sessions");
            NotificationManager nm = getSystemService(NotificationManager.class);
            if (nm != null) {
                nm.createNotificationChannel(channel);
            }
        }
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        mHandler.removeCallbacks(mTimerRunnable);
        if (mWakeLock != null && mWakeLock.isHeld()) {
            mWakeLock.release();
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
"""

with open(os.path.join(SRC_DIR, "WorkoutBackgroundService.java"), "w", encoding="utf-8") as f:
    f.write(service_java)

# 6. Copy web app assets into ASSETS_DIR
mobile_app_dir = os.path.join(WORKSPACE, "mobile_app")
shutil.copy2(os.path.join(mobile_app_dir, "index.html"), os.path.join(ASSETS_DIR, "index.html"))
shutil.copytree(os.path.join(mobile_app_dir, "images"), os.path.join(ASSETS_DIR, "images"), dirs_exist_ok=True)
if os.path.exists(os.path.join(mobile_app_dir, "manifest.json")):
    shutil.copy2(os.path.join(mobile_app_dir, "manifest.json"), os.path.join(ASSETS_DIR, "manifest.json"))

# Enhance index.html inside assets to communicate with AndroidBridge if present!
with open(os.path.join(ASSETS_DIR, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

bridge_patch = """
// Native Android Bridge Integration
function notifyAndroidStart(dayName, focus) {
  if (window.AndroidBridge && window.AndroidBridge.startBackgroundTracking) {
    window.AndroidBridge.startBackgroundTracking(dayName, focus);
  }
}
function notifyAndroidUpdate(exName, curSet, totalSets) {
  if (window.AndroidBridge && window.AndroidBridge.updateProgress) {
    window.AndroidBridge.updateProgress(exName, curSet, totalSets);
  }
}
function notifyAndroidStop() {
  if (window.AndroidBridge && window.AndroidBridge.stopBackgroundTracking) {
    window.AndroidBridge.stopBackgroundTracking();
  }
}
function notifyAndroidVibrate(ms) {
  if (window.AndroidBridge && window.AndroidBridge.vibratePhone) {
    window.AndroidBridge.vibratePhone(ms);
  }
}
"""

if "function notifyAndroidStart" not in index_html:
    index_html = index_html.replace("<script>", "<script>\n" + bridge_patch)
    index_html = index_html.replace("switchNav('tabRunner');", "notifyAndroidStart(day.day_name, day.focus);\n  switchNav('tabRunner');")
    index_html = index_html.replace("loadActiveExercise(0);", "loadActiveExercise(0);\n  notifyAndroidUpdate(day.exercises[0].name, 1, 4);")
    index_html = index_html.replace("clearInterval(sessionTimerInterval);", "notifyAndroidStop();\n  clearInterval(sessionTimerInterval);")

with open(os.path.join(ASSETS_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Android files and assets prepared successfully!")
