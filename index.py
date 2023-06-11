from real_url.douyu import DouYu
import json

def write_playlist():
    urls = []
    lv_urls = []
    try:
        s = DouYu(74751)
        urls = json.loads(s.get_real_url()).values()
    except Exception as e:
        print(f"(74751)An error occurred: {e}")

    try:
        lv = DouYu(5110403)
        lv.did = lv.get_did()
        lv_urls = json.loads(lv.get_real_url()).values()
    except Exception as e:
        print(f"(5110403)An error occurred: {e}")

    with open("playlist.m3u8", "w") as f:
        f.write("#EXTM3U\n")
        for i, url in enumerate(urls):
            f.write(f"#EXTINF:-1, Source({i})\n")
            f.write(f"{url}\n")
        for i, url in enumerate(lv_urls):
            f.write(f"#EXTINF:-1, lv Source({i})\n")
            f.write(f"{url}\n")

if __name__ == "__main__":
    write_playlist()
