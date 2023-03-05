from real_url.douyu import DouYu
import json

def write_playlist():
    s = DouYu(74751)
    s.did = s.get_did()
    urls = json.loads(s.get_real_url())
    with open("playlist.m3u8", "w") as f:
        f.write("#EXTM3U\n")
        for i, url in enumerate(urls.values()):
            f.write(f"#EXTINF:-1, Source({i})\n")
            f.write(f"{url}\n")

if __name__ == "__main__":
    write_playlist()