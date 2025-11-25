"""网易云音乐二维码登录模块

提供网易云音乐二维码登录功能，包括：
- 二维码生成和显示
- 登录状态检查
- Cookie获取和保存
- 用户友好的交互界面
"""

from music_api import qr_login
print("开始网易云音乐二维码登录流程...")
cookies = qr_login()
    
if cookies:
    print("\nCookie信息：")
    print(cookies)
else:
    print("登录失败，请重试。")
