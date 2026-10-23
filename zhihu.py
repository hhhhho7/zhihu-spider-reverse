import requests
import subprocess
def get_js_result():
    result = subprocess.run(['node', 'zhihu.js'], capture_output=True, text=True, encoding='utf-8')
    output = result.stdout.strip()
    return output
x96 = '2.0_'+get_js_result()
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.zhihu.com/hot",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",

    "user-agent": '',
    "x-api-version": "3.0.76",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": x96,
    "x-zst-81": "3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7iUZQ6nxELYqm4fBJCHMiqHPD4S1hCS974e1DrNPAQLYlUefii7q26fp2L2ZKgSfnveCgrNOQwXTt_Fq6DQye8t9DGwT9RFZQAuTLbHP2GomybO1VhRTQ6kp-XxmxgNK-GNTjTkxkhkKh0PhHix_F0P1c9NMPqo8Ag3qcgSLAheLQhOYcJe_BGCskqYqpgtCNCLL-BwxPBYKxqYYFH_zCrHKqCc1tgp9hgr0zrL9BGpLMLSYbQgGpGe1h92fUC31QRx92RV8zCV_YCLfzCHmJ0c_ZqVYibNBrDCC2CFLgbOfAgSMtgNMJHVpawe8P9LZQANLQ8cs"
}
cookies = {
}
url = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total'
params = {
    "limit": "50",
    "desktop": "true"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
print(response)
json_data = response.json()
import csv
data_list = json_data.get('data', [])
with open("zhihu_hot.csv", "w", newline="", encoding="utf-8") as f:
    # 2. 定义表头
    headers = ['热度',"标题", "内容"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for item in data_list:
        target = item.get('target', {})
        title = target.get('title_area', {}).get('text', '')
        neiron = target.get('excerpt_area', {}).get('text', '')
        redu = target.get("metrics_area", {}).get('text', '')
        row_data = {
            '热度':redu,
            "标题": title,
            "内容": neiron
        }
        writer.writerow(row_data)
print("数据已成功写入 zhihu_hot.csv！")