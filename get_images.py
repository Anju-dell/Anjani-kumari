import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

items = [
    "Paneer_tikka", "Chicken_65", "Gobi_manchurian", "Chilli_chicken", "Spring_roll",
    "Paneer_makhani", "Kadai_paneer", "Dal_makhani", "Aloo_gobi", "Palak_paneer",
    "Chicken_tikka_masala", "Rogan_josh", "Butter_chicken", "Malabar_matthi_curry", "Biryani",
    "Gulab_jamun", "Ras_malai", "Gajar_ka_halwa", "Chocolate_brownie", "Fruit_salad",
    "Limeade", "Cola", "Sprite_(drink)", "Lassi", "Iced_tea",
    "Vanilla_ice_cream", "Chocolate_ice_cream", "Strawberry_ice_cream", "Butterscotch", "Mango"
]

for item in items:
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={item}&prop=pageimages&format=json&pithumbsize=200"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            page = list(pages.values())[0]
            if 'thumbnail' in page:
                print(page['thumbnail']['source'])
            else:
                print("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/200px-Good_Food_Display_-_NCI_Visuals_Online.jpg")
    except Exception as e:
        print("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/200px-Good_Food_Display_-_NCI_Visuals_Online.jpg")
