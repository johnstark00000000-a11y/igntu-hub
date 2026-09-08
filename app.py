import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

# In-memory database (Production-ready template with default items)
db = {
    "radar": [
        {"vibe": "💖 Coffee & Deep Talks", "location": "Main Canteen Area", "lat": 22.6789, "lng": 81.7456, "time": "Active for next 30 mins", "user": "Aman (Biotech)"},
        {"vibe": "🌹 Sunset Library Walk", "location": "Central Library Lawn", "lat": 22.6775, "lng": 81.7442, "time": "Active for 1 hour", "user": "Rahul"}
    ],
    "stationery": [
        {"item": "Engineering Math Textbook", "shop": "Campus Store", "price": 420, "distance": "0.5 km"},
        {"item": "Scientific Calculator", "shop": "Student Hub", "price": 800, "distance": "1.2 km"}
    ],
    "marketplace": [
        {"item": "Lab Coat (Clean)", "seller": "Rahul", "price": 150, "contact": "Hostel 3"},
        {"item": "Bicycle", "seller": "Aman", "price": 1200, "contact": "Main Gate"}
    ],
    "vault": [
        {"subject": "Biotechnology Sem 2 Notes", "uploader": "Topper", "link": "#"},
        {"subject": "Ecology & Niche PYQs", "uploader": "Senior", "link": "#"}
    ],
    "confessions": [
        {"text": "Library top floor wali girl is a total vibe ✨, wish I had the courage to say hi!", "type": "Confession"}
    ],
    "canteen": [
        {"item": "Veg Maggi", "price": 50, "time": "5 mins"},
        {"item": "Cold Coffee with Love ☕", "price": 40, "time": "3 mins"}
    ],
    "lost_found": [
        {"item": "Casio Calculator", "location": "Lab 2", "status": "Lost"},
        {"item": "Cute Keychain", "location": "Canteen", "status": "Found"}
    ],
    "hostel_complaints": [
        {"issue": "Wi-Fi router down in corridor", "location": "Hostel 2, Floor 2", "status": "Pending"}
    ],
    "carpool": [
        {"route": "Campus to Railway Station", "time": "Today, 5:00 PM", "contact": "Aakash"}
    ],
    "memes": [
        {"caption": "When attendance is 74% but your crush sits in the front row:", "uploader": "Anonymous"}
    ],
    "mess_polls": [
        {"day": "Wednesday", "meal": "Paneer Special", "rating": 4.6, "votes": 184}
    ],
    "bunk_buddies": [
        {"msg": "Who's skipping the 10 AM lecture? Let's grab coffee instead!", "poster": "Ankit"}
    ],
    "quotes": [
        {"quote": "Tum log copy khol ke baithe ho ya furniture check kar rahe ho?", "professor": "Dr. Sharma (Biotech Dept)"}
    ],
    "midnight": [
        {"item": "Hot Maggi + Coffee Combo", "seller": "Rahul", "hostel": "Hostel 2, Room 104", "price": 70}
    ],
    "fest": [
        {"caption": "Prom night stage madness & beautiful lights ✨", "uploader": "Aman (Final Year)"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=db)

# Service worker / Manifest routing fallback if needed
@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/add/<category>', methods=['POST'])
def add_item(category):
    if category == 'radar':
        db['radar'].append({
            "vibe": request.form.get('vibe'),
            "location": request.form.get('location'),
            "lat": float(request.form.get('lat') or 22.6789),
            "lng": float(request.form.get('lng') or 81.7456),
            "time": request.form.get('time'),
            "user": "Student"
        })
    elif category == 'quotes':
        db['quotes'].append({"quote": request.form.get('quote'), "professor": request.form.get('professor')})
    elif category == 'midnight':
        db['midnight'].append({"item": request.form.get('item'), "seller": request.form.get('seller'), "hostel": request.form.get('hostel'), "price": float(request.form.get('price'))})
    elif category == 'fest':
        db['fest'].append({"caption": request.form.get('caption'), "uploader": request.form.get('uploader')})
    elif category == 'memes':
        db['memes'].append({"caption": request.form.get('caption'), "uploader": "Anonymous Student"})
    elif category == 'mess_polls':
        db['mess_polls'].append({"day": request.form.get('day'), "meal": request.form.get('meal'), "rating": float(request.form.get('rating')), "votes": 1})
    elif category == 'bunk_buddies':
        db['bunk_buddies'].append({"msg": request.form.get('msg'), "poster": "Student"})
    elif category == 'stationery':
        db['stationery'].append({"item": request.form.get('item'), "shop": request.form.get('shop'), "price": float(request.form.get('price')), "distance": request.form.get('distance')})
    elif category == 'marketplace':
        db['marketplace'].append({"item": request.form.get('item'), "seller": request.form.get('seller'), "price": float(request.form.get('price')), "contact": request.form.get('contact')})
    elif category == 'confessions':
        db['confessions'].append({"text": request.form.get('text'), "type": "Confession"})
    elif category == 'hostel_complaints':
        db['hostel_complaints'].append({"issue": request.form.get('issue'), "location": request.form.get('location'), "status": "Pending"})
    elif category == 'carpool':
        db['carpool'].append({"route": request.form.get('route'), "time": request.form.get('time'), "contact": request.form.get('contact')})
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
