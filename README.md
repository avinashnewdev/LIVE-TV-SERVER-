# 🚀 LIVE-TV-SERVER: M3U TO XTREAM CONVERTOR TRICK

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
