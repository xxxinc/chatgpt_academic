import requests

# 设置代理
proxies = {
  "http": "socks5h://127.0.0.1:10809",
  "https": "socks5h://127.0.0.1:10809",
}

# 发送请求（设置timeout参数是为了在网络连接超时时能够及时响应）
response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", 
                         headers={"Authorization": "Bearer YOUR_API_KEY"}, 
                         json={"prompt": "Hello world!", "max_tokens": 5}, 
                         proxies=proxies, 
                         timeout=10)

# 打印响应内容
print(response.json())
