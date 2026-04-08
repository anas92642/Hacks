#!/usr/bin/env python3
try:
    import requests, json, re, time, os, datetime
    from rich import print as Println
    from rich.console import Console
    from rich.panel import Panel
    from rich.columns import Columns
    from requests.exceptions import RequestException
except ModuleNotFoundError as e:
    exit(f"[Error] {str(e).capitalize()}!")

SUKSES, GAGAL, CREDITS = [], [], {"COUNT": 0}

def Banner() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    # Yahan "Anas" stylish ASCII art mein update kar diya gaya hai
    Println(Panel(r"""[bold red]     _    _   _    _    ____  
    / \  | \ | |  / \  / ___| 
   / _ \ |  \| | / _ \ \___ \ 
  / ___ \| |\  |/ ___ \ ___) |
 /_/   \_\_| \_/_/   \_\____/ 
                               
[bold white]  Developed by Anas - Turbo Speed Script""", width=59, style="bold bright_black"))
    return None

class Bypass:
    def Spam(self, session: requests.Session, cookies: str) -> None:
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Host': 'www.like4like.org',
        })
        session.get('https://www.like4like.org/user/earn-instagram-follow.php', cookies={'Cookie': cookies})

class Mission:
    def Delay(self, duration: float) -> None:
        # Milliseconds support (e.g. 0.5 for 500ms)
        stop = time.time() + duration
        while time.time() < stop:
            rem = stop - time.time()
            Println(f"[bold bright_black]   ╰─>[bold white] NEXT TASK:[bold green] {rem:.2f}s [bold white]OK:[bold green]{len(SUKSES)} [bold red]{len(GAGAL)}", end='\r')
            time.sleep(0.01)

    def Like4Like(self, cookies_l4l: str, cookies_ig: str, fast_delay: float) -> bool:
        with requests.Session() as session:
            # Task fetching logic
            res = session.get('https://www.like4like.org/api/get-tasks.php?feature=instagramfol', cookies={"Cookie": cookies_l4l})
            if '"success":true' in res.text:
                tasks = json.loads(res.text).get('data', {}).get('tasks', [])
                for z in tasks:
                    idlink, taskId = z['idlink'], z['taskId']
                    
                    # Start Task
                    session.get(f'https://www.like4like.org/api/start-task.php?idzad={idlink}&vrsta=follow&idcod={taskId}&feature=instagramfol', cookies={"Cookie": cookies_l4l})
                    
                    # Millisecond speed tweak (0.7s = 700ms)
                    time.sleep(0.7) 
                    
                    # Verify/Validate logic (Yahan aapka custom follow logic aayega)
                    # Maan lete hain validation successful rahi:
                    SUKSES.append(1)
                    
                    # User-defined millisecond delay
                    self.Delay(fast_delay)
            return True

# --- Script Instructions ---
# Jab script "Jeda Misi" (Delay) mange, toh aap "0.5" ya "1" enter karein.
# "0.5" ka matlab hai 500 milliseconds (bohot fast).
# Lekin safe earning ke liye "2.0" ya "3.0" behtar hai.
