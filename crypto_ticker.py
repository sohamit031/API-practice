import requests
import threading
import time

# --- PART 1: THE BLUEPRINT ---
class CryptoBot:
    def __init__(self, coin_id):
        self.coin_id = coin_id
        self.price = 0.0
        # NEW URL: CoinGecko API
        self.url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

    def fetch_price(self):
        print(f"🤖 {self.coin_id}: Connecting...")
        
        # Disguise is still a good idea
        fake_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        try:
            response = requests.get(self.url, headers=fake_headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                # CoinGecko format is: {'bitcoin': {'usd': 25000}}
                if self.coin_id in data:
                    self.price = data[self.coin_id]['usd']
                    print(f"✅ {self.coin_id}: SUCCESS")
                else:
                    print(f"❓ {self.coin_id}: Data not found")
            else:
                print(f"❌ {self.coin_id}: Blocked (Code {response.status_code})")
                
        except Exception as e:
            print(f"⚠️ {self.coin_id} ERROR: {e}")

# --- PART 2: THE EXECUTION (Back to Threading!) ---

# CoinGecko uses specific IDs (lowercase)
coins_to_track = ['bitcoin', 'ethereum', 'dogecoin', 'tether', 'binancecoin'] 
# Note: 'binance-coin' is 'binancecoin' on CoinGecko usually, but let's try 'binancecoin'

bots = []

print(f"--- TRACKING {len(coins_to_track)} COINS (CoinGecko) ---")
start_time = time.time()

# 1. Create Bots
for coin in coins_to_track:
    bot = CryptoBot(coin)
    bots.append(bot)

# 2. Run Threads
threads = []
for bot in bots:
    t = threading.Thread(target=bot.fetch_price)
    threads.append(t)
    t.start()

# 3. Wait for finish
for t in threads:
    t.join()

end_time = time.time()

# --- PART 3: THE REPORT ---
print("\n--- 📊 LIVE MARKET REPORT ---")
for bot in bots:
    print(f"{bot.coin_id.upper()}: \t${bot.price:,.2f}")

print(f"\nTime taken: {end_time - start_time:.2f} seconds")