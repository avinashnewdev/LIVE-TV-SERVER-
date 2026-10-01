from flask import Flask, request, redirect, Response
import requests
import json

app = Flask(__name__)

# --- APNI DETAILS YAHAN DAALEIN ---
M3U_URL = "PASTE YOUR RAW LINK"
MY_USER = "YOUR LOGIN NAME"
MY_PASS = "YOUR PASS"
MY_DOMAIN = "USERNAME.pythonanywhere.com"
# -----------------------------------

streams_cache = {}

def load_m3u():
    global streams_cache
    streams_cache.clear()
    try:
        resp = requests.get(M3U_URL)
        lines = resp.text.splitlines()
        current_name = "Unknown Channel"
        stream_id = 1
        
        for line in lines:
            line = line.strip()
            if line.startswith("#EXTINF"):
                parts = line.split(",")
                current_name = parts[-1].strip()
            elif line.startswith("http"):
                streams_cache[str(stream_id)] = {"name": current_name, "url": line}
                stream_id += 1
    except:
        pass

def send_json(data):
    # STB ke liye perfect JSON format
    return Response(json.dumps(data), mimetype='application/json')

@app.route('/player_api.php', methods=['GET', 'POST'])
@app.route('/panel_api.php', methods=['GET', 'POST'])
def player_api():
    user = request.values.get('username')
    pwd = request.values.get('password')
    action = request.values.get('action')

    # Agar user/pass match na ho
    if user != MY_USER or pwd != MY_PASS:
        return send_json({"user_info": {"auth": 0}})

    if not streams_cache:
        load_m3u()

    # 1. Login Details (Expiry date 2030 set ki hai taaki STB error na de)
    if not action:
        return send_json({
            "user_info": {
                "username": MY_USER,
                "password": MY_PASS,
                "message": "Login Success",
                "auth": 1,
                "status": "Active",
                "exp_date": "1893456000", 
                "is_trial": "0",
                "active_cons": "0",
                "created_at": "1600000000",
                "max_connections": "1",
                "allowed_output_formats": ["m3u8", "ts", "rtmp"]
            },
            "server_info": {
                "url": MY_DOMAIN,
                "port": "80",
                "https_port": "443",
                "server_protocol": "http",
                "rtmp_port": "1935",
                "timezone": "Asia/Kolkata",
                "timestamp_now": 1700000000,
                "time_now": "2024-01-01 12:00:00"
            }
        })
    
    # 2. Categories
    if action == "get_live_categories":
        return send_json([{"category_id": "1", "category_name": "Live TV", "parent_id": 0}])
    
    # 3. Channels
    if action == "get_live_streams":
        out = []
        for sid, data in streams_cache.items():
            out.append({
                "num": int(sid),
                "name": data["name"],
                "stream_type": "live",
                "stream_id": int(sid),
                "stream_icon": "",
                "epg_channel_id": None,
                "added": "1600000000",
                "category_id": "1",
                "custom_sid": "",
                "tv_archive": 0,
                "direct_source": "",
                "tv_archive_duration": 0
            })
        return send_json(out)
        
    # VOD/Series ko khali bhejna zaroori hai
    if action in ["get_vod_categories", "get_series_categories", "get_vod_streams", "get_series"]:
        return send_json([])
        
    return send_json([])

# Kuch boxes get.php ka use karte hain
@app.route('/get.php', methods=['GET', 'POST'])
def get_m3u():
    user = request.values.get('username')
    pwd = request.values.get('password')
    if user != MY_USER or pwd != MY_PASS:
        return "Unauthorized", 401
    
    if not streams_cache:
        load_m3u()
        
    m3u_output = "#EXTM3U\n"
    for sid, data in streams_cache.items():
        m3u_output += f"#EXTINF:-1,{data['name']}\n"
        m3u_output += f"http://{MY_DOMAIN}/live/{MY_USER}/{MY_PASS}/{sid}.ts\n"
        
    return Response(m3u_output, mimetype='audio/x-mpegurl')

@app.route('/xmltv.php', methods=['GET', 'POST'])
def xmltv():
    return Response('<?xml version="1.0" encoding="utf-8" ?><tv></tv>', mimetype='application/xml')

@app.route('/live/<user>/<pwd>/<path:stream_id>', methods=['GET', 'POST'])
def play_stream(user, pwd, stream_id):
    if user != MY_USER or pwd != MY_PASS:
        return "Unauthorized", 401
        
    clean_id = stream_id.split('.')[0]
    
    if not streams_cache:
        load_m3u()
        
    if clean_id in streams_cache:
        return redirect(streams_cache[clean_id]["url"])
        
    return "Not Found", 404
