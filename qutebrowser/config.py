c.auto_save.session = True
c.url.auto_search = "dns"
c.url.searchengines = {
    "DEFAULT": "https://google.com/search?q={}",
    "g": "https://google.com/search?q={}",
    "yt": "https://youtube.com/results?search_query={}",
    "gh": "https://github.com/search?q={}",
    "dr": "https://drive.google.com/drive/u/0/search?q={}",
}
c.qt.force_platform = "wayland"
c.fonts.monospace = "Monospace Regular"
c.fonts.prompts = "11pt monospace"
c.fonts.statusbar = "11pt monospace"
c.fonts.tabs = "11pt monospace"
c.scrolling.bar = "always"

c.input.insert_mode.auto_load = True

c.window.hide_decoration = True

# allow opening tabs in the background
c.tabs.background = True
c.tabs.padding = {"bottom": 3, "left": 5, "right": 5, "top": 3}
c.aliases = {
    "q": "close",
    "qa": "quit",
    "w": "session-save",
    "wq": "quit --save",
    "wqa": "quit --save",
    "src": "config-source",
    "read": "spawn --userscript readability",
}
config.bind(',l', 'spawn --userscript qute-lastpass')
config.bind(',L', 'spawn --userscript qute-lastpass --password-only')
config.bind(',p', 'spawn --userscript qute-pass')
config.bind(',P', 'spawn --userscript qute-pass --password-only')
config.bind('t', 'tab-focus')
config.bind('<Ctrl-j>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl-k>', 'completion-item-focus prev', mode='command')

config.set('content.register_protocol_handler', False, '*://mail.google.com/*')
config.set('content.register_protocol_handler', False, '*://calendar.google.com/*')

c.auto_save.session = True

# this fakes being a really recent browser, needed for slack sign in
# c.content.headers.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99999.0.3578.98 Safari/537.36"
