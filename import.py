import csv
import redis

# --- CONFIG ---
CSV_FILE = "Ubereat_US_Merchant.csv"
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None  # Mets ton mot de passe si besoin

# --- CONNEXION À REDIS ---
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# --- LECTURE DU CSV ---
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for i, row in enumerate(reader, start=1):
        # Clé Redis : merchant:{id}
        key = f"merchant:{i}"
        # Stocker la ligne entière comme hash
        r.hset(key, mapping=row)

        if i % 100 == 0:
            print(f"{i} lignes importées...")

print("✅ Import terminé !")

