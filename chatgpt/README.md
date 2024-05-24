<h1 align="center">Welcome to Sublime Text 的 ChatGPT 外掛 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0,0-blue.svg?cacheSeconds=2592000" />
  <a href="https://hipster.crazyjerry.studio/post/chatgpt-的-sublime-text4-外掛/" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

> 這是一個在 Sublime Text 上，利用 ChatGPT 實作對話已產生程式碼的外掛 

### 🏠 [Homepage](https://hipster.crazyjerry.studio/post/chatgpt-的-sublime-text4-外掛/)

安裝前需要準備：

1. Sublime Text 最新版
2. OpenAI 帳號，已有信用卡儲值（我們需要用 OpenAI API）

安裝的方式有別於使用 Package Control 安裝，這使用手動安裝，主要是把外掛中的 "chatgpt" 資料夾放到 Sublime Text 的 Packages 資料夾中就行了。 Packages 資料的夾的位置請參考這裡，可以從 Sublime Text 的 “Preferences -> Browse Packages” 開啟。

另外我們需要設定 OpenAI 的 API Key，請參考官方網站這裡 取得，在  Sublime Text 的的外掛設定： "Preferences -> package-settings -> 👽 ChatGPT -> Settings - User” 之中添加 koken 參數（也可以複製修改 Default 的設定格式）

使用上有設定 keymap，因為我是 mac用戶，所以操作上，選定一串文字以後快速鍵 cmd+g ，稍等幾秒 ChatGPT 將會回覆資料，將回應貼到選定文字的後面。
修改快速鍵的話，也是從 "Preferences -> package-settings -> 👽 ChatGPT-> Key Bindings - User" 修改即可。

手動執行的話也能在 Topbar 的 Tools 中找到 "👽 ChatGPT" 選項，點一下就執行。記得要選取你要的對話文字喔！

## Author

👤 **Jerry Lin**

* Website: https://crazyjerry.studio
* Github: [@lazyjerry](https://github.com/lazyjerry)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_