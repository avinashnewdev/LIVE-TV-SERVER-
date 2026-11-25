# 🚀 LIVE-TV-SERVER: M3U to Xtream Codes Converter

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white)
![Hosting](https://img.shields.io/badge/Hosted%20On-PythonAnywhere-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Server-24%2F7%20Active-brightgreen?style=for-the-badge)


Convert your simple `.m3u` playlist file into a **24/7 Cloud-Hosted Xtream Codes API Server** for free! Once set up, your server stays active on the cloud even when your PC is turned off.

---

## ✨ Features
- **100% Free Hosting:** Runs on GitHub + PythonAnywhere free tier.
- **24/7 Uptime:** No need to keep your PC or mobile turned on.
- **Wide Compatibility:** Works with Smart TVs, Set-Top Boxes (STB), IPTV Smarters Pro, TiviMate, and more.

---

## Step 1: Create a New Repository on GitHub
First, we need to host your `.m3u` playlist online so the server can read it.

1. Open [github.com](https://github.com) and log in (or create a free account).
2. Click the green **"New"** button to create a repository.
3. **Repository name:** Enter any name (e.g., `my-iptv` or `live-tv-server`).
4. **Visibility:** Keep it set to **Public** *(Required so PythonAnywhere can access the file without errors)*.
5. Scroll down and click **"Create repository"**.

---

## Step 2: Upload Your M3U File & Copy the RAW Link
1. On the new repository page, click **"uploading an existing file"**.
2. Click **"Choose your files"** and select your `.m3u` file from your PC or mobile.
3. Wait for the upload to reach 100%, then click **"Commit changes"**.
4. Click on your uploaded `.m3u` file name, then click the **"Raw"** button.
5. A plain-text page will open. **Copy the URL** from your browser's address bar and save it safely.

---

## Step 3: Set Up a Free Server on PythonAnywhere
1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com/) and click **"Create a beginner account"** (Free tier).
2. Sign up with your Email, Username, and Password *(Your chosen username will be part of your final server URL)*.
3. Once logged in, go to the **Web** tab in the top menu.
4. Click **"Add a new web app"**.
5. Follow the setup wizard: **Next** → Select **Flask** → Select **Python 3.10** (or the latest available version).
6. Keep the default path (`/home/username/mysite/flask_app.py`) and click **Finish**.

---

## Step 4: Add the Custom Python Code
1. Go to the **Files** tab in the top menu.
2. Open the `mysite/` folder and click on `flask_app.py`.
3. **Select all existing code and delete it.**
4. Paste the custom M3U-to-Xtream Python code from this repository into the file.
5. Locate `M3U_URL = ""` in the code and paste your **GitHub Raw link** (from Step 2) inside the quotes `""`.

---

## Step 5: Save & Reload the Server
1. Click the **Save** button at the top-right corner of the editor.

> [!WARNING]
> **DO NOT** click the `#run` button under any circumstances. Doing so can crash the server.

2. Go back to the **Web** tab (or use the top-right shortcut) and click the green **Reload (`your-username.pythonanywhere.com`)** button.
3. Reloading is mandatory—without it, your new code will not take effect.

---

## Step 6: Connect Your STB / IPTV Player
Open your Smart TV, Set-Top Box (STB), or mobile IPTV app (like **IPTV Smarters Pro** or **TiviMate**), select **Xtream Codes API**, and enter the following details:

| Field | Value | Notes |
| :--- | :--- | :--- |
| **URL (Host)** | `http://your-username.pythonanywhere.com` | Replace `your-username` with your PythonAnywhere username |
| **Username** | `admin` | Or the username you set in `flask_app.py` |
| **Password** | `1234` | Or the password you set in `flask_app.py` |

> [!TIP]
> **Login Failed?** Some IPTV apps require a port number. Try adding `:80` at the end of the URL:
> `http://your-username.pythonanywhere.com:80`

Click **Add User** or **Login**. Your playlist will load automatically, and your personal 24/7 Xtream IPTV server is ready! 🎉











# 🚀 LIVE-TV-SERVER: M3U TO XTREAM CONVERTOR TRICKS

Yeh ek detailed, step-by-step guide hai jo aapko sikhayegi ki kaise aap apni simple `.m3u` file ko ek 24/7 chalne wale **Xtream Codes API Server** mein convert kar sakte hain. Is method se aapka server cloud par hamesha active rahega, chahe aapka PC band hi kyun na ho.

1. **GitHub Par Naya Folder (Repository) Banayein:** M3U file ko internet par host karne ke liye.
Sabse pehle humein apni playlist file ko internet par rakhna hoga taaki hamara server use padh sake.

1. Apne browser mein [github.com](https://github.com) open karein aur apna account banayein (agar pehle se nahi hai). Account login karein.
2. Screen ke left side mein ya upar right corner mein ek green colour ka **"New"** button hoga, uspar click karein.
3. **Repository name:** Isme apne project ka koi bhi naam daal dein (jaise `my-iptv` ya `live-tv-server`).
4. **Public/Private:** Ise **Public** par hi set rehne dein. (Yeh bahut zaroori hai taaki PythonAnywhere ka server is file ko bina kisi error ke padh sake).
5. Page ke sabse neeche jayein aur green color ke **"Create repository"** button par click karein.


2. **M3U File Upload Karein aur RAW Link Nikalein:** Yeh link aage server mein daalna hoga.
Ab hum apni playlist ko us folder mein daalenge.

1. Naya page khulne par, aapko screen ke beech mein "uploading an existing file" ka ek chhota sa link dikhega, uspar click karein.
2. Ab **"Choose your files"** par click karein aur apne PC/Mobile se apni `.m3u` file select karein jo aap convert karna chahte hain.
3. File 100% upload hone ka wait karein. Uske baad neeche green color ke **"Commit changes"** button par click kar dein.
4. **[IMPORTANT] RAW Link Copy Karein:** Jab file upload ho jaye, toh us file ke naam par click karein. Phir screen par ek **"Raw"** naam ka button dikhega. Uspar click karein.
5. Ek naya page khulega jisme sirf text hoga. Us page ka **URL (link)** upar address bar se copy kar lein. Yeh aapki M3U file ka Raw link hai, ise kahin save kar lein.


3. **PythonAnywhere Par Free Server Setup Karein:** Aapka 24/7 chalne wala cloud server.
Is step mein hum ek free web server banayenge jo Xtream API ka kaam karega.

1. Apne browser mein [PythonAnywhere.com](https://www.pythonanywhere.com/) par jayein.
2. **"Create a beginner account"** (Free tier) par click karein aur apni Email ID, Username aur Password daal kar account banayein. (Yahan jo Username aap choose karenge, wahi aapke final URL mein aayega).
3. Login hone ke baad, aapke samne Dashboard khulega. Upar menu mein **Web** tab par click karein.
4. Left side mein **"Add a new web app"** button par click karein.
5. Ek popup aayega, usme **Next** karein -> **Flask** framework select karein -> **Python 3.10** (ya jo latest version available ho) select karein.
6. Path (jaise `/home/username/mysite/flask_app.py`) ko wahi rehne dein aur **Finish** karein. Badhai ho, aapka server ready ho gaya hai!


4. **Apna Custom Python Code Daalein:** flask_app.py ko edit karna.
Ab hum server ko batayenge ki use M3U file ko Xtream mein kaise badalna hai.

1. Upar main menu mein **Files** tab par click karein.
2. Wahan aapko `mysite/` naam ka ek folder dikhega. Us folder ko open karein.
3. Uske andar `flask_app.py` naam ki ek file hogi, uspar click karke use open karein.
4. Us file mein pehle se jo bhi code likha hai, **sab kuch select karke delete kar dein**.
5. Ab apne paas jo GitHub wali repository ka custom M3U to Xtream Python code hai, use wahan paste kar dein.
6. **Code Setup:** Code ke andar jahan `M3U_URL = ""` likha hoga, uske andar inverted commas `""` ke beech mein apna GitHub wala **Raw link** paste kar dein jo aapne Step 2 mein copy kiya tha.


5. **Save Karein aur Server Reload Karein:** Naye code ko activate karna.
Code daalne ke baad use activate karna zaroori hai.

1. Code sahi se paste karne ke baad, screen ke top right corner mein **Save** button par click karein.
2. **⚠️ WARNING:** Kisi bhi haal mein `#run` button par click **MAT** karna. Isse server crash ho sakta hai.
3. Save karne ke baad, ya toh usi screen par top right mein, ya wapas **Web** tab mein jakar ek green color ka button hoga jispar likha hoga **Reload (aapka-username.pythonanywhere.com)**.
4. Is **Reload** button ko zaroori dabayein. Agar aap reload nahi karenge, toh naya code apply nahi hoga aur error aayega.


6. **STB / IPTV Player Mein Setup Karein:** Xtream Codes details enter karna.
Aapka server ab live hai! Ab apne Smart TV, Set-Top Box (STB), ya mobile ke IPTV Player (jaise Smarters Pro, Tivimate) ko on karein aur Xtream Codes API ka option select karke yeh details daalein:

* **URL (Host):** `[http://aapka-username.pythonanywhere.com]` *(Yahan 'aapka-username' ki jagah apna PythonAnywhere ka username daalein)*
* **Username:** `admin` *(Ya jo username aapne flask_app.py ke code mein set kiya hai)*
* **Password:** `1234` *(Ya jo password aapne flask_app.py ke code mein set kiya hai)*

> **Pro Tip (Agar Login Na Ho):** Kabhi-kabhi kuch apps bina port ke URL accept nahi karte. Agar connection fail ho raha ho, toh URL ke aakhir mein port 80 lagakar try karein.
> Example: `[http://aapka-username.pythonanywhere.com:80]`


Sab kuch sahi se enter karne ke baad "Add User" ya "Login" par click karein. Aapki playlist download hona shuru ho jayegi aur Live TV chalne lagega. **Aapka apna personal Xtream IPTV server ab 24/7 chalne ke liye bilkul taiyar hai!**








# 🚀 LIVE-TV-SERVER: M3U से Xtream Codes कन्वर्टर

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white)
![Hosting](https://img.shields.io/badge/Hosted%20On-PythonAnywhere-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Server-24%2F7%20Active-brightgreen?style=for-the-badge)


यह एक स्टेप-बाय-स्टेप गाइड है जो आपको सिखाएगी कि कैसे आप अपनी साधारण `.m3u` फ़ाइल को एक 24/7 चलने वाले **Xtream Codes API सर्वर** में बदल सकते हैं। इस तरीके से आपका सर्वर क्लाउड पर हमेशा एक्टिव रहेगा, चाहे आपका PC बंद ही क्यों न हो।

---

## ✨ मुख्य फ़ीचर्स
- **100% फ्री होस्टिंग:** GitHub और PythonAnywhere के फ्री प्लान पर चलता है।
- **24/7 एक्टिव:** अपना PC या मोबाइल चालू रखने की ज़रूरत नहीं है।
- **सभी डिवाइस पर सपोर्ट:** Smart TV, Set-Top Box (STB), IPTV Smarters Pro, TiviMate आदि पर आसानी से काम करता है।

---

## स्टेप 1: GitHub पर नई Repository (फ़ोल्डर) बनाएं
सबसे पहले हमें अपनी `.m3u` प्लेलिस्ट फ़ाइल को इंटरनेट पर अपलोड करना होगा ताकि हमारा सर्वर उसे पढ़ सके।

1. अपने ब्राउज़र में [github.com](https://github.com) खोलें और लॉगिन करें (अगर अकाउंट नहीं है, तो नया फ्री अकाउंट बनाएं)।
2. स्क्रीन के बाईं ओर या ऊपर दाईं ओर हरे रंग के **"New"** बटन पर क्लिक करें।
3. **Repository name:** इसमें अपने प्रोजेक्ट का कोई भी नाम डालें (जैसे `my-iptv` या `live-tv-server`)।
4. **Public/Private:** इसे **Public** पर ही रहने दें *(यह बहुत ज़रूरी है ताकि PythonAnywhere का सर्वर इस फ़ाइल को बिना किसी एरर के पढ़ सके)*।
5. पेज के सबसे नीचे जाएं और **"Create repository"** बटन पर क्लिक करें।

---

## स्टेप 2: M3U फ़ाइल अपलोड करें और RAW लिंक कॉपी करें
1. नया पेज खुलने पर स्क्रीन के बीच में **"uploading an existing file"** लिंक पर क्लिक करें।
2. **"Choose your files"** पर क्लिक करें और अपने PC या मोबाइल से अपनी `.m3u` फ़ाइल चुनें।
3. फ़ाइल 100% अपलोड होने के बाद नीचे **"Commit changes"** बटन पर क्लिक कर दें।
4. फ़ाइल अपलोड हो जाने के बाद उसके नाम पर क्लिक करें, और फिर स्क्रीन पर दिखने वाले **"Raw"** बटन पर क्लिक करें।
5. एक नया टेक्स्ट पेज खुलेगा। ऊपर एड्रेस बार से उस पेज का **URL (Raw Link)** कॉपी करें और कहीं सेव कर लें।

---

## स्टेप 3: PythonAnywhere पर फ्री सर्वर सेटअप करें
1. अपने ब्राउज़र में [PythonAnywhere.com](https://www.pythonanywhere.com/) खोलें।
2. **"Create a beginner account"** (फ्री टियर) पर क्लिक करें और अपनी Email ID, Username और Password डालकर अकाउंट बनाएं *(यहाँ जो Username आप चुनेंगे, वही आपके फ़ाइनल URL में आएगा)*।
3. लॉगिन होने के बाद ऊपर मेन्यू में **Web** टैब पर क्लिक करें।
4. बाईं ओर **"Add a new web app"** बटन पर क्लिक करें।
5. पॉपअप में **Next** करें → **Flask** चुनें → **Python 3.10** (या जो लेटेस्ट वर्ज़न उपलब्ध हो) चुनें।
6. पाथ (`/home/username/mysite/flask_app.py`) को वैसा ही रहने दें और **Finish** पर क्लिक करें। आपका सर्वर तैयार है!

---

## स्टेप 4: कस्टम Python कोड डालें (`flask_app.py`)
1. ऊपर मेन मेन्यू में **Files** टैब पर क्लिक करें।
2. `mysite/` फ़ोल्डर खोलें और उसके अंदर `flask_app.py` फ़ाइल पर क्लिक करें।
3. उस फ़ाइल में पहले से लिखा हुआ **सारा कोड सेलेक्ट करके डिलीट कर दें**।
4. इस रिपॉजिटरी का कस्टम M3U-to-Xtream Python कोड वहाँ पेस्ट कर दें।
5. कोड के अंदर जहाँ `M3U_URL = ""` लिखा है, वहाँ इनवर्टेड कॉमा `""` के बीच में अपना **GitHub Raw लिंक** (जो आपने स्टेप 2 में कॉपी किया था) पेस्ट कर दें।

---

## स्टेप 5: सेव करें और सर्वर रीलोड करें
1. कोड पेस्ट करने के बाद ऊपर दाईं ओर **Save** बटन पर क्लिक करें।

> [!WARNING]
> किसी भी हाल में `#run` बटन पर क्लिक **न करें**। इससे सर्वर क्रैश हो सकता है।

2. सेव करने के बाद **Web** टैब में वापस जाएं और हरे रंग के **Reload (`aapka-username.pythonanywhere.com`)** बटन पर क्लिक करें।
3. **Reload** दबाना ज़रूरी है, वरना नया कोड लागू नहीं होगा और एरर आएगा।

---

## स्टेप 6: STB / IPTV प्लेयर में सेटअप करें
अब अपने Smart TV, Set-Top Box (STB), या मोबाइल के IPTV प्लेयर (जैसे **IPTV Smarters Pro**, **TiviMate**) में **Xtream Codes API** चुनें और ये जानकारी डालें:

| फ़ील्ड | जानकारी | नोट |
| :--- | :--- | :--- |
| **URL (Host)** | `http://aapka-username.pythonanywhere.com` | `aapka-username` की जगह अपना PythonAnywhere यूज़रनेम डालें |
| **Username** | `admin` | या जो यूज़रनेम आपने `flask_app.py` में सेट किया है |
| **Password** | `1234` | या जो पासवर्ड आपने `flask_app.py` में सेट किया है |

> [!TIP]
> **अगर लॉगिन न हो:** कुछ ऐप्स बिना पोर्ट के URL स्वीकार नहीं करते। अगर कनेक्शन फेल हो रहा हो, तो URL के आखिर में `:80` लगाकर ट्राई करें:
> `http://aapka-username.pythonanywhere.com:80`

सब कुछ सही से डालने के बाद **Add User** या **Login** पर क्लिक करें। आपकी प्लेलिस्ट लोड हो जाएगी और आपका पर्सनल 24/7 Xtream IPTV सर्वर चलने के लिए बिल्कुल तैयार है! 🎉

