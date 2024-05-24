import sublime
import sublime_plugin
import sys 
import os
# sublime text3 不給用 requests
import urllib.request
import json

SETTINGS_PATH = "chatgpt.sublime-settings"

class ChatgptCommand(sublime_plugin.TextCommand):
    
    def get_settings(self):
        return sublime.load_settings(SETTINGS_PATH)

    def run(self, edit):

        # 這裡輸入您的 OpenAI API 密鑰
        api_key = self.get_settings().get("token") 
        # 獲取當前選中的文本
        for region in self.view.sel():
            if not region.empty():
                user_input = self.view.substr(region)
                break
            else:
                sublime.error_message("請選擇要發送的文本。")
                return


        # 發送請求到 OpenAI API
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system","content": "你專門產出指定程式語言的軟體程式碼，重新描述需求並標記註解"},{"role": "user", "content": user_input}],
            "temperature": 0.7
        }
        request_data = json.dumps(data).encode('utf-8')
        request = urllib.request.Request(url, data=request_data, headers=headers)

        try:
            with urllib.request.urlopen(request) as response:
                response_data = json.loads(response.read().decode('utf-8'))
                # sublime.error_message(''.join(response_data))
                reply = response_data['choices'][0]['message']['content'].strip()
                self.view.insert(edit, region.end(), "\n\n" + reply)
        except urllib.error.HTTPError as e:
            sublime.error_message("HTTP Error: " + str(e.code) + "\n" + e.read().decode('utf-8'))
        except urllib.error.URLError as e:
            sublime.error_message("URL Error: " + e.reason)
