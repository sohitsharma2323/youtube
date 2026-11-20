import json
import subprocess

def get_stream_info(url):
    command = ['python','-m','yt_dlp', '-j', url]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        print("Error fetching info:", result.stderr)
        return None

if __name__ == "__main__":
    video_url ="https://youtu.be/UPwHx7GXWbg" 
    info = get_stream_info(video_url)
    if info:
        print(f"Title: {info.get('title')}")
        print(f"Channel: {info.get('channel')}")
