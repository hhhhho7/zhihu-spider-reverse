进口 requests
进口 子过程
防守 get_js_result():
 结果 = 子进程。跑([“节点”, “zhihu.js”]， capture_output=确实如此， 文本=确实如此，编码=“UTF-8”)
 输出 = 结果。学生.条形()
    回归 输出
x96 = '2.0_'+get_js_result()
标题 = {
    “接受”: "*/*",
    “接受语言”: “zh-CN，zh;q=0.9，en;q=0.8，英格兰;q=0.7，en-US;q=0.6”,
    “缓存控制”: “无缓存”,
    “普拉格玛”: “无缓存”,
    “优先级”: “U=1， i“，
    “推荐人”: “https://www.志虎.com”/热”，
    “秘书”: “\”Microsoft Edge\“;v=\“155\”， \“铬\”;v=\“155\”， \“Not（A：Brand\”;v=\“24\””,
    “安全-移动”: "?0",
    “安全-平台”: “\”Windows\”,
    “超-取-最”: “空的”,
    “安全取物模式”: “科尔斯”,
    “安全取物站”: “同源”,

    “用户代理”: '',
    “X-API 版本”: "3.0.76",
    “x-请求-with”: “取”,
 “X-ZSE——93”：“101_3_3.0”，
 “X-ZSE——96”： x96，
 “X-ZST——81”：“3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7iUZQ6nxELYqm4fBJCHMiqHPD4S1hCS974e1DrNPAQLYlUefii7q26fp2L2ZKgSfnveCgrNOQwXTt_Fq6DQye8t9DGwT9RFZQAuTLbHP2GomybO1VhRTQ6kp-XxmxgNK-GNTjTkxkhkKh0PhHix_F0P1c9NMPqo8Ag3qcgSLAheLQhOYcJe_BGCskqYqpgtCNCLL-BwxPBYKxqYYFH_zCrHKqCc1tgp9hgr0zrL9BGpLMLSYbQgGpGe1h92fUC31QRx92RV8zCV_YCLfzCHmJ0c_ZqVYibNBrDCC2CFLgbOfAgSMtgNMJHVpawe8P9LZQANLQ8cs”
}
饼干 = {
}
URL = “https://www。志虎.com/api/v3/feed/topstory/hot-list/total”
参数 = {
    “极限”: "50",
    “桌面”: “确实如此”
}
响应 = 请求数。去(URL，头部=头部，Cookies=Cookies，params=params)
印刷(回应)
json_data = 反应。json()
进口 CSV
data_list = json_data。去(“数据”, [])
其中 开门(“zhihu_hot。csv”, “W”， 换行=""，编码=“UTF-8”) 作为 f:
 标题 =['热度',"标题", "内容"]
 作者 = csv。写字人(f， fieldnames=headers)
 作家。写首()
    对于 项目在 data_list：
 目标=物品。去(“目标”, {})
 标题=目标。去(“title_area”， {}).去(“短信”, '')
 Neiron =目标。去(“excerpt_area”， {}).去(“短信”, '')
 REDU =目标。去(“metrics_area”， {}).去(“短信”, '')
 row_data ={
            '热度'：redu，
            "标题"：标题，
            "内容"：尼隆
        }
 作家。写作罗(row_data)
印刷("数据已成功写入 zhihu_hot.csv！")
